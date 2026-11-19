#!/usr/bin/env python3
"""P2.7.4b step 0a — VHF ff pre-checks at final currents [SCH].

ff / −40 °C and ff / 125 °C at V_max 1.208 V and V_min 1.181 V,
3.12–4.20 GHz: divide, duty, phase, stage currents.
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
V_MIN = 1.181
V_MAX = 1.208
VCO_TYP = 3.59e-3
PLL_HAND = 1.5e-3
FREQS = (3.12e9, 4.20e9)
CASES = (
    ("ff_m40_vmax", "mos_ff", V_MAX, -40),
    ("ff_m40_vmin", "mos_ff", V_MIN, -40),
    ("ff_125_vmax", "mos_ff", V_MAX, 125),
    ("ff_125_vmin", "mos_ff", V_MIN, 125),
)


def mean_flow(d, src):
    keep = np.real(d["time"])
    n0 = int(0.7 * len(keep))
    for key in (f"{src}:flow(br)", f"i({src})", src):
        try:
            arr = np.real(d[key])
            return float(np.mean(np.abs(arr[n0:])))
        except Exception:
            continue
    return float("nan")


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(E.OUT, exist_ok=True)
    C.apply_knobs(i_latch=0.75e-3, vhf_i_latch=0.30e-3, b2=4.0,
                  vhf_tailless=True)

    lines = [
        "# P2.7.4b step 0a — VHF ff pre-check at final currents [SCH]",
        "",
        f"VHF I_latch={C.VHF_I_LATCH*1e3:g} mA; B2={C.B2:g}; tailless; "
        f"V_min={V_MIN} V; V_max={V_MAX} V.",
        "",
        "## Cases",
        "",
        "| Case | f (GHz) | divide | max|φ| | duty min/max % | "
        "I_buf | I_CML | I_conv | I_logic | LO tot |",
        "|---|---:|---|---:|---|---:|---:|---:|---:|---:|",
    ]
    print("\n".join(lines[:6]), flush=True)
    fails = 0
    for cname, mos, vdd, temp in CASES:
        corner = (cname, mos, vdd, temp)
        for f in FREQS:
            tag = f"_ffpc_{cname}_{f/1e9:.2f}"
            try:
                path, names, ideal, ndiv, duty, v = E.build(
                    "vhf", f, corner, tag=tag)
                d = E.run(path)
                r = E.analyse(d, names, ideal, ndiv, duty, v, f)
                ok = bool(r["ok"])
                ib = mean_flow(d, "vbufs")
                ic = mean_flow(d, "vdvs")
                iv = mean_flow(d, "vcvs")
                ig = mean_flow(d, "vdgs")
                # exclude TB I_bias (vdds) — PLL HAND already has it
                ilo = ib + ic + iv + ig + VCO_TYP + PLL_HAND
                dmin, dmax = r.get("duty_min"), r.get("duty_max")
                ds = (f"{dmin:.1f}/{dmax:.1f}"
                      if dmin is not None and dmax is not None else "—")
                if not ok:
                    fails += 1
                line = (
                    f"| {cname} | {f/1e9:.2f} | {'OK' if ok else 'FAIL'} | "
                    f"{r['max_phase_err']:.2f} | {ds} | "
                    f"{ib*1e3:.3f} | {ic*1e3:.3f} | {iv*1e3:.3f} | "
                    f"{ig*1e3:.3f} | {ilo*1e3:.2f} |"
                )
            except Exception as e:
                fails += 1
                line = f"| {cname} | {f/1e9:.2f} | FAIL | — | — | — | — | — | — | — |"
                print(f"EXC {cname} {f/1e9:.2f}: {e}", flush=True)
            print(line, flush=True)
            lines.append(line)

    lines += [
        "",
        "## Gate",
        "",
        f"- Fail count: {fails}",
        "- Pass iff all cases divide (duty/phase reported for owner).",
        "",
        "FF_PRECHECK_DONE",
        "",
    ]
    path = os.path.join(OUT, "summary_vhf_a3_ff_precheck.txt")
    open(path, "w").write("\n".join(lines) + "\n")
    print("WROTE", path, flush=True)
    print("FF_PRECHECK_DONE", flush=True)
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
