# OA Tracker Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Archive OAHelper's two placement group chats daily and have Claude Code sort every shared OA question into Markdown pages by company, college and topic, committed to a private GitHub repo.

**Architecture:** Three stages with files in between. `oa.fetch` (Playwright, logged-in Chrome profile) appends raw messages to `archive/` and downloads attachments. `oa.sort` sends unsorted messages in batches to `claude -p --json-schema` and appends questions to `data/questions.jsonl`, then marks reposts as duplicates. `oa.build` regenerates the README, company pages and topic pages. `run_daily.sh` chains the stages and commits; a launchd agent runs it at 23:00.

**Tech Stack:** Python 3.12, Playwright (installed Chrome, `channel="chrome"`), pytest, Claude Code CLI 2.1.x (`claude -p`), macOS `security` (Keychain), launchd, git + gh.

**Spec:** `docs/superpowers/specs/2026-10-15-oa-tracker-design.md`

## Global Constraints

- Project root: `/Users/msr/claude_code/oa-tracker`; venv at `.venv` (playwright + pytest already installed). Run tests with `.venv/bin/python -m pytest`.
- Groups: `inter-iit` (Placement '26 OA All IIT/NIT/IIIT) and `inter-nit` (Placement '27 OA All IIT/NIT/IIIT).
- Backfill from `2026-07-20`.
- Requests to oahelper.in: sequential, at least `1.0` s apart.
- Never store sender names or user ids. Keep only the college tag suffix (`Ray0ft6_IITD` → `IITD`).
- Credentials only in the macOS Keychain, service `oa-tracker`. Never print or log the password.
- Sorting batch size `40`. Topics come only from the fixed list in `oa/common.py:TOPICS` (1–3 per question).
- Repo `MSR327/Arigatho` must stay private. `chrome_profile/`, `logs/`, `recon_out/` and `.venv/` are git-ignored (already in `.gitignore`).
- Commits end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Feed facts (from recon, 2026-10-15)

- `GET https://www.oahelper.in/api/proxy/group-chat?action=my_groups` → `{"status":"success","groups":[{"id": "<uuid>", "name": "...", "slug": "inter-iit", ...}]}`
- `GET ...?action=messages&group_id=<uuid>&limit=50[&before=<id>|&since=<id>]` → `{"status":"success","messages":[...ascending by id...],"has_more":bool,"has_newer":bool,...}`
- Message object: `{"id": 6827, "body": "", "author_name": "Ray0ft6_IITD", "user_id": 20490, "created_at": "2026-10-14T21:52:01.17629+00:00", "deleted": false, "attachment": {"name": "rystad (1).pdf", "mime": "application/pdf", "size": 1772999, "is_image": false, "inline": true} | null, "reply_to": {"id": 6808, "user_id": 16152, "author_name": "Leo0cgo_NITR", "body": "I want rystad Energy oa questions ? Pls dm me or send"} | null, ...}`. Message ids are global across groups.
- Attachment: `GET https://www.oahelper.in/api/proxy/group-chat/attachment?message_id=<id>&download=1`
- Auth is cookie-based; `BrowserContext.request` shares the cookies. Login page `/login`, button text "Sign in with college email", then email + password inputs; it POSTs to `/api/auth/college-login`.
- `claude -p ... --output-format json --json-schema '<schema>'` prints JSON whose `structured_output` field holds the validated object; `is_error` is true on failure.

## File Structure

```
oa/__init__.py        empty
oa/common.py          paths, config constants, TOPICS, log/notify, Keychain, jsonl helpers
oa/feed.py            parse_message(): raw feed message → archive record (pure)
oa/store.py           Archive (append-only monthly jsonl), attachment_relpath(), load/save state
oa/fetch.py           FeedClient (HTTP via Playwright), login, fetch_group() algorithm, CLI
oa/sort.py            prompt building, run_claude(), validation, sort_pending(), dedupe(), CLI
oa/build.py           build_site(): README / companies / topics Markdown, CLI
prompts/sort.md       batch sorting prompt template
prompts/dedupe.md     duplicate-check prompt template
run_daily.sh          fetch → sort → build → commit → push
make_schedule.py      install/remove the launchd agent
tests/test_feed.py  tests/test_store.py  tests/test_fetch_logic.py
tests/test_sort.py  tests/test_build.py  tests/conftest.py
```

---

### Task 1: Common module and feed parsing

**Files:**
- Create: `oa/__init__.py`, `oa/common.py`, `oa/feed.py`, `tests/conftest.py`, `tests/test_feed.py`

**Interfaces:**
- Produces: `oa.common` constants `ROOT, ARCHIVE, FILES, DATA, QUESTIONS, STATE, LOGS, PROFILE, PROMPTS, BASE_URL, GROUPS, BACKFILL_FROM, REQUEST_GAP, BATCH_SIZE, KEYCHAIN_SERVICE, TOPICS`; functions `log(msg: str) -> None`, `notify(msg: str) -> None`, `load_creds(service=KEYCHAIN_SERVICE) -> tuple[str, str] | None`, `save_creds(user: str, pwd: str, service=KEYCHAIN_SERVICE) -> None`, `read_jsonl(path: Path) -> list[dict]`, `append_jsonl(path: Path, rows: list[dict]) -> None`.
- Produces: `oa.feed.author_tag(name: str | None) -> str | None`, `oa.feed.parse_message(raw: dict, group: str) -> dict` returning `{"id": int, "group": str, "sent_at": str, "text": str, "author_tag": str|None, "reply_to": {"id": int, "text": str, "author_tag": str|None}|None, "attachment": {"name": str, "mime": str, "size": int, "is_image": bool}|None, "deleted": bool}`.

- [ ] **Step 1: Write the failing tests**

`tests/conftest.py`:
```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
```

`tests/test_feed.py`:
```python
from oa.feed import author_tag, parse_message

RAW = {
    "id": 6827, "client_message_id": "x", "body": "", "author_name": "Ray0ft6_IITD",
    "avatar_slug": "p", "user_id": 20490, "is_mine": False,
    "created_at": "2026-10-14T21:52:01.17629+00:00", "edited_at": None, "deleted": False,
    "attachment": {"name": "rystad (1).pdf", "mime": "application/pdf", "size": 1772999,
                   "is_image": False, "inline": True},
    "mentioned_user_ids": [],
    "reply_to": {"id": 6808, "user_id": 16152, "author_name": "Leo0cgo_NITR",
                 "body": "I want rystad Energy oa questions ? Pls dm me or send"},
    "help_reward": None, "help_status": None,
}


def test_author_tag():
    assert author_tag("Ray0ft6_IITD") == "IITD"
    assert author_tag("abc_iitkgp") == "IITKGP"
    assert author_tag("NoTagHere") is None
    assert author_tag(None) is None


def test_parse_message_keeps_content_drops_identity():
    rec = parse_message(RAW, "inter-iit")
    assert rec == {
        "id": 6827, "group": "inter-iit", "sent_at": "2026-10-14T21:52:01.17629+00:00",
        "text": "", "author_tag": "IITD",
        "reply_to": {"id": 6808, "text": "I want rystad Energy oa questions ? Pls dm me or send",
                     "author_tag": "NITR"},
        "attachment": {"name": "rystad (1).pdf", "mime": "application/pdf", "size": 1772999,
                       "is_image": False},
        "deleted": False,
    }
    assert "Ray0ft6" not in str(rec) and "20490" not in str(rec)


def test_parse_message_plain_text():
    raw = dict(RAW, id="7000", body="Amazon OA at KGP: 2 DSA", attachment=None, reply_to=None)
    rec = parse_message(raw, "inter-nit")
    assert rec["id"] == 7000 and rec["text"] == "Amazon OA at KGP: 2 DSA"
    assert rec["attachment"] is None and rec["reply_to"] is None
```

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_feed.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'oa'`

- [ ] **Step 3: Implement**

`oa/__init__.py`: empty file.

`oa/common.py`:
```python
"""Paths, settings and small helpers shared by every stage."""

