#!/usr/bin/env python3
"""P2.7.4a3 step 4 — divider check with tailless ÷3 + sized buffer [SCH].

Corners: tt 1.20 / 27 °C; ss V_min 1.181 / 125 °C. Bands UHF + VHF.
Also f_max probe on VHF ss; Monte Carlo N=20 VHF ss 4.20.
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
V_MIN = 1.181
B2 = 4.0
MC_N = 20


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(E.OUT, exist_ok=True)
    C.apply_knobs(i_latch=0.75e-3, swing=0.5, b2=B2, vhf_tailless=True)
    E.CORNERS["ss"] = ("ss", "mos_ss", V_MIN, 125)
    E.CORNERS["tt"] = ("tt", "mos_tt", 1.20, 27)

    lines = [
        "# P2.7.4a3 step 4 — divider check tailless ÷3 [SCH]",
        "",
        f"VHF_TAILLESS=True; B2={B2:g}; I_latch=0.75 mA; ss VDD={V_MIN} V.",
        "",
        "## Corners",
        "",
        "| Band | Corner | f (GHz) | divide | max|φ| | duty |",
        "|---|---|---:|---|---:|---|",
    ]
    print("\n".join(lines[:6]), flush=True)
    fails = 0
    for band in ("uhf", "vhf"):
        for cname in ("tt", "ss"):
            for f in E.CASES[band]:
                tag = f"_a3c"
                path, names, ideal, ndiv, duty, v = E.build(
                    band, f, E.CORNERS[cname], tag=tag)
                d = E.run(path)
                r = E.analyse(d, names, ideal, ndiv, duty, v, f)
                ok = bool(r["ok"])
                if not ok:
                    fails += 1
                dut = r.get("duty")
                if isinstance(dut, (list, tuple)) and len(dut) >= 2:
                    ds = f"{dut[0]:.1f}/{dut[1]:.1f}"
                else:
                    ds = str(dut)
                line = (f"| {band} | {cname} | {f/1e9:.2f} | "
                        f"{'OK' if ok else 'FAIL'} | {r['max_phase_err']:.2f} | "
                        f"{ds} |")
                print(line, flush=True)
                lines.append(line)

    # f_max VHF ss: binary-ish sweep above 4.20
    lines += ["", "## VHF ss f_max probe [SCH]", ""]
    print("f_max probe...", flush=True)
    f_max = None
    for f_ghz in (4.20, 4.50, 4.80, 5.20, 5.60, 6.00):
        f = f_ghz * 1e9
        path, names, ideal, ndiv, duty, v = E.build(
            "vhf", f, E.CORNERS["ss"], tag=f"_fm{f_ghz:.2f}",
            amp=E.tank_amp(min(f, 4.20e9)))
        d = E.run(path)
        r = E.analyse(d, names, ideal, ndiv, duty, v, f)
        ok = bool(r["ok"])
        lines.append(f"- {f_ghz:.2f} GHz: {'OK' if ok else 'FAIL'} "
                     f"(φ={r['max_phase_err']:.2f})")
        print(f"fmax {f_ghz} ok={ok}", flush=True)
        if ok:
            f_max = f_ghz
        else:
            break
    lines.append(f"**f_max_ss ≈ {f_max} GHz** (last OK; tank amp held at 4.20 level).")

    # Monte Carlo
    lines += ["", f"## Monte Carlo N={MC_N} VHF ss 4.20 [SCH]", ""]
    print("MC...", flush=True)
    rng = np.random.default_rng(42)
    n_ok = 0
    phs = []
    for i in range(MC_N):
        path, names, ideal, ndiv, duty, v = E.build(
            "vhf", 4.20e9, E.CORNERS["ss"], rng=rng, tag=f"_mc{i}")
        d = E.run(path)
        r = E.analyse(d, names, ideal, ndiv, duty, v, 4.20e9)
        ok = bool(r["ok"])
        n_ok += int(ok)
        phs.append(r["max_phase_err"])
        print(f"MC {i} ok={ok} ph={r['max_phase_err']:.2f}", flush=True)
    phs = np.array(phs, dtype=float)
    phs_ok = phs[phs < 100]
    lines.append(f"| Pass | {n_ok}/{MC_N} |")
    if len(phs_ok):
        lines.append(
            f"| max|φ| mean/σ/max (OK samples) | "
            f"{phs_ok.mean():.3f} / {phs_ok.std():.3f} / {phs_ok.max():.3f} ° |"
        )
    if n_ok < MC_N:
        fails += 1

    # Phase gates
    lines += [
        "",
        "## Gates vs a3 criteria",
        "",
        f"- UHF I/Q phase ≤ 0.46°: see table (tt/ss).",
        f"- VHF 8-phase error: max|φ| in table / MC.",
        f"- Duty: UHF ~25 %, VHF ~50 % (table).",
        f"- Corner fails count: {fails}",
        "",
    ]
    path = os.path.join(OUT, "summary_vhf_a3_corners.txt")
    open(path, "w").write("\n".join(lines) + "\n")
    open(os.path.join(E.OUT, "summary_vhf_a3_corners.txt"), "w").write(
        "\n".join(lines) + "\n")
    print("WROTE", path, flush=True)
    print("A3_CORNERS_DONE", flush=True)
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
