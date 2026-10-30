import json
import os

import pytest

from oa import sites

CF_API = {"status": "OK", "result": {"problems": [
    {"contestId": 1352, "index": "C", "name": "K-th Not Divisible by n", "rating": 1200},
    {"contestId": 2277, "index": "F", "name": "Token Re-Moving"}]}}
CSES = '<li><a href="/problemset/task/1068">Weird Algorithm</a></li><li><a href="/problemset/task/1638">Grid Paths</a>'
ATCODER = [{"id": "dp_a", "contest_id": "dp", "problem_index": "A", "name": "Frog 1"}]
PAGES = {
    "https://codeforces.com/api/problemset.problems": json.dumps(CF_API),
    "https://cses.fi/problemset/": CSES,
    "https://kenkoooo.com/atcoder/resources/problems.json": json.dumps(ATCODER),
    "https://www.geeksforgeeks.org/problems/trapping-rain-water/1": (
        "<title>Trapping Rain Water | Practice | GeeksforGeeks </title>",
        "https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1"),
    # an unknown problem still answers, with the generic title
    "https://www.geeksforgeeks.org/problems/made-up/1": "<title>Practice | GeeksforGeeks | A computer science portal</title>",
    "https://www.hackerrank.com/rest/contests/master/challenges/maximum-subarray-sum":
        json.dumps({"model": {"name": "Maximum Subarray Sum", "difficulty_name": "Hard"}}),
    "https://www.codechef.com/api/contests/PRACTICE/problems/FLOW001":
        json.dumps({"status": "success", "problem_name": "Add Two Numbers", "difficulty_rating": "400"}),
    "https://www.codechef.com/api/contests/PRACTICE/problems/NOPE": json.dumps({"status": "error"}),
}


def fetch(url):
    page = PAGES.get(url)
    if page is None:
        return None  # the site's 404
    if url.endswith("/gone/1"):
        raise sites.Unreachable(url)
    return page if isinstance(page, tuple) else (page, url)


def lists():
    return {"LeetCode": [{"id": "239", "title": "Sliding Window Maximum", "url": "u", "name": "n",
                          "short": "s", "level": "Hard"}],
            "Codeforces": sites._codeforces(fetch), "CSES": sites._cses(fetch), "AtCoder": sites._atcoder(fetch)}


def test_parsers():
    cf, cses, ac = (lists()[s] for s in ("Codeforces", "CSES", "AtCoder"))
    assert cf[0]["url"] == "https://codeforces.com/problemset/problem/1352/C" and cf[0]["level"] == "rated 1200"
    assert cf[1]["level"] == ""  # not rated yet
    assert [p["title"] for p in cses] == ["Weird Algorithm", "Grid Paths"] and cses[1]["short"] == "CSES 1638"
    assert ac[0]["url"] == "https://atcoder.jp/contests/dp/tasks/dp_a" and ac[0]["name"] == "AtCoder DP A. Frog 1"


@pytest.mark.parametrize("pick,name", [
    ({"site": "LeetCode", "id": "239", "title": "sliding window maximum"}, "n"),
    ({"site": "Codeforces", "id": "1352/C", "title": "K-th Not Divisible by n"},
     "Codeforces 1352C. K-th Not Divisible by n"),                                      # loose id
    ({"site": "Codeforces", "id": "9999Z", "title": "K-th Not Divisible by n"},
     "Codeforces 1352C. K-th Not Divisible by n"),                                      # exact title, id off
    ({"site": "Codeforces", "id": "1352C", "title": "Something else"}, None),           # invented
    ({"site": "CSES", "id": "1068", "title": "Weird Algorithm"}, "CSES: Weird Algorithm"),
    ({"site": "AtCoder", "id": "dp_a", "title": "Frog 1"}, "AtCoder DP A. Frog 1"),
    ({"site": "GeeksforGeeks", "id": "trapping-rain-water", "title": "Trapping Rain Water"},
     "GeeksforGeeks: Trapping Rain Water"),
    ({"site": "GeeksforGeeks", "id": "made-up", "title": "Made Up"}, None),
    ({"site": "GeeksforGeeks", "id": "trapping-rain-water", "title": "Two Sum"}, None),  # wrong title
    ({"site": "HackerRank", "id": "maximum-subarray-sum", "title": "Maximum Subarray Sum"},
     "HackerRank: Maximum Subarray Sum"),
    ({"site": "HackerRank", "id": "no-such", "title": "x"}, None),
    ({"site": "CodeChef", "id": "flow001", "title": "Add Two Numbers"}, "CodeChef FLOW001: Add Two Numbers"),
    ({"site": "CodeChef", "id": "NOPE", "title": "x"}, None),
    ({"site": "Kattis", "id": "1", "title": "x"}, None),
])
def test_check(pick, name):
    p = sites.Sites(lists(), fetch, gap=0).check(pick)
    assert (p and p["name"]) == name
    if p:
        assert p["site"] == pick["site"]


def test_check_keeps_the_canonical_link():
    p = sites.Sites({}, fetch, gap=0).check({"site": "GeeksforGeeks", "id": "trapping-rain-water",
                                             "title": "Trapping Rain Water"})
    assert p["url"] == "https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1"
    assert p["id"] == "trapping-rain-water-1587115621"


def test_saved_list_refreshes_monthly_and_works_offline(tmp_path):
    path = tmp_path / "cf.jsonl"
    assert len(sites.saved_list(path, lambda: sites._codeforces(fetch), 2)) == 2
    os.utime(path, (0, 0))

    def offline():
        raise sites.Unreachable("no network")
    assert len(sites.saved_list(path, offline, 2)) == 2               # the saved copy
    assert len(sites.saved_list(path, lambda: [{"id": "1"}], 2)) == 2  # a tiny reply is not saved
    assert sites.saved_list(tmp_path / "none.jsonl", offline, 2) == []