import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "archive"
FILES = ARCHIVE / "files"
DATA = ROOT / "data"
QUESTIONS = DATA / "questions.jsonl"
STATE = ROOT / "state.json"
LOGS = ROOT / "logs"
PROFILE = ROOT / "chrome_profile"
PROMPTS = ROOT / "prompts"

BASE_URL = "https://www.oahelper.in"
GROUPS = {
    "inter-iit": "Placement '26 OA All IIT/NIT/IIIT",
    "inter-nit": "Placement '27 OA All IIT/NIT/IIIT",
}
BACKFILL_FROM = "2026-07-20"
REQUEST_GAP = 1.0  # seconds between requests to oahelper.in
BATCH_SIZE = 40  # messages per claude -p call
KEYCHAIN_SERVICE = "oa-tracker"

TOPICS = [
    "Arrays", "Strings", "Hashing", "Two Pointers", "Sliding Window", "Binary Search",
    "Sorting", "Greedy", "DP", "Graphs", "Trees", "Heaps", "Stack/Queue", "Linked List",
    "Math", "Bit Manipulation", "Recursion/Backtracking", "SQL", "OS/DBMS/CN MCQ",
    "Aptitude", "Other",
]


def log(msg):
    line = f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}"
    print(line, flush=True)
    LOGS.mkdir(exist_ok=True)
    with (LOGS / "run.log").open("a") as f:
        f.write(line + "\n")


def notify(msg):
    safe = msg.replace('"', "'")
    subprocess.run(["osascript", "-e", f'display notification "{safe}" with title "OA tracker"'],
                   check=False)


def load_creds(service=KEYCHAIN_SERVICE):
    r = subprocess.run(["security", "find-generic-password", "-s", service, "-g"],
                       capture_output=True, text=True)
    acct = re.search(r'"acct"<blob>="([^"]*)"', r.stdout)
    pwd = re.search(r'^password: "(.*)"$', r.stderr, re.M)
    return (acct.group(1), pwd.group(1)) if r.returncode == 0 and acct and pwd else None


def save_creds(user, pwd, service=KEYCHAIN_SERVICE):
    subprocess.run(["security", "add-generic-password", "-U", "-s", service, "-a", user, "-w", pwd],
                   capture_output=True, check=False)


