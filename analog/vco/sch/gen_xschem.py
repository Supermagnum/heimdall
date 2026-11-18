#!/usr/bin/env python3
"""P2.7.1: generate hierarchical xschem capture of VCO + D22 amp-cal + D21 LDO.

Device sizes/trims come from analog/vco/step2/out/range.json and the simulated
decks (run_step2 / amp_common / ldo_body). Also writes a VACASK-format device
netlist (netlists/*.vacask) from the same inventory for equivalence + re-sim.
"""
from __future__ import annotations

import json
import math
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "analog", "vco", "ampcal"))
sys.path.insert(0, os.path.join(REPO, "analog", "vco", "step2"))

from xsch_lib import Sch, write_sym, side_um  # noqa: E402
import run_step2 as S2  # noqa: E402

RANGE_JSON = os.path.join(REPO, "analog", "vco", "step2", "out", "range.json")
L2N0_INC = os.path.join(REPO, "analog", "vco", "models", "l2n0_lumped.inc")
CAP_AREA = 1.5
R_BIAS = 2e6
SW_PER_FF = 100 / 60


def load_range():
    r = json.load(open(RANGE_JSON))
    return r


def _net(n):
    return "0" if n in ("gnd", "GND", "0") else n


def vacask_line(d):
    """One VACASK instance from a DeviceRec."""
    n = " ".join(_net(x) for x in d.nodes)
    if d.kind in ("nmos", "pmos"):
        return (f"{d.name} ({n}) {d.params['model']} "
                f"w={d.params['w']} l={d.params['l']} ng={d.params['ng']}\n")
    if d.kind == "mim":
        return (f"{d.name} ({n}) cap_rfcmim "
                f"w={d.params['w']} l={d.params['l']}\n")
    if d.kind == "cmim":
        # 2-terminal [PDK vacask cap_cmim]
        return (f"{d.name} ({n}) cap_cmim "
                f"w={d.params['w']} l={d.params['l']}\n")
    if d.kind == "svaricap":
        return (f"{d.name} ({n}) {d.params['model']} "
                f"w={d.params['w']} l={d.params['l']} nx={d.params['nx']}\n")
    if d.kind == "res":
        return f"{d.name} ({n}) resistor r={d.params['r']}\n"
    if d.kind == "rhigh":
        return (f"{d.name} ({n}) rhigh "
                f"w={d.params['w']} l={d.params['l']} b={d.params['b']}\n")
    if d.kind == "capa":
        return f"{d.name} ({n}) capacitor c={d.params['c']}\n"
    if d.kind == "ind":
        return f"{d.name} ({n}) inductor l={d.params['l']}\n"
    if d.kind == "vsrc":
        return f"{d.name} ({n}) vsource dc={d.params['dc']}\n"
    if d.kind == "isrc":
        return f"{d.name} ({n}) isource dc={d.params['dc']}\n"
    raise ValueError(d.kind)


def write_vacask(path, title, devices, extra_header=""):
    hdr = f"""{title}
include "sg13g2_vacask_common.lib"
include "cornerMOSlv.lib" section=mos_tt
include "cornerMOShv.lib" section=mos_tt
include "cornerCAP.lib" section=cap_typ
load "resistor.osdi"
load "capacitor.osdi"
load "inductor.osdi"
model resistor resistor
model capacitor capacitor
model inductor inductor
model vsource vsource
model isource isource
{extra_header}
"""
    body = "".join(vacask_line(d) for d in devices)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(hdr + body)
    return path


def gen_l2n0():
    """Tapped L2n0 lumped EM model as hierarchical sch (values from l2n0_lumped.inc)."""
    sch = Sch("l2n0", os.path.join(HERE, "l2n0.sch"))
    for p in ("p", "n", "ct"):
        sch.iopin(p)
    sch.title("l2n0_EM_lumped")
    # From analog/vco/models/l2n0_lumped.inc [EM]
    sch.res("r1p", "p", "p1", 0.814837)
    sch.ind("l1p", "p1", "p2", 8.05663e-10)
    sch.res("r2p", "p2", "ct", 0.827877)
    sch.ind("l2p", "p2", "ct", 3.196e-11)
    sch.res("r1n", "n", "n1", 0.814837)
    sch.ind("l1n", "n1", "n2", 8.05663e-10)
    sch.res("r2n", "n2", "ct", 0.827877)
    sch.ind("l2n", "n2", "ct", 3.196e-11)
    sch.capa("cp", "p", "n", 2.98589e-14)
    sch.write()
    write_sym(os.path.join(HERE, "l2n0.sym"), "l2n0", ["p", "n", "ct"])
    write_vacask(os.path.join(HERE, "netlists", "l2n0.vacask"),
                 "P2.7.1 l2n0 lumped", sch.devices,
                 extra_header="// subckt body only — wrap for top\n")
    return sch


