#!/bin/zsh
# Daily: fetch -> sort -> build -> commit -> push.  Usage: run_daily.sh [--no-push]
cd "${0:A:h}"
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"  # launchd has a bare PATH
PY=.venv/bin/python
mkdir -p logs
exec >> logs/daily.log 2>&1
echo "=== $(date)"

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
