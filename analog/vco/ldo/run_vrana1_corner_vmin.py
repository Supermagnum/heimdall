#!/usr/bin/env python3
"""P2.7.4a3 step 1 — VR_ANA1 pad V_min at mos corners with LO load [SCH].

Replaces the 1.08 V / 30 mV assumptions with:
  V_min_divider = V_pad(ss, 125 °C, I_VHF) − IR_route [HAND]
  V_max_divider = V_pad(ff, −40 °C, I_UHF) − IR_route_min [HAND]

Also: LO-enable step load (VCO+CP only → full LO) at ss / 125 °C.
"""
from __future__ import annotations

import math
import os
import subprocess
import sys

import numpy as np
from vacask.rawfile import rawread

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

# D21 set-point (typ pad 1.2 V @ I_typ) [HAND / prior SCH]
R_SER = 10.0
I_TYP = 9.65e-3
V_LDO_NOM = 1.2 + I_TYP * R_SER  # 1.2965
VREF = V_LDO_NOM / 2
VIN = 2.7

# Mode loads on VR_ANA1 pad (VCO + LO + CP) [HAND a2 / D21]
I_UHF = 8.44e-3   # UHF LO total after floor fix [HAND summary_floor_fix]
I_VHF = 10.69e-3  # VHF LO total after floor fix [HAND summary_floor_fix]
# Before en_lodiv: VCO (~3.59) + PLL (~1.5) ≈ 5.1 mA [HAND]
I_PRE = 5.1e-3

# Option A route pad → LO south of VCO [HAND from p27-floorplan / layout-notes]
# M2/M3 spine ≈ 350 µm × 4 µm, RSMET2 typ 88 mΩ/sq @25 °C → ×1.35 @125 °C
# Nsq = 350/4 = 87.5; R_metal_125 = 87.5 × 0.088 × 1.35 ≈ 10.4 mΩ
# Via array ~20× Via2 typ 9 Ω parallel ≈ 0.45 Ω (conservative single-stack)
# Use metal-dominated + via array: R_route ≈ 0.50 Ω @125 °C [HAND]
R_ROUTE_SS = 0.50   # Ω, pad star → LO CML taps [HAND]
R_ROUTE_FF = 0.35   # Ω, colder / min sheet [HAND]


def run(name, text):
    path = os.path.join(OUT, name + ".sim")
    open(path, "w").write(text)
    log = os.path.join(OUT, name + ".log")
    with open(log, "w") as fh:
        r = subprocess.run(
            ["vacask", name + ".sim"], cwd=OUT,
            stdout=fh, stderr=subprocess.STDOUT)
    if r.returncode:
        raise RuntimeError(name + "\n" + open(log).read()[-1200:])
    return log


def header(mos_sec, temp):
    return f"""parameters title="VR_ANA1 corner Vmin"
include "sg13g2_vacask_common.lib"
include "cornerMOSlv.lib" section={mos_sec}
include "cornerCAP.lib" section=cap_typ
include "cornerRES.lib" section=res_typ
load "resistor.osdi"
load "capacitor.osdi"
load "inductor.osdi"
model resistor resistor
model capacitor capacitor
model inductor inductor
model vsource vsource
model isource isource
"""


def sc(c):
    return math.sqrt(c * 1e15 / 1.5)


def body(il, vin=VIN):
    cout = 100e-12
    s = sc(cout)
    return f"""
vref (vref 0) vsource dc={VREF:.6g}
vin (vin 0) vsource dc={vin}
mp (vout vg vin vin) sg13_lv_pmos w=400u l=0.13u ng=80
rf1 (vout mid) resistor r=200k
rf2 (mid 0) resistor r=200k
ib (vin nb) isource dc=40u
mb (nb nb 0 0) sg13_lv_nmos w=4u l=2u ng=2
mt (t nb 0 0) sg13_lv_nmos w=8u l=2u ng=2
m1 (d1 mid t 0) sg13_lv_nmos w=16u l=2u ng=4
m2 (vg vref t 0) sg13_lv_nmos w=16u l=2u ng=4
m3 (d1 d1 vin vin) sg13_lv_pmos w=32u l=2u ng=4
m4 (vg d1 vin vin) sg13_lv_pmos w=32u l=2u ng=4
rz (vg ncg) resistor r=500
cg (ncg 0) capacitor c=100p
xout (vout 0 0) cap_rfcmim w={s:.3f}u l={s:.3f}u
rser (vout pad) resistor r={R_SER}
cpad (pad 0) capacitor c=2p
cesd (pad 0) capacitor c=1p
lbond (pad pin) inductor l=1.5n
resr (pin cbot) resistor r=0.05
cboard (cbot 0) capacitor c=100n
il (pad 0) isource dc={il}
"""


