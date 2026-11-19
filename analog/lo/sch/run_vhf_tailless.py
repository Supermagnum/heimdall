#!/usr/bin/env python3
"""P2.7.4a3 step 3 — VHF ÷3 tail-less clock pair [SCH]."""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
C.apply_knobs(i_latch=0.75e-3, swing=0.5, tail_um_per_ma=20.0,
              vhf_tailless=True)

CASES = [
    ("ss", 1.108, 125, 3.12),
    ("ss", 1.08, 125, 3.12),
    ("ss", 1.05, 125, 3.12),  # 30 mV below 1.08
    ("ss", 1.08, 125, 4.20),
    ("tt", 1.20, 27, 3.12),
    ("tt", 1.20, 27, 4.20),
]


def supply_current(d, vdd_name="vdd"):
    # Not always in raw; estimate from known I_latch count if missing
    return None


def main():
    os.makedirs(E.OUT, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for ctag, vdd, temp, f_ghz in CASES:
        mos = "mos_ss" if ctag == "ss" else "mos_tt"
        E.CORNERS[ctag] = (ctag, mos, vdd, temp)
        print(f"TRY {ctag} VDD={vdd} T={temp} f={f_ghz} tailless={C.VHF_TAILLESS}",
              flush=True)
        path, names, ideal, ndiv, duty, v = E.build(
            "vhf", f_ghz * 1e9, E.CORNERS[ctag],
            tag=f"_tl_{ctag}_{vdd:.3f}_{f_ghz:.2f}")
        # Confirm tailless netlist: no latch isource to t*
        body = open(path).read()
        n_itail = body.count("isource dc=")  # may include kick/nbias
        has_tam = "mtam " in body or "(tam " in body
        d = E.run(path)
        r = E.analyse(d, names, ideal, ndiv, duty, v, f_ghz * 1e9)
        n0 = int(0.7 * len(np.real(d["time"])))
        ckp = np.real(d["ckp"])[n0:]
        ckn = np.real(d["ckn"])[n0:]
        sw = 0.5 * 0.5 * ((ckp.max() - ckp.min()) + (ckn.max() - ckn.min()))
        ok = bool(r["ok"])
        print(f"  -> ok={ok} phase={r['max_phase_err']} "
              f"duty={r['duty_min']}/{r['duty_max']} sw={sw:.3f} "
              f"has_tam_node={has_tam}", flush=True)
        rows.append(dict(
            ctag=ctag, vdd=vdd, temp=temp, f=f_ghz, ok=ok,
            phase=r["max_phase_err"], duty=(r["duty_min"], r["duty_max"]),
            sw=sw,
        ))

    lines = [
        "# P2.7.4a3 step 3 — VHF ÷3 tail-less clock [SCH]",
        "",
        "L1.VARIANT['tailless']=True for band=vhf only; NOR keeps MOSFET tail;",
        "latch clock sources to gnd (2-high stack). I_latch=0.75 mA, swing=0.5.",
        "",
        "| Corner | VDD | T | f_VCO | divide | max|φ| | duty | buf V/side |",
        "|---|---:|---:|---:|---|---:|---|---:|",
    ]
    for r in rows:
        d0, d1 = r["duty"]
        ds = f"{d0:.1f}/{d1:.1f}" if d0 is not None else "—"
        lines.append(
            f"| {r['ctag']} | {r['vdd']:.3f} | {r['temp']} | {r['f']:.2f} | "
            f"{'OK' if r['ok'] else 'FAIL'} | {r['phase']:.2f} | {ds} | "
            f"{r['sw']:.3f} |"
        )
    ss_ok = all(r["ok"] for r in rows if r["ctag"] == "ss" and r["vdd"] >= 1.08)
    margin = next((r for r in rows if abs(r["vdd"] - 1.05) < 1e-6), None)
    lines.append("")
    if ss_ok:
        lines.append("**ss @ ≥1.08 V:** PASS [SCH].")
    else:
        lines.append("**ss @ ≥1.08 V:** FAIL [SCH].")
    if margin:
        lines.append(
            f"30 mV margin @ 1.05 V: {'PASS' if margin['ok'] else 'FAIL'} [SCH]."
        )
    if not ss_ok:
        lines.append(
            "STOP: report folded PMOS-load as next option (owner preference order)."
        )
    text = "\n".join(lines) + "\n"
    path = os.path.join(OUT, "summary_vhf_tailless.txt")
    open(path, "w").write(text)
    open(os.path.join(E.OUT, "summary_vhf_tailless.txt"), "w").write(text)
    print("WROTE", path, flush=True)
    print("TAILLESS_DONE", "PASS" if ss_ok else "FAIL", flush=True)
    return 0 if ss_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