def read_jsonl(path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def append_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
```

`oa/feed.py`:
```python
"""Turn OAHelper feed messages into archive records (no names, no user ids)."""

import re

TAG_RE = re.compile(r"_([A-Za-z][A-Za-z0-9]{1,11})$")


def author_tag(name):
    m = TAG_RE.search(name or "")
    return m.group(1).upper() if m else None


def parse_message(raw, group):
    att = raw.get("attachment")
    reply = raw.get("reply_to")
    return {
        "id": int(raw["id"]),
        "group": group,
        "sent_at": raw["created_at"],
        "text": raw.get("body") or "",
        "author_tag": author_tag(raw.get("author_name")),
        "reply_to": {
            "id": int(reply["id"]),
            "text": reply.get("body") or "",
            "author_tag": author_tag(reply.get("author_name")),
        } if reply else None,
        "attachment": {
            "name": att.get("name") or "file",
            "mime": att.get("mime") or "",
            "size": int(att.get("size") or 0),
            "is_image": bool(att.get("is_image")),
        } if att else None,
        "deleted": bool(raw.get("deleted")),
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_feed.py -v`
Expected: 3 passed

- [ ] **Step 5: Commit**

```bash
git add oa/__init__.py oa/common.py oa/feed.py tests/conftest.py tests/test_feed.py
git commit -m "Add common config and feed message parsing"
```

---

### Task 2: Archive and state store

**Files:**
- Create: `oa/store.py`, `tests/test_store.py`

**Interfaces:**
- Consumes: `oa.common.read_jsonl`, `oa.common.append_jsonl`.
- Produces: `class Archive(root: Path)` with `add(records: list[dict]) -> list[dict]` (returns only records whose id was not archived before, appends them to `root/<group>/<YYYY-MM>.jsonl`), `all() -> list[dict]` (sorted by id), `by_id() -> dict[int, dict]`; `attachment_relpath(rec: dict) -> str | None` (path relative to project root, e.g. `archive/files/6827-rystad_1_.pdf`); `load_state(path: Path) -> dict` (default `{"groups": {}, "sorted_ids": []}`); `save_state(path: Path, state: dict) -> None` (atomic).

- [ ] **Step 1: Write the failing tests**

`tests/test_store.py`:
```python
import json

from oa.store import Archive, attachment_relpath, load_state, save_state


def rec(i, month="2026-10", group="inter-iit", att=None):
    return {"id": i, "group": group, "sent_at": f"{month}-05T10:00:00+00:00", "text": f"m{i}",
            "author_tag": None, "reply_to": None, "attachment": att, "deleted": False}


def test_add_dedupes_and_splits_by_month(tmp_path):
    a = Archive(tmp_path)
    assert [r["id"] for r in a.add([rec(1, "2026-09"), rec(2)])] == [1, 2]
    assert [r["id"] for r in a.add([rec(2), rec(3)])] == [3]
    assert (tmp_path / "inter-iit" / "2026-09.jsonl").exists()
    assert len((tmp_path / "inter-iit" / "2026-10.jsonl").read_text().splitlines()) == 2
    assert [r["id"] for r in Archive(tmp_path).all()] == [1, 2, 3]
    assert set(Archive(tmp_path).by_id()) == {1, 2, 3}


def test_attachment_relpath():
    att = {"name": "rystad (1).pdf", "mime": "application/pdf", "size": 1, "is_image": False}
    assert attachment_relpath(rec(6827, att=att)) == "archive/files/6827-rystad_1_.pdf"
    assert attachment_relpath(rec(5)) is None


def test_state_roundtrip(tmp_path):
    p = tmp_path / "state.json"
    assert load_state(p) == {"groups": {}, "sorted_ids": []}
    save_state(p, {"groups": {"inter-iit": {"oldest_id": 1}}, "sorted_ids": [1]})
    assert json.loads(p.read_text())["sorted_ids"] == [1]
    assert load_state(p)["groups"]["inter-iit"]["oldest_id"] == 1
```

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_store.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'oa.store'`

- [ ] **Step 3: Implement**

`oa/store.py`:
```python
"""Append-only message archive and the small state file."""

import json
import re

from oa.common import append_jsonl, read_jsonl


class Archive:
    def __init__(self, root):
        self.root = root
        self._ids = None

    def _files(self):
        return sorted(self.root.glob("*/*.jsonl"))

    def all(self):
        rows = [r for f in self._files() for r in read_jsonl(f)]
        return sorted(rows, key=lambda r: r["id"])

    def by_id(self):
        return {r["id"]: r for r in self.all()}

    def add(self, records):
        if self._ids is None:
            self._ids = {r["id"] for r in self.all()}
        new = []
        for r in records:
            if r["id"] in self._ids:
                continue
            self._ids.add(r["id"])
            append_jsonl(self.root / r["group"] / f"{r['sent_at'][:7]}.jsonl", [r])
            new.append(r)
        return new


def attachment_relpath(rec):
    att = rec.get("attachment")
    if not att:
        return None
    safe = re.sub(r"[^A-Za-z0-9.-]+", "_", att["name"])[-80:]
    return f"archive/files/{rec['id']}-{safe}"


def load_state(path):
    if not path.exists():
        return {"groups": {}, "sorted_ids": []}
    return json.loads(path.read_text())


def save_state(path, state):
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=1))
    tmp.replace(path)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_store.py -v`
Expected: 3 passed

- [ ] **Step 5: Commit**

```bash
git add oa/store.py tests/test_store.py
git commit -m "Add message archive and state store"
```

---

### Task 3: Fetch algorithm (backfill + incremental), tested with a fake feed

**Files:**
- Create: `oa/fetch.py` (algorithm part only in this task), `tests/test_fetch_logic.py`

**Interfaces:**
- Consumes: `parse_message`, `Archive`, `attachment_relpath`, `REQUEST_GAP`, `ROOT`.
- Produces: `fetch_group(client, archive, state: dict, slug: str, group_id: str, backfill_from: str, save=lambda: None, sleep=time.sleep, max_pages: int | None = None) -> list[dict]` (returns newly archived records). `client` must have `messages(group_id, before=None, since=None) -> dict` and `attachment(message_id: int) -> bytes`. Also `download_attachments(client, records, root: Path, sleep=time.sleep, max_bytes=25_000_000) -> int` (number downloaded; skips existing files, oversize files and failed downloads, logging the last two).

- [ ] **Step 1: Write the failing tests**

`tests/test_fetch_logic.py`:
```python
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
```

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_fetch_logic.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'oa.fetch'`

- [ ] **Step 3: Implement**

`oa/fetch.py`:
```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_fetch_logic.py -v`
Expected: 3 passed

- [ ] **Step 5: Commit**

```bash
git add oa/fetch.py tests/test_fetch_logic.py
git commit -m "Add fetch algorithm: backfill to cutoff, then incremental"
```

---

### Task 4: Live fetch — HTTP client, login, CLI

**Files:**
- Modify: `oa/fetch.py` (append client, login and CLI below the Task 3 code)

**Interfaces:**
- Consumes: `fetch_group`, `download_attachments` (Task 3); `Archive`, `load_state`, `save_state` (Task 2); `BASE_URL, GROUPS, BACKFILL_FROM, PROFILE, ARCHIVE, STATE, ROOT, load_creds, save_creds, log, notify` (Task 1).
- Produces: CLI `python -m oa.fetch [--setup] [--headless] [--group SLUG] [--max-pages N]`; exit code 0 on success, 1 on failure (after a notification).

- [ ] **Step 1: Append the client, login and CLI to `oa/fetch.py`**

Add these imports to the top of `oa/fetch.py` (merge with existing ones):
```python
import argparse
import json
import re
import sys

from playwright.sync_api import sync_playwright

from oa.common import (ARCHIVE, BACKFILL_FROM, BASE_URL, GROUPS, PROFILE, ROOT, STATE,
                       load_creds, notify, save_creds)
from oa.store import Archive, load_state, save_state
```

Append:
```python
API = BASE_URL + "/api/proxy/group-chat"


class LoggedOut(Exception):
    pass


class FeedClient:
    def __init__(self, ctx):
        self.ctx = ctx

    def _json(self, params):
        r = self.ctx.request.get(API, params=params)
        if r.status in (401, 403):
            raise LoggedOut(f"HTTP {r.status}")
        try:
            data = r.json()
        except ValueError:
            raise RuntimeError(f"non-JSON reply (HTTP {r.status}): {r.text()[:200]}")
        if data.get("status") != "success":
            msg = str(data)[:200]
            raise (LoggedOut if re.search(r"auth|login|session", msg, re.I) else RuntimeError)(msg)
        return data

    def my_groups(self):
        return {g["slug"]: g["id"] for g in self._json({"action": "my_groups"})["groups"]}

    def messages(self, group_id, before=None, since=None):
        params = {"action": "messages", "group_id": group_id, "limit": 50}
        if before is not None:
            params["before"] = before
        if since is not None:
            params["since"] = since
        return self._json(params)

    def attachment(self, message_id):
        r = self.ctx.request.get(f"{API}/attachment",
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
        page.wait_for_response(lambda r: "/api/auth/" in r.url and r.request.method == "POST"
                               and r.ok and bool(typed), timeout=0)
        save_creds(typed["email"], typed["password"])
        log("Saved login to the Keychain (service oa-tracker).")
        page.wait_for_timeout(2000)
    finally:
        page.remove_listener("request", grab)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--setup", action="store_true", help="log in by hand once and save to Keychain")
    ap.add_argument("--headless", action="store_true")
    ap.add_argument("--group", choices=sorted(GROUPS))
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
                log(f"Setup done. Groups: {sorted(client.my_groups())}")
                return 0
            try:
                ids = client.my_groups()
            except LoggedOut:
                login(page, interactive=not args.headless)
                ids = client.my_groups()
            archive, state = Archive(ARCHIVE), load_state(STATE)
            total = 0
            for slug in [args.group] if args.group else GROUPS:
                if slug not in ids:
                    raise RuntimeError(f"not a member of group {slug!r}; join it on oahelper.in")
                new = fetch_group(client, archive, state, slug, ids[slug], BACKFILL_FROM,
                                  save=lambda: save_state(STATE, state), max_pages=args.max_pages)
                # all of this group's records: also retries files that failed last time
                files = download_attachments(
                    client, [r for r in archive.all() if r["group"] == slug], ROOT)
                log(f"{slug}: {len(new)} new messages, {files} files")
                total += len(new)
            log(f"fetch done: {total} new messages")
            return 0
        except Exception as e:
            log(f"fetch failed: {e!r}")
            notify(f"Fetch failed: {str(e)[:80]}")
            return 1
        finally:
            ctx.close()


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Unit tests still pass**

Run: `.venv/bin/python -m pytest -q`
Expected: all passed

- [ ] **Step 3: Live login setup (needs the user)**

The bot profile may still be logged in from recon, and then no login request would be captured. Clear its cookies first:
```bash
.venv/bin/python -c "
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    c = p.chromium.launch_persistent_context('chrome_profile', channel='chrome', headless=True)
    c.clear_cookies(); c.close()
print('cookies cleared')"
```
Run: `.venv/bin/python -m oa.fetch --setup`
User logs in by hand in the Chrome window ("Sign in with college email").
Expected log: `Saved login to the Keychain (service oa-tracker).` then `Setup done. Groups: [... 'inter-iit', 'inter-nit' ...]`.

- [ ] **Step 4: Live smoke fetch — one page of one group**

Run: `.venv/bin/python -m oa.fetch --headless --group inter-nit --max-pages 1`
Expected: `inter-nit: 50 new messages, N files` and `archive/inter-nit/2026-10.jsonl` exists with 50 lines containing no `author_name` key. Check: `grep -c author_name archive/inter-nit/*.jsonl` → 0 for every file.

- [ ] **Step 5: Live auto-login check**

Clear the profile's cookies again with the Step 3 snippet, then run: `.venv/bin/python -m oa.fetch --headless --group inter-nit --max-pages 1`
Expected: `Logging in as <email>` then a successful fetch. If the selector or response wait fails, fix `login()` against the live page before continuing.

- [ ] **Step 6: Commit (code only; archive data is committed by the daily run)**

```bash
git add oa/fetch.py
git commit -m "Add live feed client, Keychain login and fetch CLI"
```

---

### Task 5: Sort — prompt, Claude call, validation, batching

**Files:**
- Create: `prompts/sort.md`, `oa/sort.py`, `tests/test_sort.py`

**Interfaces:**
- Consumes: `Archive`, `attachment_relpath`, `load_state`, `save_state`, `QUESTIONS`, `TOPICS`, `PROMPTS`, `ROOT`, `ARCHIVE`, `STATE`, `BATCH_SIZE`, `GROUPS`, `log`, `notify`, `read_jsonl`, `append_jsonl`.
- Produces: `SORT_SCHEMA: dict`; `class ClaudeError(Exception)`; `class UsageLimit(ClaudeError)`; `format_message(rec: dict) -> str`; `build_batch_prompt(batch: list[dict], companies: list[str]) -> str`; `run_claude(prompt: str, schema: dict) -> dict`; `to_questions(shares: list[dict], batch_ids: set[int]) -> list[dict]` (raises `ValueError` on invalid data); `is_sortable(rec: dict) -> bool`; `sort_pending(archive, state, runner=run_claude, batch_size=BATCH_SIZE, limit=None, save=lambda: None, questions_path=QUESTIONS) -> list[dict]`. Question row: `{"qid": str, "company": str, "college": str, "date": "YYYY-MM-DD", "role": "intern"|"fte"|"unknown", "title": str, "text": str, "topics": [str], "source_ids": [int], "duplicate_of": str|None}`.

- [ ] **Step 1: Write the failing tests**

`tests/test_sort.py`:
```python
import pytest

from oa.sort import (ClaudeError, UsageLimit, build_batch_prompt, format_message, is_sortable,
                     sort_pending, to_questions)
from oa.store import Archive


def rec(i, text="", att=None, reply=None, deleted=False):
    return {"id": i, "group": "inter-iit", "sent_at": "2026-10-14T21:52:01+00:00", "text": text,
            "author_tag": "IITD", "reply_to": reply, "attachment": att, "deleted": deleted}


PDF = {"name": "rystad (1).pdf", "mime": "application/pdf", "size": 10, "is_image": False}
REPLY = {"id": 6808, "text": "I want rystad Energy oa questions?", "author_tag": "NITR"}


def share(**kw):
    s = {"company": "Rystad Energy", "college": "IIT Delhi", "date": "2026-10-14", "role": "fte",
         "source_ids": [6827], "questions": [{"title": "Max subarray", "text": "Given...",
                                              "topics": ["Arrays", "DP"]}]}
    s.update(kw)
    return s


def test_format_message_has_context_and_file():
    line = format_message(rec(6827, att=PDF, reply=REPLY))
    assert "[6827] 2026-10-14 IITD" in line
    assert 'reply to [6808] (NITR): "I want rystad Energy oa questions?"' in line
    assert "archive/files/6827-rystad_1_.pdf (application/pdf)" in line


def test_build_batch_prompt_lists_messages_topics_companies():
    p = build_batch_prompt([rec(1, "Amazon OA today")], ["Amazon", "Google"])
    assert "[1] 2026-10-14 IITD" in p and "Amazon OA today" in p
    assert "Sliding Window" in p and "Amazon, Google" in p


def test_is_sortable():
    assert is_sortable(rec(1, "hi"))
    assert is_sortable(rec(1, att=PDF))
    assert not is_sortable(rec(1, ""))
    assert not is_sortable(rec(1, "x", deleted=True))


def test_to_questions_valid():
    rows = to_questions([share(), share(questions=[{"title": "A", "text": "a", "topics": ["SQL"]},
                                                   {"title": "B", "text": "b", "topics": ["Math"]}])],
                        {6827})
    assert [r["qid"] for r in rows] == ["6827-1", "6827-2", "6827-3"]
    assert rows[0]["company"] == "Rystad Energy" and rows[0]["duplicate_of"] is None


@pytest.mark.parametrize("bad", [
    share(source_ids=[999]),                       # not in this batch
    share(date="14 Oct"),                          # bad date
    share(role="sde"),                             # bad role
    share(company=" "),                            # empty company
    share(questions=[{"title": "A", "text": "a", "topics": ["Cooking"]}]),  # unknown topic
])
def test_to_questions_rejects(bad):
    with pytest.raises(ValueError):
        to_questions([bad], {6827})


def test_sort_pending_batches_retries_and_skips(tmp_path):
    a = Archive(tmp_path / "archive")
    a.add([rec(1, "Amazon OA: two sum"), rec(2, ""), rec(3, "Google OA"), rec(4, "chat")])
    state = {"groups": {}, "sorted_ids": []}
    calls = []

    def runner(prompt, schema):
        calls.append(prompt)
        if "[1]" in prompt:
            return {"shares": [share(company="Amazon", source_ids=[1])]}
        if len(calls) == 2:
            raise ClaudeError("flaky")
        return {"shares": []}

    qpath = tmp_path / "q.jsonl"
    rows = sort_pending(a, state, runner=runner, batch_size=1, questions_path=qpath)
    assert [r["company"] for r in rows] == ["Amazon"]
    assert sorted(state["sorted_ids"]) == [1, 2, 3, 4]  # 2 is empty: marked sorted without a call
    assert len(calls) == 4  # 1, 3 (fail), 3 (retry), 4
    assert qpath.read_text().count('"Amazon"') == 1


def test_sort_pending_stops_on_usage_limit(tmp_path):
    a = Archive(tmp_path / "archive")
    a.add([rec(1, "x"), rec(2, "y")])
    state = {"groups": {}, "sorted_ids": []}

    def runner(prompt, schema):
        raise UsageLimit("usage limit reached")

    with pytest.raises(UsageLimit):
        sort_pending(a, state, runner=runner, batch_size=1, questions_path=tmp_path / "q.jsonl")
    assert state["sorted_ids"] == []
```

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_sort.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'oa.sort'`

- [ ] **Step 3: Write the prompt template**

`prompts/sort.md`:
```markdown
You are sorting messages from an Indian campus-placement group chat where students share
online-assessment (OA) questions from companies' hiring tests.

Below are chat messages. Each starts with `[id] date college-tag` of the poster (e.g. IITD =
IIT Delhi, NITR = NIT Rourkela, KGP/IITKGP = IIT Kharagpur). A message may be a reply (the
replied-to text is shown), and may have an attachment path. Attachments are screenshots or
PDFs of OA questions: open them with the Read tool and transcribe the questions.

Find every message (or group of consecutive messages) that actually shares OA questions.
Ignore requests ("anyone has X OA?"), greetings, results, referrals and other chatter.
For each share, return:
- company: the hiring company. Reuse one of these existing names when it matches: {companies}
- college: full canonical name of the campus where the OA was held, e.g. "IIT Kharagpur",
  "IIT Bombay", "NIT Trichy". Use the poster's college tag unless the text says otherwise.
  Use "Unknown" if there is no clue.
- date: YYYY-MM-DD the OA was held if the message says so ("yesterday", "on 12th"),
  otherwise the message date.
- role: "intern", "fte" (full-time / placement) or "unknown".
- source_ids: ids of the messages this share came from.
- questions: one entry per question with a short title, the full question text (transcribed
  from attachments when needed; include constraints and examples if visible), and 1-3 topics
  from exactly this list: {topics}

Return {{"shares": []}} if no message shares OA questions.

Messages:

{messages}
```

- [ ] **Step 4: Implement `oa/sort.py`**

```python
"""Stage 2: have Claude Code turn archived messages into structured OA questions."""

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import date

from oa.common import (ARCHIVE, BATCH_SIZE, LOGS, PROMPTS, QUESTIONS, ROOT, STATE, TOPICS,
                       append_jsonl, log, notify, read_jsonl)
from oa.store import Archive, attachment_relpath, load_state, save_state

SORT_SCHEMA = {
    "type": "object",
    "properties": {"shares": {"type": "array", "items": {
        "type": "object",
        "properties": {
            "company": {"type": "string"},
            "college": {"type": "string"},
            "date": {"type": "string", "pattern": r"^\d{4}-\d{2}-\d{2}$"},
            "role": {"enum": ["intern", "fte", "unknown"]},
            "source_ids": {"type": "array", "items": {"type": "integer"}, "minItems": 1},
            "questions": {"type": "array", "minItems": 1, "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "text": {"type": "string"},
                    "topics": {"type": "array", "items": {"enum": TOPICS},
                               "minItems": 1, "maxItems": 3},
                },
                "required": ["title", "text", "topics"], "additionalProperties": False}},
        },
        "required": ["company", "college", "date", "role", "source_ids", "questions"],
        "additionalProperties": False}}},
    "required": ["shares"], "additionalProperties": False,
}


class ClaudeError(Exception):
    pass


class UsageLimit(ClaudeError):
    pass


def format_message(rec):
    lines = [f"[{rec['id']}] {rec['sent_at'][:10]} {rec['author_tag'] or '?'}"]
    if rec["reply_to"]:
        r = rec["reply_to"]
        lines.append(f'  reply to [{r["id"]}] ({r["author_tag"] or "?"}): "{r["text"][:300]}"')
    if rec["attachment"]:
        lines.append(f"  attachment: {attachment_relpath(rec)} ({rec['attachment']['mime']})")
    if rec["text"]:
        lines.append("  " + rec["text"].replace("\n", "\n  "))
    return "\n".join(lines)


def build_batch_prompt(batch, companies):
    template = (PROMPTS / "sort.md").read_text()
    return template.format(
        companies=", ".join(companies) or "(none yet)",
        topics=", ".join(TOPICS),
        messages="\n\n".join(format_message(r) for r in batch),
    )


def run_claude(prompt, schema):
    cmd = ["claude", "-p", prompt, "--output-format", "json", "--no-session-persistence",
           "--allowedTools", "Read", "--json-schema", json.dumps(schema)]
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=1200)
    try:
        out = json.loads(r.stdout)
    except ValueError:
        msg = (r.stdout + r.stderr)[-500:]
        raise (UsageLimit if re.search(r"limit", msg, re.I) else ClaudeError)(msg)
    if out.get("is_error") or out.get("structured_output") is None:
        msg = str(out.get("result") or out.get("subtype"))[:500]
        raise (UsageLimit if re.search(r"usage limit|rate limit|limit reached", msg, re.I)
               else ClaudeError)(msg)
    return out["structured_output"]


