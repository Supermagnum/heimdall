#!/usr/bin/env python3
"""P2.7.4a3 — wide tail × raised clock CM combination [SCH].

÷3 only via ideal level-shift on latch clock gates; ÷2 path unused (VHF TB).
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402
import run_vhf_clock_cm_sweep as CM  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
VT = 0.45  # [HAND]
DENS = (60.0, 120.0)   # ×3 and ×6 of 20 µm/mA
CMS = (0.60, 0.70, 0.80)
VDDS = (1.108, 1.08)


def latch_stack(d, n0):
    """Return tail / clock / latch V_DS means for master latch am."""
    def m(n):
        try:
            return float(np.mean(np.real(d[n])[n0:]))
        except Exception:
            return float("nan")
    tam, s1, s2 = m("tam"), m("s1am"), m("s2am")
    q1p, q1n = m("q1p"), m("q1n")
    nb = m("nb_lo")
    return dict(
        tail_vds=tam,
        vdsat=max(nb - VT, 0.05),
        ck_vds=0.5 * ((s1 - tam) + (s2 - tam)),
        latch_vds=0.5 * ((q1p - s1) + (q1n - s2)),
        nb=nb,
    )


def run_case(vdd, dens, tcm, f_ghz=3.12):
    C.apply_knobs(i_latch=0.75e-3, swing=0.5, tail_um_per_ma=dens, tail_l="0.13u")
    E.CORNERS["ss"] = ("ss", "mos_ss", vdd, 125)
    # Estimate buf CM ~0.52 at 1.108 from prior; measure after with delta from 0.52
    # Use fixed ref CM 0.52 for delta so target gate CM ≈ tcm
    cm_ref = 0.524 if vdd > 1.09 else 0.504
    delta = tcm - cm_ref
    tag = f"_d{int(dens)}_cm{int(tcm*100)}"
    path, names, ideal, ndiv, duty, v = CM.build_cm(
        "vhf", f_ghz * 1e9, E.CORNERS["ss"], delta, tag)
    print(f"TRY dens={dens} tcm={tcm} vdd={vdd} delta={delta:+.3f} "
          f"w={C.tail_w():.1f}u", flush=True)
    d = E.run(path)
    n0 = int(0.7 * len(np.real(d["time"])))
    cm_buf, sw, _, _ = CM.clk_stats(d, n0)
    cm_g = CM.gate_cm(d, n0)
    st = latch_stack(d, n0)
    r = E.analyse(d, names, ideal, ndiv, duty, v, f_ghz * 1e9)
    stages = CM.stage_ok(d, v, f_ghz * 1e9)
    cml_ok = all(ok for lab, ok, _ in stages if lab in ("q1p", "orp"))
    ok = bool(r["ok"]) and cml_ok
    print(f"  -> ok={ok} phase={r['max_phase_err']} gate_cm={cm_g} "
          f"tail={st['tail_vds']:.3f}/{st['vdsat']:.3f} "
          f"ck={st['ck_vds']:.3f} latch={st['latch_vds']:.3f}", flush=True)
    return dict(
        dens=dens, tcm=tcm, vdd=vdd, ok=ok, phase=r["max_phase_err"],
        cm_buf=cm_buf, sw=sw, cm_g=cm_g, **st,
        duty=(r["duty_min"], r["duty_max"]),
    )


def main():
    os.makedirs(E.OUT, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for dens in DENS:
        for tcm in CMS:
            for vdd in VDDS:
                rows.append(run_case(vdd, dens, tcm))

    # Smallest dens + lowest CM that PASS at 1.108
    winners = [r for r in rows if r["ok"] and abs(r["vdd"] - 1.108) < 1e-6]
    winners.sort(key=lambda r: (r["dens"], r["tcm"]))
    best = winners[0] if winners else None

    # Margin: if best, also check vdd = best_vdd - 0.03
    margin = None
    if best:
        print("MARGIN check at VDD-30mV", flush=True)
        margin = run_case(best["vdd"] - 0.03, best["dens"], best["tcm"])

    lines = [
        "# P2.7.4a3 — wide tail × raised clock CM [SCH]",
        "",
        "I_latch=0.75 mA; swing=0.5; ideal series CM shift on ÷3 latch clocks only.",
        "",
        "| dens µm/mA | target CM | VDD | divide | max|φ| | "
        "tail V_DS | V_dsat | ck V_DS | latch V_DS | gate CM |",
        "|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        g = r["cm_g"] if r["cm_g"] is not None else float("nan")
        lines.append(
            f"| {r['dens']:.0f} | {r['tcm']:.2f} | {r['vdd']:.3f} | "
            f"{'OK' if r['ok'] else 'FAIL'} | {r['phase']:.2f} | "
            f"{r['tail_vds']:.3f} | {r['vdsat']:.3f} | {r['ck_vds']:.3f} | "
            f"{r['latch_vds']:.3f} | {g:.3f} |"
        )
    lines.append("")
    if best:
        lines.append(
            f"**Smallest PASS at 1.108 V:** dens={best['dens']:.0f} µm/mA, "
            f"CM={best['tcm']:.2f} V; tail V_DS={best['tail_vds']:.3f} vs "
            f"V_dsat={best['vdsat']:.3f} [SCH]."
        )
        if margin:
            lines.append(
                f"Margin at VDD={margin['vdd']:.3f}: "
                f"{'PASS' if margin['ok'] else 'FAIL'} "
                f"(phase={margin['phase']:.2f}) [SCH]."
            )
    else:
        lines.append(
            "**No PASS** in dens×CM matrix [SCH]. Next: tail-less clock on ÷3 only."
        )
    text = "\n".join(lines) + "\n"
    path = os.path.join(OUT, "summary_vhf_combo_fix.txt")
    open(path, "w").write(text)
    open(os.path.join(E.OUT, "summary_vhf_combo_fix.txt"), "w").write(text)
    print("WROTE", path, flush=True)
    print("COMBO_DONE", "PASS" if best else "FAIL",
          best and (best["dens"], best["tcm"]), flush=True)
    return 0 if best else 1


if __name__ == "__main__":
    raise SystemExit(main())
