#!/usr/bin/env python3
"""P2.7.4a3 step 3 — size LO buffer for ≥0.5 V/side @ 4.20 ss V_min [SCH].

Tail-less ÷3; D22 tank amp unchanged (run_equiv.tank_amp). Smallest B2 that
meets the swing target; report buffer current estimate and area [HAND].
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
V_MIN = 1.181  # VR_ANA1 divider min [SCH/HAND summary_vrana1_corner_vmin]
TARGET_SW = 0.50  # V per side
F = 4.20e9
# B2 = last inverter NMOS width (µm); PMOS = 2×B2. Default 4.
B2_SWEEP = (4.0, 5.0, 6.0, 8.0, 10.0, 12.0)


def buf_sw(d):
    n0 = int(0.7 * len(np.real(d["time"])))
    ckp = np.real(d["ckp"])[n0:]
    ckn = np.real(d["ckn"])[n0:]
    return float(0.25 * ((ckp.max() - ckp.min()) + (ckn.max() - ckn.min())))


def buf_current(_d):
    """Supply current not in default raw saves — use HAND scale in report."""
    return None


def one(b2):
    C.apply_knobs(i_latch=0.75e-3, swing=0.5, b2=b2, vhf_tailless=True)
    E.CORNERS["ss"] = ("ss", "mos_ss", V_MIN, 125)
    tag = f"_bs_b{b2:g}"
    path, names, ideal, ndiv, duty, v = E.build(
        "vhf", F, E.CORNERS["ss"], tag=tag)
    d = E.run(path)
    r = E.analyse(d, names, ideal, ndiv, duty, v, F)
    sw = buf_sw(d)
    ib = buf_current(d)
    print(f"B2={b2:g} ok={r['ok']} ph={r['max_phase_err']:.2f} "
          f"sw={sw:.3f} Ibuf={ib}", flush=True)
    return dict(b2=b2, ok=bool(r["ok"]), phase=r["max_phase_err"], sw=sw,
                ibuf=ib)


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(E.OUT, exist_ok=True)
    rows = []
    for b2 in B2_SWEEP:
        rows.append(one(b2))

    # pick smallest B2 with sw>=TARGET and ok
    pick = None
    for r in rows:
        if r["ok"] and r["sw"] >= TARGET_SW - 1e-3:
            pick = r
            break

    # Area [HAND]: last inv 2 sides × (Wn×0.13 + Wp×0.13) µm² rough active
    def area_um2(b2):
        # per side: NMOS B2×0.13 + PMOS 2B2×0.13; ×2 sides; + fixed front stages
        # front: b1 2/4, bm 3/6, cross 0.5/1 + 1/2 — fixed ~ (2+4+3+6+0.5+1+1+2)*0.13*2
        fixed = (2 + 4 + 3 + 6 + 0.5 + 1 + 1 + 2) * 0.13 * 2
        last = 2 * (b2 + 2 * b2) * 0.13
        return fixed + last

    lines = [
        "# P2.7.4a3 — LO buffer sizing @ 4.20 GHz ss V_min [SCH]",
        "",
        f"VDD={V_MIN} V (VR_ANA1 V_min); mos_ss / 125 °C; tailless ÷3;",
        f"tank amp = tank_amp(4.20) = {E.tank_amp(F):.3f} V/side (D22 unchanged);",
        f"target ≥ {TARGET_SW:.2f} V/side at ÷3 clock.",
        "",
        "| B2 (µm) | divide | max|φ| | buf V/side | I_buf [SCH] | area last+front [HAND µm²] |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for r in rows:
        ib = f"{r['ibuf']*1e3:.2f} mA" if r["ibuf"] is not None else "n/a"
        lines.append(
            f"| {r['b2']:g} | {'OK' if r['ok'] else 'FAIL'} | "
            f"{r['phase']:.2f} | {r['sw']:.3f} | {ib} | {area_um2(r['b2']):.1f} |"
        )

    lines += ["", "## Pick", ""]
    if pick is None:
        lines.append(
            "**FAIL:** no B2 in sweep meets ≥0.5 V/side with divide OK. "
            "Need extra stage or other change (owner)."
        )
        # still report best swing
        best = max(rows, key=lambda x: x["sw"])
        lines.append(
            f"Best swing: B2={best['b2']:g} sw={best['sw']:.3f} "
            f"ok={best['ok']}."
        )
        # HAND current scale if SCH missing: prior B2=4 → ~1.0 mA [HAND a2]
        lines.append(
            "I_buf: if raw lacks i(vbufs), use HAND scale ∝ B2 from "
            "1.00 mA @ B2=4 [HAND summary_floor_fix]."
        )
        rc = 1
    else:
        b2 = pick["b2"]
        # HAND current if needed
        ib_sch = pick["ibuf"]
        ib_hand = 1.00e-3 * (b2 / 4.0)  # rough [HAND]
        ib = ib_sch if ib_sch is not None else ib_hand
        tag = "SCH" if ib_sch is not None else "HAND"
        dI = ib - 1.00e-3
        lines += [
            f"**Selected B2 = {b2:g} µm** (last inv {b2:g}/{2*b2:g} µm).",
            f"Swing {pick['sw']:.3f} V/side ≥ {TARGET_SW}; divide OK "
            f"(phase {pick['phase']:.2f}°).",
            f"Buffer current ≈ {ib*1e3:.2f} mA [{tag}] "
            f"(Δ vs B2=4 baseline 1.00 mA: {dI*1e3:+.2f} mA).",
            f"Buffer active area ≈ {area_um2(b2):.0f} µm² [HAND] "
            f"(was {area_um2(4.0):.0f} µm² at B2=4).",
            "",
            "Apply: `C.apply_knobs(b2=..., vhf_tailless=True)`; set circuit.B2.",
        ]
        # persist knobs for later steps
        open(os.path.join(OUT, "buffer_size_knobs.json"), "w").write(
            f'{{"b2": {b2}, "v_min": {V_MIN}, "sw": {pick["sw"]}, '
            f'"vhf_tailless": true, "i_latch": 0.75e-3}}\n'
        )
        C.apply_knobs(b2=b2, vhf_tailless=True)
        # write default into circuit module file? leave to caller — set B2 default
        rc = 0

    path = os.path.join(OUT, "summary_vhf_buffer_size.txt")
    open(path, "w").write("\n".join(lines) + "\n")
    print("WROTE", path, flush=True)
    print("BUFFER_SIZE_DONE", flush=True)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
