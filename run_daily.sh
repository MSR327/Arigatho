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

# After a wake from sleep Wi-Fi can take a while; without this the fetch fails outright
# (seen 15 and 24 Oct). Wait up to 20 min.
for i in {1..80}; do
  /usr/bin/curl -s -m 5 -o /dev/null https://www.oahelper.in && break
  echo "$(date +%T) no network yet"; sleep 15
done

# A failed fetch still leaves what it read, and any backlog, to sort
/usr/bin/caffeinate -i $PY -m oa.fetch --headless || echo "fetch failed; sorting what is already saved"
/usr/bin/caffeinate -i $PY -m oa.sort
$PY -m oa.build

git add -A archive data companies topics site README.md practice.md state.json
if ! git diff --cached --quiet; then
  git commit -q -m "Update $(date +%F)"
fi
# Push whatever is not on GitHub yet (also earlier days whose push failed), with retries.
if [[ "$1" != "--no-push" ]] && [[ -n "$(git log origin/main..main --oneline 2>/dev/null)" ]]; then
  for try in 1 2 3; do
    git push -q && break
    echo "push failed (try $try)"
    if [[ $try == 3 ]]; then
      $PY -c 'from oa.common import notify; notify("git push failed, will retry next run")'
    else
      sleep 60
    fi
  done
fi
echo "=== done $(date)"
