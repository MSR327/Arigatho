from oa.fetch import download_attachments, fetch_group
from oa.store import Archive


def raw(i, day):
    return {"id": i, "body": f"m{i}", "author_name": "x_IITB", "user_id": 1,
            "created_at": f"2026-{day}T10:00:00+00:00", "deleted": False,
            "attachment": None, "reply_to": None}


class FakeFeed:
    """Serves self.msgs (ascending) with the real API's before/since/limit behaviour."""

    def __init__(self, msgs, limit=2):
        self.msgs, self.limit, self.calls = msgs, limit, []

    def messages(self, group_id, before=None, since=None):
        self.calls.append((before, since))
        if since is not None:
            newer = [m for m in self.msgs if m["id"] > since]
            return {"status": "success", "messages": newer[:self.limit],
                    "has_more": False, "has_newer": len(newer) > self.limit}
        older = [m for m in self.msgs if before is None or m["id"] < before]
        page = older[-self.limit:]
        return {"status": "success", "messages": page,
                "has_more": len(older) > self.limit, "has_newer": False}

    def attachment(self, message_id):
        return b"%PDF fake"


MSGS = [raw(1, "07-01"), raw(2, "07-25"), raw(3, "08-01"), raw(4, "09-01"), raw(5, "10-01")]


def test_backfill_stops_at_cutoff_then_incremental(tmp_path):
    a, state, feed = Archive(tmp_path), {"groups": {}, "sorted_ids": []}, FakeFeed(list(MSGS))
    new = fetch_group(feed, a, state, "inter-iit", "g", "2026-07-20", sleep=lambda s: None)
    assert sorted(r["id"] for r in new) == [2, 3, 4, 5]  # id 1 is before the cutoff
    gs = state["groups"]["inter-iit"]
    assert gs["backfill_done"] and gs["newest_id"] == 5

    feed.msgs += [raw(6, "10-02"), raw(7, "10-03"), raw(8, "10-04")]
    new = fetch_group(feed, a, state, "inter-iit", "g", "2026-07-20", sleep=lambda s: None)
    assert [r["id"] for r in new] == [6, 7, 8]
    assert state["groups"]["inter-iit"]["newest_id"] == 8


def test_backfill_resumes_after_interruption(tmp_path):
    a, state, feed = Archive(tmp_path), {"groups": {}, "sorted_ids": []}, FakeFeed(list(MSGS))
    fetch_group(feed, a, state, "inter-iit", "g", "2026-07-20", sleep=lambda s: None, max_pages=1)
    assert not state["groups"]["inter-iit"]["backfill_done"]
    assert state["groups"]["inter-iit"]["oldest_id"] == 4
    fetch_group(feed, a, state, "inter-iit", "g", "2026-07-20", sleep=lambda s: None)
    assert [r["id"] for r in a.all()] == [2, 3, 4, 5]


def test_download_attachments(tmp_path):
    rec = {"id": 9, "group": "inter-iit", "sent_at": "2026-10-01T00:00:00+00:00", "text": "",
           "author_tag": None, "reply_to": None, "deleted": False,
           "attachment": {"name": "q.pdf", "mime": "application/pdf", "size": 9, "is_image": False}}
    big = dict(rec, id=10, attachment=dict(rec["attachment"], size=10**9))

    class Broken(FakeFeed):
        def attachment(self, message_id):
            raise RuntimeError("HTTP 404")

    assert download_attachments(Broken([]), [rec], tmp_path, sleep=lambda s: None) == 0
    n = download_attachments(FakeFeed([]), [rec, big], tmp_path, sleep=lambda s: None)
    assert n == 1
    assert (tmp_path / "archive/files/9-q.pdf").read_bytes() == b"%PDF fake"
    assert not (tmp_path / "archive/files/10-q.pdf").exists()
