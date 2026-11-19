#!/usr/bin/env python3
"""Run exactly one equiv case: band corner freq_ghz. Appends summary row."""
from __future__ import annotations
import os, re, sys
import run_equiv as E

def main():
    if len(sys.argv) != 4:
        print("usage: run_one_equiv_case.py band corner freq_ghz", file=sys.stderr)
        return 2
    band, corner, f = sys.argv[1], sys.argv[2], float(sys.argv[3]) * 1e9
    path, names, ideal, ndiv, duty, vdd = E.build(band, f, E.CORNERS[corner])
    print("sim", path, flush=True)
    d = E.run(path)
    r = E.analyse(d, names, ideal, ndiv, duty, vdd, f)
    dmin, dmax = r["duty_min"], r["duty_max"]
    duty_s = f"{dmin:.1f}/{dmax:.1f}" if dmin is not None else "—"
    mpe = r["max_phase_err"]
    lim = E.REF["uhf_phase_max_deg"] if band == "uhf" else E.REF["vhf_phase_max_deg"] + 0.5
    gate = ("PASS" if r["ok"] and mpe <= lim + 0.2 else
            "FAIL" if not r["ok"] else "PHASE")
    row = (f"| {band} | {corner} | {f/1e9:.2f} | "
           f"{'OK' if r['ok'] else 'FAIL'} | {mpe:.2f}° | {duty_s} | {gate} |")
    print(row, flush=True)
    sum_path = os.path.join(E.OUT, "summary_equiv_lo.txt")
    if os.path.isfile(sum_path):
        txt = open(sum_path).read()
    else:
        txt = (
            "# P2.7.4a2 equivalence — xschem inventory netlist [SCH]\n\n"
            "Step-3 topology; MOSFET CML tails (nbias TG); TSPC weak keepers "
            "(no 1 GOhm). I_latch=0.5 mA.\n\n"
            "## Cases\n\n"
            "| Band | Corner | f_VCO | divide | max |φ−ideal| | duty | gate |\n"
            "|---|---|---|---|---|---|---|\n"
        )
    pat = rf"\| {band} \| {corner} \| {f/1e9:.2f} \|.*\n"
    if re.search(pat, txt):
        txt = re.sub(pat, row + "\n", txt)
    else:
        if not txt.endswith("\n"):
            txt += "\n"
        txt += row + "\n"
    open(sum_path, "w").write(txt)
    print("WROTE", sum_path, flush=True)
    print("CASE_DONE", flush=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