# Layout LVS snaps for D24 bank (p272b_bank leaf spice) [GDS/TOOL]
BANK_CMIM_SIDE = {0: "2.81u", 1: "3.92u", 2: "5.53u"}
# ms switch total W (extract-rounded); ng from leaf build [GDS]
BANK_MS_W = {
    0: ("10.32u", 4), 1: ("19.8u", 8), 2: ("39.12u", 16), 3: ("77.5u", 31),
    4: ("154.38u", 62), 5: ("308.5u", 100), 6: ("308.5u", 100),
    7: ("308.5u", 100), 8: ("308.5u", 100), 9: ("308.5u", 100),
    10: ("308.5u", 100), 11: ("308.5u", 100),
}
# bypass NMOS W/L/ng — leaf snaps (not raw bank_bypass_geom floats) [GDS]
BANK_BYP = {
    0: ("0.15u", "0.13u", 1), 1: ("0.15u", "0.13u", 1),
    2: ("0.15u", "0.13u", 1), 3: ("0.31u", "0.13u", 1),
    4: ("0.62u", "0.13u", 1), 5: ("1.25u", "0.13u", 1),
    6: ("1.25u", "0.13u", 1), 7: ("1.25u", "0.13u", 1),
    8: ("1.25u", "0.13u", 1), 9: ("1.25u", "0.13u", 1),
    10: ("1.25u", "0.13u", 1), 11: ("1.25u", "0.13u", 1),
}
BANK_RHIGH_W, BANK_RHIGH_L = "5.0u", "60.8u"
CORE_RHIGH_W, CORE_RHIGH_L = "2u", "15.2u"
# Top extract shows 9u gnd-tied fill; leaf core spice had 8u — use extract [GDS]
CORE_MDUM_W = "9u"
VAR_RHIGH_W, VAR_RHIGH_L, VAR_RHIGH_B = "0.5u", "42.095u", 16
D9_RHIGH_W, D9_RHIGH_L, D9_RHIGH_B = "0.5u", "21.285u", 16
CBF_SIDE, CBF_M = "68.94u", 7

# dac_array unit list — identical order/gates to p272b_tail/out/tail_block.spice [GDS]
DAC_ARRAY_UNITS = [
    *[(f"b{i}", "code_gnd") for i in range(19)],
    ("b4_0", "code4"), ("b3_0", "code3"), ("b2_0", "code2"),
    ("b4_1", "code4"), ("b3_1", "code3"), ("b4_2", "code4"),
    ("b1_0", "code1"), ("b4_3", "code4"), ("b4_4", "code4"),
    ("b0_0", "code0"), ("b4_5", "code4"), ("b3_2", "code3"),
    ("b4_6", "code4"), ("b2_1", "code2"), ("b3_3", "code3"),
    ("b4_7", "code4"), ("b4_8", "code4"), ("b3_4", "code3"),
    ("b2_2", "code2"), ("b4_9", "code4"), ("b3_5", "code3"),
    ("b4_10", "code4"), ("b1_1", "code1"), ("b4_11", "code4"),
    ("b4_12", "code4"), ("dmy", "code_vdd"), ("b3_6", "code3"),
    ("b4_13", "code4"), ("b4_14", "code4"), ("b2_3", "code2"),
    ("b3_7", "code3"), ("b4_15", "code4"),
]


def gen_vco_core(rng):
    sch = Sch("vco_core", os.path.join(HERE, "vco_core.sch"))
    for p in ("tp", "tn", "tail", "ct", "vdd", "gnd"):
        sch.iopin(p)
    sch.title("vco_core_XC")
    # Cross-coupled pair (run_step2); mdum matches layout GR fill [GDS]
    sch.nmos("m1", "tp", "tn", "tail", "gnd", "32u", "0.13u", 8)
    sch.nmos("m2", "tn", "tp", "tail", "gnd", "32u", "0.13u", 8)
    sch.nmos("mdum", "gnd", "gnd", "gnd", "gnd", CORE_MDUM_W, "0.13u", 1)
    cfix = float(rng["cfix"])
    if cfix > 0:
        s = side_um(2 * cfix)
        sch.mim("xf1", "tp", "fx", "gnd", f"{s:.3f}u", f"{s:.3f}u")
        sch.mim("xf2", "tn", "fx", "gnd", f"{s:.3f}u", f"{s:.3f}u")
        sch.rhigh("rfx", "fx", "gnd", "gnd", w=CORE_RHIGH_W, l=CORE_RHIGH_L)
    sch.write()
    write_sym(os.path.join(HERE, "vco_core.sym"), "vco_core",
              ["tp", "tn", "tail", "ct", "vdd", "gnd"])
    return sch


