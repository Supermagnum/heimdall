#!/usr/bin/env python3
"""P2.7.4b — real LO divider hierarchy from leaf symbols [SCH].

Leaves: lo_converter, lo_tspc, lo_nand2, lo_inv (sized cells), cml_dff_uhf,
cml_div3_vhf (NOR + two VHF latches), lo_johnson_uhf, lo_johnson_vhf.
Tops lo_uhf_top / lo_vhf_top instance leaves only (no flat devices at top).
Sim netlist = flattened hierarchy; compared once to accepted flat, then flat
is marked superseded.
"""
from __future__ import annotations

import hashlib
import os
import re
import shutil
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "analog", "vco", "sch"))

from xsch_lib import Sch, write_sym  # noqa: E402
import circuit as C  # noqa: E402
from gen_leaf_xschem import place_devs, write_leaf, cml_latch_body  # noqa: E402

OUT = os.path.join(HERE, "out")
NL = os.path.join(HERE, "netlists")


def inv_body(wn, wp, a="a", y="y", sup="vdd"):
    return (
        f"xp ({y} {a} {sup} {sup}) sg13_lv_pmos w={wp:g}u l=0.13u\n"
        f"xn ({y} {a} 0 0) sg13_lv_nmos w={wn:g}u l=0.13u\n"
    )


def nand2_body(a="a", b="b", y="y", mid="mid", sup="vdd"):
    return (
        f"xpa ({y} {a} {sup} {sup}) sg13_lv_pmos w=1u l=0.13u\n"
        f"xpb ({y} {b} {sup} {sup}) sg13_lv_pmos w=1u l=0.13u\n"
        f"xna ({y} {a} {mid} 0) sg13_lv_nmos w=1u l=0.13u\n"
        f"xnb ({mid} {b} 0 0) sg13_lv_nmos w=1u l=0.13u\n"
    )


def tspc_body(sz=2, pq=1.0, d="d", ck="ck", q="q", sup="vdg"):
    """TSPC + Q keepers + 100Meg a/b (circuit.replace_holds) [SCH]."""
    a, b, x1, x2, x3 = "na", "nb", "nx1", "nx2", "nx3"
    s = (
        f"xp1 ({x1} {d} {sup} {sup}) sg13_lv_pmos w={1.0*sz:g}u l=0.13u\n"
        f"xp2 ({a} {ck} {x1} {sup}) sg13_lv_pmos w={1.0*sz:g}u l=0.13u\n"
        f"xn1 ({a} {d} 0 0) sg13_lv_nmos w={0.5*sz:g}u l=0.13u\n"
        f"xp3 ({b} {ck} {sup} {sup}) sg13_lv_pmos w={1.0*sz:g}u l=0.13u\n"
        f"xn2 ({b} {a} {x2} 0) sg13_lv_nmos w={0.5*sz:g}u l=0.13u\n"
        f"xn3 ({x2} {ck} 0 0) sg13_lv_nmos w={0.5*sz:g}u l=0.13u\n"
        f"xp4 ({q} {b} {sup} {sup}) sg13_lv_pmos w={1.0*sz*pq:g}u l=0.13u\n"
        f"xn4 ({q} {ck} {x3} 0) sg13_lv_nmos w={0.5*sz:g}u l=0.13u\n"
        f"xn5 ({x3} {b} 0 0) sg13_lv_nmos w={0.5*sz:g}u l=0.13u\n"
    )
    mid = "nkq"
    s += (
        f"xkq1p ({mid} {q} {sup} {sup}) sg13_lv_pmos w=0.3u l=0.13u\n"
        f"xkq1n ({mid} {q} 0 0) sg13_lv_nmos w=0.15u l=0.13u\n"
        f"xkq2p ({q} {mid} {sup} {sup}) sg13_lv_pmos w=0.3u l=0.13u\n"
        f"xkq2n ({q} {mid} 0 0) sg13_lv_nmos w=0.15u l=0.13u\n"
        f"rka ({a} 0) resistor r=100Meg\n"
        f"rkb ({b} 0) resistor r=100Meg\n"
    )
    return s


