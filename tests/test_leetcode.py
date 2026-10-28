import json
import os
import time

from oa import leetcode

RAW = {"stat_status_pairs": [
    {"stat": {"frontend_question_id": i, "question__title": f"Problem {i}",
              "question__title_slug": f"problem-{i}"}, "difficulty": {"level": 1 + i % 3}}
    for i in range(1, 1201)] + [
    {"stat": {"frontend_question_id": "LCP 1", "question__title": "x", "question__title_slug": "x"},
     "difficulty": {"level": 1}}]}


def test_load_saves_and_matches(tmp_path):
    path = tmp_path / "lc.jsonl"
    p = leetcode.load(path, fetch=lambda: RAW)
    assert len(p) == 1200 and path.exists()  # the non-numeric id is skipped
    assert p.match({"number": 7, "title": "problem 7"})["slug"] == "problem-7"
    assert p.match({"number": 9, "title": "Problem 7"})["id"] == 7  # exact title wins
    assert p.match({"number": 7, "title": "Something else"}) is None  # invented: dropped
    assert p.match(None) is None


def test_load_works_offline_from_saved_copy(tmp_path):
    path = tmp_path / "lc.jsonl"
    leetcode.load(path, fetch=lambda: RAW)
    old = time.time() - 40 * 86400
    os.utime(path, (old, old))
    p = leetcode.load(path, fetch=lambda: (_ for _ in ()).throw(OSError("offline")))
    assert len(p) == 1200


def test_tiny_reply_does_not_replace_the_list(tmp_path):
    path = tmp_path / "lc.jsonl"
    leetcode.load(path, fetch=lambda: RAW)
    os.utime(path, (0, 0))
    p = leetcode.load(path, fetch=lambda: {"stat_status_pairs": RAW["stat_status_pairs"][:5]})
    assert len(p) == 1200
