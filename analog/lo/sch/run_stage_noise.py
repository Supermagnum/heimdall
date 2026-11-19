#!/usr/bin/env python3
"""P2.7.4a2 step 3 — per-stage LO noise with C_ck = 15 fF / side [SCH].

Method: ZOH transient noise on each isolated stage (clean clock in).
Falls back note if tran fails (PSS/pnoise not run unless needed).
"""
from __future__ import annotations

import json
import math
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path.insert(0, HERE)
import circuit as C  # noqa: E402

C_CK = 15e-15
F_VCO_UHF, F_VCO_VHF = 3.84e9, 4.20e9
CORNER = ("tt", "mos_tt", 1.20, 27)
TSTOP = 0.4e-6
TARGET_UHF = -151.0


def parse_opts():
    i = next((float(a[2:]) for a in sys.argv[1:] if a.startswith("i=")),
             C.I_LATCH * 1e3)
    b2 = next((float(a[3:]) for a in sys.argv[1:] if a.startswith("b2=")),
              C.B2)
    C.apply_knobs(i_latch=i * 1e-3, b2=b2)
    return [a for a in sys.argv[1:] if a in ("uhf", "vhf")] or ["uhf", "vhf"]


def nbias_standin():
    w = C.tail_w(C.I_LATCH)
    return (f"iref_nb (vdd nbias) isource dc={C.I_LATCH:.4e}\n"
            f"mdi_tb (nbias nbias 0 0) sg13_lv_nmos "
            f"w={w:g}u l={C.TAIL_L}\n"
            f"en_lodiv (en_lodiv 0) vsource dc=1.2\n"
            + C.lo_bias_netlist("vdd"))


def noisy(body):
    return re.sub(
        r"(\) resistor r=(\S+))(?=\s|$)",
        lambda m: m.group(1) + " noisy=1",
        body,
    )


def tie_spectrum(t, v, th, f0):
    s = v > th
    idx = np.where(~s[:-1] & s[1:])[0]
    if len(idx) < 8:
        return float("nan"), float("nan")
    te = t[idx] + (th - v[idx]) * (t[idx + 1] - t[idx]) / (v[idx + 1] - v[idx])
    p = 1.0 / f0
    n0 = np.round((te - te[0]) / p)
    err = te - te[0] - n0 * p
    if len(err) > 2:
        coef = np.polyfit(n0, err, 1)
        err = err - np.polyval(coef, n0)
    jit = float(np.std(err))
    L0 = 10 * math.log10(max(4 * math.pi ** 2 * f0 ** 2 * jit ** 2, 1e-30))
    return L0, jit


def write_run(name, mos, temp, hdr_extra, body, probe, f_out, vdd):
    path = os.path.join(OUT, name + ".sim")
    warm = round(30e-9 * max(f_out, 1e6)) / max(f_out, 1e6)
    open(path, "w").write(
        hdr_extra + body
        + "\ncontrol\n  abort always\n  options rawfile=\"binary\"\n"
        f"  options temp={temp}\n  options strictsave=1\n"
        f'  analysis warm tran stop={warm:.6e} step=5p maxstep=5p '
        f'icmode="uic" store="ss"\n'
        f"  save v({probe})\n"
        f'  analysis tr tran stop={TSTOP:.4e} step=5p maxstep=5p '
        f'ic="ss" icmode="uic" noisemode="zoh" noisefmax=5G '
        f'noisefmin=50k oversample=1\nendc\n'
    )
    log = os.path.join(OUT, name + ".log")
    import shutil
    from vacask.rawfile import rawread
    raw_mine = os.path.join(OUT, name + ".tr.raw")
    work = os.path.join(OUT, f"_w_{name}")
    if os.path.isdir(work):
        shutil.rmtree(work)
    os.makedirs(work)
    shutil.copy2(path, os.path.join(work, name + ".sim"))
    with open(log, "w") as fh:
        r = subprocess.run(["vacask", name + ".sim"], cwd=work,
                           stdout=fh, stderr=subprocess.STDOUT)
    if r.returncode:
        return dict(ok=False, method="tran-zoh FAILED",
                    err=open(log).read()[-300:], stage=name, f_out=f_out)
    raw_shared = os.path.join(work, "tr.raw")
    if not os.path.isfile(raw_shared):
        return dict(ok=False, method="tran-zoh no raw", stage=name, f_out=f_out)
    shutil.copy2(raw_shared, raw_mine)
    d = rawread(raw_mine).get()
    t, v = np.real(d["time"]), np.real(d[probe])
    L, jit = tie_spectrum(t, v, vdd / 2, f_out)
    if math.isnan(L):
        return dict(ok=False, method="tran-zoh no edges", stage=name, f_out=f_out)
    return dict(ok=True, method="tran-zoh", L=L, jit=jit, f_out=f_out, stage=name)