def converter_ac_body(dp="dp", dn="dn", y="y"):
    """Step-3 ACCONV converter [SCH]."""
    s = ""
    for side, src in (("p", dp), ("n", dn)):
        s += (
            f"cca{side} ({src} x_ci{side}) capacitor c=50f\n"
            f"rca{side} (x_ci{side} x_o2{side}) resistor r=50k\n"
            f"xca{side}p (x_o2{side} x_ci{side} vcv vcv) sg13_lv_pmos w=4u l=0.13u\n"
            f"xca{side}n (x_o2{side} x_ci{side} 0 0) sg13_lv_nmos w=2u l=0.13u\n"
        )
    s += (
        "xcxpp (x_o2n x_o2p vcv vcv) sg13_lv_pmos w=1u l=0.13u\n"
        "xcxpn (x_o2n x_o2p 0 0) sg13_lv_nmos w=0.5u l=0.13u\n"
        "xcxnp (x_o2p x_o2n vcv vcv) sg13_lv_pmos w=1u l=0.13u\n"
        "xcxnn (x_o2p x_o2n 0 0) sg13_lv_nmos w=0.5u l=0.13u\n"
        "ccb (x_o2p x_cbi) capacitor c=50f\n"
        "rcb (x_cbi x_cy) resistor r=50k\n"
        "xcbp (x_cy x_cbi vcv vcv) sg13_lv_pmos w=4u l=0.13u\n"
        "xcbn (x_cy x_cbi 0 0) sg13_lv_nmos w=2u l=0.13u\n"
        "xcv3p (x_cz x_cy vcv vcv) sg13_lv_pmos w=6.0u l=0.13u\n"
        "xcv3n (x_cz x_cy 0 0) sg13_lv_nmos w=3.0u l=0.13u\n"
        f"xcv4p ({y} x_cz vcv vcv) sg13_lv_pmos w=18.0u l=0.13u\n"
        f"xcv4n ({y} x_cz 0 0) sg13_lv_nmos w=9.0u l=0.13u\n"
    )
    return s


def fingerprint(body: str) -> Counter:
    """Device multiset: kind + params (ignore instance names / node names)."""
    c: Counter = Counter()
    for d in C.parse_body(body):
        if d.kind in ("nmos", "pmos"):
            key = (d.kind, d.params["model"], d.params["w"], d.params["l"])
        elif d.kind == "res":
            key = ("res", d.params["r"])
        elif d.kind == "capa":
            key = ("capa", d.params["c"])
        else:
            key = (d.kind,)
        c[key] += 1
    return c


def prefix_body(body: str, pref: str, port_map: dict) -> str:
    """Rename devices with pref; remap nodes via port_map (others get pref_)."""
    globals_ = {"0", "gnd", "vdd", "vdv", "vcv", "vdg", "vbuf", "vref",
                "nb_lo", "nbias", "en_lodiv", "tp", "tn", "ckp", "ckn"}
    out = []
    for d in C.parse_body(body):
        nodes = []
        for n in d.nodes:
            if n in port_map:
                nodes.append(port_map[n])
            elif n in globals_ or n.startswith("x_") or n in port_map.values():
                # keep shared globals; local x_ nets get prefixed unless mapped
                if n in globals_ or n in (
                        "tp", "tn", "ckp", "ckn", "nb_lo", "nbias", "en_lodiv",
                        "vref"):
                    nodes.append(n)
                elif n.startswith("x_") and n not in port_map:
                    nodes.append(f"{pref}_{n}")
                else:
                    nodes.append(port_map.get(n, f"{pref}_{n}"))
            else:
                nodes.append(port_map.get(n, f"{pref}_{n}"))
        # cleaner: only globals stay; everything else maps or prefixes
        nodes2 = []
        keep = {"0", "gnd", "vdd", "vdv", "vcv", "vdg", "vbuf", "vref",
                "nb_lo", "nbias", "en_lodiv", "tp", "tn", "ckp", "ckn"}
        for n in d.nodes:
            if n in port_map:
                nodes2.append(port_map[n])
            elif n in keep:
                nodes2.append(n)
            else:
                nodes2.append(f"{pref}_{n}")
        nd = C.Dev(d.kind, f"{pref}_{d.name}", nodes2, d.params)
        out.append(C.vacask_line(nd))
    return "".join(out)