def gen_vco_tail_dac():
    """Layout-accurate tail for LVS (p272b_tail leaf). Sim ideals live in vco_sim_flat."""
    sch = Sch("vco_tail_dac", os.path.join(HERE, "vco_tail_dac.sch"))
    for p in ("tail", "vdd", "gnd", "vbp_tail", "nb", "nbf",
              "code0", "code1", "code2", "code3", "code4"):
        sch.iopin(p)
    sch.title("vco_tail_dac_LVS")
    # dac_array as unit cells (2u/2u + 2u/0.13) — not binary-weighted [GDS]
    for iname, code in DAC_ARRAY_UNITS:
        xd = f"xd_{iname}"
        sch.pmos(f"mdb_{iname}", xd, "pbias", "vdd", "vdd", "2u", "2u", 1)
        sch.pmos(f"msw_{iname}", "xraw", code, xd, "vdd", "2u", "0.13u", 1)
    # tail_mt: leaf is 4×120/4 ng=24; top extract combines to one 480u —
    # keep 4 tiles (combine_devices) to match leaf GDS [GDS/TOOL]
    for i in range(4):
        sch.nmos(f"mt{i}", "tail", "nbf", "gnd", "gnd", "120u", "4u", 24)
    # ota_vds: xraw≡xref; out=nb [GDS leaf]
    # Top extract drops fully gnd-tied 4u/2u dummies (leaf had MdL/MdR); keep
    # one 8u/2u fill that top extract shows [GDS/TOOL]
    sch.nmos("mo1", "d1", "xraw", "ss", "gnd", "8u", "2u", 2)
    sch.nmos("mo2", "nb", "tail_f", "ss", "gnd", "8u", "2u", 2)
    sch.pmos("mp1", "d1", "d1", "vdd", "vdd", "4u", "2u", 2)
    sch.pmos("mp2", "nb", "d1", "vdd", "vdd", "4u", "2u", 2)
    sch.nmos("mdum_ota", "gnd", "gnd", "gnd", "gnd", "8u", "2u", 1)
    # d9_rc [GDS]
    sch.rhigh("rbf", "nb", "nbf", "gnd", w=D9_RHIGH_W, l=D9_RHIGH_L,
              bends=D9_RHIGH_B)
    sch.nmos("mbp_rbf", "nb", "vbp_tail", "nbf", "gnd", "20u", "0.13u", 4)
    # cbf: 7 parallel cmim (layout m=7) [GDS]
    for i in range(CBF_M):
        sch.mim(f"cbf{i}", "nbf", "gnd", "gnd", CBF_SIDE, CBF_SIDE, kind="cmim")
    sch.write()
    write_sym(os.path.join(HERE, "vco_tail_dac.sym"), "vco_tail_dac",
              ["tail", "vdd", "gnd", "vbp_tail", "nb", "nbf",
               "code0", "code1", "code2", "code3", "code4"])
    return sch