def op_pad(tag, mos, temp, il):
    text = header(mos, temp) + body(il) + f"""
control
  abort always
  options temp={temp} reltol=1e-4 rawfile="binary" strictsave=1
  save v(vout) v(pad) v(vg)
  analysis op1 op
endc
"""
    run(f"vmin_{tag}", text)
    op = rawread(os.path.join(OUT, "op1.raw")).get()
    vout = float(np.real(op["vout"]).ravel()[0])
    vpad = float(np.real(op["pad"]).ravel()[0])
    return vout, vpad


def step_lo_enable(mos, temp, i_pre, i_post):
    """Step pad load from pre-LO (VCO+CP) to full mode current."""
    b = body(i_pre)
    b = b.replace(
        f"il (pad 0) isource dc={i_pre}",
        f'il0 (pad 0) isource dc={i_pre}\n'
        f'il1 (pad 0) isource type="pulse" val0=0 val1={i_post - i_pre:.6g} '
        f"delay=5u rise=1n fall=1n width=30u period=80u",
    )
    text = header(mos, temp) + b + f"""
control
  abort always
  options temp={temp} reltol=1e-3 rawfile="binary" strictsave=1
  save v(vout) v(pad)
  analysis tr1 tran stop=40u step=2n
endc
"""
    run(f"step_lo_{mos}_{temp}", text)
    tr = rawread(os.path.join(OUT, "tr1.raw")).get()
    t = np.real(tr["time"]).ravel()
    vp = np.real(tr["pad"]).ravel()
    v0 = float(vp[(t > 3e-6) & (t < 4.5e-6)].mean())
    v1 = float(vp[(t > 25e-6) & (t < 30e-6)].mean())
    post = vp[t > 5.002e-6]
    dvpk = (float(post[:2000].min()) - v0) * 1e3
    return v0, v1, dvpk