def to_questions(shares, batch_ids):
    rows, seq = [], Counter()
    for s in shares:
        if not s["company"].strip() or not s["college"].strip():
            raise ValueError(f"empty company/college: {s}")
        date.fromisoformat(s["date"])
        if s["role"] not in ("intern", "fte", "unknown"):
            raise ValueError(f"bad role {s['role']!r}")
        if not s["source_ids"] or not set(s["source_ids"]) <= batch_ids:
            raise ValueError(f"source_ids {s['source_ids']} not in batch")
        base = min(s["source_ids"])
        for q in s["questions"]:
            if not q["topics"] or len(q["topics"]) > 3 or not set(q["topics"]) <= set(TOPICS):
                raise ValueError(f"bad topics {q['topics']}")
            seq[base] += 1
            rows.append({"qid": f"{base}-{seq[base]}", "company": s["company"].strip(),
                         "college": s["college"].strip(), "date": s["date"], "role": s["role"],
                         "title": q["title"].strip(), "text": q["text"].strip(),
                         "topics": q["topics"], "source_ids": sorted(s["source_ids"]),
                         "duplicate_of": None})
    return rows


def is_sortable(rec):
    return not rec["deleted"] and bool(rec["text"].strip() or rec["attachment"])


def known_companies(rows):
    seen = set(GROUP_COMPANIES)
    seen.update(r["company"] for r in rows)
    return sorted(seen)


