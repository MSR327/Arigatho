"""Stage 2: have Claude Code turn archived messages into structured OA questions."""

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import date

from oa import leetcode
from oa.common import (ARCHIVE, BATCH_SIZE, COLLEGE_ALIASES, COMPANY_ALIASES, LOGS, MODELS, PROMPTS,
                       QUESTIONS, RESERVE_FROM, ROOT, STATE, TOPICS, append_jsonl, canonical, load_groups, log,
                       notify, read_jsonl, short_error)
from oa.store import Archive, attachment_relpath, load_state, save_state

REV = 2  # rows sorted or enriched with the v2 topic list and LeetCode matching
ENRICH_BATCH = 30  # questions per claude -p call when re-tagging existing questions

LEETCODE_SCHEMA = {"anyOf": [
    {"type": "null"},
    {"type": "object", "properties": {"number": {"type": "integer"}, "title": {"type": "string"}},
     "required": ["number", "title"], "additionalProperties": False}]}

SORT_SCHEMA = {
    "type": "object",
    "properties": {"shares": {"type": "array", "items": {
        "type": "object",
        "properties": {
            "company": {"type": "string"},
            "college": {"type": "string"},
            "date": {"type": "string", "pattern": r"^\d{4}-\d{2}-\d{2}$"},
            "role": {"enum": ["intern", "fte", "unknown"]},
            "position": {"type": "string"},
            "round": {"enum": ["oa", "interview", "other"]},
            "source_ids": {"type": "array", "items": {"type": "integer"}, "minItems": 1},
            "questions": {"type": "array", "minItems": 1, "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "text": {"type": "string"},
                    "topics": {"type": "array", "items": {"enum": TOPICS},
                               "minItems": 1, "maxItems": 3},
                    "leetcode": LEETCODE_SCHEMA,
                },
                "required": ["title", "text", "topics", "leetcode"], "additionalProperties": False}},
        },
        "required": ["company", "college", "date", "role", "position", "round", "source_ids",
                     "questions"],
        "additionalProperties": False}}},
    "required": ["shares"], "additionalProperties": False,
}

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


def group_context(slug, groups):
    """One line telling Claude where these messages were posted."""
    g = groups.get(slug)
    if not g:
        return "These messages come from an OAHelper placement group chat."
    name, place = g.get("name") or slug, g.get("company") or ""
    if g.get("role") == "Campus":
        return (f'These messages come from "{name}", the placement group of {place}: an OA discussed '
                f"here was most likely held at {place}, unless a message says otherwise.")
    if g.get("role") == "OA preparation":
        return (f'These messages come from "{name}", the group for {place} OAs: the company is '
                f"{place} unless a message says otherwise.")
    return f'These messages come from the OAHelper group "{name}".'


def group_rank(slug, groups):
    """Order to sort groups in, so a run stopped by the usage limit has done the most useful
    ones: company OA groups, the user's campus, the placement/intern batches, other campuses."""
    role = (groups.get(slug) or {}).get("role")
    if slug.startswith("campus-iit-kharagpur"):
        return 1
    return {"OA preparation": 0, None: 2, "Internship": 3, "Campus": 4}.get(role, 5)


def build_batch_prompt(batch, companies, groups=None):
    template = (PROMPTS / "sort.md").read_text()
    parts, current = [], None
    for r in batch:
        if r["group"] != current:
            current = r["group"]
            parts.append(f"── Posted in: {group_context(current, groups or {})} ──")
        parts.append(format_message(r))
    return template.format(
        companies=", ".join(companies) or "(none yet)",
        topics=", ".join(TOPICS),
        messages="\n\n".join(parts),
    )


USAGE = {"five_hour": None}  # latest share (0-1) of the 5-hour window used, as claude reports it


def run_claude(prompt, schema, model=None):
    used = USAGE["five_hour"]
    if used is not None and used >= RESERVE_FROM:
        raise UsageLimit(f"keeping the last {1 - RESERVE_FROM:.0%} of the 5-hour limit free "
                         f"({used:.0%} used)")
    cmd = ["claude", "-p", prompt, "--output-format", "stream-json", "--verbose",
           "--no-session-persistence", *(["--model", model] if model else []),
           "--allowedTools", "Read", "--json-schema", json.dumps(schema)]
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=1200)
    out = None
    for line in r.stdout.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get("type") == "rate_limit_event":
            window = (event.get("rate_limit_info") or {}).get("unifiedWindows", {}).get("five_hour", {})
            if "utilization" in window:
                USAGE["five_hour"] = window["utilization"]
        elif event.get("type") == "result":
            out = event
    if out is None:
        msg = (r.stdout + r.stderr)[-500:]
        raise (UsageLimit if re.search(r"limit", msg, re.I) else ClaudeError)(msg)
    if out.get("is_error") or out.get("structured_output") is None:
        msg = str(out.get("result") or out.get("subtype"))[:500]
        raise (UsageLimit if re.search(r"usage limit|session limit|rate limit|limit reached|hit your .*limit", msg, re.I)
               else ClaudeError)(msg)
    return out["structured_output"]


