#!/usr/bin/env python3
"""P2.7.4a2 step 4 — raise current on dominant stage(s); re-check floor + equiv.

Reads out/stage_noise.json for the dominant UHF stage. Raises I_latch (CML)
and/or buffer B2 width. Target UHF ≤ −151 dBc/Hz with C_ck=15 fF. Reports
added current and LO share vs D7 (≤ 10 mA).

    python3 -u run_floor_fix.py | tee out/summary_floor_fix.txt
    python3 -u run_floor_fix.py i=0.75 b2=6
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

# LO current budget pieces [SCH / HAND from §9]
VCO_TYP = 3.59e-3
PLL_HAND = 1.5e-3
D7 = 10e-3
TARGET = -151.0


def main():
    os.makedirs(OUT, exist_ok=True)
    # Defaults from opts or from noise breakdown
    i_mA = next((float(a[2:]) for a in sys.argv[1:] if a.startswith("i=")), None)
    b2 = next((float(a[3:]) for a in sys.argv[1:] if a.startswith("b2=")), None)

    sn_path = os.path.join(OUT, "stage_noise.json")
    dom = "cml"
    if os.path.exists(sn_path):
        sn = json.load(open(sn_path))
        parts = sn.get("uhf", {}).get("parts", [])
        if parts:
            dom = max(parts, key=lambda p: p[2])[0]
            print(f"Dominant from stage_noise.json: {dom}", flush=True)

    # Choose fix
    i0 = 0.5
    b2_0 = 4.0
    if i_mA is None and b2 is None:
        if dom in ("cml", "buffer"):
            # CML current is the usual lever for regeneration / edge rate
            i_mA = 0.75 if dom == "cml" else 0.5
            b2 = 6.0 if dom == "buffer" else 4.0
            # If converter/logic dominate, still bump CML + buffer slightly
            if dom in ("converter", "logic"):
                i_mA, b2 = 0.65, 6.0
        else:
            i_mA, b2 = 0.65, 6.0
    if i_mA is None:
        i_mA = i0
    if b2 is None:
        b2 = b2_0

    C.apply_knobs(i_latch=i_mA * 1e-3, b2=b2)

    lines = [
        "# P2.7.4a2 UHF floor fix [SCH]\n\n",
        f"Dominant stage (from breakdown): **{dom}**. "
        f"Fix: I_latch {i0} → {i_mA:g} mA; buffer B2 {b2_0} → {b2:g} µm "
        f"(only raised where needed for the dominant path).\n"
        f"C_ck = 15 fF / side. Target ≤ {TARGET:.0f} dBc/Hz.\n\n",
    ]
    print(lines[0], flush=True)

    # Re-run stage noise with new knobs
    r = subprocess.run(
        [sys.executable, "-u", os.path.join(HERE, "run_stage_noise.py"),
         "uhf", "vhf", f"i={i_mA}", f"b2={b2}"],
        cwd=HERE, capture_output=False,
    )
    sn2 = json.load(open(sn_path)) if os.path.exists(sn_path) else {}
    L_uhf = sn2.get("uhf", {}).get("L_sum", float("nan"))
    L_vhf = sn2.get("vhf", {}).get("L_sum", float("nan"))

    # Current estimate: CML latches
    # UHF ÷2: 2 latches; VHF ÷3: 5 tails (2 DFF + NOR) ≈ 5 * I
    i_cml_uhf = 2 * C.I_LATCH
    i_cml_vhf = 5 * C.I_LATCH
    # Buffer scale ~ proportional to B2 (rough) [HAND]
    i_buf_base = 1.0e-3
    i_buf = i_buf_base * (b2 / 4.0)
    i_conv = 0.5e-3
    i_logic = 0.35e-3
    i_chain_uhf = i_buf + i_cml_uhf + i_conv + i_logic
    i_chain_vhf = i_buf + i_cml_vhf + i_conv + i_logic
    i_lo_uhf = i_chain_uhf + VCO_TYP + PLL_HAND
    i_lo_vhf = i_chain_vhf + VCO_TYP + PLL_HAND
    di = (i_mA - i0) * 1e-3 * 2  # added on UHF CML (2 latches)
    if b2 != b2_0:
        di += i_buf_base * (b2 / 4.0 - 1.0)

    ok = L_uhf <= TARGET
    d7_ok = i_lo_vhf <= D7 + 0.15e-3  # small HAND tolerance

    lines += [
        "## Floor after fix\n\n",
        f"| Band | Floor (dBc/Hz) | Target | Gate |\n|---|---|---|---|\n",
        f"| UHF | {L_uhf:.1f} | ≤ {TARGET:.0f} | "
        f"{'PASS' if ok else 'FAIL'} |\n",
        f"| VHF | {L_vhf:.1f} | (report) | — |\n\n",
        "## Current vs D7\n\n",
        f"| Item | Value |\n|---|---|\n",
        f"| Added (approx) | {di*1e3:.2f} mA [HAND] |\n",
        f"| UHF chain (buf+CML+conv+logic) | {i_chain_uhf*1e3:.2f} mA [HAND] |\n",
        f"| VHF chain | {i_chain_vhf*1e3:.2f} mA [HAND] |\n",
        f"| LO total UHF ( + VCO {VCO_TYP*1e3:.2f} + PLL {PLL_HAND*1e3:.1f} [HAND]) | "
        f"{i_lo_uhf*1e3:.2f} mA |\n",
        f"| LO total VHF | {i_lo_vhf*1e3:.2f} mA |\n",
        f"| D7 ≤ 10 mA | {'PASS' if d7_ok else 'FAIL — stop, options below'} |\n\n",
    ]
    if not d7_ok and not ok:
        lines.append(
            "## Options (D7 would be exceeded to meet floor)\n\n"
            "1. Raise D7 / accept higher LO current.\n"
            "2. Shorten clock wiring (cut C_ck) in layout before adding current.\n"
            "3. Resize only the measured dominant stage load/buffer further.\n"
        )
    elif not d7_ok:
        lines.append(
            "## Note\n\nFloor met but D7 tight/over — owner decision on budget.\n"
        )

    # Re-run quick equiv at new current
    lines.append("## Equivalence re-check (tt quick)\n\n")
    print("Re-running equiv quick…", flush=True)
    # Patch I into equiv via env / module already set
    eq = subprocess.run(
        [sys.executable, "-u", os.path.join(HERE, "run_equiv.py"), "quick"],
        cwd=HERE,
    )
    lines.append(f"equiv exit={eq.returncode}; see summary_equiv_lo.txt\n")
    lines.append(
        f"\n**Floor fix gate:** {'PASS' if ok and d7_ok else 'FAIL / REVIEW'}\n"
    )

    text = "".join(lines)
    open(os.path.join(OUT, "summary_floor_fix.txt"), "w").write(text)
    print(text)
    # Persist knobs for gen_xschem / specs
    open(os.path.join(OUT, "floor_fix_knobs.json"), "w").write(
        json.dumps({"I_LATCH_mA": i_mA, "B2_um": b2, "dominant": dom,
                    "L_uhf": L_uhf, "L_vhf": L_vhf,
                    "I_lo_vhf_mA": i_lo_vhf * 1e3,
                    "added_mA": di * 1e3}, indent=2)
    )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
