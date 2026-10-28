"""Stage 3: regenerate README, company, topic and practice pages from data/questions.jsonl."""

import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta

from oa import leetcode
from oa.common import ARCHIVE, QUESTIONS, ROOT, SKIP_GROUPS, TOPIC_GROUPS, load_groups, read_jsonl
from oa.store import Archive, attachment_relpath


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "unknown"


def gh_anchor(text, seen):
    """The id GitHub gives a Markdown heading: lowercase, punctuation dropped, spaces to
    hyphens, and -1, -2... for repeats on the same page."""
    a = re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")
    n = seen[a]
    seen[a] += 1
    return a if n == 0 else f"{a}-{n}"


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def message_lines(root):
    """{message id: (path, line)}, so a source link opens the exact line of the chat log."""
    loc = {}
    for f in sorted(root.glob("*/*.jsonl")):
        for n, line in enumerate(f.read_text().splitlines(), 1):
            if line.strip():
                loc[json.loads(line)["id"]] = (f"archive/{f.parent.name}/{f.name}", n)
    return loc


# ── question text ──

FENCE = re.compile(r"(```.*?```)", re.S)
OPTION = re.compile(r"(?:(?<=\s)|^)(?:\(([A-Ea-e])\)|([A-Ea-e])[.)])\s+")


def split_options(text):
    """"Which is right? A. x B. y C. z" -> the stem, then one line per option. Needs a run
    of at least three options lettered in order (A, B, C... or a, b, c...)."""
    if re.search(r"^\s*(?:\(?[A-Ea-e][.)]|\([A-Ea-e]\))\s", text, re.M):
        return text  # options are already on their own lines
    ms = list(OPTION.finditer(text))
    for i, m in enumerate(ms):
        first = m.group(1) or m.group(2)
        if first not in "Aa":
            continue
        run = [m]
        for nxt in ms[i + 1:]:
            if (nxt.group(1) or nxt.group(2)) == chr(ord(first) + len(run)):
                run.append(nxt)
            else:
                break
        if len(run) >= 3:
            stem = text[:run[0].start()].rstrip()
            opts = []
            for j, om in enumerate(run):
                end = run[j + 1].start() if j + 1 < len(run) else len(text)
                letter = (om.group(1) or om.group(2)).upper()
                opts.append(f"- **{letter}.** {text[om.end():end].strip()}")
            return (stem + "\n\n" if stem else "") + "\n".join(opts)
    return text


def format_text(row):
    """Question text as Markdown. Older rows hold plain text: keep its line breaks (GitHub
    would join them), stop `<vector>`-like text vanishing as HTML, and list MCQ options.
    Rows sorted with the Markdown prompt (`md`) are used as they are."""
    text = row["text"].strip()
    if row.get("md"):
        return text
    parts = FENCE.split(text)
    for i in range(0, len(parts), 2):  # outside code fences
        p = parts[i].replace("<", "&lt;")
        p = re.sub(r"(?m)^(\s*)([#>])", r"\1\\\2", p)  # a leading # or > is not a heading/quote
        p = split_options(p)
        parts[i] = re.sub(r"(?<!\n)\n(?!\n)", "  \n", p)  # single line breaks stay line breaks
    return "".join(parts)


def _lc_link(lc):
    return f"[LeetCode {lc['id']}. {lc['title']}]({leetcode.url(lc)}) ({lc['difficulty']})"


def _sources(row, messages, locs, prefix):
    links = []
    for mid in row["source_ids"]:
        m = messages.get(mid)
        if not m:
            continue
        rel = attachment_relpath(m)
        when = datetime.fromisoformat(m["sent_at"][:10]).strftime("%-d %b")
        if rel:
            links.append(f"[{m['attachment']['name']}]({prefix}{rel})")
        elif mid in locs:
            path, line = locs[mid]
            links.append(f"[chat, {when}]({prefix}{path}#L{line})")
        else:
            links.append(f"[chat, {when}]({prefix}archive/{m['group']}/{m['sent_at'][:7]}.jsonl)")
    return ", ".join(links) or "-"


def _also(reposts):
    by_college = defaultdict(list)
    for x in reposts:
        by_college[x["college"]].append(x["date"])
    parts = []
    for college, dates in sorted(by_college.items(), key=lambda kv: max(kv[1])):
        parts.append(f"{college} ({dates[0]})" if len(dates) == 1
                     else f"{college} ×{len(dates)} (last {max(dates)})")
    return ", ".join(parts)


def _role(role):
    return role.upper() if role == "fte" else role.title()


def _drive_key(r):
    return (r["date"], r["college"], r["role"], r.get("position") or "", r.get("round") or "oa")


def _drive_title(key):
    d, college, role, position, rnd = key
    title = f"{d} · {college} · {_role(role)}"
    if position:
        title += f" · {position}"
    return title + {"interview": " · Interview", "other": " · Other round"}.get(rnd, "")