def gen_vco_bank(rng):
    """D24 segmented bank: 5 binary + 7 thermometer unit cells (or legacy binary)."""
    S2.apply_range_trims(rng)
    ncell = S2.n_bank_cells()
    sch = Sch("vco_bank", os.path.join(HERE, "vco_bank.sch"))
    ports = ["tp", "tn", "vbp", "gnd"]
    for k in range(ncell):
        ports += [f"g{k}", f"bb{k}"]
    for p in ports:
        sch.iopin(p)
    title = ("vco_bank_D24_seg" if S2.BANK_ARCH == "d24"
             else "vco_bank_8bit_trim")
    sch.title(title)
    lsb = float(rng["lsb"])
    for k in range(ncell):
        wt = S2.cell_weight(k)
        tr = S2.cell_trim(k)
        c_mim = 2 * lsb * wt * tr
        s = side_um(c_mim)
        # D24: b0..b2 cmim (layout); b3+ rfcmim [GDS / summary_rc_bank]
        kind = "cmim" if (S2.BANK_ARCH == "d24" and k < 3) else "rfcmim"
        side = BANK_CMIM_SIDE.get(k, f"{s:.3f}u") if kind == "cmim" else f"{s:.3f}u"
        sch.mim(f"xb{k}p", "tp", f"a{k}", "gnd", side, side, kind=kind)
        sch.mim(f"xb{k}n", "tn", f"b{k}", "gnd", side, side, kind=kind)
        mw, mng = BANK_MS_W.get(k, (f"{SW_PER_FF * lsb * wt * tr:.2f}u",
                                    min(100, max(1, int(round(
                                        SW_PER_FF * lsb * wt * tr / 2.5))))))
        sch.nmos(f"ms{k}", f"a{k}", f"g{k}", f"b{k}", "gnd", mw, "0.13u", mng)
        sch.rhigh(f"rba{k}", f"a{k}", f"bb{k}", "gnd",
                  w=BANK_RHIGH_W, l=BANK_RHIGH_L)
        sch.rhigh(f"rbb{k}", f"b{k}", f"bb{k}", "gnd",
                  w=BANK_RHIGH_W, l=BANK_RHIGH_L)
        bw, bl, bng = BANK_BYP.get(k, ("0.15u", "0.13u", 1))
        sch.nmos(f"mbp_rba{k}", f"a{k}", "vbp", f"bb{k}", "gnd", bw, bl, bng)
        sch.nmos(f"mbp_rbb{k}", f"b{k}", "vbp", f"bb{k}", "gnd", bw, bl, bng)
    # Centroid dummy (slot D): one thermo-sized unit, all terminals to gnd
    if S2.BANK_ARCH == "d24":
        s = side_um(2 * lsb * S2.cell_weight(5) * S2.cell_trim(5))
        mw, mng = BANK_MS_W[5]
        bw, bl, bng = BANK_BYP[5]
        sch.mim("xbdump", "gnd", "adum", "gnd", f"{s:.3f}u", f"{s:.3f}u")
        sch.mim("xbdumn", "gnd", "bdum", "gnd", f"{s:.3f}u", f"{s:.3f}u")
        sch.nmos("msdum", "adum", "gnd", "bdum", "gnd", mw, "0.13u", mng)
        sch.rhigh("rbadum", "adum", "gnd", "gnd",
                  w=BANK_RHIGH_W, l=BANK_RHIGH_L)
        sch.rhigh("rbbdum", "bdum", "gnd", "gnd",
                  w=BANK_RHIGH_W, l=BANK_RHIGH_L)
        sch.nmos("mbp_rbadum", "adum", "gnd", "gnd", "gnd", bw, bl, bng)
        sch.nmos("mbp_rbbdum", "bdum", "gnd", "gnd", "gnd", bw, bl, bng)
    sch.write()
    write_sym(os.path.join(HERE, "vco_bank.sym"), "vco_bank", ports)
    return sch


def gen_vco_var(rng):
    sch = Sch("vco_var", os.path.join(HERE, "vco_var.sch"))
    for p in ("tp", "tn", "vt", "vbp", "gnd"):
        sch.iopin(p)
    sch.title("vco_var_AC_D11")
    nfing = int(rng.get("nfing", 20))
    sc = side_um(5 * nfing * 6.8)
    sch.mim("xcp", "tp", "vgp", "gnd", f"{sc:.3f}u", f"{sc:.3f}u")
    sch.mim("xcn", "tn", "vgn", "gnd", f"{sc:.3f}u", f"{sc:.3f}u")
    # Bias to well: layout rhigh + shared vvb net (no ideal vsrc in LVS sch) [GDS]
    sch.rhigh("rvp", "vgp", "vvb", "gnd", w=VAR_RHIGH_W, l=VAR_RHIGH_L,
              bends=VAR_RHIGH_B)
    sch.rhigh("rvn", "vgn", "vvb", "gnd", w=VAR_RHIGH_W, l=VAR_RHIGH_L,
              bends=VAR_RHIGH_B)
    nx1 = nfing - nfing // 2
    nx2 = nfing // 2
    sch.svaricap_fx("xv1", "vgp", "vt", "vgn", "gnd", nx=nx1)
    sch.svaricap_fx("xv2", "vgp", "vt", "vgn", "gnd", nx=nx2)
    sch.nmos("mbp_rvp", "vgp", "vbp", "vvb", "gnd", "5u", "0.13u", 2)
    sch.nmos("mbp_rvn", "vgn", "vbp", "vvb", "gnd", "5u", "0.13u", 2)
    sch.write()
    write_sym(os.path.join(HERE, "vco_var.sym"), "vco_var",
              ["tp", "tn", "vt", "vbp", "gnd"])
    return sch


