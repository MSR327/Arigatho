from collections import Counter
from datetime import datetime

import pytest

from oa.build import build_site, format_text, gh_anchor, slug, split_options

LC3 = {"id": 3, "title": "Longest Substring Without Repeating Characters",
       "slug": "longest-substring-without-repeating-characters", "difficulty": "Medium"}


def q(qid, company, college, d, title, topics, dup=None, src=None, lc=None, text=None):
    return {"qid": qid, "company": company, "college": college, "date": d, "role": "fte",
            "title": title, "text": text or f"Text of {title}", "topics": topics,
            "source_ids": src or [int(qid.split("-")[0])], "duplicate_of": dup, "leetcode": lc}


ROWS = [
    q("1-1", "Amazon", "IIT Kharagpur", "2026-10-12", "Two sum", ["Arrays", "Hashing"], src=[1]),
    q("1-2", "Amazon", "IIT Kharagpur", "2026-10-12", "LRU", ["Other"], src=[1]),
    q("5-1", "Amazon", "IIT Bombay", "2026-10-13", "Two sum again", ["Arrays"], dup="1-1"),
    q("3-1", "Nvidia", "IIT Bombay", "2026-08-01", "Bit tricks", ["Bit Manipulation"], src=[3]),
    q("6-1", "Amazon", "IIT Kharagpur", "2026-10-12", "LRU repost", ["Other"], dup="1-2"),
    q("7-1", "Amazon", "IIT Kharagpur", "2026-10-14", "LRU repost 2", ["Other"], dup="1-2"),
    q("8-1", "Amazon", "IIT Kharagpur", "2026-10-14", "Longest unique substring", ["Strings"], lc=LC3),
]
MSGS = {1: {"id": 1, "group": "inter-iit", "sent_at": "2026-10-12T10:00:00+00:00",
            "attachment": {"name": "amz.jpg", "mime": "image/jpeg", "size": 1, "is_image": True}},
        3: {"id": 3, "group": "inter-nit", "sent_at": "2026-08-01T10:00:00+00:00",
            "attachment": None},
        5: {"id": 5, "group": "inter-iit", "sent_at": "2026-10-13T10:00:00+00:00",
            "attachment": None},
        8: {"id": 8, "group": "inter-iit", "sent_at": "2026-10-14T10:00:00+00:00",
            "attachment": None}}
LOCS = {8: ("archive/inter-iit/2026-10.jsonl", 42)}
NOW = datetime(2026, 10, 15, 23, 0)


def test_slug():
    assert slug("L.E.K. Consulting") == "l-e-k-consulting"
    assert slug("Stack/Queue") == "stack-queue"


def test_gh_anchor_matches_github_and_numbers_repeats():
    seen = Counter()
    assert gh_anchor("2026-10-12 · IIT Kharagpur · FTE", seen) == "2026-10-12--iit-kharagpur--fte"
    assert gh_anchor("Q1. Two sum (easy)!", seen) == "q1-two-sum-easy"
    assert gh_anchor("Q1. Two sum (easy)!", seen) == "q1-two-sum-easy-1"


@pytest.mark.parametrize("text,want", [
    ("Pick one. A. red B. green C. blue D. none",
     "Pick one.\n\n- **A.** red\n- **B.** green\n- **C.** blue\n- **D.** none"),
    ("Choose: (a) x is 1 (b) y (c) z", "Choose:\n\n- **A.** x is 1\n- **B.** y\n- **C.** z"),
    ("Only A. and B. here", "Only A. and B. here"),            # fewer than three options
    ("Rank B. C. D. order", "Rank B. C. D. order"),            # does not start at A
    ("Q\nA. one\nB. two\nC. three", "Q\nA. one\nB. two\nC. three"),  # already one per line
])
def test_split_options(text, want):
    assert split_options(text) == want


def test_format_text_plain_rows():
    row = {"text": "Grid:\n1 2\n3 4\n#include<vector> is used\n```\nkeep <this>\n```"}
    out = format_text(row)
    assert "Grid:  \n1 2  \n3 4  \n" in out                    # line breaks kept
    assert "\\#include&lt;vector> is used" in out             # not a heading, not an HTML tag
    assert "```\nkeep <this>\n```" in out                      # code fences untouched
    assert format_text({"text": "**md** <b>", "md": True}) == "**md** <b>"


def test_build_site(tmp_path):
    (tmp_path / "companies").mkdir()
    (tmp_path / "companies" / "stale.md").write_text("old")
    build_site(ROWS, MSGS, tmp_path, NOW, LOCS)
    readme = (tmp_path / "README.md").read_text()
    assert "**4 questions · 2 companies · 2 colleges**" in readme  # duplicates are not counted
    assert ("| [Amazon](companies/amazon.md) | 3 | Arrays, Hashing, Other "
            "| IIT Bombay, IIT Kharagpur | 2026-10-14 |") in readme
    new = readme.split("## New this week")[1].split("## Companies")[0]
    assert "**Wed 14 Oct**" in new and "**Mon 12 Oct**" in new
    assert ("- [Amazon](companies/amazon.md#2026-10-12--iit-kharagpur--fte) · IIT Kharagpur · "
            "2 questions") in new
    assert "Nvidia" not in new  # not this week
    assert "**DSA:** [Arrays](topics/arrays.md) 1 · [Strings](topics/strings.md) 1" in readme
    assert "[LeetCode practice list](practice.md)" in readme
    assert not (tmp_path / "companies" / "stale.md").exists()

    amazon = (tmp_path / "companies" / "amazon.md").read_text()
    assert amazon.startswith("# Amazon\n\n**3 questions** from 2 OA drives")
    assert "- [2026-10-12 · IIT Kharagpur · FTE](#2026-10-12--iit-kharagpur--fte) · 2 questions" in amazon
    assert amazon.index("Longest unique substring") < amazon.index("Two sum")  # newest drive first
    assert "## 2026-10-12 · IIT Kharagpur · FTE" in amazon
    assert "Also asked at: IIT Bombay (2026-10-13)" in amazon
    assert "Also asked at: IIT Kharagpur ×2 (last 2026-10-14)" in amazon  # grouped per college
    assert "[amz.jpg](../archive/files/1-amz.jpg)" in amazon
    assert "[chat, 14 Oct](../archive/inter-iit/2026-10.jsonl#L42)" in amazon  # exact line
    assert ("Similar: [LeetCode 3. Longest Substring Without Repeating Characters]"
            "(https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Medium)") in amazon
    assert "Two sum again" not in amazon  # duplicate folded into the original

    topic = (tmp_path / "topics" / "arrays.md").read_text()
    assert "[Amazon](../companies/amazon.md)" in topic
    assert "[Two sum](../companies/amazon.md#q1-two-sum)" in topic
    strings = (tmp_path / "topics" / "strings.md").read_text()
    assert "[3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) Medium" in strings

    practice = (tmp_path / "practice.md").read_text()
    assert ("| [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/"
            "longest-substring-without-repeating-characters/) | Medium | "
            "[Amazon](companies/amazon.md#q1-longest-unique-substring) (IIT Kharagpur) | 1 |") in practice