def stage_buffer(band, f_vco, corner):
    ctag, mos, vdd, temp = corner
    buf = C.L2.buffer()
    body = (f"vbufs (vbuf 0) vsource dc={vdd}\n"
            f"cckp (ckp 0) capacitor c={C_CK}\n"
            f"cckn (ckn 0) capacitor c={C_CK}\n"
            + noisy(buf))
    hdr = C.HEADER.format(title="buf", mos=mos, f=f_vco, amp=0.55,
                          vcm=vdd / 2, shape=0.0, offs=0.0, t0=-1, tr=1e-12)
    hdr += "xtank (tp tn) clk\n"
    return write_run(f"st_{band}_buffer", mos, temp, hdr, body, "ckp", f_vco, vdd)


def stage_cml(band, f_vco, corner):
    ctag, mos, vdd, temp = corner
    i_, rl, w = C.L1.cml_params(C.I_LATCH, vdd)
    body_cml, out = C.L1.div_body(2 if band == "uhf" else 3, i_, rl, w, vdd)
    body_cml = body_cml.replace("(vdd ", "(vdv ")
    body_cml = C.replace_tails(body_cml, C.I_LATCH)
    f_out = f_vco / (2 if band == "uhf" else 3)
    # VHF CML NOR vref already comes from L1.div_body — no second TB source.
    body = (f"vdvs (vdv 0) vsource dc={vdd}\nvdds (vdd 0) vsource dc={vdd}\n"
            + nbias_standin()
            + f"cckp (ckp 0) capacitor c={C_CK}\n"
            + f"cckn (ckn 0) capacitor c={C_CK}\n"
            + noisy(body_cml))
    hdr = C.HEADER.format(title="cml", mos=mos, f=f_vco, amp=0.55,
                          vcm=vdd - 0.55, shape=0.0, offs=0.0, t0=-1, tr=1e-12)
    hdr += "xck (ckp ckn) clk\n"
    return write_run(f"st_{band}_cml", mos, temp, hdr, body, out[0], f_out, vdd)


def stage_converter(band, f_vco, corner):
    ctag, mos, vdd, temp = corner
    f_ck = f_vco / (2 if band == "uhf" else 3)
    conv = C.L2.converter("dp", "dn", "x_clk")
    # step3 may have replaced converter with AC — use L3 path
    if hasattr(C.L3, "converter_ac") or True:
        conv = C.L2.converter("dp", "dn", "x_clk")
    body = (f"vcvs (vcv 0) vsource dc={vdd}\n"
            f"ccko (x_clk 0) capacitor c={C_CK}\n" + noisy(conv))
    hdr = C.HEADER.format(title="conv", mos=mos, f=f_ck, amp=0.25,
                          vcm=vdd - 0.25, shape=0.0, offs=0.0, t0=-1, tr=1e-12)
    hdr += "xck (dp dn) clk\n"
    return write_run(f"st_{band}_converter", mos, temp, hdr, body, "x_clk", f_ck, vdd)


def stage_logic(band, f_vco, corner):
    ctag, mos, vdd, temp = corner
    # Pull logic-only from full chain body by building chain without CML
    # Use L2.chain CMOS part: easier — full uhf_logic via chain with ideal CML stub
    f_ck = f_vco / (2 if band == "uhf" else 3)
    f_out = f_vco / (8 if band == "uhf" else 24)
    # Build only TSPC section from step2 helpers
    if band == "uhf":
        s = (C.L2.tspc("f1", "x_q2", "x_clk", "x_q1")
             + C.L2.inv("i1", "x_q1", "x_q1b")
             + C.L2.tspc("f2", "x_q1b", "x_clk", "x_q2")
             + C.L2.inv("i2", "x_q2", "x_q2b"))
        pulses = [("x_q1", "x_q2b"), ("x_q1", "x_q2"),
                  ("x_q1b", "x_q2"), ("x_q1b", "x_q2b")]
        for k, (a, b) in enumerate(pulses):
            s += (C.L2.nand2(f"g{k}", a, b, f"x_n{k}")
                  + C.L2.tspc(f"r{k}", f"x_n{k}", "x_clk", f"x_p{k}", pq=C.L2.PQ)
                  + f"cpl{k} (x_p{k} 0) capacitor c=20f\n")
        probe = "x_p0"
    else:
        s = C.L2.tspc("f1", "x_q4", "x_clk", "x_q1")
        for k in range(2, 5):
            s += (C.L2.inv(f"i{k}", f"x_q{k-1}", f"x_d{k}")
                  + C.L2.tspc(f"f{k}", f"x_d{k}", "x_clk", f"x_q{k}"))
        for k in range(1, 5):
            s += (C.L2.inv(f"o{k}", f"x_q{k}", f"x_q{k}b")
                  + C.L2.tspc(f"r{k}a", f"x_q{k}b", "x_clk", f"x_r{k}")
                  + C.L2.tspc(f"r{k}b", f"x_q{k}", "x_clk", f"x_r{k}b")
                  + f"cr{k} (x_r{k} 0) capacitor c=10f\n")
        probe = "x_r1"
    s = C.replace_holds(s)
    body = (f"vdgs (vdg 0) vsource dc={vdd}\n"
            f'vck (x_clk 0) vsource type="pulse" val0=0 val1={vdd} '
            f"delay=0 rise=20p fall=20p width={0.5/f_ck:.4e} "
            f"period={1/f_ck:.4e}\n"
            f"ccko (x_clk 0) capacitor c={C_CK}\n" + noisy(s))
    # No clk.va needed
    hdr = (f"stage logic {band}\ninclude \"sg13g2_vacask_common.lib\"\n"
           f'include "cornerMOSlv.lib" section={mos}\n'
           "load \"resistor.osdi\"\nload \"capacitor.osdi\"\n"
           "model resistor resistor\nmodel capacitor capacitor\n"
           "model vsource vsource\nmodel isource isource\n")
    return write_run(f"st_{band}_logic", mos, temp, hdr, body, probe, f_out, vdd)