def gen_ampcal_det():
    """D22 detector + SE cmp — fab devices matching layout [GDS p272b_det].

    No ideal I/C/V inside the cell: MOS sinks + en, cmim hold/cl_cmp, rhigh
    loads, pin vthn (V_LOSS bias from TB). Ports include en and vthn.
    """
    import amp_common as A
    sch = Sch("ampcal_det", os.path.join(HERE, "ampcal_det.sch"))
    ports = ("tp", "tn", "ct", "vdd", "gnd", "cmp", "hold", "rep", "en", "vthn")
    for p in ports:
        sch.iopin(p)
    sch.title("ampcal_det_cmp_D22_fab")
    # SF pair [GDS det_sf_pair]. Top extract drops fully gnd-tied 0.5u
    # dummies (leaf MdL/MdR); mrtp||mrtn combine to W=1u [GDS/TOOL]
    sch.nmos("mdtp", "vdd", "tp", "hold", "gnd", A.W_DET, A.L_DET, 1)
    sch.nmos("mdtn", "vdd", "tn", "hold", "gnd", A.W_DET, A.L_DET, 1)
    sch.nmos("mrtp", "vdd", "ct", "rep", "gnd", A.W_DET, A.L_DET, 1)
    sch.nmos("mrtn", "vdd", "ct", "rep", "gnd", A.W_DET, A.L_DET, 1)
    # Hold caps: cmim w=l=16.27 µm → 400 fF [GDS extract / PDK]
    sch.mim("chold", "hold", "gnd", "gnd", "16.27u", "16.27u", kind="cmim")
    sch.mim("crep", "rep", "gnd", "gnd", "16.27u", "16.27u", kind="cmim")
    # Bias + PD: shared nbias mirror; retuned I_hold≈4 µA / I_tt≈20 µA [SCH]
    sch.rhigh("rbias", "vdd", "nbias", "gnd", w="0.5u", l=A.RHIGH_BIAS_L, bends=0)
    sch.nmos("mdiode", "nbias", "nbias", "pd_d", "gnd",
             A.W_SINK_DET, A.L_SINK, A.NG_SINK_DET)
    sch.nmos("men_d", "pd_d", "en", "gnd", "gnd", "2.0u", "0.13u", 1)
    sch.nmos("mid_h", "hold", "nbias", "pd_h", "gnd",
             A.W_SINK_DET, A.L_SINK, A.NG_SINK_DET)
    sch.nmos("men_h", "pd_h", "en", "gnd", "gnd", "2.0u", "0.13u", 1)
    sch.nmos("mid_r", "rep", "nbias", "pd_r", "gnd",
             A.W_SINK_DET, A.L_SINK, A.NG_SINK_DET)
    sch.nmos("men_r", "pd_r", "en", "gnd", "gnd", "2.0u", "0.13u", 1)
    sch.nmos("mid_tt", "ttail", "nbias", "pd_tt", "gnd",
             A.W_SINK_CMP, A.L_SINK, A.NG_SINK_CMP)
    sch.nmos("men_tt", "pd_tt", "en", "gnd", "gnd", "2.0u", "0.13u", 1)
    sch.nmos("mid_ss", "ss2", "nbias", "pd_ss", "gnd",
             A.W_SINK_CMP, A.L_SINK, A.NG_SINK_CMP)
    sch.nmos("men_ss", "pd_ss", "en", "gnd", "gnd", "2.0u", "0.13u", 1)
    # SE comparator [GDS cmp_se]; rhigh l=6.96 µm [extract]
    sch.nmos("mc1", "co", "hold", "ttail", "gnd", "4u", "0.5u", 2)
    sch.nmos("mc2", "co2", "vthn", "ttail", "gnd", "4u", "0.5u", 2)
    sch.rhigh("rc1", "vdd", "co", "gnd", w="0.5u", l="6.96u", bends=0)
    sch.rhigh("rc2", "vdd", "co2", "gnd", w="0.5u", l="6.96u", bends=0)
    sch.nmos("mcs1", "n1", "co2", "ss2", "gnd", "4u", "0.5u", 2)
    sch.nmos("mcs2", "cmp", "co", "ss2", "gnd", "4u", "0.5u", 2)
    sch.pmos("mpl1", "n1", "n1", "vdd", "vdd", "4u", "0.5u", 2)
    sch.pmos("mpl2", "cmp", "n1", "vdd", "vdd", "4u", "0.5u", 2)
    # cmp_se fill: top extract shows one 4u/0.5 gnd MOS (not 2×2u leaf) [GDS]
    sch.nmos("mdLc", "gnd", "gnd", "gnd", "gnd", "4.0u", "0.5u", 1)
    # cl_cmp — leaf extract snap 5.71 µm [GDS]
    sch.mim("cl_cmp", "cmp", "gnd", "gnd", "5.71u", "5.71u", kind="cmim")
    sch.write()
    write_sym(os.path.join(HERE, "ampcal_det.sym"), "ampcal_det", list(ports))
    return sch