# Company names from OAHelper's per-company group catalog, so batches agree on spelling.
GROUP_COMPANIES = [
    "Accenture", "Adobe", "Amazon", "Apple", "Blinkit", "BPCL", "BridgeHorn", "Calix",
    "Capgemini", "Cashfree", "Chargebee", "Cisco", "Cognizant", "Cohesity", "Deloitte",
    "ENTNT", "Eternal", "Futures First", "Google", "Gullak Money", "HP", "HSBC", "Humming Wave",
    "IBM", "ICICI", "IndusInd Bank", "InMobi", "Infosys", "Ivy Homes", "Juspay", "Kickdrum",
    "Kratikal", "L.E.K. Consulting", "Microsoft", "Morgan Stanley", "Myntra", "Nvidia", "Paytm",
    "Porter", "Quince", "Reliance", "Renesas Electronics", "Rystad Energy", "Silicon Labs",
    "Squarepoint", "TCS", "Teradata", "Thorogood", "Tredence", "TresVista", "Triology",
    "Virtusa", "Visa", "Zomato", "Zscaler",
]


def sort_pending(archive, state, runner=run_claude, batch_size=BATCH_SIZE, limit=None,
                 save=lambda: None, questions_path=QUESTIONS):
    done = set(state["sorted_ids"])
    pending = [r for r in archive.all() if r["id"] not in done]
    if limit is not None:
        pending = pending[:limit]
    skip = [r["id"] for r in pending if not is_sortable(r)]
    state["sorted_ids"] += skip
    save()
    todo = [r for r in pending if is_sortable(r)]
    existing = read_jsonl(questions_path)
    new_rows = []
    for i in range(0, len(todo), batch_size):
        batch = todo[i:i + batch_size]
        ids = {r["id"] for r in batch}
        prompt = build_batch_prompt(batch, known_companies(existing + new_rows))
        rows = None
        for attempt in (1, 2):
            try:
                rows = to_questions(runner(prompt, SORT_SCHEMA)["shares"], ids)
                break
            except UsageLimit:
                raise
            except (ClaudeError, ValueError, KeyError, TypeError) as e:
                log(f"batch {min(ids)}-{max(ids)} attempt {attempt} failed: {e!r}")
        if rows is None:
            append_jsonl(LOGS / "failed_batches.jsonl", [{"ids": sorted(ids)}])
            continue
        append_jsonl(questions_path, rows)
        state["sorted_ids"] += sorted(ids)
        save()
        new_rows += rows
        log(f"batch {min(ids)}-{max(ids)}: {len(rows)} questions")
    return new_rows
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_sort.py -v`
Expected: all passed

- [ ] **Step 6: Commit**

```bash
git add prompts/sort.md oa/sort.py tests/test_sort.py
git commit -m "Add Claude-based batch sorting with schema validation"
```

---

### Task 6: Duplicate pass and sort CLI

**Files:**
- Create: `prompts/dedupe.md`
- Modify: `oa/sort.py` (append), `tests/test_sort.py` (append)

**Interfaces:**
- Consumes: `run_claude`, `ClaudeError`, `UsageLimit`, `sort_pending` (Task 5).
- Produces: `DEDUPE_SCHEMA: dict`; `dedupe(new_rows: list[dict], all_rows: list[dict], runner=run_claude) -> dict[str, str]` (new qid → qid it duplicates); `apply_duplicates(path: Path, dupes: dict[str, str]) -> None`; CLI `python -m oa.sort [--limit N]` that notifies a summary.

- [ ] **Step 1: Write the failing tests (append to `tests/test_sort.py`)**

```python
from oa.sort import apply_duplicates, dedupe
from oa.common import append_jsonl, read_jsonl