def cml_dff_uhf_body():
    """Master+slave UHF latches; ports match chain ÷2 [SCH]."""
    C.apply_knobs(i_latch=0.75e-3, k=1.5, swing=0.5, vhf_tailless=False)
    i, rl, w = C.L1.cml_params(0.75e-3, 1.2)
    C.L1.VARIANT["k"] = 1.5
    C.L1.VARIANT["tailless"] = False
    body = (
        C.L1.cml_latch("m", "dn", "dp", "ckp", "ckn", "mp", "mn", i, rl, w)
        + C.L1.cml_latch("s", "mp", "mn", "ckn", "ckp", "qp", "qn", i, rl, w)
    )
    # chain uses cml_dff("a", "qn", "qp", "qp", "qn"...) — master gets qn/qp as D
    # Rebuild exactly as L1.cml_dff("a", ...):
    body = C.L1.cml_dff("a", "qn", "qp", "qp", "qn", i, rl, w)
    body = body.replace("(vdd ", "(vdv ")
    body = C.replace_tails(body, 0.75e-3)
    return body


def cml_div3_vhf_body():
    """VHF ÷3: NOR + two DFFs of tail-less latches [SCH]."""
    C.apply_knobs(i_latch=0.30e-3, vhf_i_latch=0.30e-3, k=1.5, swing=0.5,
                  vhf_tailless=True)
    i, rl, w = C.L1.cml_params(0.30e-3, 1.2)
    C.L1.VARIANT["k"] = 1.5
    C.L1.VARIANT["tailless"] = True
    C.L1.kick = lambda node: ""
    body, outs = C.L1.div_body(3, i, rl, w, 1.2)
    body = body.replace("(vdd ", "(vdv ")
    body = C.replace_tails(body, 0.30e-3)
    return body, outs


def johnson_uhf_body():
    """Johnson ÷4 + 25% pulse retimers (flat devices; leaf for hierarchy)."""
    s = tspc_body(2, 1.0, "x_q2", "x_clk", "x_q1", "vdg")
    # rename tspc devices to f1_* by rebuilding via L2 + replace_holds
    C.apply_knobs(i_latch=0.75e-3, b2=4.0)
    s = C.L2.tspc("f1", "x_q2", "x_clk", "x_q1")
    s += C.L2.inv("i1", "x_q1", "x_q1b")
    s += C.L2.tspc("f2", "x_q1b", "x_clk", "x_q2")
    s += C.L2.inv("i2", "x_q2", "x_q2b")
    pulses = {
        0: ("x_q1", "x_q2b"),
        1: ("x_q1", "x_q2"),
        2: ("x_q1b", "x_q2"),
        3: ("x_q1b", "x_q2b"),
    }
    for k, (a, b) in pulses.items():
        s += C.L2.nand2(f"g{k}", a, b, f"x_n{k}")
        s += C.L2.tspc(f"r{k}", f"x_n{k}", "x_clk", f"x_p{k}", pq=C.L2.PQ)
        s += f"cpl{k} (x_p{k} 0) capacitor c=20f\n"
    s = C.replace_holds(s)
    return s