def _plural(n, word):
    return f"{n} {word}{'' if n == 1 else 's'}"


# ── pages ──

def _company_page(company, rows, sightings, dups, messages, locs):
    """The page text, plus {qid: anchor} and {drive key: anchor} for links from other pages."""
    drives = defaultdict(list)
    for r in rows:
        drives[_drive_key(r)].append(r)
    order = sorted(drives, key=lambda k: (k[0], k[1]), reverse=True)
    colleges = sorted({r["college"] for r in sightings})
    topics = Counter(t for r in rows for t in r["topics"])
    lc = sum(1 for r in rows if r.get("leetcode"))

    seen = Counter()
    gh_anchor(company, seen)  # the page title takes the first anchor of its own text
    drive_anchor = {k: gh_anchor(_drive_title(k), seen) for k in order}
    q_anchor = {}
    body = []
    for k in order:
        body += [f"## {_drive_title(k)}", ""]
        for i, r in enumerate(sorted(drives[k], key=lambda r: r["qid"]), 1):
            heading = f"Q{i}. {r['title']}"
            q_anchor[r["qid"]] = gh_anchor(heading, seen)
            meta = [f"Topics: {', '.join(r['topics'])}"]
            if r.get("leetcode"):
                meta.append(f"Similar: {_lc_link(r['leetcode'])}")
            meta.append(f"Source: {_sources(r, messages, locs, '../')}")
            if dups.get(r["qid"]):
                meta.append(f"Also asked at: {_also(dups[r['qid']])}")
            body += [f"### {heading}", "", format_text(r), "", "<sub>" + " · ".join(meta) + "</sub>", ""]

    head = [f"# {company}", "",
            f"**{_plural(len(rows), 'question')}** from {_plural(len(drives), 'OA drive')} · "
            f"seen at {', '.join(colleges)} · latest {max(r['date'] for r in sightings)}", "",
            "**Topics:** " + " · ".join(f"[{t}](../topics/{slug(t)}.md) ({n})"
                                         for t, n in topics.most_common()), ""]
    if lc:
        head += [f"**LeetCode matches:** {lc} (see the [practice list](../practice.md))", ""]
    head += ["**Drives:**", ""]
    head += [f"- [{_drive_title(k)}](#{drive_anchor[k]}) · {_plural(len(drives[k]), 'question')}"
             for k in order]
    head += ["", "[← all companies](../README.md#companies)", "", "---", ""]
    return "\n".join(head + body), q_anchor, drive_anchor


def _topic_page(topic, rows, q_link):
    companies = {r["company"] for r in rows}
    has_lc = any(r.get("leetcode") for r in rows)
    out = [f"# {topic}", "",
           f"{_plural(len(rows), 'question')} from {_plural(len(companies), 'company')}, newest first. "
           f"[← all topics](../README.md#topics)", "",
           "| Date | Company | College | Question |" + (" LeetCode |" if has_lc else ""),
           "|---|---|---|---|" + ("---|" if has_lc else "")]
    for r in sorted(rows, key=lambda r: (r["date"], r["qid"]), reverse=True):
        line = (f"| {r['date']} | [{cell(r['company'])}](../companies/{slug(r['company'])}.md) "
                f"| {cell(r['college'])} | [{cell(r['title'])}](../{q_link[r['qid']]}) |")
        if has_lc:
            lc = r.get("leetcode")
            line += f" [{lc['id']}]({leetcode.url(lc)}) {lc['difficulty']} |" if lc else " |"
        out.append(line)
    return "\n".join(out) + "\n"


def _practice_page(originals, dups, q_link):
    by_problem = defaultdict(list)
    for r in originals:
        if r.get("leetcode"):
            by_problem[r["leetcode"]["id"]].append(r)
    out = ["# LeetCode practice list", "",
           "OA questions that are the same as (or a close variant of) a LeetCode problem. Each "
           "match was checked against LeetCode's own problem list. Most-asked first.", "",
           "[← back](README.md)", ""]
    if not by_problem:
        return "\n".join(out + ["No matches yet."]) + "\n"
    times = lambda rs: sum(1 + len(dups.get(r["qid"], [])) for r in rs)
    out += ["| LeetCode | Difficulty | Asked by | Times seen |", "|---|---|---|---|"]
    for pid, rs in sorted(by_problem.items(), key=lambda kv: (-times(kv[1]), kv[0])):
        lc = rs[0]["leetcode"]
        asked = ", ".join(f"[{cell(r['company'])}]({q_link[r['qid']]}) ({cell(r['college'])})" for r in rs)
        out.append(f"| [{lc['id']}. {cell(lc['title'])}]({leetcode.url(lc)}) | {lc['difficulty']} "
                   f"| {asked} | {times(rs)} |")
    return "\n".join(out) + "\n"


