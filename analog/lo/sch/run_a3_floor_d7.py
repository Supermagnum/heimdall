#!/usr/bin/env python3
"""P2.7.4a3 step 5 — floor (C_ck=15 fF) + D7 after tailless ÷3 [SCH/HAND].

UHF-path-only sizing already at I_latch=0.75, B2=4 (floor PASS a2). Re-measure
stage noise with tailless VHF; report LO current vs D7. Stop if D7 over.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path.insert(0, HERE)
import circuit as C  # noqa: E402

VCO_TYP = 3.59e-3
PLL_HAND = 1.5e-3
D7 = 10e-3
TARGET_UHF = -151.0
# VHF floor target from topology memo ≤ −150 at LO [PROP]; a2 had −158
TARGET_VHF = -150.0


def main():
    os.makedirs(OUT, exist_ok=True)
    os.environ["LO_SCH_OUT"] = OUT
    C.apply_knobs(i_latch=0.75e-3, b2=4.0, vhf_tailless=True)

    print("stage noise…", flush=True)
    r = subprocess.run(
        [sys.executable, "-u", os.path.join(HERE, "run_stage_noise.py"),
         "uhf", "vhf", "i=0.75", "b2=4"],
        cwd=HERE,
    )
    sn_path = os.path.join(OUT, "stage_noise.json")
    sn = json.load(open(sn_path)) if os.path.exists(sn_path) else {}
    L_uhf = sn.get("uhf", {}).get("L_sum", float("nan"))
    L_vhf = sn.get("vhf", {}).get("L_sum", float("nan"))
    parts_u = sn.get("uhf", {}).get("parts", [])
    parts_v = sn.get("vhf", {}).get("parts", [])

    # Current [HAND]: UHF 2×I; VHF tailless — 4 clocked latches + NOR still
    # draw ~I each at the designed W (conservative same as 5×I_latch).
    i_cml_uhf = 2 * C.I_LATCH
    i_cml_vhf = 5 * C.I_LATCH
    i_buf = 1.00e-3  # B2=4 [HAND a2]
    i_conv = 0.50e-3
    i_logic = 0.35e-3
    i_chain_uhf = i_buf + i_cml_uhf + i_conv + i_logic
    i_chain_vhf = i_buf + i_cml_vhf + i_conv + i_logic
    i_lo_uhf = i_chain_uhf + VCO_TYP + PLL_HAND
    i_lo_vhf = i_chain_vhf + VCO_TYP + PLL_HAND
    overrun = i_lo_vhf - D7

    lines = [
        "# P2.7.4a3 step 5 — floor + D7 (tailless ÷3, B2=4) [SCH/HAND]",
        "",
        "C_ck=15 fF/side. I_latch=0.75 mA; B2=4; VHF_TAILLESS=True.",
        f"stage_noise exit={r.returncode}.",
        "",
        "## Floor",
        "",
        "| Band | Floor (dBc/Hz) | Target | Gate |",
        "|---|---:|---:|---|",
        f"| UHF | {L_uhf:.1f} | ≤ {TARGET_UHF:.0f} | "
        f"{'PASS' if L_uhf <= TARGET_UHF else 'FAIL'} |",
        f"| VHF | {L_vhf:.1f} | ≤ {TARGET_VHF:.0f} | "
        f"{'PASS' if L_vhf <= TARGET_VHF else 'FAIL'} |",
        "",
        "## Per-stage (UHF)",
        "",
        "| Stage | L → LO (dBc/Hz) |",
        "|---|---:|",
    ]
    for name, _, L in parts_u:
        lines.append(f"| {name} | {L:.1f} |")
    lines += [
        "",
        "## Per-stage (VHF)",
        "",
        "| Stage | L → LO (dBc/Hz) |",
        "|---|---:|",
    ]
    for name, _, L in parts_v:
        lines.append(f"| {name} | {L:.1f} |")

    d7_ok = i_lo_vhf <= D7 + 0.05e-3
    lines += [
        "",
        "## LO current vs D7 (≤ 10 mA typ) [HAND]",
        "",
        "| Piece | UHF | VHF |",
        "|---|---:|---:|",
        f"| Buffer (B2=4) | {i_buf*1e3:.2f} | {i_buf*1e3:.2f} |",
        f"| CML (2× / 5× I_latch) | {i_cml_uhf*1e3:.2f} | {i_cml_vhf*1e3:.2f} |",
        f"| Converter + logic | {(i_conv+i_logic)*1e3:.2f} | "
        f"{(i_conv+i_logic)*1e3:.2f} |",
        f"| Chain subtotal | {i_chain_uhf*1e3:.2f} | {i_chain_vhf*1e3:.2f} |",
        f"| VCO typ + PLL HAND | {(VCO_TYP+PLL_HAND)*1e3:.2f} | "
        f"{(VCO_TYP+PLL_HAND)*1e3:.2f} |",
        f"| **LO total** | **{i_lo_uhf*1e3:.2f}** | **{i_lo_vhf*1e3:.2f}** |",
        "",
        f"D7: {'PASS' if d7_ok else f'FAIL — VHF over by {overrun*1e3:.2f} mA'}.",
        "",
    ]
    if not d7_ok:
        lines += [
            "## STOP — D7 overrun (owner)",
            "",
            f"Smallest VHF LO total with UHF-path-only sizing: "
            f"**{i_lo_vhf*1e3:.2f} mA** (−{overrun*1e3:.2f} mA vs 10 mA).",
            "Options:",
            "1. Accept / raise D7 by ≥ 0.7 mA for VHF typ.",
            "2. Cut C_ck in layout (reduce I_latch back toward 0.5 mA) "
            "if floor still holds.",
            "3. Share / duty-cycle bias or shrink converter clock driver.",
            "4. Measure tailless ÷3 current [SCH] — HAND 5×I may be high; "
            "if lower, re-close D7.",
            "",
            "Peak MC N=20: unchanged VCO (D22) — prior PASS 1.249+3σ ≤ 1.50 "
            "[PEX-RC] `analog/vco/step3/out/summary_pex_vco_peak_mc_schstyle.txt` "
            "(not re-run; no VCO change).",
            "",
        ]

    path = os.path.join(OUT, "summary_a3_floor_d7.txt")
    open(path, "w").write("\n".join(lines) + "\n")
    print("WROTE", path, flush=True)
    print("\n".join(lines), flush=True)
    print("A3_FLOOR_DONE", flush=True)
    return 0 if d7_ok and L_uhf <= TARGET_UHF else 1


if __name__ == "__main__":
    raise SystemExit(main())
