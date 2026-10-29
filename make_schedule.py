"""Install (or remove) the launchd job that runs run_daily.sh.

Usage: .venv/bin/python make_schedule.py [HH:MM ...]   (default 23:00)
       .venv/bin/python make_schedule.py --resume-only   (only the resume job; daily untouched)
       .venv/bin/python make_schedule.py --remove        (removes both jobs)
"""

import plistlib
import subprocess
import sys
from pathlib import Path

LABEL = "com.oa-tracker.daily"
RESUME = "com.oa-tracker.resume"
ROOT = Path(__file__).resolve().parent
AGENTS = Path.home() / "Library/LaunchAgents"
UID = subprocess.run(["id", "-u"], capture_output=True, text=True).stdout.strip()
LOG = str(ROOT / "logs" / "launchd.log")


def install(label, plist):
    """(Re)load one launchd job: bootout, write the plist, bootstrap."""
    path = AGENTS / f"{label}.plist"
    subprocess.run(["launchctl", "bootout", f"gui/{UID}/{label}"], capture_output=True)
    path.write_bytes(plistlib.dumps({"Label": label, "StandardOutPath": LOG,
                                     "StandardErrorPath": LOG, **plist}))
    r = subprocess.run(["launchctl", "bootstrap", f"gui/{UID}", str(path)], capture_output=True, text=True)
    return "OK" if r.returncode == 0 else r.stderr


def remove(label):
    subprocess.run(["launchctl", "bootout", f"gui/{UID}/{label}"], capture_output=True)
    (AGENTS / f"{label}.plist").unlink(missing_ok=True)


def install_resume():
    # Every 15 min resume.sh checks logs/resume_at and reruns the tracker once the window has reset.
    return install(RESUME, {"ProgramArguments": ["/bin/zsh", str(ROOT / "resume.sh")],
                            "StartInterval": 900})


if sys.argv[1:] == ["--remove"]:
    remove(LABEL)
    remove(RESUME)
    print("removed")
    sys.exit(0)
if sys.argv[1:] == ["--resume-only"]:
    print(f"{RESUME}: every 15 min, reruns after a usage-limit stop", install_resume())
    sys.exit(0)

times = sys.argv[1:] or ["23:00"]
print(f"{LABEL}: daily at {', '.join(times)}", install(LABEL, {
    "ProgramArguments": ["/bin/zsh", str(ROOT / "run_daily.sh")],
    "StartCalendarInterval": [{"Hour": int(t.split(":")[0]), "Minute": int(t.split(":")[1])}
                              for t in times],
}))
