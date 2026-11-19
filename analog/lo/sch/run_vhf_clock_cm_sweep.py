#!/usr/bin/env python3
"""P2.7.4a3 — ideal clock-CM level-shift sweep on VHF ÷3 [SCH].

Original tail (20 µm/mA) and R_L (swing 0.5). Buffer still drives ckp/ckn;
CML clock gates get series ideal V sources that raise/lower CM only.
"""
from __future__ import annotations

import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
# Restore pre-3a/3b defaults
C.apply_knobs(i_latch=0.75e-3, swing=0.5, tail_um_per_ma=20.0, tail_l="0.13u")


def patch_cml_clock_gates(body: str, delta: float) -> str:
    """Series ideal level-shift into CML latch clock gates only."""
    # Master/slave clock devices: m{name}5 gate=ckp, m{name}6 gate=ckn
    body = re.sub(
        r"^(m\S+5) \((\S+) ckp (\S+) (\S+)\) (sg13_lv_nmos.*)$",
        r"\1 (\2 ckp_g \3 \4) \5",
        body,
        flags=re.M,
    )
    body = re.sub(
        r"^(m\S+6) \((\S+) ckn (\S+) (\S+)\) (sg13_lv_nmos.*)$",
        r"\1 (\2 ckn_g \3 \4) \5",
        body,
        flags=re.M,
    )
    body += (
        f"vlsp (ckp_g ckp) vsource dc={delta:.4f}\n"
        f"vlsn (ckn_g ckn) vsource dc={delta:.4f}\n"
    )
    return body


def build_cm(band, f, corner, delta, tag):
    ctag, mos, vdd, temp = corner
    body, names, ideal, ndiv, duty = C.build_band_body(band, vdd)
    body = patch_cml_clock_gates(body, delta)
    i_l = C.I_LATCH
    en = ('en_lodiv (en_lodiv 0) vsource type="pulse" val0=0 '
          f'val1={vdd} delay=2n rise=100p fall=100p width=1\n')
    sup = (f'type="pulse" val0=0 val1={vdd} delay=0.2n rise=1n '
           f"fall=1n width=1")
    _, rl, _ = C.L1.cml_params(i_l, vdd)
    vref = vdd - i_l * rl / 2
    body = re.sub(
        r"^vref \(vref 0\) vsource dc=\S+",
        f"vref (vref 0) vsource dc={vref:.3f}",
        body,
        flags=re.M,
    )
    tb = (
        f"vbufs (vbuf 0) vsource {sup}\n"
        f"vdvs (vdv 0) vsource {sup}\n"
        f"vcvs (vcv 0) vsource {sup}\n"
        f"vdgs (vdg 0) vsource {sup}\n"
        f"vdds (vdd 0) vsource {sup}\n"
        + en + E.nbias_standin(i_l)
    )
    stop = 3e-9 + 20 * 24 / f
    name = f"lo_cm_{band}_{ctag}_{f/1e9:.2f}{tag}"
    path = os.path.join(E.OUT, name + ".sim")
    a = E.tank_amp(f)
    open(path, "w").write(
        C.HEADER.format(title=f"P2.7.4a3 CM {name}", mos=mos,
                        f=f, amp=a, vcm=vdd / 2, shape=0.0, offs=0.0,
                        t0=-1.0, tr=1e-12)
        + tb + "xtank (tp tn) clk\n" + body
        + "\ncontrol\n  abort always\n  options rawfile=\"binary\"\n"
        f"  options temp={temp}\n"
        f"  analysis tr tran stop={stop:.4e} step=5p maxstep=5p\nendc\n"
    )
    return path, names, ideal, ndiv, duty, vdd


def clk_stats(d, n0):
    ckp = np.real(d["ckp"])[n0:]
    ckn = np.real(d["ckn"])[n0:]
    # per-side swing and CM from mid of each
    sw_p = 0.5 * (ckp.max() - ckp.min())
    sw_n = 0.5 * (ckn.max() - ckn.min())
    cm = 0.5 * (0.5 * (ckp.max() + ckp.min()) + 0.5 * (ckn.max() + ckn.min()))
    return float(cm), float(0.5 * (sw_p + sw_n)), float(sw_p), float(sw_n)


def gate_cm(d, n0):
    """CM at level-shifted CML gates if present."""
    try:
        gp = np.real(d["ckp_g"])[n0:]
        gn = np.real(d["ckn_g"])[n0:]
        return float(0.5 * (0.5 * (gp.max() + gp.min()) +
                            0.5 * (gn.max() + gn.min())))
    except Exception:
        return None


def tail_vds(d, n0):
    try:
        return float(np.mean(np.real(d["tam"])[n0:]))
    except Exception:
        return None


def stage_ok(d, vdd, f_vco):
    th = 0.5 * vdd
    t = np.real(d["time"])
    rows = []
    for lab, node, div in (
        ("buf", "ckp", 1.0),
        ("q1p", "q1p", 3.0),
        ("orp", "orp", 3.0),
        ("x_clk", "x_clk", 3.0),
        ("x_r1", "x_r1", 24.0),
    ):
        try:
            v = np.real(d[node])
        except Exception:
            rows.append((lab, False, None))
            continue
        e = E.edges(t, v, th)
        if len(e) < 4:
            rows.append((lab, False, None))
            continue
        f = 1.0 / float(np.median(np.diff(e)))
        ok = abs(f - f_vco / div) / (f_vco / div) < 0.08
        rows.append((lab, ok, f))
    return rows