def build_site(rows, messages, out, now, locs=None, groups=None):
    locs = locs or {}
    originals = [r for r in rows if not r["duplicate_of"]]
    dups = defaultdict(list)
    for r in rows:
        if r["duplicate_of"]:
            dups[r["duplicate_of"]].append(r)
    by_company, by_topic = defaultdict(list), defaultdict(list)
    by_college = defaultdict(Counter)
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
    q_link, drive_link = {}, {}
    for company, rs in by_company.items():
        page, q_anchor, d_anchor = _company_page(company, rs, sightings[company], dups, messages, locs)
        (out / "companies" / f"{slug(company)}.md").write_text(page)
        q_link.update({q: f"companies/{slug(company)}.md#{a}" for q, a in q_anchor.items()})
        drive_link.update({(company,) + k: f"companies/{slug(company)}.md#{a}" for k, a in d_anchor.items()})
    for topic, rs in by_topic.items():
        (out / "topics" / f"{slug(topic)}.md").write_text(_topic_page(topic, rs, q_link))
    (out / "practice.md").write_text(_practice_page(originals, dups, q_link))

    # README
    week_ago = (now - timedelta(days=7)).date().isoformat()
    recent = defaultdict(list)
    for r in originals:
        if r["date"] >= week_ago:
            recent[r["date"]].append(r)
    colleges = {r["college"] for r in originals if r["college"] != "Unknown"}
    md = ["# OA Questions Tracker", "",
          f"**{len(originals)} questions · {len(by_company)} companies · {len(colleges)} colleges** "
          f"· updated {now:%-d %b %Y, %H:%M}", "",
          "[New this week](#new-this-week) · [Companies](#companies) · [Topics](#topics) · "
          "[Colleges](#colleges) · [LeetCode practice list](practice.md)", "",
          "Online-assessment questions shared in the OAHelper placement groups, sorted by company, "
          "topic and college. Each company page lists its OA drives, newest first. A question "
          "shared again later is folded into the first time it was seen (\"also asked at\").", "",
          *([f"Read daily from {_plural(len(groups), 'OAHelper group')}: "
             f"{sum(1 for g in groups.values() if g.get('role') == 'OA preparation')} company OA groups, "
             f"{sum(1 for g in groups.values() if g.get('role') == 'Campus')} campus groups, and the "
             "placement and intern batch groups. New groups are joined automatically.", ""]
            if groups else []),
          "## New this week", ""]
    if not recent:
        md.append("Nothing new in the last 7 days.")
    for d in sorted(recent, reverse=True):
        md += [f"**{datetime.fromisoformat(d):%a %-d %b}**", ""]
        groups = Counter((r["company"], r["college"], _drive_key(r)) for r in recent[d])
        for (c, col, key), n in sorted(groups.items(), key=lambda kv: (-kv[1], kv[0])):
            link = drive_link.get((c,) + key, f"companies/{slug(c)}.md")
            md.append(f"- [{c}]({link}) · {col} · {_plural(n, 'question')}")
        md.append("")
    md += ["## Companies", "", "| Company | Questions | Main topics | Colleges | Latest |",
           "|---|---|---|---|---|"]
    for company, rs in sorted(by_company.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        seen = sightings[company]
        cols = sorted({r["college"] for r in seen})
        cols_txt = ", ".join(cols[:3]) + (f" +{len(cols) - 3} more" if len(cols) > 3 else "")
        top = ", ".join(t for t, _ in Counter(t for r in rs for t in r["topics"]).most_common(3))
        md.append(f"| [{cell(company)}](companies/{slug(company)}.md) | {len(rs)} | {cell(top)} "
                  f"| {cell(cols_txt)} | {max(r['date'] for r in seen)} |")
    md += ["", "## Topics", ""]
    for group, topics in TOPIC_GROUPS.items():
        present = [t for t in topics if by_topic.get(t)]
        if present:
            md.append(f"**{group}:** " + " · ".join(
                f"[{t}](topics/{slug(t)}.md) {len(by_topic[t])}" for t in present) + "  ")
    older = sorted(t for t in by_topic if not any(t in ts for ts in TOPIC_GROUPS.values()))
    if older:  # topics from an older list
        md.append("**Older tags:** " + " · ".join(
            f"[{t}](topics/{slug(t)}.md) {len(by_topic[t])}" for t in older) + "  ")
    md += ["", "## Colleges", "", "<details>",
           f"<summary>Questions by college ({len(by_college)})</summary>", "",
           "| College | Companies (questions) |", "|---|---|"]
    for college in sorted(by_college):
        parts = ", ".join(f"{c} ({n})" for c, n in by_college[college].most_common())
        md.append(f"| {cell(college)} | {cell(parts)} |")
    md += ["", "</details>"]
    (out / "README.md").write_text("\n".join(md) + "\n")


def main():
    rows = read_jsonl(QUESTIONS)
    groups = {k: v for k, v in load_groups().items() if k not in SKIP_GROUPS}
    build_site(rows, Archive(ARCHIVE).by_id(), ROOT, datetime.now(), message_lines(ARCHIVE), groups)
    print(f"built pages for {len(rows)} questions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
