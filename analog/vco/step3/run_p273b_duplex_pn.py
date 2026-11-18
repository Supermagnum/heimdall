#!/usr/bin/env python3
"""P2.7.3b — system PN at duplex with post-layout VCO curve [PEX-RC lumped + MODEL].

Updates the P2.6 step-2 total with VCO L(1 MHz) from summary_pex_vco_pn /
pex_pn_l1m.json (bank-omitted PSS + bank/det/CML bounds). Same D19 loop,
CP FoM, LO floors as run_p26s2.check_total.
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(HERE, "out")
LAYOUT = os.path.join(HERE, "..", "layout", "p272c", "out")
P26 = os.path.join(REPO, "analog", "pll", "p26", "step2")
sys.path.insert(0, os.path.join(REPO, "analog", "pll-model"))
import pll_model as pm  # noqa: E402

# Curve: measured PEX points + linear fill for 3.40 / 3.90 (no direct sim)
# Values are L@1 MHz WITH bounds (bank +0.59, det 0, CML +0.5) [PEX-RC lumped+SCH/HAND]
VCO_1M_RAW = [
    (3.12e9, -125.14),
    (3.20e9, -124.84),
    (3.65e9, -122.39),
    (4.20e9, -119.29),
]
BOUNDS = 0.59 + 0.0 + 0.5


def curve_with_bounds():
    xs = [x for x, _ in VCO_1M_RAW]
    ys = [y + BOUNDS for _, y in VCO_1M_RAW]
    # denser interp anchors matching prior table shape
    freqs = [3.12e9, 3.40e9, 3.65e9, 3.90e9, 4.20e9]
    return [(f, float(np.interp(f, xs, ys))) for f in freqs]


def main():
    vco = curve_with_bounds()
    # P2.6 step2 accepted numbers (cp_noise.json not in tree; from summary_cp /
    # summary_total.txt) [SCH]
    fom, fc = -203.8, 79e3
    lo_floor = {"VHF": -154.0, "UHF": -150.1}

    lines = [
        "# P2.7.3b system PN at duplex — post-layout VCO [PEX-RC lumped + MODEL]\n\n",
        "VCO L(1 MHz) from bank-omitted PSS on schematic + PEX lumped C/R/tail/"
        "couplings, plus bank-switch +0.59 dB [SCH], detector +0.0 [HAND], "
        f"CML +0.5 [HAND] (total +{BOUNDS:.2f} dB). Magic 2-terminal svaricap "
        "not used; PDK 4-terminal schematic svaricap kept [TOOL].\n\n",
        "VCO curve (with bounds) [PEX-RC lumped+SCH/HAND]:\n",
    ]
    for f, L in vco:
        lines.append(f"- {f/1e9:.2f} GHz → {L:.1f} dBc/Hz\n")
    lines.append(
        f"\nLoop: D19 60 kHz / 55°. CP FoM {fom:.1f} dBc/Hz, 1/f {fc/1e3:.0f} kHz "
        f"[SCH summary_cp tt 50 µA]. LO floors VHF {lo_floor['VHF']:.1f} / "
        f"UHF {lo_floor['UHF']:.1f} [SCH p26]. Limit −136 dBc/Hz (25 W).\n\n"
    )
    lines.append(
        "| Ref | Band | RF (MHz) | VCO (GHz) | L(1 MHz) VCO | PN duplex | "
        "VCO / CP / R / SD | LO floor | Total | Limit | Margin |\n"
    )
    lines.append("|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|\n")

    class A:
        pass

    a = A()
    a.kvco, a.icp, a.fc_vco = 40e6, 50e-6, 200e3
    a.fom_cp, a.fc_cp, a.mash = fom, fc, 3
    a.ref_profile = [-110, -135, -150, -155, -158, -160]

    worst_m = 1e9
    worst_row = None
    for ref in (32e6, 36e6):
        for band, (n_lo, dup, (flo, fhi)) in pm.BANDS.items():
            for frf in (flo, fhi):
                fvco = frf * n_lo
                n_fb = fvco / ref
                a.l1m = float(np.interp(
                    fvco, [x for x, _ in vco], [y for _, y in vco]))
                lf = pm.design_loop(60e3, 62.0, a.kvco, a.icp, n_fb)
                pn = pm.noise(
                    np.array([dup]), a, lf, n_fb, ref, n_lo,
                    3 if band == "VHF" else 2)
                floor = lo_floor[band]
                tot = 10 * math.log10(
                    10 ** (pn["total"][0] / 10) + 10 ** (floor / 10))
                mar = pm.LIM_PN_25W - tot
                if mar < worst_m:
                    worst_m = mar
                    worst_row = (ref, band, frf, fvco, a.l1m, tot, mar)
                lines.append(
                    f"| {ref/1e6:.0f} | {band} | {frf/1e6:.0f} | "
                    f"{fvco/1e9:.3f} | {a.l1m:.1f} | {pn['total'][0]:.1f} | "
                    f"{pn['vco'][0]:.1f} / {pn['cp'][0]:.1f} / "
                    f"{pn['r'][0]:.1f} / {pn['sd'][0]:.1f} | {floor:.1f} | "
                    f"{tot:.1f} | {pm.LIM_PN_25W:.0f} | {mar:+.1f} |\n"
                )

    ref, band, frf, fvco, l1m, tot, mar = worst_row
    lines.append(
        f"\n**Worst:** {band} {frf/1e6:.0f} MHz @ ref {ref/1e6:.0f} MHz — "
        f"total {tot:.1f} dBc/Hz, margin {mar:+.1f} dB "
        f"(was +2.8 dB SCH at VHF 175 MHz). "
        f"VCO L(1 MHz) {l1m:.1f} at {fvco/1e9:.3f} GHz "
        f"[PEX-RC lumped+bounds]. Gate vs −136: "
        f"{'PASS' if worst_m >= 0 else 'FAIL'}.\n"
    )
    text = "".join(lines)
    for p in (
        os.path.join(OUT, "summary_pex_duplex_pn.txt"),
        os.path.join(LAYOUT, "summary_pex_duplex_pn.txt"),
    ):
        open(p, "w").write(text)
    open(os.path.join(OUT, "pex_duplex_pn.json"), "w").write(json.dumps({
        "vco_curve_with_bounds": [[f, L] for f, L in vco],
        "bounds_db": BOUNDS,
        "worst_margin_db": worst_m,
        "worst": {
            "ref": ref, "band": band, "frf": frf, "fvco": fvco,
            "l1m": l1m, "total": tot, "margin": mar,
        },
    }, indent=2) + "\n")
    print(text)
    return 0 if worst_m >= 0 else 1


if __name__ == "__main__":
    sys.exit(main())