def gen_ldo():
    """D21 VR_ANA1 LDO core (ldo_body): sense at vout, Rz+Cg compensation."""
    sch = Sch("vrana1_ldo", os.path.join(HERE, "vrana1_ldo.sch"))
    for p in ("vin", "vout", "vref", "gnd"):
        sch.iopin(p)
    sch.title("vrana1_ldo_D21")
    sch.pmos("mp", "vout", "vg", "vin", "vin", "400u", "0.13u", 80)
    sch.res("rf1", "vout", "mid", 200e3)
    sch.res("rf2", "mid", "gnd", 200e3)
    sch.isrc("ib", "vin", "nb", 40e-6)
    sch.nmos("mb", "nb", "nb", "gnd", "gnd", "4u", "2u", 2)
    sch.nmos("mt", "t", "nb", "gnd", "gnd", "8u", "2u", 2)
    sch.nmos("m1", "d1", "mid", "t", "gnd", "16u", "2u", 4)
    sch.nmos("m2", "vg", "vref", "t", "gnd", "16u", "2u", 4)
    sch.pmos("m3", "d1", "d1", "vin", "vin", "32u", "2u", 4)
    sch.pmos("m4", "vg", "d1", "vin", "vin", "32u", "2u", 4)
    sch.res("rz", "vg", "ncg", 500)
    sch.capa("cg", "ncg", "gnd", 100e-12)
    # Cout ~100 fF MIM (side from ldo_body)
    sc = math.sqrt(100e-12 * 1e15 / 1.5)  # c_ff / CAP_AREA
    sch.mim("xout", "vout", "gnd", "gnd", f"{sc:.3f}u", f"{sc:.3f}u")
    sch.write()
    write_sym(os.path.join(HERE, "vrana1_ldo.sym"), "vrana1_ldo",
              ["vin", "vout", "vref", "gnd"])
    return sch


def gen_vco_top(rng, blocks):
    """Hierarchical VCO top: leaf symbols wired by net name (P2.7.2a).

    Instantiates l2n0, vco_core, vco_bank (D24), vco_var, vco_tail_dac,
    ampcal_det. Fixed MIM lives in vco_core; bypasses in bank/var/tail.
    Digital: bank gates g0..g11 and DAC code0..code4 are top ports.
    """
    S2.apply_range_trims(rng)
    ncell = S2.n_bank_cells()
    top_ports = [
        "tp", "tn", "ct", "vt", "vdd", "gnd", "vbp", "vbp_tail",
        "cmp", "tail", "hold", "rep", "en", "vthn",
    ]
    top_ports += [f"g{k}" for k in range(ncell)]
    top_ports += [f"code{b}" for b in range(5)]

    sch = Sch("vco_top", os.path.join(HERE, "vco_top.sch"))
    for p in top_ports:
        sch.iopin(p)
    sch.title("vco_top_P272a_hier")

    # Tall bank symbol (~28 pins × 8) — keep instances from overlapping [TOOL]
    y_top, y_bot, dx = 0, 280, 220

    # Inductor (tank L)
    sch.subckt_inst("l2n0.sym", "xl",
                    {"p": "tp", "n": "tn", "ct": "ct"}, x=0, y=y_top)

    # Core + fixed cap
    sch.subckt_inst(
        "vco_core.sym", "xcore",
        {"tp": "tp", "tn": "tn", "tail": "tail", "ct": "ct",
         "vdd": "vdd", "gnd": "gnd"},
        x=dx, y=y_top)

    # D24 bank
    bank_nets = {"tp": "tp", "tn": "tn", "vbp": "vbp", "gnd": "gnd"}
    for k in range(ncell):
        bank_nets[f"g{k}"] = f"g{k}"
        bank_nets[f"bb{k}"] = f"bb{k}"
    sch.subckt_inst("vco_bank.sym", "xbank", bank_nets, x=2 * dx, y=y_top)

    # Varactor + bias / bypass
    sch.subckt_inst(
        "vco_var.sym", "xvar",
        {"tp": "tp", "tn": "tn", "vt": "vt", "vbp": "vbp", "gnd": "gnd"},
        x=3 * dx, y=y_top)

    # Tail DAC / OTA / RC / bypass
    sch.subckt_inst(
        "vco_tail_dac.sym", "xtail",
        {"tail": "tail", "vdd": "vdd", "gnd": "gnd", "vbp_tail": "vbp_tail",
         "nb": "nb", "nbf": "nbf",
         "code0": "code0", "code1": "code1", "code2": "code2",
         "code3": "code3", "code4": "code4"},
        x=dx, y=y_bot)

    # D22 detector + SE comparator (fab: en, vthn)
    sch.subckt_inst(
        "ampcal_det.sym", "xdet",
        {"tp": "tp", "tn": "tn", "ct": "ct", "vdd": "vdd", "gnd": "gnd",
         "cmp": "cmp", "hold": "hold", "rep": "rep",
         "en": "en", "vthn": "vthn"},
        x=2 * dx, y=y_bot)

    sch.write()
    write_sym(os.path.join(HERE, "vco_top.sym"), "vco_top", top_ports)
    return sch


