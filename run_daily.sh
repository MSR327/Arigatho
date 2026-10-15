#!/bin/zsh
# Daily: fetch -> sort -> build -> commit -> push.  Usage: run_daily.sh [--no-push]
cd "${0:A:h}"
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"  # launchd has a bare PATH
PY=.venv/bin/python
mkdir -p logs
exec >> logs/daily.log 2>&1
echo "=== $(date)"

# One run at a time: a long backfill sort may still be going when the next run starts.
LOCK=logs/run.lock
if ! mkdir $LOCK 2>/dev/null; then
  if kill -0 "$(cat $LOCK/pid 2>/dev/null)" 2>/dev/null; then
    echo "previous run still going, skipping"; exit 0
  fi
  rm -rf $LOCK && mkdir $LOCK
fi
echo $$ > $LOCK/pid
trap 'rm -rf $LOCK' EXIT

/usr/bin/caffeinate -i $PY -m oa.fetch --headless || exit 1
/usr/bin/caffeinate -i $PY -m oa.sort
$PY -m oa.build

git add -A archive data companies topics README.md state.json
if ! git diff --cached --quiet; then
  git commit -q -m "Update $(date +%F)"
  if [[ "$1" != "--no-push" ]]; then
    git push -q || $PY -c 'from oa.common import notify; notify("git push failed, will retry next run")'
  fi
fi
echo "=== done $(date)"