def q(qid, company, title):
    return {"qid": qid, "company": company, "college": "IIT Delhi", "date": "2026-10-01",
            "role": "fte", "title": title, "text": title, "topics": ["Arrays"],
            "source_ids": [int(qid.split("-")[0])], "duplicate_of": None}


def test_dedupe_marks_repeats_per_company():
    old = [q("1-1", "Amazon", "Two sum"), q("2-1", "Google", "LRU cache")]
    new = [q("9-1", "Amazon", "Two Sum (pairs)"), q("9-2", "Amazon", "Max flow"),
           q("10-1", "Visa", "Only one")]
    prompts = []

    def runner(prompt, schema):
        prompts.append(prompt)
        return {"matches": [{"qid": "9-1", "duplicate_of": "1-1"},
                            {"qid": "9-2", "duplicate_of": None}]}

    assert dedupe(new, old + new, runner=runner) == {"9-1": "1-1"}
    assert len(prompts) == 1  # Visa has nothing to compare with -> no call
    assert "LRU cache" not in prompts[0]  # only the same company is shown


def test_dedupe_ignores_invalid_targets():
    old = [q("1-1", "Amazon", "Two sum")]
    new = [q("9-1", "Amazon", "x")]
    runner = lambda p, s: {"matches": [{"qid": "9-1", "duplicate_of": "404-1"}]}
    assert dedupe(new, old + new, runner=runner) == {}


def test_apply_duplicates(tmp_path):
    p = tmp_path / "q.jsonl"
    append_jsonl(p, [q("1-1", "Amazon", "a"), q("9-1", "Amazon", "a again")])
    apply_duplicates(p, {"9-1": "1-1"})
    assert [r["duplicate_of"] for r in read_jsonl(p)] == [None, "1-1"]
```

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_sort.py -v`
Expected: FAIL with `ImportError: cannot import name 'apply_duplicates'`

- [ ] **Step 3: Write `prompts/dedupe.md`**

```markdown
These are OA questions asked by {company}. EXISTING questions are already in our list; NEW
questions were just added. For each NEW question, decide whether it is the same problem as an
EXISTING question or an earlier NEW one (same task, possibly reworded, different numbers or
examples). Return one match per NEW question: duplicate_of is the qid it repeats, or null.

EXISTING:
{existing}

NEW:
{new}
```

- [ ] **Step 4: Append to `oa/sort.py`**

```python
DEDUPE_SCHEMA = {
    "type": "object",
    "properties": {"matches": {"type": "array", "items": {
        "type": "object",
        "properties": {"qid": {"type": "string"},
                       "duplicate_of": {"type": ["string", "null"]}},
        "required": ["qid", "duplicate_of"], "additionalProperties": False}}},
    "required": ["matches"], "additionalProperties": False,
}


def _brief(r):
    return f"- {r['qid']}: {r['title']} :: {r['text'][:400]}"


def dedupe(new_rows, all_rows, runner=run_claude):
    new_ids = {r["qid"] for r in new_rows}
    dupes = {}
    for company in sorted({r["company"] for r in new_rows}):
        same = [r for r in all_rows if r["company"].lower() == company.lower()]
        existing = [r for r in same if r["qid"] not in new_ids and not r["duplicate_of"]]
        new = [r for r in same if r["qid"] in new_ids]
        if not existing and len(new) < 2:
            continue
        prompt = (PROMPTS / "dedupe.md").read_text().format(
            company=company, existing="\n".join(map(_brief, existing)) or "(none)",
            new="\n".join(map(_brief, new)))
        try:
            matches = runner(prompt, DEDUPE_SCHEMA)["matches"]
        except UsageLimit:
            raise
        except (ClaudeError, KeyError, TypeError) as e:
            log(f"dedupe {company} failed: {e!r}")
            continue
        valid = {r["qid"] for r in same}
        for m in matches:
            if (m["qid"] in new_ids and m["duplicate_of"] in valid
                    and m["duplicate_of"] != m["qid"]):
                dupes[m["qid"]] = m["duplicate_of"]
    return dupes


def apply_duplicates(path, dupes):
    rows = read_jsonl(path)
    for r in rows:
        if r["qid"] in dupes:
            r["duplicate_of"] = dupes[r["qid"]]
    tmp = path.with_suffix(".tmp")
    tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    tmp.replace(path)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, help="only sort the first N pending messages")
    args = ap.parse_args(argv)
    archive, state = Archive(ARCHIVE), load_state(STATE)
    new_rows, stopped = [], None
    try:
        new_rows = sort_pending(archive, state, limit=args.limit,
                                save=lambda: save_state(STATE, state))
        if new_rows:
            apply_duplicates(QUESTIONS, dedupe(new_rows, read_jsonl(QUESTIONS)))
    except UsageLimit as e:
        stopped = str(e)[:80]
        log(f"stopped early: {e}")
    fresh = Counter(r["company"] for r in new_rows)
    summary = ", ".join(f"{c} {n}" for c, n in fresh.most_common(5))
    msg = f"{len(new_rows)} new questions" + (f": {summary}" if summary else "")
    if stopped:
        msg += " (stopped early: usage limit, continues next run)"
    log(msg)
    notify(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest -q`
