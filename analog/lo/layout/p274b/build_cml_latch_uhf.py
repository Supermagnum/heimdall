#!/usr/bin/env python3
"""P2.7.4b — assemble cml_latch_uhf from proven sub-cells [SCH].

Placement (2026-11-20):
  pair_loads left; regen M90 east so E-face d1/d2 meet pair E;
  x_rg chosen so bboxes do not overlap (east-lane overhang);
  clk_pair south; tail south of clk.
No metal through child cells; gap stubs only.
"""
from __future__ import annotations

import gzip
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path[:0] = [
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python",
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python/"
    "pycell4klayout-api/source/python",
]
import pya  # noqa: E402
import sg13g2_pycell_lib  # noqa: E402, F401

DBU = 0.001
GAP_NS = 3.0
GAP_EW = 1.0
# qp/qn stub may exceed 5 µm when M90 clears east-lane bbox overhang [GDS]
STUB_MAX = 12.0
R_W, R_L = "2.0u", "5.334u"


def um(x):
    return int(round(float(x) / DBU))


def parse_pins(ly, cid, m1txt):
    pins = {}
    for s in ly.cell(cid).shapes(m1txt).each():
        if not s.is_text():
            continue
        raw = s.text
        if isinstance(raw, tuple):
            name = raw[0]
        else:
            m = re.match(r"\('([^']+)'", str(raw))
            name = m.group(1) if m else str(raw)
        pins[name] = (s.text_dtrans.disp.x, s.text_dtrans.disp.y)
    return pins


def load_cell(ly, gds_name, cell_name):
    src = pya.Layout()
    src.read(os.path.join(OUT, gds_name))
    src_top = None
    for c in src.each_cell():
        if c.name == cell_name:
            src_top = c
            break
    if src_top is None:
        src_top = src.top_cell()
    cid = ly.add_cell(cell_name + "_lib")
    ly.cell(cid).copy_tree(src_top)
    ly.cell(cid).name = cell_name
    return cid


def map_pins(pins0, x, y, mirror=False):
    out = {}
    for n, (px, py) in pins0.items():
        if mirror:
            out[n] = (x - px, y + py)
        else:
            out[n] = (x + px, y + py)
    return out


