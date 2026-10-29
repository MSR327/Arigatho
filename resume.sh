#!/bin/zsh
# Rerun the tracker after a usage-limit stop, once the 5-hour window has reset.
# oa.sort writes the wanted epoch time to logs/resume_at; launchd calls this every 15 minutes.
cd "${0:A:h}"
[[ -f logs/resume_at ]] || exit 0
(( $(date +%s) >= $(<logs/resume_at) )) || exit 0
rm -f logs/resume_at
# --no-push: the scheduled daily run pushes; a resume only needs to sort and rebuild locally.
exec /bin/zsh run_daily.sh --no-push
