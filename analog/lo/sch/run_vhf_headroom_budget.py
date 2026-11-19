#!/usr/bin/env python3
"""P2.7.4a3 headroom budget for failing CML ÷3 at ss [SCH].

Uses the a3diag transient (stuck ÷3) last-25% levels. V_dsat estimated as
max(Vgs−Vt, 0) with Vt≈0.45 V at ss/125 [HAND/DS order]; shortfall vs
2·V_dsat stack + swing.
"""
from __future__ import annotations

import os
import sys

import numpy as np
from vacask.rawfile import rawread

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
RAW = os.path.join(HERE, "out_sole", "lo_eq_vhf_ss_3.12_a3diag.tr.raw")
VT = 0.45  # ss/125 LV NMOS order [HAND]


def last(d, n, n0):
    return np.real(d[n])[n0:]


def main():
    if not os.path.isfile(RAW):
        print("MISSING", RAW, file=sys.stderr)
        return 2
    d = rawread(RAW).get()
    t = np.real(d["time"])
    n0 = int(0.75 * len(t))
    vdd = float(np.mean(last(d, "vdd", n0)))
    nb = float(np.mean(last(d, "nb_lo", n0)))

    # Master latch of DFF a (feeds q1): name "am" in step1 cml_dff("a",...)
    # Stack (active track side when ckp high): RL → q → data pair → s1 → ck → t → gnd
    rows = []

    def add(stage, device, vd, vs, vg=None, note=""):
        vds = vd - vs
        vgs = (vg - vs) if vg is not None else None
        vdsat = max((vgs - VT), 0.05) if vgs is not None else None
        margin = (vds - vdsat) if vdsat is not None else None
        rows.append((stage, device, vd, vs, vgs, vds, vdsat, margin, note))

    # Tail of master latch am
    tam = float(np.mean(last(d, "tam", n0)))
    add("÷3 latch1 master", "tail mtam", tam, 0.0, nb, "MOSFET tail")
    # Clock pair sources at tam; drains s1am / s2am
    s1am = float(np.mean(last(d, "s1am", n0)))
    s2am = float(np.mean(last(d, "s2am", n0)))
    ckp = float(np.mean(last(d, "ckp", n0)))
    ckn = float(np.mean(last(d, "ckn", n0)))
    add("÷3 latch1 master", "ck pair→s1", s1am, tam, ckp, "clock switch")
    add("÷3 latch1 master", "ck pair→s2", s2am, tam, ckn, "clock switch")
    q1p = float(np.mean(last(d, "q1p", n0)))
    q1n = float(np.mean(last(d, "q1n", n0)))
    # Slave outputs are q1p/q1n — use slave stack "as"
    tas = float(np.mean(last(d, "tas", n0)))
    s1as = float(np.mean(last(d, "s1as", n0)))
    s2as = float(np.mean(last(d, "s2as", n0)))
    add("÷3 latch1 slave", "tail mtas", tas, 0.0, nb, "MOSFET tail")
    add("÷3 latch1 slave", "ck→s1", s1as, tas, ckn, "ckn track")
    add("÷3 latch1 slave", "ck→s2", s2as, tas, ckp, "ckp hold")
    add("÷3 latch1 slave", "load side q1p", q1p, s1as, None, "drain of data/regen")
    add("÷3 latch1 slave", "load side q1n", q1n, s2as, None, "drain of data/regen")
    load_p = vdd - q1p
    load_n = vdd - q1n

    # NOR tail tg for comparison
    tg = float(np.mean(last(d, "tg", n0)))
    add("÷3 NOR", "tail mtg", tg, 0.0, nb, "gate tail")

    # UHF-style comparison: if orp from ÷2 path not present same way — skip
    # Budget: need VDD >= swing + Vdsat_data + Vdsat_ck + Vdsat_tail (3 stack)
    # With I*RL swing target 0.5 V
    swing = 0.5
    # Use measured Vdsat of tail and clock from Vgs
    vdsat_tail = max(nb - VT, 0.05)
    # clock overdrive: ckp mean is mid — use peak approx VDD/2+amp/2 ~ 0.95 from prior
    ckp_max = float(np.max(last(d, "ckp", n0)))
    vdsat_ck = max(ckp_max - tam - VT, 0.05)  # rough when on
    # data pair: gate from complementary ~q, rough
    vdsat_data = 0.15  # [HAND] min saturation overdrive target
    need = swing + vdsat_data + vdsat_ck + vdsat_tail
    short = need - vdd

    lines = [
        "# P2.7.4a3 — CML ÷3 headroom budget at failing ss [SCH]",
        "",
        f"Source raw: `{os.path.relpath(RAW, HERE)}` (last 25 % of stuck transient).",
        f"VDD mean={vdd:.3f} V; nb_lo={nb:.3f} V; Vt≈{VT:.2f} V [HAND].",
        "",
        "## Device table (÷3 latch 1 + NOR tail)",
        "",
        "| Stage | Device | V_D | V_S | V_GS | V_DS | V_dsat≈ | V_DS−V_dsat | note |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for stage, device, vd, vs, vgs, vds, vdsat, margin, note in rows:
        gss = f"{vgs:.3f}" if vgs is not None else "—"
        vsat = f"{vdsat:.3f}" if vdsat is not None else "—"
        mar = f"{margin*1e3:.0f} mV" if margin is not None else "—"
        lines.append(
            f"| {stage} | {device} | {vd:.3f} | {vs:.3f} | {gss} | {vds:.3f} | "
            f"{vsat} | {mar} | {note} |"
        )
    lines += [
        "",
        f"Load drop at q1p/q1n: {load_p*1e3:.0f} / {load_n*1e3:.0f} mV "
        f"(want ~I·R_L/2 ≈ {swing/2*1e3:.0f} mV for balanced CML) [SCH].",
        "",
        "## Stack budget (saturated track path)",
        "",
        f"| Term | Value |",
        f"|---|---:|",
        f"| Target swing I·R_L | {swing*1e3:.0f} mV |",
        f"| V_dsat tail (Vgs−Vt) | {vdsat_tail*1e3:.0f} mV |",
        f"| V_dsat clock (rough) | {vdsat_ck*1e3:.0f} mV |",
        f"| V_dsat data (target) | {vdsat_data*1e3:.0f} mV |",
        f"| Sum needed | {need*1e3:.0f} mV |",
        f"| VDD | {vdd*1e3:.0f} mV |",
        f"| **Shortfall** | **{short*1e3:.0f} mV** |",
        "",
        "Measured stuck state: both q1p and q1n near VDD (load drop "
        f"{load_p*1e3:.0f}/{load_n*1e3:.0f} mV) → current starved / triode tail–clock "
        "stack; differential frozen (~140 mV) [SCH].",
        "",
        "## Supply (step 2)",
        "",
        "Rail: **VR_ANA1 pad** (D21) — feeds VCO + LO + CP. Not an external bench rail.",
        "Pad ss min = **1.108 V** [HAND] (`summary_vrana1_pad_corners.txt` / D21).",
        "No separate SCH LDO OP at mos_ss / 125 °C found; LDO verify table is typ Vin [SCH].",
        "LO decks historically used **1.08 V** as a conservative floor (≤ pad min).",
        "This job: budget at failing 1.08 V raw; fix checks at **1.108 V** then margin at 1.08 V.",
    ]
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "summary_vhf_headroom_budget.txt")
    open(path, "w").write("\n".join(lines) + "\n")
    print("WROTE", path)
    print(f"SHORTFALL_mV={short*1e3:.0f} VDD={vdd:.3f} need={need:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
