"""Stage 1: pull new messages from the OAHelper placement groups into archive/."""

import argparse
import json
import re
import sys
import time

from playwright.sync_api import sync_playwright

from oa.common import (ARCHIVE, BACKFILL_FROM, BASE_URL, GROUPS_FILE, PROFILE, REQUEST_GAP, ROOT,
                       SKIP_GROUPS, STATE, load_creds, log, notify, save_creds, short_error)
from oa.feed import parse_message
from oa.store import Archive, attachment_relpath, load_state, save_state


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
            log(f"attachment {rec['id']} failed: {short_error(e)}")
            continue
        finally:
            sleep(REQUEST_GAP)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        count += 1
    return count


API = BASE_URL + "/api/proxy/group-chat"


class LoggedOut(Exception):
    pass


class FeedClient:
    def __init__(self, ctx, sleep=time.sleep):
        self.ctx = ctx
        self.sleep = sleep

    def _json(self, params, tries=4):
        """GET the API. Server hiccups (5xx, an HTML error page) are retried with a pause."""
        for attempt in range(1, tries + 1):
            r = self.ctx.request.get(API, params=params)
            if r.status in (401, 403):
                raise LoggedOut(f"HTTP {r.status}")
            try:
                data = r.json()
                break
            except ValueError:
                if attempt == tries:
                    raise RuntimeError(f"non-JSON reply (HTTP {r.status}): {r.text()[:120]}")
                self.sleep(10 * attempt)
        if data.get("status") != "success":
            msg = str(data)[:200]
            raise (LoggedOut if re.search(r"auth|login|session", msg, re.I) else RuntimeError)(msg)
        return data

    def my_groups(self):
        return self._json({"action": "my_groups"})["groups"]

    def join_new_groups(self, joined, sleep=time.sleep):
        """Join every group in OAHelper's directory that we are not in yet (the site's own
        Join request). Returns the groups joined."""
        new = []
        for g in self._json({"action": "directory", "q": ""})["groups"]:
            if g["id"] in joined or g["slug"] in SKIP_GROUPS:
                continue
            r = self.ctx.request.post(API, data={"action": "join", "group_id": g["id"]})
            try:
                ok = r.ok and r.json().get("status") == "success"
            except ValueError:
                ok = False
            if ok:
                new.append(g)
            else:
                log(f"could not join {g['slug']}: HTTP {r.status}")
            sleep(2)
        return new

    def messages(self, group_id, before=None, since=None):
        params = {"action": "messages", "group_id": group_id, "limit": 50}
        if before is not None:
            params["before"] = before
        if since is not None:
            params["since"] = since
        return self._json(params)

    def attachment(self, message_id):
        r = self.ctx.request.get(f"{API}/attachment", timeout=180_000,  # big PDFs stream slowly
                                 params={"message_id": message_id, "download": 1})
        if r.status != 200:
            raise RuntimeError(f"attachment {message_id}: HTTP {r.status}")
        return r.body()


def login(page, interactive):
    """Log in through the page. Uses Keychain creds; falls back to (and learns from) a manual login."""
    typed = {}

    def grab(req):
        if req.method == "POST" and "/api/auth/" in req.url:
            try:
                body = json.loads(req.post_data or "{}")
            except ValueError:
                return
            if body.get("email") and body.get("password"):
                typed.update(email=body["email"], password=body["password"])

    page.on("request", grab)
    try:
        page.goto(BASE_URL + "/login")
        creds = load_creds()
        if creds:
            log(f"Logging in as {creds[0]}")
            try:
                page.get_by_text("Sign in with college email").click(timeout=5000)
            except Exception:
                pass
            page.locator("input[type=email]:visible").first.fill(creds[0])
            page.locator("input[type=password]:visible").first.fill(creds[1])
            with page.expect_response(lambda r: "/api/auth/" in r.url
                                      and r.request.method == "POST", timeout=20000) as resp:
                page.locator("input[type=password]:visible").first.press("Enter")
            if resp.value.ok:
                page.wait_for_timeout(2000)
                return
            log(f"Auto-login failed (HTTP {resp.value.status})")
        if not interactive:
            raise LoggedOut("cannot log in without a window; run: python -m oa.fetch --setup")
        log("Log in by hand in the Chrome window (college email + password)...")
        page.wait_for_event("response", predicate=lambda r: "/api/auth/" in r.url
                            and r.request.method == "POST" and r.ok and bool(typed), timeout=0)
        save_creds(typed["email"], typed["password"])
        log("Saved login to the Keychain (service oa-tracker).")
        page.wait_for_timeout(2000)
    finally:
        page.remove_listener("request", grab)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--setup", action="store_true", help="log in by hand once and save to Keychain")
    ap.add_argument("--headless", action="store_true")
    ap.add_argument("--group", help="only this group (slug)")
    ap.add_argument("--max-pages", type=int, help="limit backfill pages (smoke test)")
    args = ap.parse_args(argv)

    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            str(PROFILE), channel="chrome", headless=args.headless and not args.setup)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        client = FeedClient(ctx)
        try:
            if args.setup:
                login(page, interactive=True)
                log(f"Setup done. Groups: {len(client.my_groups())}")
                return 0
            try:
                groups = client.my_groups()
            except LoggedOut:
                login(page, interactive=not args.headless)
                groups = client.my_groups()
            joined = client.join_new_groups({g["id"] for g in groups})
            if joined:
                names = ", ".join(g["name"] for g in joined)
                log(f"joined {len(joined)} new groups: {names}")
                notify(f"Now also reading {len(joined)} new OAHelper group(s): {names[:80]}")
                groups = client.my_groups()
            GROUPS_FILE.parent.mkdir(parents=True, exist_ok=True)
            GROUPS_FILE.write_text(json.dumps(
                {g["slug"]: {k: g.get(k) for k in ("name", "company", "role")} for g in groups},
                indent=1, sort_keys=True) + "\n")
            ids = {g["slug"]: g["id"] for g in groups}
            slugs = [args.group] if args.group else sorted(s for s in ids if s not in SKIP_GROUPS)
            log(f"reading {len(slugs)} groups")
            archive, state = Archive(ARCHIVE), load_state(STATE)
            total = 0
            failed = []
            for slug in slugs:
                if slug not in ids:
                    raise RuntimeError(f"not a member of group {slug!r}; join it on oahelper.in")
                try:
                    new = fetch_group(client, archive, state, slug, ids[slug], BACKFILL_FROM,
                                      save=lambda: save_state(STATE, state), max_pages=args.max_pages)
                except LoggedOut:
                    raise
                except Exception as e:  # one group's trouble must not stop the others
                    log(f"{slug}: skipped this run ({short_error(e)})")
                    failed.append(slug)
                    continue
                if new:
                    log(f"{slug}: {len(new)} new messages")
                total += len(new)
            if failed and len(failed) == len(slugs):
                raise RuntimeError("every group failed")
            # one pass for files: also retries ones that failed last time
            files = download_attachments(client, [r for r in archive.all() if r["group"] in slugs], ROOT)
            log(f"{files} files downloaded")
            log(f"fetch done: {total} new messages" + (f", {len(failed)} groups skipped" if failed else ""))
            return 0
        except Exception as e:
            log(f"fetch failed: {short_error(e)}")
            notify(f"Fetch failed: {short_error(e)[:80]}")
            return 1
        finally:
            ctx.close()


if __name__ == "__main__":
    sys.exit(main())
