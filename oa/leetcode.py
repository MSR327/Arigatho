"""The LeetCode problem list, used to check Claude's "similar LeetCode problem" suggestions:
one is kept only if it names a real problem (number and title agree, or the title is exact)."""

import json
import re
import time
import urllib.request

from oa.common import LEETCODE, log, short_error

API = "https://leetcode.com/api/problems/all/"
MAX_AGE = 30 * 86400  # refresh the saved list monthly
DIFFICULTY = {1: "Easy", 2: "Medium", 3: "Hard"}


def norm(title):
    return re.sub(r"[^a-z0-9]+", "", (title or "").lower())


def parse(data):
    problems = []
    for pair in data["stat_status_pairs"]:
        st = pair["stat"]
        try:
            pid = int(st["frontend_question_id"])
        except (TypeError, ValueError):
            continue
        problems.append({"id": pid, "title": st["question__title"], "slug": st["question__title_slug"],
                         "difficulty": DIFFICULTY.get(pair["difficulty"]["level"], "?")})
    return sorted(problems, key=lambda p: p["id"])


class Problems:
    def __init__(self, problems):
        self.by_id = {p["id"]: p for p in problems}
        self.by_title = {norm(p["title"]): p for p in problems}

    def __len__(self):
        return len(self.by_id)

    def match(self, suggestion):
        """The real problem for a {"number", "title"} suggestion, or None."""
        if not suggestion:
            return None
        title = norm(suggestion.get("title"))
        p = self.by_id.get(suggestion.get("number"))
        if p and norm(p["title"]) == title:
            return dict(p)
        p = self.by_title.get(title)  # number off but the exact title exists
        return dict(p) if p else None


def load(path=LEETCODE, refresh=True, fetch=None):
    """Problems from the saved list, refreshed from leetcode.com when older than a month.
    Works offline from the saved copy; empty if there is none."""
    stale = not path.exists() or time.time() - path.stat().st_mtime > MAX_AGE
    if refresh and stale:
        try:
            if fetch is None:
                req = urllib.request.Request(API, headers={"User-Agent": "Mozilla/5.0"})
                fetch = lambda: json.load(urllib.request.urlopen(req, timeout=30))
            problems = parse(fetch())
            if len(problems) > 1000:  # sanity check before replacing the saved list
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("".join(json.dumps(p) + "\n" for p in problems))
        except Exception as e:
            log(f"LeetCode list refresh failed (using the saved copy): {short_error(e)}")
    if not path.exists():
        return Problems([])
    return Problems([json.loads(line) for line in path.read_text().splitlines() if line.strip()])


def url(p):
    return f"https://leetcode.com/problems/{p['slug']}/"
