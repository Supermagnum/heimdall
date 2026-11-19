#!/usr/bin/env python3
"""Run a single equiv case: band corner f_GHz [tag]. Prints one table row."""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run_equiv as E  # noqa: E402


def main():
    if len(sys.argv) < 4:
        print("usage: run_equiv_one.py band corner f_GHz [tag]", file=sys.stderr)
        return 2
    band, cname, f_g = sys.argv[1], sys.argv[2], float(sys.argv[3])
    tag = sys.argv[4] if len(sys.argv) > 4 else ""
    f = f_g * 1e9
    os.makedirs(E.OUT, exist_ok=True)
    try:
        path, names, ideal, ndiv, duty, vdd = E.build(
            band, f, E.CORNERS[cname], tag=tag)
        d = E.run(path)
        r = E.analyse(d, names, ideal, ndiv, duty, vdd, f)
        lim = (E.REF["uhf_phase_max_deg"] if band == "uhf"
               else E.REF["vhf_phase_max_deg"] + 0.5)
        ph_ok = r["max_phase_err"] <= lim + 0.2
        gate = ("PASS" if r["ok"] and ph_ok else
                "FAIL" if not r["ok"] else "PHASE")
        dmin, dmax = r["duty_min"], r["duty_max"]
        duty_s = (f"{dmin:.1f}/{dmax:.1f}"
                  if dmin is not None and dmax is not None else "—")
        mpe = r["max_phase_err"]
        mpe_s = f"{mpe:.2f}°" if mpe is not None else "—"
        row = (f"| {band} | {cname} | {f_g:.2f} | "
               f"{'OK' if r['ok'] else 'FAIL'} | "
               f"{mpe_s} | {duty_s} | {gate} |")
        print(row, flush=True)
        return 0 if gate == "PASS" else 1
    except Exception as e:
        row = (f"| {band} | {cname} | {f_g:.2f} | error | — | — | "
               f"FAIL ({str(e)[-80:]}) |")
        print(row, flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
