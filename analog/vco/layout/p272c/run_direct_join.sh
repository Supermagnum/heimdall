#!/usr/bin/env bash
# P2.7.2c direct bank–core join: one net group at a time; stop on first hard fail.
# DRC (density + SVaricap M1.b waived) must be clean every group.
# Unique LVS/netgen is the full-assembly gate (decisions: "full-assembly unique LVS");
# intermediate groups still run both tools — stop early if they report a short-like
# failure after power (opens are expected before tn_tp/controls complete).
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
  set +e
  python3 -u run_drc_lvs.py --cell vco_top 2>&1 | tee "out/summary_drc_lvs_${g}.txt"
  rc=${PIPESTATUS[0]}
  set -e
  prove=$(cat out/summary_prove_vco_top.txt 2>/dev/null || true)
  echo "prove: $prove" | tee -a out/summary_direct_join.txt
  if ! grep -q 'drc_clean=True' out/summary_prove_vco_top.txt; then
    echo "STOP: DRC fail at $g" | tee -a out/summary_direct_join.txt
    exit 2
  fi
  kl=$(grep -o 'klayout=[^ ]*' out/summary_prove_vco_top.txt | cut -d= -f2)
  ng=$(grep -o 'netgen=[^ ]*' out/summary_prove_vco_top.txt | cut -d= -f2)
  if [[ "$g" == "controls" ]]; then
    if [[ "$kl" != "True" ]]; then
      echo "STOP: KLayout LVS fail at full join ($g)" | tee -a out/summary_direct_join.txt
      exit 3
    fi
    if [[ "$ng" != "True" ]]; then
      echo "STOP: netgen fail at full join ($g)" | tee -a out/summary_direct_join.txt
      exit 4
    fi
  else
    # Intermediate: flag short-like LVS failure after power is on (opens OK early)
    if [[ "$g" != "place" && "$kl" != "True" ]]; then
      if grep -qiE 'short|mega|many nets|Netlists don.t match' \
           out/lvs_vco_top/vco_top.log out/netgen_vco_top.log 2>/dev/null; then
        echo "STOP: LVS short-like fail at $g (klayout=$kl netgen=$ng)" \
          | tee -a out/summary_direct_join.txt
        exit 3
      fi
      echo "NOTE: LVS not unique yet at $g (klayout=$kl netgen=$ng) — continue" \
        | tee -a out/summary_direct_join.txt
    fi
  fi
  echo "PASS group $g (drc clean; lvs klayout=$kl netgen=$ng)" \
    | tee -a out/summary_direct_join.txt
done
echo "ALL GROUPS PASS" | tee -a out/summary_direct_join.txt
exit 0
