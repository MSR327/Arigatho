# OA Tracker — Design

Date: 2026-10-15
Status: approved in chat, pending spec review

## Problem

OAHelper (https://www.oahelper.in/groups) has large mixed group chats where
students share online-assessment (OA) questions from their campus as text,
screenshots or PDFs. The chats are huge, so questions get lost and there is no
way to see "what did company X ask, at which college, when".

## Goal

A private git repo that is updated automatically every day with every OA
question shared in the tracked groups, organised by company, college and topic,
each linking back to its original message or file.

## Scope

**Groups tracked** (mixed groups only; per-company groups are out of scope):
- Placement '26 OA All IIT/NIT/IIIT
- Placement '27 OA All IIT/NIT/IIIT
- 2027 Batch Intern
- 2028 Batch Intern

**History:** messages from 2026-07-20 onward (`BACKFILL_FROM` in config).

**Out of scope:** solving questions, difficulty ratings, a web UI, publishing the
repo. The repo stays private: the content is other students' posts from a
members-only site and OA questions are commonly under NDA.

## Architecture

Three stages with files between them; each stage runs on its own.

```
OAHelper groups
  │ fetch  (Python + Playwright, logged-in Chrome profile)
  ▼
archive/<group-slug>/<YYYY-MM>.jsonl   raw messages, append-only
archive/files/<message-id>-<n>.<ext>   downloaded images / PDFs
  │ sort   (Claude Code headless: `claude -p`)
  ▼
data/questions.jsonl                   one structured question per line
  │ build  (plain Python, deterministic)
  ▼
README.md, companies/<slug>.md, topics/<slug>.md
```

`run_daily.sh` runs fetch → sort → build → `git commit` → `git push`, then
posts a macOS notification summarising what was new.

### Stage 1: fetch

- Uses a persistent Chrome profile (`chrome_profile/`, git-ignored) driven by
  Playwright with the installed Chrome (`channel="chrome"`).
- Login: email + password. The first run is a manual login. The bot captures the
  credentials from the login request and stores them in the macOS Keychain
  (service `oa-tracker`), the same as the iMediX booking bot. Later runs log in
  automatically, and only if the stored session has expired.
- Reads messages through the same chat feed the page uses
  (`/api/proxy/group-chat/...`), requested from inside the logged-in browser
  context. The exact endpoints and response shape are confirmed in a recon step
  before this stage is written.
- Rate: at most about 1 request per second, sequential.
- Incremental: `state.json` stores a per-group cursor (last message id/time
  archived). First run pages back to `BACKFILL_FROM`.
- Each message is stored as one JSON line:
  `{id, group, sent_at, text, attachments: [{url, file, type}]}`.
  **Sender names and ids are not stored.**
- Attachments (images, PDFs) are downloaded to `archive/files/`.
- A group's cursor advances only after its new messages and files are written.

### Stage 2: sort

- Input: archived messages that are not yet in `state.json.sorted_ids`.
- Processed in batches of about 40 messages. Each batch's text and attachment
  paths go to `claude -p` with read-only file access, so Claude can open the
  images and PDFs.
- The prompt asks Claude to ignore chatter and, for each actual OA share,
  return:
  ```json
  {"company": "...", "college": "...", "date": "YYYY-MM-DD", "role": "intern|fte|unknown",
   "questions": [{"title": "...", "text": "...", "topics": ["DP", "..."]}],
   "source_ids": ["..."]}
  ```
- `date` is the day the OA was held if the message says so ("yesterday",
  "on 12th"), otherwise the day the message was posted. `college` is the
  campus where the OA was held, which is usually the poster's college.
- College names are normalised to canonical names (for example "kgp",
  "iitkgp" and "IIT KGP" all become "IIT Kharagpur"). Anything unidentifiable
  becomes "Unknown".
- Topics are 1–3 tags from a fixed list: Arrays, Strings, Hashing, Two Pointers,
  Sliding Window, Binary Search, Sorting, Greedy, DP, Graphs, Trees, Heaps,
  Stack/Queue, Linked List, Math, Bit Manipulation, Recursion/Backtracking, SQL,
  OS/DBMS/CN MCQ, Aptitude, Other.
- Company names are normalised to canonical names. The OAHelper group catalog's
  company list is used as the reference.
- Duplicate pass: for each company that got new questions, a second short
  `claude -p` call compares the new questions with that company's existing
  titles. Repeats are marked `duplicate_of: <question id>` and keep their
  college and date as "also asked at".
- Output is validated against the schema. A bad batch is retried once; if it
  fails again it is logged to `logs/` and left unsorted for the next run.
- If a usage limit stops the run, the unsorted messages simply wait for the
  next run.

### Stage 3: build

Regenerates all Markdown from `data/questions.jsonl`. No network access and no
Claude calls.

- `README.md`: last-updated line with totals, then **New this week**,
  **By company** (table: company, question count, colleges, latest date),
  **By college** and **By topic** (with counts and links).
- `companies/<slug>.md`: newest first, grouped by date · college · role. Each
  question has a title, text, topic tags, a source link to the archive message
  or file, and an "also asked at" line built from its duplicates.
- `topics/<slug>.md`: every question with that tag across companies, linking to
  the company pages.

## Scheduling

A launchd LaunchAgent runs `run_daily.sh` daily at 23:00 (configurable; more
times can be added). A run missed while the Mac was asleep happens on wake.
The run is wrapped in `caffeinate -i`.

## Errors and failure handling

| Failure | Behaviour |
|---|---|
| Login fails / session lost | macOS notification + log; nothing is committed |
| Feed format changed (unexpected response) | fetch stops for that group; cursor not advanced; notification |
| Usage limit / Claude error mid-sort | remaining messages stay unsorted; next run continues |
| Invalid Claude output | one retry, then the batch is logged and skipped for later |
| git push fails | commit stays local; notification; next run pushes again |

## Repo layout

```
oa-tracker/
  oa/            fetch.py, sort.py, build.py, common.py (config, paths, Keychain)
  prompts/       sort.md, dedupe.md
  tests/         test_fetch_parse.py, test_build.py, fixtures/
  archive/       raw messages + files (committed)
  data/          questions.jsonl (committed)
  companies/  topics/  README.md          (generated, committed)
  state.json     cursors + sorted ids (committed)
  logs/          (git-ignored)
  chrome_profile/ (git-ignored)
  run_daily.sh  make_schedule.py
```

## Testing

1. **Recon:** the user logs in once while the page's feed requests and responses
   are captured. These samples become the parser test fixtures.
2. **Unit tests:** fetch response parsing (fixtures → message records); build
   (sample `questions.jsonl` → expected Markdown); schema validation for sort
   output.
3. **Sort trial:** run sort on 30–40 real messages and show the user the
   resulting questions before starting the full backfill.
4. **Dry runs:** `run_daily.sh --no-push` for the first end-to-end run.

## Open items (resolved during implementation, not design)

- Exact feed endpoints, pagination and attachment URL format: from recon.
- GitHub remote URL: the user creates the private repo and provides it.
