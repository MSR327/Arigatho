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
    q("6-1", "Amazon", "IIT Kharagpur", "2026-10-12", "LRU repost", ["Other"], dup="1-2"),
    q("7-1", "Amazon", "IIT Kharagpur", "2026-10-14", "LRU repost 2", ["Other"], dup="1-2"),
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
    assert "| [Amazon](companies/amazon.md) | 2 | IIT Bombay, IIT Kharagpur | 2026-10-14 |" in readme
    assert "Amazon · IIT Kharagpur · 2026-10-12 · 2 questions" in readme  # new this week
    assert "Nvidia · IIT Bombay" not in readme.split("## By company")[0]  # not this week
    assert "[Bit Manipulation](topics/bit-manipulation.md) | 1" in readme
    assert not (tmp_path / "companies" / "stale.md").exists()

    amazon = (tmp_path / "companies" / "amazon.md").read_text()
    assert amazon.index("Two sum") < amazon.index("LRU")
    assert "## 2026-10-12 · IIT Kharagpur · FTE" in amazon
    assert "also asked at: IIT Bombay (2026-10-13)" in amazon
    assert "also asked at: IIT Kharagpur ×2 (last 2026-10-14)" in amazon  # grouped per college
    assert "[amz.jpg](../archive/files/1-amz.jpg)" in amazon
    assert "Two sum again" not in amazon  # duplicate folded into the original

    topic = (tmp_path / "topics" / "arrays.md").read_text()
    assert "[Amazon](../companies/amazon.md)" in topic and "Two sum" in topic
