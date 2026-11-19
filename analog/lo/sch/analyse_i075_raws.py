#!/usr/bin/env python3
"""Re-analyse existing I_latch=0.75 mA equiv raws (no re-sim)."""
from __future__ import annotations

import os
import sys

os.environ.setdefault("LO_SCH_OUT", "out_a2_i075")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run_equiv as E  # noqa: E402
from vacask.rawfile import rawread  # noqa: E402


def main():
    cases = [
        ("uhf", "tt", 3.20), ("uhf", "tt", 3.84),
        ("uhf", "ss", 3.20), ("uhf", "ss", 3.84),
        ("vhf", "tt", 3.12), ("vhf", "tt", 4.20),
        ("vhf", "ss", 3.12), ("vhf", "ss", 4.20),
    ]
    print("# I_latch=0.75 mA re-analyse existing raws [SCH]\n")
    print("| Band | Corner | f_VCO | divide | max |φ−ideal| | duty | gate |")
    print("|---|---|---|---|---|---|---|")
    rows = [
        "| Band | Corner | f_VCO | divide | max |φ−ideal| | duty | gate |",
        "|---|---|---|---|---|---|---|",
    ]
    for band, c, fg in cases:
        f = fg * 1e9
        tag = "_i075"
        name = f"lo_eq_{band}_{c}_{fg:.2f}{tag}"
        raw = os.path.join(E.OUT, name + ".tr.raw")
        if not os.path.isfile(raw):
            row = f"| {band} | {c} | {fg:.2f} | no-raw | — | — | SKIP |"
            print(row, flush=True)
            rows.append(row)
            continue
        _path, names, ideal, ndiv, duty, vdd = E.build(
            band, f, E.CORNERS[c], tag=tag, i_latch=0.75e-3)
        d = rawread(raw).get()
        r = E.analyse(d, names, ideal, ndiv, duty, vdd, f)
        lim = (E.REF["uhf_phase_max_deg"] if band == "uhf"
               else E.REF["vhf_phase_max_deg"] + 0.5)
        mpe = r["max_phase_err"]
        ph_ok = (mpe is not None) and mpe <= lim + 0.2
        gate = ("PASS" if r["ok"] and ph_ok else
                "FAIL" if not r["ok"] else "PHASE")
        dmin, dmax = r["duty_min"], r["duty_max"]
        duty_s = (f"{dmin:.1f}/{dmax:.1f}" if dmin is not None else "—")
        mpe_s = f"{mpe:.2f}°" if mpe is not None else "—"
        ok_s = "OK" if r["ok"] else "FAIL"
        row = (f"| {band} | {c} | {fg:.2f} | {ok_s} | {mpe_s} | "
               f"{duty_s} | {gate} |")
        print(row, flush=True)
        rows.append(row)
    path = os.path.join(E.OUT, "summary_equiv_i075.txt")
    open(path, "w").write("# I_latch=0.75 mA [SCH]\n\n" + "\n".join(rows) + "\n")
    print("I075_ANALYSE_DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