def main():
    lines = [
        "# P2.7.4a3 — VR_ANA1 real supply minimum [SCH + HAND]",
        "",
        f"LDO sense target V_LDO={V_LDO_NOM:.4f} V (Vref={VREF:.4f}); R_ser={R_SER:.0f} Ω;",
        f"Vin={VIN} V. Loads: UHF={I_UHF*1e3:.2f} mA, VHF={I_VHF*1e3:.2f} mA,",
        f"pre-en_lodiv≈{I_PRE*1e3:.1f} mA [HAND a2/D21].",
        "",
        "## Operating-point pad voltage [SCH]",
        "",
        "| Corner | MOS | T (°C) | I_load | V_LDO | V_pad | ΔV_R |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    print("\n".join(lines[:8]), flush=True)
    rows = []
    cases = [
        ("tt_typ", "mos_tt", 27, I_TYP, "tt typ"),
        ("ss_vhf", "mos_ss", 125, I_VHF, "ss VHF"),
        ("ss_uhf", "mos_ss", 125, I_UHF, "ss UHF"),
        ("ff_uhf", "mos_ff", -40, I_UHF, "ff UHF"),
        ("ff_vhf", "mos_ff", -40, I_VHF, "ff VHF"),
        ("tt_vhf", "mos_tt", 27, I_VHF, "tt VHF"),
    ]
    for tag, mos, temp, il, lab in cases:
        try:
            vo, vp = op_pad(tag, mos, temp, il)
            dvr = (vo - vp) * 1e3
            rows.append((lab, mos, temp, il, vo, vp, dvr, None))
            line = (f"| {lab} | {mos} | {temp} | {il*1e3:.2f} mA | "
                    f"{vo:.4f} | {vp:.4f} | {dvr:.1f} mV |")
            print(line, flush=True)
            lines.append(line)
        except Exception as e:
            err = str(e).splitlines()[-1][:60]
            line = f"| {lab} | {mos} | {temp} | {il*1e3:.2f} mA | FAIL | | | {err} |"
            print(line, flush=True)
            lines.append(line)
            rows.append((lab, mos, temp, il, None, None, None, err))

    # Pick V_pad ss / ff
    def find(lab):
        for r in rows:
            if r[0] == lab and r[5] is not None:
                return r[5]
        return None

    v_ss = find("ss VHF")
    v_ff = find("ff UHF")  # light load → higher pad = max
    v_ff_alt = find("ff VHF")
    v_tt = find("tt typ")

    lines += [
        "",
        "## Supply-route IR [HAND]",
        "",
        "Option A (p27-floorplan): pad star → LO south of VCO ≈ 350 µm M2/M3",
        "at w ≥ 4 µm. RSMET2 typ 88 mΩ/sq [DS] ×1.35 @125 °C → metal ≈ 10 mΩ;",
        "via array ≈ 0.45 Ω → **R_route_ss ≈ 0.50 Ω**, R_route_ff ≈ 0.35 Ω [HAND].",
        f"IR_ss @ I_VHF = {R_ROUTE_SS * I_VHF * 1e3:.2f} mV; "
        f"IR_ff @ I_UHF = {R_ROUTE_FF * I_UHF * 1e3:.2f} mV.",
        "",
        "## V_min / V_max at the divider [SCH − HAND]",
        "",
    ]
    if v_ss is not None:
        ir = R_ROUTE_SS * I_VHF
        vmin = v_ss - ir
        lines.append(
            f"- **V_min (ss / 125 °C, VHF load)** = V_pad {v_ss:.4f} − "
            f"IR {ir*1e3:.2f} mV = **{vmin:.4f} V**"
        )
        print(f"V_min = {vmin:.4f} V (pad {v_ss:.4f} − IR {ir*1e3:.2f} mV)",
              flush=True)
    else:
        vmin = None
        lines.append("- **V_min: SCH FAIL** — see table")
        print("V_min FAIL", flush=True)

    if v_ff is not None:
        irf = R_ROUTE_FF * I_UHF
        vmax = v_ff - irf
        lines.append(
            f"- **V_max (ff / −40 °C, UHF load)** = V_pad {v_ff:.4f} − "
            f"IR {irf*1e3:.2f} mV = **{vmax:.4f} V**"
        )
        if v_ff_alt is not None:
            lines.append(
                f"  (ff VHF pad {v_ff_alt:.4f} V for reference)"
            )
    else:
        vmax = None
        lines.append("- **V_max: SCH FAIL**")

    if v_tt is not None:
        lines.append(f"- tt typ pad (check) = {v_tt:.4f} V [SCH]")

    lines += [
        "",
        "## LO-enable step load at ss / 125 °C [SCH]",
        "",
        f"Pulse I_pad {I_PRE*1e3:.1f} → {I_VHF*1e3:.2f} mA (≈ en_lodiv).",
        "",
        "| Mode | V_pad pre | V_pad post | ΔVpk (mV) |",
        "|---|---:|---:|---:|",
    ]
    print("step load...", flush=True)
    try:
        v0, v1, dvpk = step_lo_enable("mos_ss", 125, I_PRE, I_VHF)
        line = f"| VHF en_lodiv | {v0:.4f} | {v1:.4f} | {dvpk:.1f} |"
        print(line, flush=True)
        lines.append(line)
        try:
            v0u, v1u, dvu = step_lo_enable("mos_ss", 125, I_PRE, I_UHF)
            line = f"| UHF en_lodiv | {v0u:.4f} | {v1u:.4f} | {dvu:.1f} |"
            print(line, flush=True)
            lines.append(line)
        except Exception as e:
            lines.append(f"| UHF en_lodiv | FAIL | | {str(e)[:40]} |")
    except Exception as e:
        lines.append(f"| VHF en_lodiv | FAIL | | {str(e)[:50]} |")
        print("step FAIL", e, flush=True)

    lines += [
        "",
        "## Replacement of prior assumptions",
        "",
        "Prior LO checks used VDD=1.08 V and a 30 mV margin to 1.05 V [HAND].",
        "Those are **replaced** by V_min above for subsequent a3 buffer / ÷3 work.",
        "",
    ]
    if vmin is not None:
        lines.append(
            f"**Use VDD = {vmin:.3f} V** (rounded) for ss / 125 °C divider TBs."
        )
    if vmax is not None:
        lines.append(
            f"**Use VDD = {vmax:.3f} V** (rounded) for ff / −40 °C max checks."
        )

    path = os.path.join(OUT, "summary_vrana1_corner_vmin.txt")
    open(path, "w").write("\n".join(lines) + "\n")
    print("WROTE", path, flush=True)
    if vmin is None:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
