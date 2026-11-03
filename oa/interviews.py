"""Written interview experiences, by company: what a company asks after the online test.

data/interviews.jsonl holds one experience per line, as structured questions with a link to the
source. Only the extracted questions are kept here, not the articles themselves.

Daily, this reads SWG IIT Kharagpur's public RSS feed and adds any new placement article. Older
articles and other sources were read once and added with --merge.
"""

import argparse
import hashlib
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime
from email.utils import parsedate_to_datetime
from pathlib import Path

from oa import leetcode
from oa.common import (COMPANY_ALIASES, INTERVIEWS, MODELS, PROMPTS, QUESTIONS, TOPICS, append_jsonl, canonical,
                       log, read_jsonl, short_error)
from oa.sort import ClaudeError, UsageLimit, run_claude

FEED = "https://medium.com/feed/@swgiitkgp"
SWG = "SWG Foresight, IIT Kharagpur"
USER_AGENT = "Arigatho/1.0 (+https://github.com/MSR327/Arigatho)"
KINDS = {"oa", "technical", "hr", "case", "gd", "puzzle", "managerial", "other"}
TIERS = {"student-body", "first-person", "anonymous"}
MODES = {"on-campus", "off-campus", "unknown"}
COMPANY_SUFFIX = re.compile(r"[\s,]+(pvt\.?\s*)?(ltd\.?|limited|inc\.?|llp)\s*$", re.I)
# Same company, the name its OA page uses (keys are lowercase), so its two views link up
OA_NAMES = {
    "navi technologies": "Navi", "axxela research & analytics": "Axxela", "axtria ingenious insights": "Axtria",
    "icici bank": "ICICI", "sedemac mechatronics": "Sedemac", "samsung r&d bangalore": "Samsung Research Bangalore",
    "squarepoint capital": "Squarepoint", "zs associates": "ZS", "zomato (eternal)": "Eternal (Zomato)",
    "auctus advisors (ycp auctus)": "Auctus Advisors", "ultimate kronos group (ukg)": "UKG", "cbs (japan)": "CBS",
    "hindustan petroleum corporation": "HPCL", "micron technology": "Micron", "ey india": "EY", "slb tech": "SLB",
    "saint-gobain research india": "Saint-Gobain",
}
PERSONAL = re.compile(r"[\w.+-]+@[\w-]+\.\w+|\b(?:\+?91[ -]?)?[6-9]\d{9}\b|linkedin\.com/|\bcgpa\s*(?:of|:|=)?\s*\d",
                      re.I)

