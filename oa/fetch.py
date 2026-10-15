"""Stage 1: pull new messages from the OAHelper placement groups into archive/."""

import time

from oa.common import REQUEST_GAP, log
from oa.feed import parse_message
from oa.store import attachment_relpath


def fetch_group(client, archive, state, slug, group_id, backfill_from,
                save=lambda: None, sleep=time.sleep, max_pages=None):
    gs = state["groups"].setdefault(
        slug, {"oldest_id": None, "newest_id": None, "backfill_done": False})
    new = []
    pages = 0

    def track(recs):
        ids = [r["id"] for r in recs]
        gs["oldest_id"] = min(ids + ([gs["oldest_id"]] if gs["oldest_id"] else []))
        gs["newest_id"] = max(ids + ([gs["newest_id"]] if gs["newest_id"] else []))

    # Older pages until the cutoff date (first run, or resuming an interrupted one).
    while not gs["backfill_done"]:
        if max_pages is not None and pages >= max_pages:
            return new
        page = client.messages(group_id, before=gs["oldest_id"])
        pages += 1
        recs = [parse_message(m, slug) for m in page["messages"]]
        keep = [r for r in recs if r["sent_at"][:10] >= backfill_from]
        new += archive.add(keep)
        if recs:
            track(recs)
        if not recs or not page.get("has_more") or len(keep) < len(recs):
            gs["backfill_done"] = True
        save()
        sleep(REQUEST_GAP)

    # Newer messages since the last run.
    while True:
        page = client.messages(group_id, since=gs["newest_id"])
        recs = [parse_message(m, slug) for m in page["messages"]]
        new += archive.add(recs)
        if recs:
            track(recs)
        save()
        sleep(REQUEST_GAP)
        if not recs or not page.get("has_newer"):
            return new


def download_attachments(client, records, root, sleep=time.sleep, max_bytes=25_000_000):
    count = 0
    for rec in records:
        rel = attachment_relpath(rec)
        if not rel or rec["deleted"]:
            continue
        path = root / rel
        if path.exists():
            continue
        if rec["attachment"]["size"] > max_bytes:
            log(f"skip attachment {rec['id']}: {rec['attachment']['size']} bytes")
            continue
        try:
            data = client.attachment(rec["id"])
        except Exception as e:
            log(f"attachment {rec['id']} failed: {e!r}")
            continue
        finally:
            sleep(REQUEST_GAP)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        count += 1
    return count
