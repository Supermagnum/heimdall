#!/usr/bin/env python3
"""P2.7.4a3 step 4 — final corners / duty / MC with sized currents [SCH]."""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
V_MIN = 1.181
MC_N = 20


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(E.OUT, exist_ok=True)
    C.apply_knobs(i_latch=0.75e-3, vhf_i_latch=0.30e-3, b2=4.0,
                  vhf_tailless=True)
    E.CORNERS["ss"] = ("ss", "mos_ss", V_MIN, 125)
    E.CORNERS["tt"] = ("tt", "mos_tt", 1.20, 27)

    lines = [
        "# P2.7.4a3 final corners — sized currents [SCH]",
        "",
        f"UHF I_latch={C.I_LATCH*1e3:g} mA; VHF I_latch={C.VHF_I_LATCH*1e3:g} mA; "
        f"B2={C.B2:g}; tailless; ss VDD={V_MIN} V.",
        "",
        "## Corners",
        "",
        "| Band | Corner | f (GHz) | divide | max|φ| | duty min/max % |",
        "|---|---|---:|---|---:|---|",
    ]
    print("\n".join(lines[:6]), flush=True)
    fails = 0
    for band in ("uhf", "vhf"):
        for cname in ("tt", "ss"):
            for f in E.CASES[band]:
                path, names, ideal, ndiv, duty, v = E.build(
                    band, f, E.CORNERS[cname], tag="_fin")
                d = E.run(path)
                r = E.analyse(d, names, ideal, ndiv, duty, v, f)
                ok = bool(r["ok"])
                if not ok:
                    fails += 1
                dmin, dmax = r.get("duty_min"), r.get("duty_max")
                ds = (f"{dmin:.1f}/{dmax:.1f}"
                      if dmin is not None and dmax is not None else "—")
                line = (f"| {band} | {cname} | {f/1e9:.2f} | "
                        f"{'OK' if ok else 'FAIL'} | {r['max_phase_err']:.2f} | "
                        f"{ds} |")
                print(line, flush=True)
                lines.append(line)

    lines += ["", "## VHF ss f_max [SCH]", ""]
    f_max = None
    for f_ghz in (4.20, 4.50, 4.80, 5.20, 5.60, 6.00):
        f = f_ghz * 1e9
        path, names, ideal, ndiv, duty, v = E.build(
            "vhf", f, E.CORNERS["ss"], tag=f"_ffm{f_ghz:.2f}",
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
    lines.append(f"**f_max_ss ≈ {f_max} GHz**")

    lines += ["", f"## Monte Carlo N={MC_N} VHF ss 4.20 [SCH]", ""]
    rng = np.random.default_rng(42)
    n_ok = 0
    phs = []
    for i in range(MC_N):
        path, names, ideal, ndiv, duty, v = E.build(
            "vhf", 4.20e9, E.CORNERS["ss"], rng=rng, tag=f"_fmc{i}")
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
            f"| max|φ| mean/σ/max | "
            f"{phs_ok.mean():.3f} / {phs_ok.std():.3f} / {phs_ok.max():.3f} ° |"
        )
    if n_ok < MC_N:
        fails += 1

    lines += [
        "",
        "## Gates",
        "",
        f"- Corner fails: {fails}",
        "- UHF I/Q ≤ 0.46°: see max|φ| column",
        "- VHF 8-phase: table + MC",
        "- Duty: UHF ~25 %, VHF ~50 % (min/max column)",
        "",
    ]
    path = os.path.join(OUT, "summary_vhf_a3_final_corners.txt")
    open(path, "w").write("\n".join(lines) + "\n")
    print("WROTE", path, flush=True)
    print("FINAL_CORNERS_DONE", flush=True)
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
