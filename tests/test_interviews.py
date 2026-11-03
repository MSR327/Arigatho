import json
from datetime import datetime

import pytest

from oa import interviews as iv
from oa import sort
from oa.build import build_site
from oa.leetcode import Problems
from oa.sort import UsageLimit

KADANE = {"id": 53, "title": "Maximum Subarray", "slug": "maximum-subarray", "difficulty": "Medium"}
SWG = "https://medium.com/@swgiitkgp/foresight-2025-placement-at-acme-1a2b3c"


def question(**over):
    return {"title": "Max subarray", "text": "Find the largest sum.", "topics": ["Arrays", "DP"],
            "leetcode": None, **over}


def experience(**over):
    return {"url": SWG, "source": "SWG Foresight, IIT Kharagpur", "tier": "student-body",
            "published": "2025-11-20", "company": "Acme", "position": "SDE", "campus": "IIT Kharagpur",
            "mode": "on-campus", "process": "Online test, then one technical interview.",
            "rounds": [{"name": "Technical interview 1", "kind": "technical", "detail": "",
                        "questions": [question()]}],
            "prep": ["Revise DP"], **over}


def test_clean_keeps_a_good_experience_and_gives_it_a_stable_id():
    row, problems = iv.clean(experience())

    assert problems == []
    assert row["id"] == iv.clean(experience())[0]["id"]
    assert row["company"] == "Acme"


def test_an_anonymous_post_is_allowed_and_keeps_its_label():
    row, problems = iv.clean(experience(tier="anonymous", source="Reddit r/developersIndia"))

    assert problems == []
    assert row["tier"] == "anonymous"


def test_clean_uses_the_company_names_the_oa_pages_use():
    known = {"Bluestone", "Navi", "Eternal (Zomato)"}

    assert iv.clean(experience(company="BlueStone"), known=known)[0]["company"] == "Bluestone"
    assert iv.clean(experience(company="Navi Technologies"), known=known)[0]["company"] == "Navi"
    assert iv.clean(experience(company="ZOMATO"), known=known)[0]["company"] == "Eternal (Zomato)"
    assert iv.clean(experience(company="Quant Solar Pvt. Ltd."), known=known)[0]["company"] == "Quant Solar"


@pytest.mark.parametrize("over, expected", [
    ({"url": "http://example.com/a"}, "url"),
    ({"published": "last year"}, "published"),
    ({"company": " "}, "company"),
    ({"tier": "blog"}, "tier"),
    ({"mode": "remote"}, "mode"),
    ({"rounds": [{"name": "x", "kind": "chat", "detail": "", "questions": []}]}, "kind"),
    ({"rounds": []}, "rounds"),
])
def test_clean_reports_what_is_wrong(over, expected):
    _, problems = iv.clean(experience(**over))

    assert any(expected in p for p in problems)


def test_clean_rejects_invented_topics_and_empty_questions():
    round_ = {"name": "x", "kind": "technical", "detail": "",
              "questions": [question(topics=["Vibes"])]}
    assert any("topics" in p for p in iv.clean(experience(rounds=[round_]))[1])

    round_ = {"name": "x", "kind": "technical", "detail": "", "questions": [question(text=" ")]}
    assert any("text" in p for p in iv.clean(experience(rounds=[round_]))[1])


@pytest.mark.parametrize("text", ["Mail me at someone@example.com", "Call 9876543210",
                                  "See linkedin.com/in/someone", "I had a CGPA of 9.1"])
def test_clean_flags_personal_details_anywhere_in_the_row(text):
    round_ = {"name": "x", "kind": "hr", "detail": "", "questions": [question(text=text)]}

    assert any("personal" in p for p in iv.clean(experience(rounds=[round_]))[1])
    assert any("personal" in p for p in iv.clean(experience(prep=[text]))[1])


