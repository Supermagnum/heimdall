#!/usr/bin/env python3
"""VHF ss smoke at current I_LATCH."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402


def main():
    print("I", C.I_LATCH, flush=True)
    rows = []
    for fg in (3.12, 4.20):
        f = fg * 1e9
        path, names, ideal, ndiv, duty, vdd = E.build(
            "vhf", f, E.CORNERS["ss"], tag="_i075")
        d = E.run(path)
        r = E.analyse(d, names, ideal, ndiv, duty, vdd, f)
        lim = E.REF["vhf_phase_max_deg"] + 0.5
        ok_div = "OK" if r["ok"] else "FAIL"
        gate = ("PASS" if r["ok"] and r["max_phase_err"] <= lim + 0.2
                else "FAIL" if not r["ok"] else "PHASE")
        dmin, dmax = r["duty_min"], r["duty_max"]
        duty_s = (f"{dmin:.1f}/{dmax:.1f}" if dmin is not None else "—")
        row = (f"| vhf | ss | {fg:.2f} | {ok_div} | "
               f"{r['max_phase_err']:.2f}° | {duty_s} | {gate} |")
        print(row, flush=True)
        rows.append(row)
    os.makedirs(E.OUT, exist_ok=True)
    open(os.path.join(E.OUT, "vhf_ss_rows.txt"), "w").write(
        "\n".join(rows) + "\n")
    print("VHF_SS_DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
