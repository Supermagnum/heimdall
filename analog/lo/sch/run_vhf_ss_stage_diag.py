#!/usr/bin/env python3
"""P2.7.4a3 step 1: VHF ss stage-by-stage divide check [SCH].

One corner (mos_ss / 1.08 V / 125 C), real MOSFET tails, I_latch from circuit.
Reports first-failing stage and cause hint; writes summary_vhf_ss_a3.txt.
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402

STAGES = [
    ("1_buffer", "ckp", 1.0, "VCO buffer"),
    ("2_cml_ff1", "q1p", 3.0, "CML ÷3 latch 1"),
    ("2_cml_ff2", "q2p", 3.0, "CML ÷3 latch 2"),
    ("2_cml_out", "orp", 3.0, "CML ÷3 NOR out"),
    ("3_converter", "x_clk", 3.0, "CML→CMOS converter"),
    ("4_johnson_q1", "x_q1", 24.0, "Johnson ÷8 q1"),
    ("5_retime_0", "x_r1", 24.0, "retimed 0° LO"),
]


def freq_duty(t, v, th):
    e = E.edges(t, v, th)
    if len(e) < 4:
        return None, None, float(np.min(v)), float(np.max(v))
    per = np.diff(e)
    f = 1.0 / float(np.median(per))
    # duty from high time between rising edges via mid-crossing fall
    s = v > th
    fall = np.where(s[:-1] & ~s[1:])[0]
    if len(fall) < 2 or len(e) < 3:
        return f, None, float(np.min(v)), float(np.max(v))
    # approximate duty from fraction above th in last 30% of run
    n0 = int(0.7 * len(v))
    duty = 100.0 * float(np.mean(v[n0:] > th))
    return f, duty, float(np.min(v)), float(np.max(v))


def main():
    f_vco = 3.12e9
    corner = E.CORNERS["ss"]
    print(f"I_LATCH={C.I_LATCH*1e3:.3f} mA SWING={C.SWING} TAIL_L={C.TAIL_L}",
          flush=True)
    path, names, ideal, ndiv, duty, vdd = E.build(
        "vhf", f_vco, corner, tag="_a3diag")
    print("sim", path, "vdd", vdd, flush=True)
    d = E.run(path)
    t = np.real(d["time"])
    th = 0.5 * vdd
    rows = []
    first_fail = None
    for key, node, div, label in STAGES:
        try:
            v = np.real(d[node])
        except Exception:
            rows.append((key, label, node, "MISSING", None, None, None, None))
            if first_fail is None:
                first_fail = (key, label, "node missing from raw")
            continue
        f, du, vmin, vmax = freq_duty(t, v, th)
        f_exp = f_vco / div
        if f is None:
            ok = False
            note = "no edges"
        else:
            err = abs(f - f_exp) / f_exp
            # ÷2 lock of ÷3 is classic: f ≈ f_vco/2
            ok = err < 0.08
            note = f"err={100*err:.1f}%"
            if not ok and abs(f - f_vco / 2) / (f_vco / 2) < 0.08:
                note += "; looks like f/2 lock"
        rows.append((key, label, node, "OK" if ok else "FAIL", f, du, vmin, vmax))
        print(f"{key:14s} {label:22s} {node:6s} "
              f"{'OK' if ok else 'FAIL':4s} f={f if f else float('nan'):.3e} "
              f"exp={f_exp:.3e} duty={du} swing={vmax-vmin:.3f}V [{note}]",
              flush=True)
        if not ok and first_fail is None:
            cause = note
            if vmax - vmin < 0.15:
                cause = f"collapsed swing {vmin:.3f}..{vmax:.3f} V ({note})"
            elif f is not None and abs(f - f_vco / 2) / (f_vco / 2) < 0.08:
                cause = ("÷3 in f/2 regenerative lock "
                         f"(f={f/1e9:.3f} GHz; headroom/regen/bias)")
            elif f is None:
                cause = (f"no edges at {node}; stuck "
                         f"{vmin:.3f}..{vmax:.3f} V (bias/tail/enable)")
            first_fail = (key, label, cause)

    r = E.analyse(d, names, ideal, ndiv, duty, vdd, f_vco)
    lim = E.REF["vhf_phase_max_deg"] + 0.5
    gate = ("PASS" if r["ok"] and r["max_phase_err"] <= lim + 0.2
            else "FAIL")
    print("CHAIN", "ok", r["ok"], "phase", r["max_phase_err"],
          "duty", r["duty_min"], r["duty_max"], "gate", gate, flush=True)

    out = os.path.join(E.OUT, "summary_vhf_ss_a3.txt")
    lines = [
        "# P2.7.4a3 step 1 — VHF ss stage diag [SCH]",
        "",
        f"Corner: mos_ss / VDD={vdd} V / 125 C; f_VCO={f_vco/1e9:.2f} GHz; "
        f"I_latch={C.I_LATCH*1e3:.3f} mA; MOSFET tails; real xschem netlist path.",
        "",
        "| Stage | Node | divide | f [Hz] | duty % | swing V | gate |",
        "|---|---|---|---|---|---|---|",
    ]
    for key, label, node, g, f, du, vmin, vmax in rows:
        fs = f"{f:.4e}" if f is not None else "—"
        dus = f"{du:.1f}" if du is not None else "—"
        sw = f"{vmax-vmin:.3f}" if vmin is not None else "—"
        lines.append(
            f"| {label} ({key}) | {node} | — | {fs} | {dus} | {sw} | {g} |")
    lines += [
        "",
        f"Chain analyse: ok={r['ok']} max|φ−ideal|={r['max_phase_err']:.2f}° "
        f"duty={r['duty_min']}/{r['duty_max']} gate={gate}",
        "",
    ]
    if first_fail:
        lines += [
            f"**First fail:** {first_fail[0]} / {first_fail[1]}",
            f"**Cause:** {first_fail[2]}",
            "",
            "STOP for owner (decisions.md: VHF ss checked first; redesign before "
            "current sizing if divide fails).",
        ]
    else:
        lines.append("All probed stages divide within 8 % of expected frequency.")
    open(out, "w").write("\n".join(lines) + "\n")
    print("WROTE", out, flush=True)
    print("VHF_SS_A3_DONE", "FAIL" if first_fail else "PASS", flush=True)
    return 1 if first_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
