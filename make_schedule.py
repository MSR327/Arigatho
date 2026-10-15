"""Install (or remove) the launchd job that runs run_daily.sh.

Usage: .venv/bin/python make_schedule.py [HH:MM ...]   (default 23:00)
       .venv/bin/python make_schedule.py --remove
"""

import plistlib
import subprocess
import sys
from pathlib import Path

LABEL = "com.oa-tracker.daily"
ROOT = Path(__file__).resolve().parent
PLIST = Path.home() / "Library/LaunchAgents" / f"{LABEL}.plist"
UID = subprocess.run(["id", "-u"], capture_output=True, text=True).stdout.strip()

subprocess.run(["launchctl", "bootout", f"gui/{UID}/{LABEL}"], capture_output=True)
if sys.argv[1:] == ["--remove"]:
    PLIST.unlink(missing_ok=True)
    print("removed")
    sys.exit(0)

times = sys.argv[1:] or ["23:00"]
PLIST.write_bytes(plistlib.dumps({
    "Label": LABEL,
    "ProgramArguments": ["/bin/zsh", str(ROOT / "run_daily.sh")],
    "StartCalendarInterval": [{"Hour": int(t.split(":")[0]), "Minute": int(t.split(":")[1])}
                              for t in times],
    "StandardOutPath": str(ROOT / "logs" / "launchd.log"),
    "StandardErrorPath": str(ROOT / "logs" / "launchd.log"),
}))
r = subprocess.run(["launchctl", "bootstrap", f"gui/{UID}", str(PLIST)], capture_output=True, text=True)
print(f"{LABEL}: daily at {', '.join(times)}", "OK" if r.returncode == 0 else r.stderr)
