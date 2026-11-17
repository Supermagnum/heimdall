#!/usr/bin/env bash
# P2.7.2c direct bank–core join: one net group at a time; stop on first fail.
# Run inside hpretl/iic-osic-tools from this directory.
set -euo pipefail
cd "$(dirname "$0")"
ORDER=(place power ct tail tn_tp vt controls)
ACC=""
: > out/summary_direct_join.txt
echo "# P2.7.2c direct join log" | tee -a out/summary_direct_join.txt
for g in "${ORDER[@]}"; do
  if [[ -z "$ACC" ]]; then
    ACC="$g"
  else
    ACC="$ACC,$g"
  fi
  echo "" | tee -a out/summary_direct_join.txt
  echo "## group $g (nets=$ACC)" | tee -a out/summary_direct_join.txt
  python3 -u build_assemble.py --nets "$ACC" 2>&1 | tee "out/summary_build_${g}.txt"
  cp -f out/summary_build_log.txt "out/summary_build_${g}_log.txt" || true
  python3 -u run_drc_lvs.py --cell vco_top 2>&1 | tee "out/summary_drc_lvs_${g}.txt"
  # Parse prove line from summary_prove_vco_top.txt
  prove=$(tail -n 5 out/summary_prove_vco_top.txt 2>/dev/null || true)
  echo "prove: $prove" | tee -a out/summary_direct_join.txt
  if ! grep -q 'drc_clean=True' out/summary_prove_vco_top.txt; then
    echo "STOP: DRC fail at $g" | tee -a out/summary_direct_join.txt
    exit 2
  fi
  if ! grep -Eq 'klayout=True|klayout_lvs=True|klayout PASS' out/summary_prove_vco_top.txt \
     && ! grep -q 'klayout=True' out/summary_prove_vco_top.txt; then
    # run_drc_lvs writes drc_clean=… klayout=… netgen=…
    if ! grep -q 'klayout=True' out/summary_prove_vco_top.txt; then
      echo "STOP: KLayout LVS fail at $g" | tee -a out/summary_direct_join.txt
      exit 3
    fi
  fi
  if ! grep -q 'netgen=True' out/summary_prove_vco_top.txt; then
    echo "STOP: netgen fail at $g" | tee -a out/summary_direct_join.txt
    exit 4
  fi
  echo "PASS group $g" | tee -a out/summary_direct_join.txt
done
echo "ALL GROUPS PASS" | tee -a out/summary_direct_join.txt
exit 0