def main():
    ly = pya.Layout()
    ly.dbu = DBU
    ly.technology_name = "sg13g2"
    m1 = ly.layer(8, 0)
    m1pin = ly.layer(8, 2)
    m1txt = ly.layer(8, 25)

    pl_cid = load_cell(ly, "cml_pair_loads.gds", "cml_pair_loads")
    rg_cid = load_cell(ly, "cml_regen_xc.gds", "cml_regen_xc")
    ck_cid = load_cell(ly, "cml_clk_pair.gds", "cml_clk_pair")
    tl_cid = load_cell(ly, "cml_tail.gds", "cml_tail")

    def strip_all_pin_texts(cid):
        """Remove M1txt recursively so only top-cell ports remain [netgen]."""
        cell = ly.cell(cid)
        for sh in list(cell.shapes(m1txt).each()):
            if sh.is_text():
                sh.delete()
        for i in cell.each_inst():
            strip_all_pin_texts(i.cell_index)

    # Leaves already have join pins on bbox faces; gap stubs only (no reach-in).
    pp0_raw = parse_pins(ly, pl_cid, m1txt)
    rp0_raw = parse_pins(ly, rg_cid, m1txt)
    cp0_raw = parse_pins(ly, ck_cid, m1txt)
    tp0_raw = parse_pins(ly, tl_cid, m1txt)
    print("leaf face pins pair", pp0_raw, flush=True)
    print("leaf face pins regen", rp0_raw, flush=True)
    print("leaf face pins clk", cp0_raw, flush=True)
    print("leaf face pins tail", tp0_raw, flush=True)

    pp0 = {
        "qn": pp0_raw["d1"], "qp": pp0_raw["d2"], "s1a": pp0_raw["s"],
        "dp": pp0_raw["g1"], "dn": pp0_raw["g2"],
        "gnd": pp0_raw["gnd"], "vdd": pp0_raw["vdd"],
    }
    rp0 = {
        "qn": rp0_raw["d1"], "qp": rp0_raw["d2"],
        "s2a": rp0_raw["s"], "gnd": rp0_raw["gnd"],
    }
    cp0 = {
        "s1a": cp0_raw["d1"], "s2a": cp0_raw["d2"], "ta": cp0_raw["s"],
        "ckp": cp0_raw["g1"], "ckn": cp0_raw["g2"], "gnd": cp0_raw["gnd"],
    }
    tp0 = {
        "ta": tp0_raw["drain"], "nb_lo": tp0_raw["nb_lo"], "gnd": tp0_raw["gnd"],
    }
    for cid in (pl_cid, rg_cid, ck_cid, tl_cid):
        strip_all_pin_texts(cid)
    pbb0 = ly.cell(pl_cid).bbox().to_dtype(ly.dbu)
    rbb0 = ly.cell(rg_cid).bbox().to_dtype(ly.dbu)
    cbb0 = ly.cell(ck_cid).bbox().to_dtype(ly.dbu)
    tbb0 = ly.cell(tl_cid).bbox().to_dtype(ly.dbu)

    top = ly.create_cell("cml_latch_uhf")

    # clk at origin; N drains define s1/s2 X targets
    x_ck, y_ck = 0.0, 0.0
    top.insert(pya.CellInstArray(
        ck_cid, pya.Trans(pya.Trans.R0, um(x_ck), um(y_ck))))
    cp = map_pins(cp0, x_ck, y_ck)
    cbb = cbb0  # at origin

    # Place by bbox gap; N–S stubs only in the clear gap (no metal through children).
    gap_ns = GAP_NS + max(0.0, cbb.top - cp["s1a"][1]) + max(
        0.0, pp0["s1a"][1] - pbb0.bottom)
    x_pl = cp["s1a"][0] - pp0["s1a"][0]
    y_pl = cbb.top + gap_ns - pbb0.bottom
    # Regen M90: E-face d1/d2 meet pair E. x_rg clears bbox overhang.
    rbb0 = ly.cell(rg_cid).bbox().to_dtype(ly.dbu)
    # After M90: world_x = x_rg - local_x; left = x_rg - rbb0.right
    x_rg_pin = (x_pl + max(pp0["qn"][0], pp0["qp"][0]) + GAP_EW
                + max(rp0["qn"][0], rp0["qp"][0]))
    x_rg_bb = x_pl + pbb0.right + GAP_EW + rbb0.right
    x_rg = max(x_rg_pin, x_rg_bb)
    y_rg = y_pl + (pp0["qn"][1] - rp0["qn"][1])
    rbb_try = ly.cell(rg_cid).bbox().transformed(
        pya.Trans(pya.Trans.M90, um(x_rg), um(y_rg))).to_dtype(ly.dbu)
    lift = (cbb.top + GAP_NS) - rbb_try.bottom
    if lift > 0:
        y_pl += lift
        y_rg += lift
    top.insert(pya.CellInstArray(
        pl_cid, pya.Trans(pya.Trans.R0, um(x_pl), um(y_pl))))
    pp = map_pins(pp0, x_pl, y_pl)
    pbb = ly.cell(pl_cid).bbox().transformed(
        pya.Trans(pya.Trans.R0, um(x_pl), um(y_pl))).to_dtype(ly.dbu)
    top.insert(pya.CellInstArray(
        rg_cid, pya.Trans(pya.Trans.M90, um(x_rg), um(y_rg))))
    rp = map_pins(rp0, x_rg, y_rg, mirror=True)
    rbb = ly.cell(rg_cid).bbox().transformed(
        pya.Trans(pya.Trans.M90, um(x_rg), um(y_rg))).to_dtype(ly.dbu)

    gap_ns_t = GAP_NS + max(0.0, cp["ta"][1] - cbb.bottom) + max(
        0.0, tbb0.top - tp0["ta"][1])
    x_tl = cp["ta"][0] - tp0["ta"][0]
    y_tl = cbb.bottom - gap_ns_t - tbb0.top
    top.insert(pya.CellInstArray(
        tl_cid, pya.Trans(pya.Trans.R0, um(x_tl), um(y_tl))))
    tp = map_pins(tp0, x_tl, y_tl)
    tbb = ly.cell(tl_cid).bbox().transformed(
        pya.Trans(pya.Trans.R0, um(x_tl), um(y_tl))).to_dtype(ly.dbu)

    assert pbb.bottom >= cbb.top - 0.01, (pbb.bottom, cbb.top)
    assert rbb.bottom >= cbb.top - 0.01, (rbb.bottom, cbb.top)
    assert cbb.bottom >= tbb.top - 0.01, (cbb.bottom, tbb.top)
    print(f"bbox gaps NS pair-clk={pbb.bottom - cbb.top:.3f} "
          f"regen-clk={rbb.bottom - cbb.top:.3f} "
          f"clk-tail={cbb.bottom - tbb.top:.3f} [GDS]", flush=True)

    def box(x0, y0, x1, y1):
        top.shapes(m1).insert(pya.DBox(
            min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    def pin(x, y, name):
        box(x - 0.25, y - 0.25, x + 0.25, y + 0.25)
        top.shapes(m1pin).insert(pya.DBox(x - 0.2, y - 0.2, x + 0.2, y + 0.2))
        top.shapes(m1txt).insert(pya.DText(name, pya.DTrans(x, y)))

    # --- gap stubs (M1 only, outside child bboxes) ---
    for net in ("qn", "qp"):
        xa, ya = pp[net]
        xb, yb = rp[net]
        assert abs(ya - yb) < 0.05, (net, ya, yb)
        x_l = pbb.right
        x_r = rbb.left
        stub = abs(xb - xa)
        print(f"{net} stub L={stub:.3f} µm Y={ya:.3f} "
              f"corridor={x_r - x_l:.3f} [GDS]", flush=True)
        assert x_r >= x_l - 0.01, (net, x_l, x_r)
        box(x_l, ya - 0.20, x_r, ya + 0.20)

    # N–S: metal only in inter-bbox gap, touching faces (no intrusion) [M1.b].
    def gap_only_ns(x_north, y_north, x_south, y_south, bb_n, bb_s, label):
        y_hi = bb_n.bottom
        y_lo = bb_s.top
        print(f"{label} gap-only dX={abs(x_north - x_south):.3f} "
              f"gapY={y_hi - y_lo:.3f} pinDY={abs(y_north - y_south):.3f} [GDS]",
              flush=True)
        assert y_hi >= y_lo + 0.5, (label, y_hi, y_lo)
        x = 0.5 * (x_north + x_south)
        box(x - 0.20, y_lo, x + 0.20, y_hi)
        if abs(x_north - x) > 0.05:
            box(min(x_north, x), y_hi - 0.40, max(x_north, x), y_hi)
        if abs(x_south - x) > 0.05:
            box(min(x_south, x), y_lo, max(x_south, x), y_lo + 0.40)
        box(x_north - 0.20, y_hi - 0.40, x_north + 0.20, y_hi)
        box(x_south - 0.20, y_lo, x_south + 0.20, y_lo + 0.40)

    xs, ys = pp["s1a"]
    xd, yd = cp["s1a"]
    gap_only_ns(xs, ys, xd, yd, pbb, cbb, "s1")
    xs2, ys2 = rp["s2a"]
    xd2, yd2 = cp["s2a"]
    gap_only_ns(xs2, ys2, xd2, yd2, rbb, cbb, "s2")
    xcs, ycs = cp["ta"]
    xtd, ytd = tp["ta"]
    gap_only_ns(xcs, ycs, xtd, ytd, cbb, tbb, "ta")

    # gnd: west rail for pair/clk/tail; regen gnd on E — east drop, south, west.
    x_west = min(pbb.left, cbb.left, tbb.left, rbb.left) - 3.0
    for bb, (xg, yg) in (
            (pbb, pp["gnd"]), (cbb, cp["gnd"]), (tbb, tp["gnd"])):
        box(x_west - 0.20, yg - 0.20, bb.left, yg + 0.20)
    xg_r, yg_r = rp["gnd"]
    x_east_g = max(rbb.right, cbb.right) + 2.0
    y_jog = min(rbb.bottom, cbb.bottom, tbb.bottom) - 2.0
    box(rbb.right, yg_r - 0.20, x_east_g, yg_r + 0.20)
    box(x_east_g - 0.20, y_jog - 0.20, x_east_g + 0.20, yg_r + 0.20)
    box(x_west - 0.20, y_jog - 0.20, x_east_g + 0.20, y_jog + 0.20)
    ys_g = [pp["gnd"][1], cp["gnd"][1], tp["gnd"][1], yg_r, y_jog]
    box(x_west - 0.20, min(ys_g), x_west + 0.20, max(ys_g))

    # Top ports (names already on children; re-export fan-out)
    for name, (x, y) in (
            ("dp", pp["dp"]), ("dn", pp["dn"]),
            ("ckp", cp["ckp"]), ("ckn", cp["ckn"]),
            ("vdd", pp["vdd"]), ("nb_lo", tp["nb_lo"]),
            ("qn", pp["qn"]), ("qp", pp["qp"])):
        pin(x, y, name)
    y_gnd_pin = 0.5 * (min(ys_g) + max(ys_g))
    box(x_west - 2.0, y_gnd_pin - 0.20, x_west + 0.20, y_gnd_pin + 0.20)
    pin(x_west - 1.5, y_gnd_pin, "gnd")

    qnL = abs(rp["qn"][0] - pp["qn"][0])
    qpL = abs(rp["qp"][0] - pp["qp"][0])
    checks = [
        (f"qp/qn stub short (<{STUB_MAX} µm)", max(qnL, qpL) < STUB_MAX),
        ("qp/qn Y-aligned",
         abs(pp["qn"][1] - rp["qn"][1]) < 0.05
         and abs(pp["qp"][1] - rp["qp"][1]) < 0.05),
        (f"s2 stub short (<{STUB_MAX} µm)", abs(xs2 - xd2) < STUB_MAX),
        ("E faces clear gap",
         min(rp["qn"][0], rp["qp"][0]) >= max(pp["qn"][0], pp["qp"][0])),
        ("bboxes no EW overlap", rbb.left >= pbb.right - 0.01),
    ]
    for msg, ok in checks:
        print(f"CHECK {'PASS' if ok else 'FAIL'}: {msg}", flush=True)

    gds = os.path.join(OUT, "cml_latch_uhf.gds")
    ly.write(gds)
    with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
        shutil.copyfileobj(f, z)

    # Flat LVS vs xschem leaf; dummies combine 3+4.5+3+6 = 16.5
    open(os.path.join(OUT, "cml_latch_uhf.spice"), "w").write(
        "* P2.7.4b cml_latch_uhf flat LVS [SCH]\n"
        ".subckt cml_latch_uhf dp dn ckp ckn qp qn nb_lo vdd gnd\n"
        "Mma1 qn dp s1a gnd sg13_lv_nmos w=7.50u l=0.13u\n"
        "Mma2 qp dn s1a gnd sg13_lv_nmos w=7.50u l=0.13u\n"
        "Mma3 qn qp s2a gnd sg13_lv_nmos w=11.25u l=0.13u\n"
        "Mma4 qp qn s2a gnd sg13_lv_nmos w=11.25u l=0.13u\n"
        "Mma5 s1a ckp ta gnd sg13_lv_nmos w=7.50u l=0.13u\n"
        "Mma6 s2a ckn ta gnd sg13_lv_nmos w=7.50u l=0.13u\n"
        "Mmta ta nb_lo gnd gnd sg13_lv_nmos w=15.0u l=0.13u\n"
        f"Rrlp vdd qn gnd rppd w={R_W} l={R_L} ps=0u b=0 m=1\n"
        f"Rrln vdd qp gnd rppd w={R_W} l={R_L} ps=0u b=0 m=1\n"
        "Mdum gnd gnd gnd gnd sg13_lv_nmos w=16.5u l=0.13u\n"
        ".ends\n"
    )
    open(os.path.join(OUT, "summary_build_cml_latch_uhf.txt"), "w").write(
        f"pair ({x_pl:.3f},{y_pl:.3f}) regen M90 ({x_rg:.3f},{y_rg:.3f})\n"
        f"clk (0,0) tail ({x_tl:.3f},{y_tl:.3f})\n"
        f"qn stub {qnL:.3f} qp stub {qpL:.3f} s2 dX {abs(xs2 - xd2):.3f}\n"
        + "\n".join(f"{'PASS' if ok else 'FAIL'} {m}" for m, ok in checks)
        + "\n"
    )
    print("WROTE", gds, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
