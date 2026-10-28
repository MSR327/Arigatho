"""Paths, settings and small helpers shared by every stage."""

import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "archive"
FILES = ARCHIVE / "files"
DATA = ROOT / "data"
QUESTIONS = DATA / "questions.jsonl"
STATE = ROOT / "state.json"
LOGS = ROOT / "logs"
PROFILE = ROOT / "chrome_profile"
PROMPTS = ROOT / "prompts"
LEETCODE = DATA / "leetcode.jsonl"
GITHUB_REPO = "MSR327/Arigatho"

BASE_URL = "https://www.oahelper.in"
# Every joined OAHelper group is read, except these (an event and the site team's chat).
SKIP_GROUPS = {"navratri-challenge", "oahelper-team"}
GROUPS_FILE = DATA / "groups.json"  # name, company/college and kind of each group, saved by fetch
BACKFILL_FROM = "2026-07-20"
REQUEST_GAP = 1.0  # seconds between requests to oahelper.in
BATCH_SIZE = 40  # messages per claude -p call
# Cheapest model that does each job well, to spare the Claude plan: sorting reads screenshots and
# whole conversations; matching reposts and re-tagging are simple text comparisons.
MODELS = {"sort": "sonnet", "dedupe": "haiku", "enrich": "haiku"}
# Stop starting claude calls once this share of the plan's 5-hour window is used, so the user
# keeps the rest for themselves; the run stops cleanly and the next one continues.
RESERVE_FROM = 0.90
KEYCHAIN_SERVICE = "oa-tracker"

# Grouped for the README; TOPICS (the flat list Claude chooses from) is built from these.
TOPIC_GROUPS = {
    "DSA": ["Arrays", "Strings", "Hashing", "Two Pointers", "Sliding Window", "Binary Search",
            "Sorting", "Greedy", "DP", "Graphs", "Trees", "Heaps", "Stack/Queue", "Linked List",
            "Math", "Bit Manipulation", "Recursion/Backtracking"],
    "CS & software": ["SQL", "OS/DBMS/CN MCQ", "OOP", "Code Output (C/C++/Java/Python)",
                      "Python & Pandas", "ML/AI", "Web Dev", "Software Engineering"],
    "EE & core": ["Circuits", "Analog Electronics", "Digital Electronics", "Signals & Systems",
                  "Control Systems", "Communication", "Mechanical"],
    "Finance & business": ["Finance", "Guesstimates & Cases"],
    "General": ["Aptitude", "Verbal", "Puzzles", "HR & Behavioral", "OA Format", "Other"],
}
TOPICS = [t for group in TOPIC_GROUPS.values() for t in group]


# Same place, different spellings (keys are lowercase). Applied to every question.
COLLEGE_ALIASES = {
    "iit (ism) dhanbad": "IIT Dhanbad", "iit ism dhanbad": "IIT Dhanbad",
    "ism dhanbad": "IIT Dhanbad", "nit karnataka": "NIT Surathkal",
    "nitk surathkal": "NIT Surathkal", "nit tiruchirappalli": "NIT Trichy",
    "iit (bhu) varanasi": "IIT BHU", "iit bhu varanasi": "IIT BHU", "iit kgp": "IIT Kharagpur",
    "dtu": "Delhi Technological University",
    "bhu": "IIT BHU",  # the groups are IIT/NIT/IIIT-only, so a "_BHU" poster is from IIT (BHU)
}
COMPANY_ALIASES = {
    "eternal": "Eternal (Zomato)", "zomato": "Eternal (Zomato)", "amex": "American Express",
    "info edge": "InfoEdge",
}


def load_groups():
    """{slug: {"name", "company", "role"}} as last saved by fetch."""
    return json.loads(GROUPS_FILE.read_text()) if GROUPS_FILE.exists() else {}


def canonical(name, aliases):
    name = " ".join(name.split())
    return aliases.get(name.lower(), name)


def log(msg):
    line = f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}"
    print(line, flush=True)
    LOGS.mkdir(exist_ok=True)
    with (LOGS / "run.log").open("a") as f:
        f.write(line + "\n")


def short_error(e):
    """One-line error text. Playwright errors append a call log with request cookies."""
    first = (str(e).splitlines() or [""])[0]
    return f"{type(e).__name__}: {first[:160]}"


def notify(msg):
    safe = msg.replace('"', "'")
    subprocess.run(["osascript", "-e", f'display notification "{safe}" with title "OA tracker"'],
                   check=False)


def load_creds(service=KEYCHAIN_SERVICE):
    r = subprocess.run(["security", "find-generic-password", "-s", service, "-g"],
                       capture_output=True, text=True)
    acct = re.search(r'"acct"<blob>="([^"]*)"', r.stdout)
    pwd = re.search(r'^password: "(.*)"$', r.stderr, re.M)
    return (acct.group(1), pwd.group(1)) if r.returncode == 0 and acct and pwd else None


def save_creds(user, pwd, service=KEYCHAIN_SERVICE):
    subprocess.run(["security", "add-generic-password", "-U", "-s", service, "-a", user, "-w", pwd],
                   capture_output=True, check=False)


def read_jsonl(path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def append_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