Expected: all passed

- [ ] **Step 6: Commit**

```bash
git add prompts/dedupe.md oa/sort.py tests/test_sort.py
git commit -m "Add duplicate pass and sort CLI"
```

---

### Task 7: Build Markdown pages

**Files:**
- Create: `oa/build.py`, `tests/test_build.py`

**Interfaces:**
- Consumes: `read_jsonl`, `QUESTIONS`, `ROOT`, `ARCHIVE`, `Archive`, `attachment_relpath`.
- Produces: `slug(name: str) -> str`; `build_site(rows: list[dict], messages: dict[int, dict], out: Path, now: datetime) -> None` writing `out/README.md`, `out/companies/<slug>.md`, `out/topics/<slug>.md` (it removes and recreates `companies/` and `topics/`); CLI `python -m oa.build`.

- [ ] **Step 1: Write the failing tests**

`tests/test_build.py`:
```python
from datetime import datetime

from oa.build import build_site, slug


def q(qid, company, college, d, title, topics, dup=None, src=None):
    return {"qid": qid, "company": company, "college": college, "date": d, "role": "fte",
            "title": title, "text": f"Text of {title}", "topics": topics,
            "source_ids": src or [int(qid.split("-")[0])], "duplicate_of": dup}


ROWS = [
    q("1-1", "Amazon", "IIT Kharagpur", "2026-10-12", "Two sum", ["Arrays", "Hashing"], src=[1]),
    q("1-2", "Amazon", "IIT Kharagpur", "2026-10-12", "LRU", ["Other"], src=[1]),
    q("5-1", "Amazon", "IIT Bombay", "2026-10-13", "Two sum again", ["Arrays"], dup="1-1"),
    q("3-1", "Nvidia", "IIT Bombay", "2026-08-01", "Bit tricks", ["Bit Manipulation"], src=[3]),
]
MSGS = {1: {"id": 1, "group": "inter-iit", "sent_at": "2026-10-12T10:00:00+00:00",
            "attachment": {"name": "amz.jpg", "mime": "image/jpeg", "size": 1, "is_image": True}},
        3: {"id": 3, "group": "inter-nit", "sent_at": "2026-08-01T10:00:00+00:00",
            "attachment": None},
        5: {"id": 5, "group": "inter-iit", "sent_at": "2026-10-13T10:00:00+00:00",
            "attachment": None}}
NOW = datetime(2026, 10, 15, 23, 0)


def test_slug():
    assert slug("L.E.K. Consulting") == "l-e-k-consulting"
    assert slug("Stack/Queue") == "stack-queue"


def test_build_site(tmp_path):
    (tmp_path / "companies").mkdir()
    (tmp_path / "companies" / "stale.md").write_text("old")
    build_site(ROWS, MSGS, tmp_path, NOW)
    readme = (tmp_path / "README.md").read_text()
    assert "3 questions · 2 companies" in readme  # duplicates are not counted
    assert "| [Amazon](companies/amazon.md) | 2 | IIT Bombay, IIT Kharagpur | 2026-10-13 |" in readme
    assert "Amazon · IIT Kharagpur · 2026-10-12 · 2 questions" in readme  # new this week
    assert "Nvidia · IIT Bombay" not in readme.split("## By company")[0]  # not this week
    assert "[Bit Manipulation](topics/bit-manipulation.md) | 1" in readme
    assert not (tmp_path / "companies" / "stale.md").exists()

    amazon = (tmp_path / "companies" / "amazon.md").read_text()
    assert amazon.index("Two sum") < amazon.index("LRU")
    assert "## 2026-10-12 · IIT Kharagpur · FTE" in amazon
    assert "also asked at: IIT Bombay (2026-10-13)" in amazon
    assert "[amz.jpg](../archive/files/1-amz.jpg)" in amazon
    assert "Two sum again" not in amazon  # duplicate folded into the original

    topic = (tmp_path / "topics" / "arrays.md").read_text()
    assert "[Amazon](../companies/amazon.md)" in topic and "Two sum" in topic
```

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_build.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'oa.build'`

- [ ] **Step 3: Implement `oa/build.py`**

```python
"""Stage 3: regenerate README, company and topic pages from data/questions.jsonl."""

import re
import shutil
import sys
from collections import defaultdict
from datetime import datetime, timedelta

from oa.common import ARCHIVE, QUESTIONS, ROOT, read_jsonl
from oa.store import Archive, attachment_relpath


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "unknown"


def _sources(row, messages, prefix):
    links = []
    for mid in row["source_ids"]:
        m = messages.get(mid)
        rel = attachment_relpath(m) if m else None
        if rel:
            links.append(f"[{m['attachment']['name']}]({prefix}{rel})")
        elif m:
            links.append(f"[msg {mid}]({prefix}archive/{m['group']}/{m['sent_at'][:7]}.jsonl)")
    return ", ".join(links) or "-"


def _company_page(company, rows, dups, messages):
    out = [f"# {company} OA", ""]
    groups = defaultdict(list)
    for r in rows:
        groups[(r["date"], r["college"], r["role"])].append(r)
    for (d, college, role) in sorted(groups, key=lambda k: (k[0], k[1]), reverse=True):
        out += [f"## {d} · {college} · {role.upper() if role == 'fte' else role.title()}", ""]
        for i, r in enumerate(sorted(groups[(d, college, role)], key=lambda r: r["qid"]), 1):
            out += [f"### Q{i}. {r['title']}", "", r["text"], "",
                    f"Topics: {', '.join(r['topics'])}  ", f"📎 source: {_sources(r, messages, '../')}"]
            seen = dups.get(r["qid"], [])
            if seen:
                also = ", ".join(f"{x['college']} ({x['date']})" for x in sorted(seen, key=lambda x: x["date"]))
                out.append(f"🔁 also asked at: {also}")
            out.append("")
    return "\n".join(out)


