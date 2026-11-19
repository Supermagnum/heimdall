#!/usr/bin/env python3
"""P2.7.4a3 diagnosis: VHF ÷3 vs frequency (tailed / tailless) [SCH].

Also ÷3 at ≤2.1 GHz for re-ordered-chain option (clock = VCO/2).
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
FREQS = (3.12, 3.40, 3.70, 4.00, 4.20)  # GHz at VCO
LOW_F = (1.56, 1.70, 1.85, 2.00, 2.10)  # GHz (= VCO/2 for re-order)
VDDS = (1.108, 1.08, 1.05)


def buf_sw(d):
    n0 = int(0.7 * len(np.real(d["time"])))
    ckp = np.real(d["ckp"])[n0:]
    ckn = np.real(d["ckn"])[n0:]
    return float(0.25 * ((ckp.max() - ckp.min()) + (ckn.max() - ckn.min())))


def stack(d):
    n0 = int(0.7 * len(np.real(d["time"])))

    def m(n):
        try:
            return float(np.mean(np.real(d[n])[n0:]))
        except Exception:
            return float("nan")

    tam = m("tam")
    s1, s2 = m("s1am"), m("s2am")
    return tam, 0.5 * ((s1 - tam) + (s2 - tam))


def one(tailless, vdd, f_ghz, tag):
    C.apply_knobs(i_latch=0.75e-3, swing=0.5, tail_um_per_ma=20.0,
                  vhf_tailless=tailless, b2=4.0)
    E.CORNERS["ss"] = ("ss", "mos_ss", vdd, 125)
    path, names, ideal, ndiv, duty, v = E.build(
        "vhf", f_ghz * 1e9, E.CORNERS["ss"], tag=tag)
    d = E.run(path)
    r = E.analyse(d, names, ideal, ndiv, duty, v, f_ghz * 1e9)
    sw = buf_sw(d)
    tv, ck = stack(d)
    ok = bool(r["ok"])
    mode = "TL" if tailless else "TD"
    print(f"{mode} VDD={vdd} f={f_ghz:.2f} ok={ok} ph={r['max_phase_err']:.2f} "
          f"sw={sw:.3f} tail={tv:.3f} ck={ck:.3f}", flush=True)
    return dict(mode=mode, vdd=vdd, f=f_ghz, ok=ok, phase=r["max_phase_err"],
                sw=sw, tail_vds=tv, ck_vds=ck)


def main():
    os.makedirs(E.OUT, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    rows = []
    # Full VCO-rate sweep at 1.108 and 1.08
    for tailless in (False, True):
        for vdd in (1.108, 1.08):
            for f in FREQS:
                tag = f"_fd_{'tl' if tailless else 'td'}_{vdd:.3f}_{f:.2f}"
                rows.append(one(tailless, vdd, f, tag))
    # Low-freq ÷3 (re-order) at 1.08 and 1.05 — tailed first, then tailless if needed
    low_rows = []
    for vdd in (1.08, 1.05):
        for f in LOW_F:
            low_rows.append(one(False, vdd, f, f"_lo_td_{vdd:.3f}_{f:.2f}"))
    # If any tailed low-f fails, add tailless
    if any(not r["ok"] for r in low_rows):
        for vdd in (1.08, 1.05):
            for f in LOW_F:
                low_rows.append(one(True, vdd, f, f"_lo_tl_{vdd:.3f}_{f:.2f}"))

    def classify(mode, vdd):
        pts = [r for r in rows if r["mode"] == mode and abs(r["vdd"] - vdd) < 1e-6]
        oks = [r["ok"] for r in pts]
        if all(oks):
            return "all PASS"
        if not any(oks):
            return "headroom (fails all f)"
        # find first fail freq
        for r in pts:
            if not r["ok"]:
                return f"drive/BW (fails above ~{r['f']:.2f} GHz)"
        return "mixed"

    lines = [
        "# P2.7.4a3 diagnosis — VHF ÷3 vs frequency [SCH]",
        "",
        "mos_ss / 125 °C; I_latch=0.75 mA; swing=0.5; real buffer (B2=4); MOSFET NOR tail.",
        "TD = stacked tailed latches; TL = VARIANT tailless (clock→gnd).",
        "",
        "## VCO-rate sweep",
        "",
        "| Mode | VDD | f_VCO | divide | max|φ| | buf V/side | tail V_DS | ck V_DS |",
        "|---|---:|---:|---|---:|---:|---:|---:|",
    ]
    for r in rows:
        lines.append(
            f"| {r['mode']} | {r['vdd']:.3f} | {r['f']:.2f} | "
            f"{'OK' if r['ok'] else 'FAIL'} | {r['phase']:.2f} | "
            f"{r['sw']:.3f} | {r['tail_vds']:.3f} | {r['ck_vds']:.3f} |"
        )
    lines += ["", "## Failure class", ""]
    for mode in ("TD", "TL"):
        for vdd in (1.108, 1.08):
            lines.append(f"- {mode} @ {vdd:.3f} V: **{classify(mode, vdd)}**")
    lines += [
        "",
        "## ÷3 at ≤ 2.1 GHz (re-ordered chain clock = VCO/2) [SCH]",
        "",
        "| Mode | VDD | f_ck | divide | max|φ| | buf V/side |",
        "|---|---:|---:|---|---:|---:|",
    ]
    for r in low_rows:
        lines.append(
            f"| {r['mode']} | {r['vdd']:.3f} | {r['f']:.2f} | "
            f"{'OK' if r['ok'] else 'FAIL'} | {r['phase']:.2f} | {r['sw']:.3f} |"
        )
    path = os.path.join(OUT, "summary_vhf_freq_diag.txt")
    open(path, "w").write("\n".join(lines) + "\n")
    open(os.path.join(E.OUT, "summary_vhf_freq_diag.txt"), "w").write(
        "\n".join(lines) + "\n")
    print("WROTE", path, flush=True)
    print("FREQ_DIAG_DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