def sum_to_lo(rows, f_lo):
    sig2, parts = 0.0, []
    for r in rows:
        if not r.get("ok"):
            continue
        s2 = 10 ** (r["L"] / 10) / (4 * math.pi ** 2 * r["f_out"] ** 2)
        L_lo = 10 * math.log10(max(4 * math.pi ** 2 * f_lo ** 2 * s2, 1e-30))
        parts.append((r["stage"].split("_")[-1], r["L"], L_lo, r["jit"]))
        sig2 += s2
    L_sum = 10 * math.log10(max(4 * math.pi ** 2 * f_lo ** 2 * sig2, 1e-30))
    return L_sum, parts


def main():
    os.makedirs(OUT, exist_ok=True)
    bands = parse_opts()
    lines = [
        "# P2.7.4a2 per-stage LO noise [SCH]\n\n",
        f"C_ck={C_CK*1e15:g} fF/side. I_latch={C.I_LATCH*1e3:g} mA, "
        f"B2={C.B2:g} µm. Method: ZOH transient noise.\n\n",
    ]
    print(lines[0], flush=True)
    all_results = {}
    for band in bands:
        f_vco = F_VCO_UHF if band == "uhf" else F_VCO_VHF
        f_lo = f_vco / (8 if band == "uhf" else 24)
        print(f"## {band.upper()}\n", flush=True)
        rows = []
        for fn in (stage_buffer, stage_cml, stage_converter, stage_logic):
            m = fn(band, f_vco, CORNER)
            st = fn.__name__.replace("stage_", "")
            m["stage"] = f"{band}_{st}"
            print(f"  {st}: ok={m.get('ok')} L={m.get('L', float('nan')):.1f} "
                  f"method={m.get('method')}", flush=True)
            if m.get("ok"):
                rows.append(m)
        L_sum, parts = sum_to_lo(rows, f_lo)
        table = [f"## {band.upper()}\n\n",
                 "| Stage | Method | f_out | jit fs | L@f_out | L→LO |\n"
                 "|---|---|---|---|---|---|\n"]
        for name, Lm, Llo, jit in parts:
            table.append(
                f"| {name} | tran-zoh | — | {jit*1e15:.0f} | {Lm:.1f} | {Llo:.1f} |\n"
            )
        for st in ("buffer", "cml", "converter", "logic"):
            if not any(p[0] == st for p in parts):
                table.append(f"| {st} | FAILED | — | — | — | — |\n")
        table.append(f"\n**Summed LO floor:** {L_sum:.1f} dBc/Hz [SCH]\n")
        if band == "uhf":
            table.append(
                f"Target ≤ {TARGET_UHF:.0f} → "
                f"{'PASS' if L_sum <= TARGET_UHF else 'FAIL'}\n\n")
        else:
            table.append("\n")
        lines.append("".join(table))
        all_results[band] = {"L_sum": L_sum, "parts": parts}
        print(f"Summed: {L_sum:.1f} dBc/Hz\n", flush=True)

    if "uhf" in all_results and all_results["uhf"]["parts"]:
        dom = max(all_results["uhf"]["parts"], key=lambda p: p[2])
        lines.append(f"## Dominant UHF stage\n\n**{dom[0]}** "
                     f"({dom[2]:.1f} dBc/Hz → LO)\n")
    open(os.path.join(OUT, "summary_stage_noise.txt"), "w").write("".join(lines))
    open(os.path.join(OUT, "stage_noise.json"), "w").write(
        json.dumps(all_results, indent=2))
    print("Wrote out/summary_stage_noise.txt", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
