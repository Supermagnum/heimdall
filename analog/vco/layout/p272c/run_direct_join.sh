#!/usr/bin/env bash
# P2.7.2c direct bank–core join: one net group at a time; stop on first hard fail.
# DRC (density + SVaricap M1.b waived) must be clean every group.
# Intermediate (decisions 2026-11-18): DRC clean and no merge of two named nets
# (extract port names with "|"); opens of nets not yet routed are allowed.
# Unique KLayout + netgen only required at full join (controls).
# Run inside hpretl/iic-osic-tools from this directory.
set -euo pipefail
cd "$(dirname "$0")"
ORDER=(place power ct tail tn_tp vt controls)
ACC=""
: > out/summary_direct_join.txt
echo "# P2.7.2c direct join log" | tee -a out/summary_direct_join.txt

named_merges() {
  # KLayout extract merges named nets as a|b in the .SUBCKT port list [TOOL].
  local cir=""
  for cir in out/lvs_vco_top/vco_top_lvs_extracted.cir \
             out/lvs_vco_top/vco_top_extracted.cir; do
    [[ -f "$cir" ]] || continue
    python3 - "$cir" <<'PY'
import re, sys
txt = open(sys.argv[1], errors="ignore").read()
# First .SUBCKT header only (ports may wrap with +)
m = re.search(r"\.SUBCKT\s+\S+(.*?)(?=\n[A-Z*.])", txt, re.S | re.I)
if not m:
    sys.exit(0)
hdr = m.group(1)
ports = re.findall(r"[A-Za-z0-9_$.|]+", hdr)
merges = sorted({p for p in ports if "|" in p})
if merges:
    print(" ".join(merges))
    sys.exit(1)
sys.exit(0)
PY
    return $?
  done
  return 0
}

list_opens() {
  # Duplicate-label opens show as name$N on the extract port list [TOOL].
  local cir=""
  for cir in out/lvs_vco_top/vco_top_lvs_extracted.cir \
             out/lvs_vco_top/vco_top_extracted.cir; do
    [[ -f "$cir" ]] || continue
    python3 - "$cir" <<'PY'
import re, sys
txt = open(sys.argv[1], errors="ignore").read()
m = re.search(r"\.SUBCKT\s+\S+(.*?)(?=\n[A-Z*.])", txt, re.S | re.I)
if not m:
    sys.exit(0)
ports = re.findall(r"[A-Za-z0-9_$.|]+", m.group(1))
opens = sorted({p for p in ports if re.search(r"\$\d+$", p)})
if opens:
    print(" ".join(opens))
PY
    return 0
  done
}

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
  merges=""
  set +e
  merges=$(named_merges)
  merge_rc=$?
  set -e
  opens=$(list_opens || true)
  if [[ -n "$opens" ]]; then
    echo "opens (allowed intermediate): $opens" | tee -a out/summary_direct_join.txt
  fi
  if [[ $merge_rc -ne 0 ]]; then
    echo "STOP: named-net merge at $g: $merges" | tee -a out/summary_direct_join.txt
    exit 3
  fi
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
    echo "NOTE: LVS unique not required yet at $g (klayout=$kl netgen=$ng)" \
      | tee -a out/summary_direct_join.txt
  fi
  echo "PASS group $g (drc clean; no named merge; lvs klayout=$kl netgen=$ng)" \
    | tee -a out/summary_direct_join.txt
done
echo "ALL GROUPS PASS" | tee -a out/summary_direct_join.txt
exit 0
