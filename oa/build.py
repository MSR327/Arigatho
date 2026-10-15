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
