"""Practice sites for the "nearest problem" link on each coding question. Claude names a problem
and it is kept only if the site has it under that id and title, so no invented link reaches the
pages. LeetCode, Codeforces, CSES and AtCoder publish their whole problem list (saved, refreshed
monthly); GeeksforGeeks, HackerRank and CodeChef are asked about one problem at a time."""

import gzip
import html
import json
import re
import time
import urllib.error
import urllib.request

from oa import leetcode
from oa.common import CACHE, log, short_error

# In the order Claude should prefer them when two problems are about as close: students practise
# on LeetCode and GeeksforGeeks first.
SITES = ["LeetCode", "GeeksforGeeks", "Codeforces", "CSES", "AtCoder", "HackerRank", "CodeChef"]
MAX_AGE = 30 * 86400
norm = leetcode.norm


class Unreachable(Exception):
    """The site could not be asked (network or server error): try the question again next run."""


def get(url):
    """(text, final url) of a page, or None if the site says there is no such page."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept-Encoding": "gzip"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                body = gzip.decompress(body)
            return body.decode("utf-8", "replace"), r.geturl()
    except urllib.error.HTTPError as e:
        if 400 <= e.code < 500:
            return None
        raise Unreachable(f"{url}: HTTP {e.code}") from e
    except OSError as e:  # no network, timeout
        raise Unreachable(f"{url}: {short_error(e)}") from e


def key(pid):
    """Ids compare loosely: 1352C, 1352/C and 1352c are the same Codeforces problem."""
    return re.sub(r"[^a-z0-9]", "", str(pid).lower())


def same_title(a, b):
    a, b = norm(a), norm(b)
    return bool(a) and (a == b or (min(len(a), len(b)) >= 8 and (a in b or b in a)))


# ── sites that publish their whole list ──

def _leetcode():
    return [{"id": str(p["id"]), "title": p["title"], "url": leetcode.url(p),
             "name": f"LeetCode {p['id']}. {p['title']}", "short": f"LC {p['id']}",
             "level": p["difficulty"]}
            for p in leetcode.load().by_id.values()]


def _codeforces(fetch=get):
    data = json.loads(fetch("https://codeforces.com/api/problemset.problems")[0])
    return [{"id": f"{p['contestId']}{p['index']}", "title": p["name"],
             "url": f"https://codeforces.com/problemset/problem/{p['contestId']}/{p['index']}",
             "name": f"Codeforces {p['contestId']}{p['index']}. {p['name']}",
             "short": f"CF {p['contestId']}{p['index']}",
             "level": f"rated {p['rating']}" if p.get("rating") else ""}
            for p in data["result"]["problems"] if p.get("contestId")]


def _cses(fetch=get):
    page = fetch("https://cses.fi/problemset/")[0]
    return [{"id": pid, "title": html.unescape(t), "url": f"https://cses.fi/problemset/task/{pid}",
             "name": f"CSES: {html.unescape(t)}", "short": f"CSES {pid}", "level": ""}
            for pid, t in re.findall(r'href="/problemset/task/(\d+)/?">([^<]+)<', page)]


def _atcoder(fetch=get):
    data = json.loads(fetch("https://kenkoooo.com/atcoder/resources/problems.json")[0])
    return [{"id": p["id"], "title": p["name"],
             "url": f"https://atcoder.jp/contests/{p['contest_id']}/tasks/{p['id']}",
             "name": f"AtCoder {p['contest_id'].upper()} {p['problem_index']}. {p['name']}",
             "short": f"AtCoder {p['contest_id'].upper()} {p['problem_index']}", "level": ""}
            for p in data]


LISTS = {"Codeforces": (_codeforces, 5000), "CSES": (_cses, 300), "AtCoder": (_atcoder, 5000)}


def saved_list(path, download, minimum, refresh=True):
    """A site's problem list from its saved copy, downloaded again when older than a month.
    Works offline from the saved copy; empty if there is none."""
    stale = not path.exists() or time.time() - path.stat().st_mtime > MAX_AGE
    if refresh and stale:
        try:
            problems = download()
            if len(problems) >= minimum:  # sanity check before replacing the saved list
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("".join(json.dumps(p, ensure_ascii=False) + "\n" for p in problems))
        except Exception as e:
            log(f"{path.stem} list refresh failed (using the saved copy): {short_error(e)}")
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


# ── sites asked one problem at a time ──

def _gfg(pid, fetch=get):
    slug = re.sub(r"[^a-z0-9-]", "", pid.lower().strip("/").split("/")[-1])
    page = slug and fetch(f"https://www.geeksforgeeks.org/problems/{slug}/1")
    # an unknown problem still answers 200, with the site's generic title
    m = page and re.search(r"<title>\s*(.+?)\s*\|\s*Practice\s*\|\s*GeeksforGeeks", page[0])
    if not m:
        return None
    title = html.unescape(m.group(1))
    return {"id": page[1].rstrip("/").split("/")[-2], "title": title, "url": page[1],
            "name": f"GeeksforGeeks: {title}", "short": "GfG", "level": ""}


def _hackerrank(pid, fetch=get):
    slug = re.sub(r"[^a-z0-9-]", "", pid.lower())
    page = slug and fetch(f"https://www.hackerrank.com/rest/contests/master/challenges/{slug}")
    model = page and json.loads(page[0]).get("model")
    if not model or not model.get("name"):
        return None
    return {"id": slug, "title": model["name"], "url": f"https://www.hackerrank.com/challenges/{slug}/problem",
            "name": f"HackerRank: {model['name']}", "short": "HackerRank",
            "level": model.get("difficulty_name") or ""}


def _codechef(pid, fetch=get):
    code = re.sub(r"[^A-Za-z0-9_]", "", pid).upper()
    page = code and fetch(f"https://www.codechef.com/api/contests/PRACTICE/problems/{code}")
    data = page and json.loads(page[0])
    if not data or data.get("status") != "success" or not data.get("problem_name"):
        return None
    rating = data.get("difficulty_rating")
    return {"id": code, "title": data["problem_name"], "url": f"https://www.codechef.com/problems/{code}",
            "name": f"CodeChef {code}: {data['problem_name']}", "short": f"CodeChef {code}",
            "level": f"rated {rating}" if rating and str(rating) != "0" else ""}


LOOKUPS = {"GeeksforGeeks": _gfg, "HackerRank": _hackerrank, "CodeChef": _codechef}


class Sites:
    def __init__(self, lists, fetch=get, gap=1.0):
        """lists: {site: [problem, ...]} for the sites that publish one; gap: seconds to wait
        before each question to a site asked problem by problem."""
        self.by_id = {s: {key(p["id"]): p for p in ps} for s, ps in lists.items()}
        self.by_title = {s: {norm(p["title"]): p for p in ps} for s, ps in lists.items()}
        self.fetch, self.gap = fetch, gap

    def check(self, pick):
        """The real problem for a {"site", "id", "title"} pick, or None.
        Raises Unreachable when the site could not be asked."""
        site, pid, title = pick.get("site"), str(pick.get("id") or ""), pick.get("title")
        if site in self.by_id:
            p = self.by_id[site].get(key(pid))
            if p and same_title(p["title"], title):
                return dict(p, site=site)
            p = self.by_title[site].get(norm(title))  # id off but the exact title exists
            return dict(p, site=site) if p else None
        if site in LOOKUPS and pid:
            time.sleep(self.gap)
            p = LOOKUPS[site](pid, self.fetch)
            return dict(p, site=site) if p and same_title(p["title"], title) else None
        return None


def load(refresh=True):
    lists = {"LeetCode": _leetcode()}
    for site, (download, minimum) in LISTS.items():
        lists[site] = saved_list(CACHE / f"{site.lower()}.jsonl", download, minimum, refresh)
    return Sites(lists)