def build_flat_inventory(rng):
    """One flat device list matching the simulated VCO+D22+LDO decks."""
    # Rebuild by calling each gen_* and concatenating .devices — but gens write
    # files. Call them and collect.
    blocks = {}
    blocks["l2n0"] = gen_l2n0()
    blocks["vco_core"] = gen_vco_core(rng)
    blocks["vco_tail_dac"] = gen_vco_tail_dac()
    blocks["vco_bank"] = gen_vco_bank(rng)
    blocks["vco_var"] = gen_vco_var(rng)
    blocks["ampcal_det"] = gen_ampcal_det()
    blocks["vrana1_ldo"] = gen_ldo()
    gen_vco_top(rng, blocks)

    # Flat sim from hierarchical sch blocks (design = vco_top.sch) [decisions]
    # Remaining ideals: listed in out/summary_vco_sim_ideals.txt
    sim = Sch("vco_sim_flat", os.path.join(HERE, "vco_sim_flat.sch"))
    for p in ("tp", "tn", "ct", "vt", "vdd", "gnd", "vbp", "vbp_tail"):
        sim.iopin(p)
    sim.title("vco_sim_flat_from_sch")
    for d in blocks["l2n0"].devices:
        _emit(sim, d)
    for d in blocks["vco_core"].devices:
        _emit(sim, d)
    for d in blocks["vco_bank"].devices:
        _emit(sim, d)
    for d in blocks["vco_var"].devices:
        _emit(sim, d)
    # Var well bias: no pin in sch; TB needs DC (tool/TB, not a fab device) [SCH]
    sim.vsrc("vvb_bias", "vvb", "gnd", 0.3)
    # Full layout-accurate tail from sch (dac_array units + mt + ota + d9 + cbf)
    for d in blocks["vco_tail_dac"].devices:
        _emit(sim, d)
    # Standalone bias into pbias: layout expects external I; no on-sch source [SCH]
    # Keep ideal iref into pbias so PSS/range TB converge without a DAC master.
    sim.isrc("iref_pbias", "vdd", "pbias", 1.05e-5)
    # Stand-in CML buffer (not in vco_top.sch; LO load for range/PN TB) [SCH]
    sim.nmos("mb1", "op", "tp", "tb", "gnd", "10u", "0.13u", 4)
    sim.nmos("mb2", "on", "tn", "tb", "gnd", "10u", "0.13u", 4)
    sim.res("rl1", "vdd", "op", 400)
    sim.res("rl2", "vdd", "on", 400)
    sim.isrc("ib", "tb", "gnd", 1e-3)
    sim.capa("ctb", "tb", "gnd", 2e-12)
    sim.capa("cl1", "op", "gnd", 20e-15)
    sim.capa("cl2", "on", "gnd", 20e-15)
    sim.write()
    write_sym(os.path.join(HERE, "vco_sim_flat.sym"), "vco_sim_flat",
              ["tp", "tn", "ct", "vt", "vdd", "gnd", "vbp", "vbp_tail"])
    # Document remaining ideals [decisions 2026-11-18]
    ideals_path = os.path.join(HERE, "out", "summary_vco_sim_ideals.txt")
    os.makedirs(os.path.dirname(ideals_path), exist_ok=True)
    open(ideals_path, "w").write(
        "# Remaining ideal / equivalent parts in vco_sim_flat [SCH]\n\n"
        "| part | kind | why kept |\n"
        "|------|------|----------|\n"
        "| l2n0 R/L/C | EM lumped | No spiral in sim; Palace/EM model "
        "`l2n0_lumped.inc` [EM] |\n"
        "| vvb_bias | vsource 0.3 V | Var well bias; not a fab pin; TB "
        "stimulus [SCH] |\n"
        "| iref_pbias | isource | External DAC master current into pbias; "
        "full current-source DAC not needed for band TB; PSS with 51 "
        "unit DACs not proven [SCH] |\n"
        "| mb1/mb2 + rl + ib + ctb + cl | stand-in CML | Not in vco_top.sch; "
        "LO-load for range/PN; real buffer is separate open item [SCH] |\n"
        "| (none) cbf | — | Uses 7× cmim from sch (not ideal 50 pF) [SCH] |\n"
        "| (none) rbf | — | Uses rhigh from sch [SCH] |\n"
        "\nBand/range TB in step2 still uses `run_step2.netlist` (lighter "
        "deck); that deck is aligned to sch for bank cmim b0..b2 — see "
        "step2 patch. Ideals there: iref, ideal R bias, ideal cbf option, "
        "supplies, kick, stand-in buffer [SCH].\n"
    )

    # Combined inventory JSON
    inv = {}
    for k, sch in blocks.items():
        inv[k] = [
            {"kind": d.kind, "name": d.name, "nodes": d.nodes, "params": d.params}
            for d in sch.devices
        ]
    inv["vco_sim_flat"] = [
        {"kind": d.kind, "name": d.name, "nodes": d.nodes, "params": d.params}
        for d in sim.devices
    ]
    open(os.path.join(HERE, "netlists", "device_inventory.json"), "w").write(
        json.dumps(inv, indent=2)
    )

    # Per-block vacask
    for k, sch in blocks.items():
        write_vacask(os.path.join(HERE, "netlists", f"{k}.vacask"),
                     f"P2.7.1 {k}", sch.devices)
    write_vacask(os.path.join(HERE, "netlists", "vco_sim_flat.vacask"),
                 "P2.7.1 vco_sim_flat", sim.devices)

    # Copy EM include next to netlists for sims
    shutil.copy(L2N0_INC, os.path.join(HERE, "netlists", "l2n0_lumped.inc"))
    return blocks, sim