def run_one(vdd, delta, tag, f_ghz=3.12):
    E.CORNERS["ss"] = ("ss", "mos_ss", vdd, 125)
    path, names, ideal, ndiv, duty, v = build_cm(
        "vhf", f_ghz * 1e9, E.CORNERS["ss"], delta, tag)
    print(f"TRY vdd={vdd} delta={delta:+.3f} tag={tag}", flush=True)
    d = E.run(path)
    n0 = int(0.7 * len(np.real(d["time"])))
    cm_buf, sw, sw_p, sw_n = clk_stats(d, n0)
    cm_g = gate_cm(d, n0)
    tv = tail_vds(d, n0)
    r = E.analyse(d, names, ideal, ndiv, duty, v, f_ghz * 1e9)
    st = stage_ok(d, v, f_ghz * 1e9)
    all_cml = all(ok for lab, ok, _ in st if lab in ("q1p", "orp"))
    print(f"  buf_cm={cm_buf:.3f} sw={sw:.3f} gate_cm={cm_g} "
          f"tail_vds={tv} ok={r['ok']} phase={r['max_phase_err']} "
          f"stages={[(a,b) for a,b,_ in st]}", flush=True)
    return dict(vdd=vdd, delta=delta, cm_buf=cm_buf, sw=sw, sw_p=sw_p,
                sw_n=sw_n, cm_g=cm_g, tail_vds=tv, ok=bool(r["ok"]),
                phase=r["max_phase_err"], stages=st,
                all_cml=all_cml and bool(r["ok"]))


def main():
    os.makedirs(E.OUT, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    # Baseline diagnosis at both supplies (delta=0)
    base = []
    for vdd, tag in ((1.108, "_pad"), (1.08, "_flr")):
        base.append(run_one(vdd, 0.0, tag + "_d0"))

    # Sweep CM via delta relative to buffer CM at 1.108
    cm0 = base[0]["cm_buf"]
    # Target absolute CM values
    targets = [0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80]
    sweep = []
    first_pass = None
    for vdd in (1.108, 1.08):
        for tcm in targets:
            delta = tcm - cm0
            # keep gates inside ~0..vdd+0.1
            if tcm < 0.25 or tcm > vdd - 0.05:
                continue
            row = run_one(vdd, delta, f"_cm{int(tcm*100)}")
            row["tcm"] = tcm
            sweep.append(row)
            if row["all_cml"] and first_pass is None and vdd == 1.108:
                first_pass = row

    lines = [
        "# P2.7.4a3 — VHF ÷3 clock CM diagnosis + ideal level-shift sweep [SCH]",
        "",
        "Defaults: I_latch=0.75 mA, swing=0.5 (R_L), tail 20 µm/mA, L=0.13u.",
        "Level-shift: series ideal V on CML latch clock gates only (buffer ckp/ckn unchanged).",
        "",
        "## Baseline (delta=0)",
        "",
        "| VDD | buf CM | V/side | divide | max|φ| | tail V_DS |",
        "|---:|---:|---:|---|---:|---:|",
    ]
    for b in base:
        lines.append(
            f"| {b['vdd']:.3f} | {b['cm_buf']:.3f} | {b['sw']:.3f} | "
            f"{'OK' if b['ok'] else 'FAIL'} | {b['phase']:.2f} | "
            f"{b['tail_vds'] if b['tail_vds'] is not None else float('nan'):.3f} |"
        )
    lines += [
        "",
        "## CM sweep (target absolute CM at CML gates ≈ buf_CM + delta)",
        "",
        "| VDD | target CM | delta | gate CM | divide | max|φ| | tail V_DS | all CML |",
        "|---:|---:|---:|---:|---|---:|---:|---|",
    ]
    for s in sweep:
        gcm = s["cm_g"] if s["cm_g"] is not None else float("nan")
        tv = s["tail_vds"] if s["tail_vds"] is not None else float("nan")
        lines.append(
            f"| {s['vdd']:.3f} | {s.get('tcm', float('nan')):.2f} | "
            f"{s['delta']:+.3f} | {gcm:.3f} | "
            f"{'OK' if s['ok'] else 'FAIL'} | {s['phase']:.2f} | "
            f"{tv:.3f} | {'Y' if s['all_cml'] else 'N'} |"
        )
    lines.append("")
    if first_pass:
        lines += [
            f"**Lowest CM that fixes at 1.108 V:** target≈{first_pass.get('tcm')} "
            f"(delta={first_pass['delta']:+.3f} V); "
            f"tail V_DS={first_pass['tail_vds']:.3f} V [SCH].",
            "Next: schematic fix (lower buffer swing or AC+bias) to reach this CM.",
        ]
    else:
        lines += [
            "**No CM in sweep fixed divide** at 1.108 V [SCH].",
            "STOP for owner: topology choice (unstacked / folded / MCML / boosted sink).",
        ]
    text = "\n".join(lines) + "\n"
    path = os.path.join(OUT, "summary_vhf_clock_cm_sweep.txt")
    open(path, "w").write(text)
    open(os.path.join(E.OUT, "summary_vhf_clock_cm_sweep.txt"), "w").write(text)
    print("WROTE", path, flush=True)
    print("CM_SWEEP_DONE", "PASS" if first_pass else "FAIL", flush=True)
    return 0 if first_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