def _topic_page(topic, rows):
    out = [f"# {topic}", "", "| Date | Company | College | Question |", "|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: r["date"], reverse=True):
        out.append(f"| {r['date']} | [{r['company']}](../companies/{slug(r['company'])}.md) "
                   f"| {r['college']} | {r['title']} |")
    return "\n".join(out) + "\n"


def build_site(rows, messages, out, now):
    originals = [r for r in rows if not r["duplicate_of"]]
    dups = defaultdict(list)
    for r in rows:
        if r["duplicate_of"]:
            dups[r["duplicate_of"]].append(r)
    by_company, by_topic, by_college = defaultdict(list), defaultdict(list), defaultdict(lambda: defaultdict(int))
    sightings = defaultdict(list)  # originals + reposts, for colleges/latest date
    for r in rows:
        sightings[r["company"]].append(r)
    for r in originals:
        by_company[r["company"]].append(r)
        for t in r["topics"]:
            by_topic[t].append(r)
        by_college[r["college"]][r["company"]] += 1

    for sub in ("companies", "topics"):
        shutil.rmtree(out / sub, ignore_errors=True)
        (out / sub).mkdir(parents=True)
    for company, rs in by_company.items():
        (out / "companies" / f"{slug(company)}.md").write_text(_company_page(company, rs, dups, messages))
    for topic, rs in by_topic.items():
        (out / "topics" / f"{slug(topic)}.md").write_text(_topic_page(topic, rs))

    week_ago = (now - timedelta(days=7)).date().isoformat()
    recent = defaultdict(int)
    for r in originals:
        if r["date"] >= week_ago:
            recent[(r["date"], r["company"], r["college"])] += 1

    md = ["# OA Questions Tracker", "",
          f"Last updated {now:%d %b %Y %H:%M} · {len(originals)} questions · {len(by_company)} companies",
          "", "## New this week", ""]
    md += [f"- {c} · {col} · {d} · {n} question{'s' if n > 1 else ''}"
           for (d, c, col), n in sorted(recent.items(), reverse=True)] or ["- nothing new"]
    md += ["", "## By company", "", "| Company | Questions | Colleges | Latest |", "|---|---|---|---|"]
    for company, rs in sorted(by_company.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        seen = sightings[company]
        colleges = ", ".join(sorted({r["college"] for r in seen}))
        md.append(f"| [{company}](companies/{slug(company)}.md) | {len(rs)} | {colleges} "
                  f"| {max(r['date'] for r in seen)} |")
    md += ["", "## By college", ""]
    for college in sorted(by_college):
        parts = ", ".join(f"{c} ({n})" for c, n in sorted(by_college[college].items(), key=lambda kv: -kv[1]))
        md.append(f"**{college}:** {parts}  ")
    md += ["", "## By topic", "", "| Topic | Questions |", "|---|---|"]
    for topic, rs in sorted(by_topic.items(), key=lambda kv: -len(kv[1])):
        md.append(f"| [{topic}](topics/{slug(topic)}.md) | {len(rs)} |")
    (out / "README.md").write_text("\n".join(md) + "\n")


def main():
    rows = read_jsonl(QUESTIONS)
    build_site(rows, Archive(ARCHIVE).by_id(), ROOT, datetime.now())
    print(f"built pages for {len(rows)} questions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_build.py -v`
Expected: 2 passed

- [ ] **Step 5: Commit**

```bash
git add oa/build.py tests/test_build.py
git commit -m "Add Markdown site builder"
```

---

### Task 8: Daily runner and launchd schedule

**Files:**
- Create: `run_daily.sh`, `make_schedule.py`

**Interfaces:**
- Consumes: CLIs `python -m oa.fetch --headless`, `python -m oa.sort`, `python -m oa.build`.
- Produces: `run_daily.sh [--no-push]`; `make_schedule.py [HH:MM ...] | --remove` managing launchd label `com.oa-tracker.daily`.

- [ ] **Step 1: Write `run_daily.sh`**

```zsh
#!/bin/zsh
# Daily: fetch -> sort -> build -> commit -> push.  Usage: run_daily.sh [--no-push]
cd "${0:A:h}"
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"  # launchd has a bare PATH
PY=.venv/bin/python
mkdir -p logs
exec >> logs/daily.log 2>&1
echo "=== $(date)"

/usr/bin/caffeinate -i $PY -m oa.fetch --headless || exit 1
/usr/bin/caffeinate -i $PY -m oa.sort
$PY -m oa.build

git add -A archive data companies topics README.md state.json
if ! git diff --cached --quiet; then
  git commit -q -m "Update $(date +%F)"
  if [[ "$1" != "--no-push" ]]; then
    git push -q || $PY -c 'from oa.common import notify; notify("git push failed, will retry next run")'
  fi
fi
echo "=== done $(date)"
```

- [ ] **Step 2: Write `make_schedule.py`**

```python
"""Install (or remove) the launchd job that runs run_daily.sh.

Usage: .venv/bin/python make_schedule.py [HH:MM ...]   (default 23:00)
       .venv/bin/python make_schedule.py --remove
"""

import plistlib
import subprocess
import sys
from pathlib import Path

LABEL = "com.oa-tracker.daily"
ROOT = Path(__file__).resolve().parent
PLIST = Path.home() / "Library/LaunchAgents" / f"{LABEL}.plist"
UID = subprocess.run(["id", "-u"], capture_output=True, text=True).stdout.strip()

subprocess.run(["launchctl", "bootout", f"gui/{UID}/{LABEL}"], capture_output=True)
if sys.argv[1:] == ["--remove"]:
    PLIST.unlink(missing_ok=True)
    print("removed")
    sys.exit(0)

times = sys.argv[1:] or ["23:00"]
PLIST.write_bytes(plistlib.dumps({
    "Label": LABEL,
    "ProgramArguments": ["/bin/zsh", str(ROOT / "run_daily.sh")],
    "StartCalendarInterval": [{"Hour": int(t.split(":")[0]), "Minute": int(t.split(":")[1])}
                              for t in times],
    "StandardOutPath": str(ROOT / "logs" / "launchd.log"),
    "StandardErrorPath": str(ROOT / "logs" / "launchd.log"),
}))
r = subprocess.run(["launchctl", "bootstrap", f"gui/{UID}", str(PLIST)], capture_output=True, text=True)
print(f"{LABEL}: daily at {', '.join(times)}", "OK" if r.returncode == 0 else r.stderr)
```

- [ ] **Step 3: Make executable and syntax-check**

Run: `chmod +x run_daily.sh && zsh -n run_daily.sh && .venv/bin/python -m py_compile make_schedule.py && echo ok`
Expected: `ok`

- [ ] **Step 4: Commit**

```bash
git add run_daily.sh make_schedule.py
git commit -m "Add daily runner and launchd scheduler"
```

---

### Task 9: Live trial, backfill and schedule (with the user)

**Files:** none new (data files are produced and committed by the run).

- [ ] **Step 1: Trial sort on 40 real messages**

Precondition: Task 4 steps 3–4 done (Keychain login + one page of `inter-nit` archived).
Run: `.venv/bin/python -m oa.sort --limit 40 && .venv/bin/python -m oa.build`
Expected: log `batch ...: N questions`. Show the user `README.md` and one company page. Check by hand against the archived messages: right companies, college from the tag, screenshots transcribed, chatter ignored. Adjust `prompts/sort.md` if needed (then reset: delete `data/questions.jsonl` and set `"sorted_ids": []` in `state.json`, and rerun this step).

- [ ] **Step 2: Full backfill fetch**

Run: `.venv/bin/python -m oa.fetch --headless`
Expected: both groups back to 2026-07-20; `state.json` shows `"backfill_done": true` for both. At ~1 request/s, this takes minutes plus attachment downloads.

- [ ] **Step 3: First end-to-end run without push**

Run: `./run_daily.sh --no-push; tail -30 logs/daily.log`
Expected: fetch done, sort batches (may stop early on a usage limit; that's fine), build done, one local commit. Repeat on following days if the sort was stopped early.

- [ ] **Step 4: Push and verify the repo is private**

Run: `gh repo view MSR327/Arigatho --json visibility --jq .visibility && git push`
Expected: `PRIVATE`, then the push succeeds. Do not push if it prints `PUBLIC`.

- [ ] **Step 5: Install the schedule**

Run: `.venv/bin/python make_schedule.py 23:00`
Expected: `com.oa-tracker.daily: daily at 23:00 OK`. Verify with `launchctl print gui/$(id -u)/com.oa-tracker.daily | grep state`.
