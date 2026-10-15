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