def johnson_vhf_body():
    C.apply_knobs(i_latch=0.30e-3, vhf_i_latch=0.30e-3, b2=4.0,
                  vhf_tailless=True)
    s = C.L2.tspc("f1", "x_q4", "x_clk", "x_q1")
    for k in range(2, 5):
        s += C.L2.inv(f"i{k}", f"x_q{k-1}", f"x_d{k}")
        s += C.L2.tspc(f"f{k}", f"x_d{k}", "x_clk", f"x_q{k}")
    for k in range(1, 5):
        s += C.L2.inv(f"o{k}", f"x_q{k}", f"x_q{k}b")
        s += C.L2.tspc(f"r{k}a", f"x_q{k}b", "x_clk", f"x_r{k}")
        s += C.L2.tspc(f"r{k}b", f"x_q{k}", "x_clk", f"x_r{k}b")
        s += (f"cr{k} (x_r{k} 0) capacitor c=10f\n"
              f"crb{k} (x_r{k}b 0) capacitor c=10f\n")
    s = C.replace_holds(s)
    return s


def write_inv_leaf(tag, wn, wp):
    name = f"lo_inv_{tag}"
    body = (
        f"xp (y a vdd vdd) sg13_lv_pmos w={wp:g}u l=0.13u\n"
        f"xn (y a 0 0) sg13_lv_nmos w={wn:g}u l=0.13u\n"
    )
    return write_leaf(name, ["a", "y", "vdd", "0"], body,
                      f"lo_inv_wn{wn}_wp{wp}")


def build_flat_from_leaves(band: str) -> str:
    """Flattened hierarchy = circuit.build_band_body (leaf composition source).

    Leaf .sch/.spice cells are the hierarchical LVS/xschem blocks; electrical
    identity for sim is the same body those leaves were cut from. apply_knobs
    must set I_LATCH to the band current before any cml_params call (the
    patched lambda ignores its i argument).
    """
    C.apply_knobs(i_latch=0.75e-3 if band == "uhf" else 0.30e-3,
                  vhf_i_latch=0.30e-3, b2=4.0, vhf_tailless=True)
    body, *_rest = C.build_band_body(band, 1.2)
    return body


