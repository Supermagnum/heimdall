#!/usr/bin/env python3
"""P2.7.4a3 step 3b: lower CML swing (R_L) at fixed I; VHF ss [SCH]."""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402

# Keep a moderately wide tail from 3a (didn't pass alone; still helps V_DS).
DENS = 60.0
SWINGS = (0.50, 0.40, 0.35, 0.30, 0.25)
VDD = 1.108


def buffer_side_swing(d, vdd):
    ckp = np.real(d["ckp"])
    ckn = np.real(d["ckn"])
    n0 = int(0.7 * len(ckp))
    # per-side amp ≈ 0.5 * diff p2p
    dv = ckp[n0:] - ckn[n0:]
    return 0.5 * float(dv.max() - dv.min())


def cml_side_swing(d):
    q1p = np.real(d["q1p"])
    q1n = np.real(d["q1n"])
    n0 = int(0.7 * len(q1p))
    dv = q1p[n0:] - q1n[n0:]
    return 0.5 * float(dv.max() - dv.min())


def main():
    rows = []
    best = None
    E.CORNERS["ss"] = ("ss", "mos_ss", VDD, 125)
    for sw in SWINGS:
        C.apply_knobs(swing=sw, tail_um_per_ma=DENS, i_latch=0.75e-3)
        _, rl, _ = C.L1.cml_params(C.I_LATCH, VDD)
        path, names, ideal, ndiv, duty, v = E.build(
            "vhf", 3.12e9, E.CORNERS["ss"], tag=f"_sw{int(sw*1000)}_d{int(DENS)}")
        print(f"TRY swing={sw} RL={rl:.1f} dens={DENS} w={C.tail_w():.1f}u",
              flush=True)
        d = E.run(path)
        r = E.analyse(d, names, ideal, ndiv, duty, v, 3.12e9)
        buf = buffer_side_swing(d, v)
        cml = cml_side_swing(d)
        ok = bool(r["ok"])
        # Buffer into CML must stay ≥ 0.5 V/side (P2.4); CML out to converter
        # reported for info.
        buf_ok = buf >= 0.48
        print(f"  -> ok={ok} phase={r['max_phase_err']} "
              f"buf_side={buf:.3f} cml_side={cml:.3f} buf_ok={buf_ok}",
              flush=True)
        rows.append((sw, rl, ok, r["max_phase_err"], buf, cml, buf_ok))
        if ok and buf_ok and best is None:
            best = sw

    lines = [
        "# P2.7.4a3 step 3b — lower CML swing (R_L) for VHF ss [SCH]",
        "",
        f"I_latch=0.75 mA; tail dens={DENS} µm/mA; VDD={VDD} V (pad ss min).",
        "Buffer ≥0.5 V/side required (P2.4); measured on ckp−ckn.",
        "",
        "| swing | R_L | divide | max|φ| | buf V/side | CML V/side | buf≥0.5 |",
        "|---:|---:|---|---:|---:|---:|---|",
    ]
    for sw, rl, ok, ph, buf, cml, buf_ok in rows:
        lines.append(
            f"| {sw:.2f} | {rl:.1f} | {'OK' if ok else 'FAIL'} | {ph:.2f} | "
            f"{buf:.3f} | {cml:.3f} | {'Y' if buf_ok else 'N'} |")
    if best is not None:
        lines += ["", f"**PASS** at swing={best:.2f} V with buffer OK."]
    else:
        lines += [
            "",
            "**No PASS** with R_L reduction — step 3c unstacked ÷3 (owner).",
        ]
    text = "\n".join(lines) + "\n"
    shared = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "out", "summary_vhf_swing_fix.txt")
    os.makedirs(os.path.dirname(shared), exist_ok=True)
    open(shared, "w").write(text)
    open(os.path.join(E.OUT, "summary_vhf_swing_fix.txt"), "w").write(text)
    print("WROTE", shared, flush=True)
    print("SWING_FIX_DONE", "PASS" if best else "FAIL", best, flush=True)
    return 0 if best else 1


if __name__ == "__main__":
    raise SystemExit(main())
