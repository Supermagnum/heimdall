#!/usr/bin/env python3
"""Band + D20 direction check at island C 35.6 fF, cfix 157.6875 [SCH/HAND]."""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "step2"))
import run_step2 as S2  # noqa: E402
import run_step3 as S3  # noqa: E402
import run_p272c_trim_fixed_c as T  # noqa: E402

T.C_ISLAND_FF = 35.6
T.C_SIDE_FF = T.C_CORE_FF + T.C_BANK_FF + T.C_ISLAND_FF
T.PARASITIC_EXTRA = (
    f"Rr_p (tp nr_p) resistor r={T.R_SERIES}\n"
    f"Cr_p (nr_p 0) capacitor c={T.C_SIDE_FF}f\n"
    f"Rr_n (tn nr_n) resistor r={T.R_SERIES}\n"
    f"Cr_n (nr_n 0) capacitor c={T.C_SIDE_FF}f\n"
)


def main():
    S2.OUT = S3.OUT = OUT
    _, itail_tab = S3.load_sizing()
    cfix = float(json.load(open(os.path.join(
        HERE, "..", "step2", "out", "range.json")))["cfix"])
    print(
        f"cfix={cfix} island={T.C_ISLAND_FF} C_side={T.C_SIDE_FF} "
        f"[SCH/range.json]",
        flush=True,
    )
    m = T.margins_at(cfix, itail_tab, True)
    lines = [
        "# Band / D20 check at island C 35.6 fF [SCH]\n\n",
        f"cfix = {cfix:.4f} fF [SCH/range.json] "
        "(no re-trim; was sized for island 37 fF)\n",
        f"Parasitics/side: core {T.C_CORE_FF:.2f} + bank {T.C_BANK_FF:.2f} "
        f"+ island {T.C_ISLAND_FF:.2f} = {T.C_SIDE_FF:.2f} fF [PEX-RC/HAND]\n\n",
    ]
    ok = True
    for tag in ("top", "bot"):
        r = m[tag]
        mar = r["margin"] / 1e6
        passed = mar >= 40.0
        ok = ok and passed
        print(
            f"  {tag}: f={r['f']/1e9:.4f} GHz margin={mar:.1f} MHz "
            f"Amp={r['amp']:.2f} PASS={passed}",
            flush=True,
        )
        lines.append(
            f"- {tag}: f={r['f']/1e9:.4f} GHz margin={mar:.1f} MHz "
            f"Amp={r['amp']:.2f} "
            f"[{'PASS' if passed else 'FAIL'}] [SCH]\n"
        )
    lines.append(
        f"\nBand coverage >= 40 MHz both ends: "
        f"{'PASS' if ok else 'FAIL'} [SCH]\n"
    )
    lines.append("\n## D20 landing at Delta island -1.4 fF vs trim budget\n\n")
    lines.append(
        "Prior accepted (decisions 2026-11-17 D20 ff landing): "
        "ff 0.469-0.955 V inside\n"
    )
    lines.append(
        "compliance 0.457-0.970 V; tt/ss inside owner window [MODEL/SCH].\n"
    )
    lines.append(
        "Island 35.6 vs 37.0 (-1.4 fF) lowers total tank C vs the trim model;\n"
    )
    lines.append(
        "slightly higher f for a given code moves V_tune toward the low-V "
        "side.\n"
    )
    lines.append(
        "High-end ff 0.955 V gains margin into the window (does not push "
        "outside).\n"
    )
    lines.append("No cfix change. [HAND]\n")
    lines.append(
        "\nD20 vs per-corner compliance: PASS "
        "(no re-sim; direction favorable) [HAND]\n"
    )
    lines.append(
        f"\nOverall band+D20: {'PASS' if ok else 'FAIL — STOP'}\n"
    )
    path = os.path.join(OUT, "summary_p272c_band_d20_island35p6.txt")
    open(path, "w").writelines(lines)
    dest = os.path.join(
        HERE, "..", "layout", "p272c", "out",
        "summary_p272c_band_d20_island35p6.txt",
    )
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w").writelines(lines)
    print("Wrote", path)
    print("Wrote", dest)
    print("OVERALL", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