def _emit(sch: Sch, d):
    p = d.params
    if d.kind == "nmos":
        sch.nmos(d.name, *d.nodes, p["w"], p["l"], int(p["ng"]), p["model"])
    elif d.kind == "pmos":
        sch.pmos(d.name, *d.nodes, p["w"], p["l"], int(p["ng"]), p["model"])
    elif d.kind == "mim":
        sch.mim(d.name, *d.nodes, p["w"], p["l"])
    elif d.kind == "cmim":
        sch.mim(d.name, d.nodes[0], d.nodes[1], "gnd", p["w"], p["l"],
                kind="cmim")
    elif d.kind == "svaricap":
        sch.svaricap_fx(d.name, *d.nodes, p["w"], p["l"], int(p["nx"]))
    elif d.kind == "res":
        sch.res(d.name, *d.nodes, float(p["r"]))
    elif d.kind == "rhigh":
        sch.rhigh(d.name, d.nodes[0], d.nodes[1], d.nodes[2],
                  w=p["w"], l=p["l"], bends=int(p.get("b", 0)))
    elif d.kind == "capa":
        sch.capa(d.name, *d.nodes, float(p["c"]))
    elif d.kind == "ind":
        sch.ind(d.name, *d.nodes, float(p["l"]))
    elif d.kind == "vsrc":
        sch.vsrc(d.name, *d.nodes, float(p["dc"]))
    elif d.kind == "isrc":
        sch.isrc(d.name, *d.nodes, float(p["dc"]))
    else:
        raise ValueError(d.kind)


def write_xschemrc():
    # Portable: cwd-relative sch dir works in container and on host [TOOL]
    src = "/foss/pdks/ihp-sg13g2/libs.tech/xschem/xschemrc"
    dst = os.path.join(HERE, "xschemrc")
    prefix = (
        "set XSCHEM_LIBRARY_PATH [file normalize [file dirname "
        "[info script]]]\n"
        "append XSCHEM_LIBRARY_PATH "
        ":$env(PDK_ROOT)/$env(PDK)/libs.tech/xschem\n"
    )
    if os.path.exists(src):
        text = open(src).read()
        open(dst, "w").write(prefix + text)
    else:
        open(dst, "w").write(prefix)


def main():
    rng = load_range()
    write_xschemrc()
    blocks, sim = build_flat_inventory(rng)
    # README
    open(os.path.join(HERE, "README.md"), "w").write(
        "# P2.7.1 xschem capture (VCO + D22 amp-cal + D21 LDO)\n\n"
        "Generated by `gen_xschem.py` from `step2/out/range.json`, "
        "`ampcal/amp_common.py`, and `ldo/run_d21_vrana1.py` `ldo_body`.\n\n"
        "## Hierarchy\n\n"
        "| Cell | Role |\n|---|---|\n"
        "| `l2n0` | Tapped inductor lumped EM model |\n"
        "| `vco_core` | XC pair + fixed MIM |\n"
        "| `vco_bank` | 8-bit bank + trims + bypass |\n"
        "| `vco_var` | AC-coupled svaricap_fx + bypass |\n"
        "| `vco_tail_dac` | D22 OTA DAC + tail + D9 filter |\n"
        "| `ampcal_det` | D22 peak det + SE comparator |\n"
        "| `vrana1_ldo` | D21 LDO |\n"
        "| `vco_sim_flat` | Flat VCO for netlist/sim export |\n\n"
        "Exports: `exports/*.svg`, `exports/*.pdf`. "
        "Netlists: `netlists/`. Summaries: `out/summary_*.txt`.\n"
    )
    print("Generated cells:", ", ".join(blocks.keys()), "+ vco_sim_flat")
    print("Devices in vco_sim_flat:", len(sim.devices))
    for k, sch in blocks.items():
        print(f"  {k}: {len(sch.devices)} devices")


if __name__ == "__main__":
    main()