def test_clean_checks_a_leetcode_match_against_the_real_list():
    problems = Problems([KADANE])
    good = question(leetcode={"id": 53, "title": "Maximum Subarray"})
    wrong = question(leetcode={"id": 99999, "title": "Not a real problem"})
    rounds = [{"name": "x", "kind": "technical", "detail": "", "questions": [good, wrong]}]

    qs = iv.clean(experience(rounds=rounds), problems=problems)[0]["rounds"][0]["questions"]

    assert qs[0]["leetcode"] == KADANE
    assert qs[1]["leetcode"] is None


def test_recent_keeps_two_years_of_swg_and_one_year_of_everything_else():
    now = datetime(2026, 11, 4)
    rows = [{"source": "SWG Foresight, IIT Kharagpur", "published": "2024-11-04"},
            {"source": "SWG Foresight, IIT Kharagpur", "published": "2024-11-03"},
            {"source": "GeeksforGeeks", "published": "2025-11-04"},
            {"source": "GeeksforGeeks", "published": "2025-11-03"}]

    assert [r["published"] for r in iv.recent(rows, now)] == ["2024-11-04", "2025-11-04"]


def feed(*items):
    body = "".join(
        f"<item><title><![CDATA[{t}]]></title><link>{u}?source=rss</link>"
        f"<pubDate>Sun, 23 Nov 2025 10:00:00 GMT</pubDate><content:encoded><![CDATA[<p>Round <b>one</b></p>]]>"
        f"</content:encoded></item>" for t, u in items)
    return ('<rss xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0"><channel>'
            f"{body}</channel></rss>")


def test_parse_feed_takes_placements_only():
    xml = feed(("FORESIGHT(2025) | Placement at Acme | A Person", SWG),
               ("FORESIGHT(2025) | Internship at Acme | A Person", "https://medium.com/@swgiitkgp/b"),
               ("Interdisciplinary Switchover Chronicles", "https://medium.com/@swgiitkgp/c"))

    articles = iv.parse_feed(xml)

    assert [a["url"] for a in articles] == [SWG]
    assert articles[0]["published"] == "2025-11-23"
    assert articles[0]["text"] == "Round one"


@pytest.mark.parametrize("title, kept", [("Placement at International Paper", True), ("Placement at Intel", True),
                                         ("Placement at Acme | Intership", False), ("Internship at Acme", False),
                                         ("Intern to Placement at Acme", False)])
def test_parse_feed_tells_internships_from_company_names(title, kept):
    assert bool(iv.parse_feed(feed((title, SWG)))) is kept


def extracted(**over):
    row = experience()
    for key in ("url", "source", "tier", "published", "campus", "mode"):
        row.pop(key)
    return {"is_full_time_placement": True, **row, **over}


def test_update_extracts_only_new_articles_and_saves_them(tmp_path):
    path = tmp_path / "interviews.jsonl"
    path.write_text(json.dumps(iv.clean(experience(url="https://medium.com/@swgiitkgp/old"))[0]) + "\n")
    xml = feed(("Placement at Old", "https://medium.com/@swgiitkgp/old"), ("Placement at Acme", SWG))
    prompts = []

    added = iv.update(path, fetch=lambda: xml, runner=lambda p, s, model=None: prompts.append(p) or extracted(),
                      now=datetime(2026, 1, 1))

    assert added == 1
    assert len(prompts) == 1
    rows = iv.read_rows(path)
    assert len(rows) == 2
    assert rows[1]["source"] == "SWG Foresight, IIT Kharagpur"
    assert rows[1]["campus"] == "IIT Kharagpur"


def test_update_remembers_an_article_that_is_not_a_placement(tmp_path):
    path = tmp_path / "interviews.jsonl"
    xml = feed(("Placement at Acme", SWG))
    calls = []

    def runner(p, s, model=None):
        calls.append(p)
        return extracted(is_full_time_placement=False)

    iv.update(path, fetch=lambda: xml, runner=runner, now=datetime(2026, 1, 1))
    iv.update(path, fetch=lambda: xml, runner=runner, now=datetime(2026, 1, 1))

    assert len(calls) == 1
    assert [r for r in iv.read_rows(path) if not r.get("skipped")] == []