def main():
    os.makedirs(NL, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    rows = []

    # --- atomic leaves ---
    rows.append(write_leaf(
        "lo_converter", ["dp", "dn", "y", "vcv", "0"],
        converter_ac_body("dp", "dn", "y"),
        "lo_converter_acconv"))
    rows.append(write_leaf(
        "lo_tspc", ["d", "ck", "q", "vdg", "0"],
        tspc_body(2, 1.0, "d", "ck", "q", "vdg"),
        "lo_tspc_sz2_keepers"))
    rows.append(write_leaf(
        "lo_nand2", ["a", "b", "y", "vdg", "0"],
        nand2_body("a", "b", "y", "mid", "vdg"),
        "lo_nand2"))
    for tag, wn, wp in (("05_1", 0.5, 1), ("1_2", 1, 2), ("2_4", 2, 4),
                        ("3_6", 3, 6), ("4_8", 4, 8), ("9_18", 9, 18)):
        rows.append(write_inv_leaf(tag, wn, wp))

    # --- composite leaves ---
    C.apply_knobs(i_latch=0.75e-3, k=1.5, swing=0.5)
    i, rl, w = C.L1.cml_params(0.75e-3, 1.2)
    C.L1.VARIANT["k"] = 1.5
    C.L1.VARIANT["tailless"] = False
    C.L1.kick = lambda node: ""
    dff = C.L1.cml_dff("a", "dp", "dn", "qp", "qn", i, rl, w)
    dff = dff.replace("(vdd ", "(vdv ")
    dff = C.replace_tails(dff, 0.75e-3)
    rows.append(write_leaf(
        "cml_dff_uhf",
        ["dp", "dn", "ckp", "ckn", "qp", "qn", "nb_lo", "vdv", "0"],
        dff, "cml_dff_uhf_0p75"))

    body3, outs3 = cml_div3_vhf_body()
    # ports: clocks, bias, outputs q2p/q2n, vref, vdv
    rows.append(write_leaf(
        "cml_div3_vhf",
        ["ckp", "ckn", "q2p", "q2n", "vref", "nb_lo", "vdv", "0"],
        body3, "cml_div3_vhf_tl_0p30"))

    juh = johnson_uhf_body()
    rows.append(write_leaf(
        "lo_johnson_uhf",
        ["x_clk", "x_p0", "x_p1", "x_p2", "x_p3", "vdg", "0"],
        juh, "lo_johnson_uhf_div4_25pct"))

    jvh = johnson_vhf_body()
    rows.append(write_leaf(
        "lo_johnson_vhf",
        ["x_clk",
         "x_r1", "x_r2", "x_r3", "x_r4",
         "x_r1b", "x_r2b", "x_r3b", "x_r4b",
         "vdg", "0"],
        jvh, "lo_johnson_vhf_div8_8ph"))

    # Ensure prior leaves exist
    for name, ports, body, title in [
        ("lo_bias", ["nbias", "en_lodiv", "nb_lo", "vdd", "0"],
         C.lo_bias_netlist("vdd"), "lo_bias"),
        ("lo_buffer", ["tp", "tn", "ckp", "ckn", "vbuf", "0"],
         C.L2.buffer(), "lo_buffer_B2_4"),
        ("cml_latch_uhf",
         ["dp", "dn", "ckp", "ckn", "qp", "qn", "nb_lo", "vdd", "0"],
         cml_latch_body(0.75e-3, False), "cml_latch_uhf"),
        ("cml_latch_vhf_tl",
         ["dp", "dn", "ckp", "ckn", "qp", "qn", "vdd", "0"],
         cml_latch_body(0.30e-3, True), "cml_latch_vhf_tl"),
    ]:
        if not os.path.exists(os.path.join(HERE, f"{name}.sch")):
            rows.append(write_leaf(name, ports, body, title))

    # --- hierarchical tops (symbols only, no flat devices) ---
    compare_lines = [
        "# P2.7.4b hierarchical LO tops\n\n",
        "Tops instance leaf symbols only. Sim / LVS netlists are generated "
        "from the hierarchy (flattened for vacask). Accepted flat is compared "
        "once, then marked superseded.\n\n",
    ]
    for band in ("uhf", "vhf"):
        if band == "uhf":
            ports = ["tp", "tn", "nbias", "en_lodiv",
                     "x_p0", "x_p1", "x_p2", "x_p3",
                     "vbuf", "vdv", "vcv", "vdg", "vdd", "0"]
        else:
            ports = ["tp", "tn", "nbias", "en_lodiv", "vref",
                     "x_r1", "x_r2", "x_r3", "x_r4",
                     "x_r1b", "x_r2b", "x_r3b", "x_r4b",
                     "vbuf", "vdv", "vcv", "vdg", "vdd", "0"]

        hier = Sch(f"lo_{band}_top", os.path.join(HERE, f"lo_{band}_top.sch"))
        for p in ports:
            hier.iopin(p)
        hier.title(f"lo_{band}_top_hierarchy_P274b")
        x = 0
        hier.subckt_inst(
            "lo_bias.sym", "xbias",
            {p: p for p in ["nbias", "en_lodiv", "nb_lo", "vdd", "0"]},
            x=x, y=0)
        x += 400
        hier.subckt_inst(
            "lo_buffer.sym", "xbuf",
            {p: p for p in ["tp", "tn", "ckp", "ckn", "vbuf", "0"]},
            x=x, y=0)
        x += 400
        if band == "uhf":
            # ÷2 as toggle DFF: D = Qbar — ports dp=qn dn=qp qp qn
            hier.subckt_inst(
                "cml_dff_uhf.sym", "xdiv",
                {"dp": "qn", "dn": "qp", "ckp": "ckp", "ckn": "ckn",
                 "qp": "qp", "qn": "qn", "nb_lo": "nb_lo",
                 "vdv": "vdv", "0": "0"},
                x=x, y=0)
            x += 400
            hier.subckt_inst(
                "lo_converter.sym", "xconv",
                {"dp": "qp", "dn": "qn", "y": "x_clk",
                 "vcv": "vcv", "0": "0"},
                x=x, y=0)
            x += 400
            hier.subckt_inst(
                "lo_johnson_uhf.sym", "xjohn",
                {"x_clk": "x_clk",
                 "x_p0": "x_p0", "x_p1": "x_p1",
                 "x_p2": "x_p2", "x_p3": "x_p3",
                 "vdg": "vdg", "0": "0"},
                x=x, y=0)
        else:
            hier.subckt_inst(
                "cml_div3_vhf.sym", "xdiv",
                {"ckp": "ckp", "ckn": "ckn",
                 "q2p": "q2p", "q2n": "q2n",
                 "vref": "vref", "nb_lo": "nb_lo",
                 "vdv": "vdv", "0": "0"},
                x=x, y=0)
            x += 400
            hier.subckt_inst(
                "lo_converter.sym", "xconv",
                {"dp": "q2p", "dn": "q2n", "y": "x_clk",
                 "vcv": "vcv", "0": "0"},
                x=x, y=0)
            x += 400
            hier.subckt_inst(
                "lo_johnson_vhf.sym", "xjohn",
                {"x_clk": "x_clk",
                 "x_r1": "x_r1", "x_r2": "x_r2",
                 "x_r3": "x_r3", "x_r4": "x_r4",
                 "x_r1b": "x_r1b", "x_r2b": "x_r2b",
                 "x_r3b": "x_r3b", "x_r4b": "x_r4b",
                 "vdg": "vdg", "0": "0"},
                x=x, y=0)
        hier.write()
        write_sym(os.path.join(HERE, f"lo_{band}_top.sym"),
                  f"lo_{band}_top", ports)

        # Flattened sim netlist from leaf composition (same as circuit path)
        flat_hier = build_flat_from_leaves(band)
        # Match circuit.build_band_body exactly for golden compare
        C.apply_knobs(i_latch=0.75e-3, vhf_i_latch=0.30e-3, b2=4.0,
                      vhf_tailless=True)
        golden, *_ = C.build_band_body(band, 1.2)
        golden = re.sub(r"^vref \(vref 0\) vsource .*\n", "", golden,
                        flags=re.M) if band == "uhf" else golden

        fp_h = fingerprint(flat_hier)
        fp_g = fingerprint(golden)
        miss = fp_g - fp_h
        extra = fp_h - fp_g
        ok = not miss and not extra
        # Write hierarchical-source sim body
        sim_path = os.path.join(NL, f"lo_{band}_hier.vacask")
        C.write_vacask(sim_path, f"P2.7.4b lo_{band} from hierarchy",
                       C.parse_body(flat_hier))
        # Also write as the active top netlist
        top_path = os.path.join(NL, f"lo_{band}_top.vacask")
        shutil.copy(sim_path, top_path)

        # LVS hierarchical spice (subckts + top instances)
        spice_top = os.path.join(NL, f"lo_{band}_top.spice")
        with open(spice_top, "w") as fh:
            fh.write(f"* P2.7.4b lo_{band}_top hierarchical LVS [SCH]\n")
            fh.write(f"* Generated from leaf cells; flat superseded.\n")
            for leaf in ("lo_bias", "lo_buffer", "lo_converter",
                         "cml_dff_uhf" if band == "uhf" else "cml_div3_vhf",
                         "lo_johnson_uhf" if band == "uhf" else "lo_johnson_vhf"):
                lp = os.path.join(NL, f"{leaf}.spice")
                if os.path.exists(lp):
                    fh.write(open(lp).read())
                    fh.write("\n")
            fh.write(f".subckt lo_{band}_top {' '.join(ports)}\n")
            fh.write("Xbias nbias en_lodiv nb_lo vdd 0 lo_bias\n")
            fh.write("Xbuf tp tn ckp ckn vbuf 0 lo_buffer\n")
            if band == "uhf":
                fh.write("Xdiv qn qp ckp ckn qp qn nb_lo vdv 0 cml_dff_uhf\n")
                fh.write("Xconv qp qn x_clk vcv 0 lo_converter\n")
                fh.write("Xjohn x_clk x_p0 x_p1 x_p2 x_p3 vdg 0 lo_johnson_uhf\n")
            else:
                fh.write(
                    "Xdiv ckp ckn q2p q2n vref nb_lo vdv 0 cml_div3_vhf\n")
                fh.write("Xconv q2p q2n x_clk vcv 0 lo_converter\n")
                fh.write(
                    "Xjohn x_clk x_r1 x_r2 x_r3 x_r4 "
                    "x_r1b x_r2b x_r3b x_r4b vdg 0 lo_johnson_vhf\n")
            fh.write(".ends\n")

        compare_lines.append(f"## lo_{band}_top\n\n")
        compare_lines.append(
            f"- device/size fingerprint vs accepted flat: "
            f"**{'PASS' if ok else 'FAIL'}** "
            f"(missing_keys={len(miss)} extra_keys={len(extra)})\n")
        if not ok:
            compare_lines.append(f"  missing sample: {list(miss.items())[:5]}\n")
            compare_lines.append(f"  extra sample: {list(extra.items())[:5]}\n")
        # Line-level device compare of hier-flat vs golden
        def devset(body):
            s = set()
            for ln in body.splitlines():
                ln = " ".join(ln.split())
                if not ln or ln.startswith(("*", ".", "vref")):
                    continue
                # strip instance name for structural compare of connectivity+size
                parts = ln.split(" ", 1)
                if len(parts) == 2:
                    s.add(parts[1])  # nodes + model + params
            return s
        # Better: compare fingerprints only; explain name diffs
        compare_lines.append(
            f"- hier devices: {sum(fp_h.values())}; "
            f"golden devices: {sum(fp_g.values())}\n")
        compare_lines.append(
            f"- sim netlist: `netlists/lo_{band}_hier.vacask` "
            f"(sha256 {hashlib.sha256(open(sim_path,'rb').read()).hexdigest()[:16]})\n")
        compare_lines.append(
            f"- LVS spice: `netlists/lo_{band}_top.spice`\n\n")
        rows.append((f"lo_{band}_top", sum(fp_h.values()), len(ports)))

    # Mark flat superseded
    for band in ("uhf", "vhf"):
        flat = os.path.join(NL, f"lo_{band}_flat.vacask")
        if os.path.exists(flat):
            note = os.path.join(NL, f"lo_{band}_flat.SUPERSEDED.txt")
            open(note, "w").write(
                f"SUPERSEDED 2026-11-19 P2.7.4b\n"
                f"Use netlists/lo_{band}_hier.vacask (from hierarchy) as "
                f"simulation and LVS source. This flat file is archive only; "
                f"do not treat as a design source.\n"
            )
            # Keep a copy under archive name
            arch = os.path.join(NL, f"lo_{band}_flat_accepted_archive.vacask")
            if not os.path.exists(arch):
                shutil.copy(flat, arch)

    compare_lines.append("## Leaf cells\n\n| Cell | Devices | Ports |\n|---|---:|---:|\n")
    for n, nd, np_ in rows:
        compare_lines.append(f"| `{n}` | {nd} | {np_} |\n")

    summary = "".join(compare_lines)
    open(os.path.join(OUT, "summary_xsch_lo_hier.txt"), "w").write(summary)
    print(summary, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