QUESTION_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "text": {"type": "string"},
        "topics": {"type": "array", "items": {"enum": TOPICS}, "minItems": 1, "maxItems": 3},
        "leetcode": {"anyOf": [
            {"type": "null"},
            {"type": "object", "properties": {"id": {"type": "integer"}, "title": {"type": "string"}},
             "required": ["id", "title"]}]},
    },
    "required": ["title", "text", "topics", "leetcode"],
}
EXTRACT_SCHEMA = {
    "type": "object",
    "properties": {
        "is_full_time_placement": {"type": "boolean"},
        "company": {"type": "string"},
        "position": {"type": "string"},
        "process": {"type": "string"},
        "rounds": {"type": "array", "items": {
            "type": "object",
            "properties": {"name": {"type": "string"}, "kind": {"enum": sorted(KINDS)},
                           "detail": {"type": "string"},
                           "questions": {"type": "array", "items": QUESTION_SCHEMA}},
            "required": ["name", "kind", "detail", "questions"]}},
        "prep": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["is_full_time_placement", "company", "position", "process", "rounds", "prep"],
}


def read_rows(path=INTERVIEWS):
    return read_jsonl(path)


def company_name(name, known=()):
    """The name the OA pages use for this company, so a company's two views link up."""
    name = COMPANY_SUFFIX.sub("", " ".join((name or "").split()))
    name = canonical(name, {**COMPANY_ALIASES, **OA_NAMES})
    return {k.casefold(): k for k in known}.get(name.casefold(), name)


def _strip(value):
    return " ".join(str(value or "").split())


def _problems_in(row):
    out = []
    if not str(row.get("url") or "").startswith("https://"):
        out.append("url: must be https")
    try:
        date.fromisoformat(str(row.get("published")))
    except ValueError:
        out.append(f"published: not a date ({row.get('published')!r})")
    if not _strip(row.get("company")):
        out.append("company: empty")
    if row.get("tier") not in TIERS:
        out.append(f"tier: {row.get('tier')!r}")
    if row.get("mode") not in MODES:
        out.append(f"mode: {row.get('mode')!r}")
    if not _strip(row.get("source")):
        out.append("source: empty")
    rounds = row.get("rounds")
    if not rounds:
        out.append("rounds: none")
    for rnd in rounds or []:
        if rnd.get("kind") not in KINDS:
            out.append(f"kind: {rnd.get('kind')!r}")
        for q in rnd.get("questions") or []:
            if not _strip(q.get("title")) or not _strip(q.get("text")):
                out.append("text: a question has no title or text")
            topics = q.get("topics") or []
            if not topics or len(topics) > 3 or not set(topics) <= set(TOPICS):
                out.append(f"topics: {topics}")
    writing = [row.get("process"), row.get("position"), *(row.get("prep") or [])]
    for rnd in rounds or []:
        writing += [rnd.get("name"), rnd.get("detail")]
        for q in rnd.get("questions") or []:
            writing += [q.get("title"), q.get("text")]
    if any(PERSONAL.search(str(w or "")) for w in writing):
        out.append("personal details in the text")
    return out


def clean(row, known=(), problems=None):
    """(normalised row, list of problems). A row with problems must not be saved."""
    found = _problems_in(row)
    if found:
        return row, found

    def match(suggestion):
        if not suggestion:
            return None
        if "slug" in suggestion:  # already checked against the real list
            return suggestion
        number = suggestion.get("id", suggestion.get("number"))
        return problems.match({"number": number, "title": suggestion.get("title")}) if problems else None

    url = row["url"].split("?")[0].rstrip("/")
    return {
        "id": hashlib.sha1(url.encode()).hexdigest()[:10],
        "url": url,
        "source": _strip(row["source"]),
        "tier": row["tier"],
        "published": str(row["published"]),
        "company": company_name(row["company"], known),
        "position": _strip(row.get("position")),
        "campus": _strip(row.get("campus")),
        "mode": row["mode"],
        "process": _strip(row.get("process")),
        "rounds": [{"name": _strip(r.get("name")), "kind": r["kind"], "detail": _strip(r.get("detail")),
                    "questions": [{"title": _strip(q["title"]), "text": q["text"].strip(),
                                   "topics": q["topics"], "leetcode": match(q.get("leetcode"))}
                                  for q in r.get("questions") or []]}
                   for r in row["rounds"]],
        "prep": [_strip(p) for p in row.get("prep") or [] if _strip(p)][:3],
    }, []


def recent(rows, now):
    """Two years of SWG, one year of everything else (what the user asked to keep)."""
    def floor(years):
        return now.replace(year=now.year - years).date().isoformat()

    return [r for r in rows
            if r["published"] >= floor(2 if r["source"].startswith("SWG") else 1)]


def shown(rows, now):
    return sorted(recent([r for r in rows if not r.get("skipped")], now),
                  key=lambda r: (r["published"], r["url"]), reverse=True)


def parse_feed(xml):
    """Placement articles in the feed: {url, title, published, text}."""
    ns = {"c": "http://purl.org/rss/1.0/modules/content/"}
    articles = []
    for item in ET.fromstring(xml).iter("item"):
        title = item.findtext("title") or ""
        if not re.search(r"placement at", title, re.I) or re.search(r"\bint(?:er|e)?r?n?ship\b|\bintern\b", title, re.I):
            continue
        body = re.sub(r"<[^>]+>", " ", item.findtext("c:encoded", default="", namespaces=ns))
        articles.append({
            "url": (item.findtext("link") or "").split("?")[0].rstrip("/"),
            "title": title,
            "published": parsedate_to_datetime(item.findtext("pubDate")).date().isoformat(),
            "text": " ".join(html.unescape(body).split()),
        })
    return articles


def fetch_feed():
    req = urllib.request.Request(FEED, headers={"User-Agent": USER_AGENT})
    return urllib.request.urlopen(req, timeout=30).read().decode()


def known_companies():
    return {r["company"] for r in read_jsonl(QUESTIONS)}


def build_prompt(article, known):
    template = (PROMPTS / "interview.md").read_text()
    names = ", ".join(sorted(known)) or "(none yet)"
    # format() would trip on any brace in the article, so the article goes in last
    return (template.replace("{companies}", names).replace("{topics}", ", ".join(TOPICS))
            .replace("{title}", article["title"]).replace("{text}", article["text"]))


def update(path=INTERVIEWS, fetch=fetch_feed, runner=run_claude, problems=None, known=None, now=None):
    """Add new placement articles from the feed. Returns how many were added."""
    now = now or datetime.now()
    known = known_companies() if known is None else known
    seen = {r["url"] for r in read_rows(path)}
    added = 0
    for article in parse_feed(fetch()):
        if article["url"] in seen:
            continue
        try:
            out = runner(build_prompt(article, known), EXTRACT_SCHEMA, model=MODELS.get("sort"))
        except UsageLimit as e:
            log(f"interviews: stopped at the usage limit, the rest wait for the next run ({e})")
            break
        except ClaudeError as e:
            log(f"interviews: could not read {article['url']}: {short_error(e)}")
            continue
        if not out.pop("is_full_time_placement", True):
            append_jsonl(path, [{"url": article["url"], "skipped": True}])  # don't pay to read it again
            continue
        row, found = clean({**out, "url": article["url"], "source": SWG, "tier": "student-body",
                            "published": article["published"], "campus": "IIT Kharagpur", "mode": "on-campus"},
                           known=known, problems=problems)
        if found:
            log(f"interviews: left out {article['url']}: {'; '.join(found)}")
            continue
        append_jsonl(path, [row])
        added += 1
    return added


def merge(files, path=INTERVIEWS, known=(), problems=None):
    """Add experiences from JSONL files. Returns (added, [(url, problems)])."""
    seen = {r["url"] for r in read_rows(path)}
    added, rejected = 0, []
    for src in files:
        for raw in read_jsonl(Path(src)):
            row, found = clean(raw, known=known, problems=problems)
            if found:
                rejected.append((raw.get("url"), found))
            elif row["url"] not in seen:
                seen.add(row["url"])
                append_jsonl(path, [row])
                added += 1
    return added, rejected


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--merge", nargs="+", help="add experiences from these JSONL files instead of the feed")
    args = ap.parse_args(argv)
    problems = leetcode.load()
    if args.merge:
        added, rejected = merge(args.merge, known=known_companies(), problems=problems)
        log(f"interviews: {added} added, {len(rejected)} rejected")
        for url, found in rejected:
            print(f"REJECTED {url}: {'; '.join(found)}")
        return 0
    try:
        log(f"interviews: {update(problems=problems)} new experiences")
    except Exception as e:  # the feed being down must not stop the daily run
        log(f"interviews: skipped this run ({short_error(e)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