def to_questions(shares, batch_ids, problems=None):
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
            rows.append({"qid": f"{base}-{seq[base]}",
                         "company": canonical(s["company"], COMPANY_ALIASES),
                         "college": canonical(s["college"], COLLEGE_ALIASES),
                         "date": s["date"], "role": s["role"],
                         "position": (s.get("position") or "").strip(),
                         "round": s.get("round") or "oa",
                         "title": q["title"].strip(), "text": q["text"].strip(),
                         "topics": q["topics"], "source_ids": sorted(s["source_ids"]),
                         "leetcode": problems.match(q.get("leetcode")) if problems else None,
                         "rev": REV, "md": True, "deduped": False, "duplicate_of": None})
    return rows


def is_sortable(rec):
    return not rec["deleted"] and bool(rec["text"].strip() or rec["attachment"])


def known_companies(rows):
    seen = set(GROUP_COMPANIES)
    seen.update(r["company"] for r in rows)
    return sorted(seen)


def sort_pending(archive, state, runner=None, batch_size=BATCH_SIZE, limit=None,
                 save=lambda: None, questions_path=QUESTIONS, problems=None):
    runner = runner or (lambda prompt, schema: run_claude(prompt, schema, model=MODELS["sort"]))
    done = set(state["sorted_ids"])
    pending = [r for r in archive.all() if r["id"] not in done]
    if limit is not None:
        pending = pending[:limit]
    skip = [r["id"] for r in pending if not is_sortable(r)]
    state["sorted_ids"] += skip
    save()
    groups = load_groups()
    todo = sorted((r for r in pending if is_sortable(r)),
                  key=lambda r: (group_rank(r["group"], groups), r["group"], r["id"]))
    batches = [todo[i:i + batch_size] for i in range(0, len(todo), batch_size)]
    existing = read_jsonl(questions_path)
    new_rows = []
    for batch in batches:
        ids = {r["id"] for r in batch}
        prompt = build_batch_prompt(batch, known_companies(existing + new_rows), groups)
        rows = None
        for attempt in (1, 2):
            try:
                rows = to_questions(runner(prompt, SORT_SCHEMA)["shares"], ids, problems)
                break
            except UsageLimit:
                raise
            except (ClaudeError, ValueError, KeyError, TypeError) as e:
                log(f"batch {min(ids)}-{max(ids)} attempt {attempt} failed: {short_error(e)}")
        if rows is None:
            append_jsonl(LOGS / "failed_batches.jsonl", [{"ids": sorted(ids)}])
            continue
        append_jsonl(questions_path, rows)
        state["sorted_ids"] += sorted(ids)
        save()
        new_rows += rows
        log(f"batch {min(ids)}-{max(ids)}: {len(rows)} questions")
    return new_rows


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


def normalize_rows(rows):
    for r in rows:
        r["company"] = canonical(r["company"], COMPANY_ALIASES)
        r["college"] = canonical(r["college"], COLLEGE_ALIASES)
    return rows


def dedupe(new_rows, all_rows, runner=run_claude, failed=None):
    new_ids = {r["qid"] for r in new_rows}
    order = {r["qid"]: i for i, r in enumerate(all_rows)}  # only point at earlier rows: no cycles
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
            log(f"dedupe {company} failed: {short_error(e)}")
            if failed is not None:
                failed.append(company)
            continue
        valid = {r["qid"] for r in same}
        for m in matches:
            if (m["qid"] in new_ids and m["duplicate_of"] in valid
                    and order[m["duplicate_of"]] < order[m["qid"]]):
                dupes[m["qid"]] = m["duplicate_of"]
    return dupes


def dedupe_pending(path=QUESTIONS, runner=None, chunk=60):
    """Check rows not yet checked for reposts (deduped is False), company by company in chunks.
    Saves progress when stopped by the usage limit; rows whose check failed stay unchecked."""
    runner = runner or (lambda prompt, schema: run_claude(prompt, schema, model=MODELS["dedupe"]))
    rows = read_jsonl(path)
    pending = [r for r in rows if r.get("deduped") is False]
    matches, checked = {}, 0
    try:
        for company in sorted({r["company"] for r in pending}):
            mine = [r for r in pending if r["company"] == company]
            for i in range(0, len(mine), chunk):
                part, failed = mine[i:i + chunk], []
                matches.update(dedupe(part, rows, runner, failed))
                if failed:
                    continue
                for r in part:
                    r["deduped"] = True
                checked += len(part)
    finally:
        write_rows(path, rows)
        apply_duplicates(path, matches)
    return checked