def test_update_stops_at_the_usage_limit_and_keeps_earlier_results(tmp_path):
    path = tmp_path / "interviews.jsonl"
    other = "https://medium.com/@swgiitkgp/second"
    xml = feed(("Placement at Acme", SWG), ("Placement at Other", other))
    answers = iter([extracted(), UsageLimit("limit")])

    def runner(p, s, model=None):
        a = next(answers)
        if isinstance(a, Exception):
            raise a
        return a

    assert iv.update(path, fetch=lambda: xml, runner=runner, now=datetime(2026, 1, 1)) == 1
    assert [r["url"] for r in iv.read_rows(path)] == [SWG]


def test_update_asks_the_resume_job_to_continue_after_the_limit_resets(tmp_path, monkeypatch):
    monkeypatch.setitem(sort.USAGE, "resets_at", 1000)
    xml = feed(("Placement at Acme", SWG))

    def runner(p, s, model=None):
        raise UsageLimit("limit")

    iv.update(tmp_path / "interviews.jsonl", fetch=lambda: xml, runner=runner, now=datetime(2026, 1, 1))

    assert (tmp_path / "logs" / "resume_at").read_text() == "1300"  # 5 minutes after the reset


def test_update_leaves_out_an_extraction_that_fails_the_checks(tmp_path):
    path = tmp_path / "interviews.jsonl"
    xml = feed(("Placement at Acme", SWG))
    bad = extracted(prep=["Mail me at someone@example.com"])

    assert iv.update(path, fetch=lambda: xml, runner=lambda p, s, model=None: bad,
                     now=datetime(2026, 1, 1)) == 0
    assert iv.read_rows(path) == []


def test_merge_adds_new_urls_and_reports_rejects(tmp_path):
    src = tmp_path / "agent.jsonl"
    bad = experience(url="https://example.com/bad", published="soon")
    src.write_text("\n".join(json.dumps(r) for r in [experience(), experience(), bad]) + "\n")
    path = tmp_path / "interviews.jsonl"

    added, rejected = iv.merge([str(src)], path)  # paths arrive as text from the command line

    assert added == 1
    assert [url for url, _ in rejected] == ["https://example.com/bad"]
    assert [r["url"] for r in iv.read_rows(path)] == [SWG]


def built(tmp_path, rows):
    build_site([], {}, tmp_path, datetime(2026, 11, 4), interviews=rows)
    return json.loads((tmp_path / "site" / "interviews.json").read_text())


def test_build_writes_the_site_data_and_a_page_per_company(tmp_path):
    row = iv.clean(experience(rounds=[{"name": "Technical interview 1", "kind": "technical", "detail": "45 min",
                                       "questions": [question(leetcode=KADANE)]}]))[0]

    data = built(tmp_path, [row])

    x = data["experiences"][0]
    assert x["c"] == "Acme"
    assert x["url"] == SWG
    q = x["rounds"][0]["qs"][0]
    assert q["t"] == "Max subarray"
    assert q["lc"]["u"] == "https://leetcode.com/problems/maximum-subarray/"
    page = (tmp_path / "interviews" / "acme.md").read_text()
    assert "Technical interview 1" in page
    assert "Max subarray" in page
    assert SWG in page
    assert "Acme" in (tmp_path / "interviews" / "README.md").read_text()


def test_build_leaves_out_old_and_skipped_rows(tmp_path):
    old = iv.clean(experience(published="2020-01-01", url="https://example.com/old"))[0]
    skipped = {"url": "https://example.com/skip", "skipped": True}

    assert built(tmp_path, [old, skipped])["experiences"] == []


def test_build_lists_newest_first_and_counts_only_shown_rows(tmp_path):
    a = iv.clean(experience(url="https://example.com/a", published="2025-12-01"))[0]
    b = iv.clean(experience(url="https://example.com/b", published="2026-02-01"))[0]

    data = built(tmp_path, [a, b])

    assert [x["url"] for x in data["experiences"]] == ["https://example.com/b", "https://example.com/a"]
    assert data["count"] == 2


def test_readme_points_to_the_interviews(tmp_path):
    built(tmp_path, [iv.clean(experience())[0]])

    assert "interviews/README.md" in (tmp_path / "README.md").read_text()