def write_rows(path, rows):
    tmp = path.with_suffix(".tmp")
    tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    tmp.replace(path)


def apply_duplicates(path, dupes):
    rows = read_jsonl(path)
    parent = {r["qid"]: r["duplicate_of"] for r in rows}
    parent.update(dupes)

    def root(qid):  # follow repost -> original chains
        seen = {qid}
        while parent.get(qid) and parent[qid] not in seen:
            qid = parent[qid]
            seen.add(qid)
        return qid

    for r in rows:
        r["duplicate_of"] = root(r["qid"]) if parent.get(r["qid"]) else None
    write_rows(path, rows)


ENRICH_SCHEMA = {
    "type": "object",
    "properties": {"items": {"type": "array", "items": {
        "type": "object",
        "properties": {"qid": {"type": "string"},
                       "topics": {"type": "array", "items": {"enum": TOPICS},
                                  "minItems": 1, "maxItems": 3},
                       "leetcode": LEETCODE_SCHEMA},
        "required": ["qid", "topics", "leetcode"], "additionalProperties": False}}},
    "required": ["items"], "additionalProperties": False,
}


def build_enrich_prompt(rows):
    qs = "\n\n".join(f"[{r['qid']}] {r['company']}: {r['title']}\n{r['text'][:1500]}" for r in rows)
    return (PROMPTS / "enrich.md").read_text().format(topics=", ".join(TOPICS), questions=qs)


def enrich(path=QUESTIONS, runner=None, problems=None, batch_size=ENRICH_BATCH, limit=None):
    """Re-tag existing questions with the current topic list and LeetCode matches. Saves after
    every batch and skips rows already done, so it can stop (usage limit) and resume."""
    runner = runner or (lambda prompt, schema: run_claude(prompt, schema, model=MODELS["enrich"]))
    rows = normalize_rows(read_jsonl(path))  # also applies newer name aliases
    todo = [r for r in rows if not r["duplicate_of"] and r.get("rev", 1) < REV]
    if limit is not None:
        todo = todo[:limit]
    by_qid = {r["qid"]: r for r in rows}
    done = 0
    for i in range(0, len(todo), batch_size):
        batch = todo[i:i + batch_size]
        ids = {r["qid"] for r in batch}
        try:
            items = runner(build_enrich_prompt(batch), ENRICH_SCHEMA)["items"]
        except UsageLimit:
            raise
        except (ClaudeError, KeyError, TypeError) as e:
            log(f"enrich batch {i // batch_size + 1} failed: {short_error(e)}")
            continue
        for it in items:
            r = by_qid.get(it.get("qid"))
            topics = it.get("topics") or []
            if it.get("qid") not in ids or not topics or len(topics) > 3 or not set(topics) <= set(TOPICS):
                continue
            r["topics"] = topics
            r["leetcode"] = problems.match(it.get("leetcode")) if problems else None
            r["rev"] = REV
            done += 1
        write_rows(path, rows)
        log(f"enrich batch {i // batch_size + 1}: {done}/{len(todo)} questions re-tagged")
    return done


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, help="only sort the first N pending messages")
    ap.add_argument("--dedupe-all", action="store_true",
                    help="one-off: normalise names and re-check every question for reposts")
    ap.add_argument("--enrich", action="store_true",
                    help="re-tag existing questions with the current topics and LeetCode matches")
    args = ap.parse_args(argv)
    if args.enrich:
        try:
            n = enrich(problems=leetcode.load(), limit=args.limit)
            log(f"enrich: {n} questions re-tagged")
        except UsageLimit as e:
            log(f"enrich stopped early (usage limit); run it again later: {e}")
        return 0
    if args.dedupe_all:
        rows = normalize_rows(read_jsonl(QUESTIONS))
        write_rows(QUESTIONS, rows)
        originals = [r for r in rows if not r["duplicate_of"]]
        dupes = dedupe(originals, rows)
        apply_duplicates(QUESTIONS, dupes)
        log(f"dedupe-all: {len(dupes)} reposts folded into originals")
        return 0
    archive, state = Archive(ARCHIVE), load_state(STATE)
    before, stopped = len(read_jsonl(QUESTIONS)), None
    try:
        sort_pending(archive, state, limit=args.limit,
                     save=lambda: save_state(STATE, state), problems=leetcode.load())
    except UsageLimit as e:
        stopped = str(e)[:80]
        log(f"stopped early: {e}")
    new_rows = read_jsonl(QUESTIONS)[before:]
    try:
        dedupe_pending()  # also picks up rows left unchecked by earlier stopped runs
    except UsageLimit as e:
        stopped = stopped or str(e)[:80]
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
