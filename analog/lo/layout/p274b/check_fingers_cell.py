#!/usr/bin/env python3
"""Finger-count check for P2.7.4b GDS — one count per MOSFET leaf [TOOL].

Walks the instance tree but only records ng on nmos/pmos (or sg13_*mos)
leaves. Parent cells that also hold poly shapes are ignored so devices are
not double-counted. Expectation is an exact multiset of ng values
(equality), not a lower bound.
"""
from __future__ import annotations

import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path[:0] = [
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python",
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python/pycell4klayout-api/source/python",
]
import pya  # noqa: E402

# cell -> exact multiset of ng on MOSFET leaves (sorted for compare) [SCH/GDS]
EXPECT: dict[str, list[int]] = {
    "cml_diff_pair": [1, 1, 5, 5],
    "cml_diff_pair_vhf": [1, 1, 5, 5],
    "cml_pair_loads": [1, 1, 5, 5],
    "cml_pair_loads_vhf": [1, 1, 5, 5],
    "cml_regen_xc": [1, 1, 5, 5],
    "cml_regen_xc_vhf": [1, 1, 5, 5],
    "cml_clk_pair": [1, 1, 5, 5],
    "cml_clk_pair_vhf": [1, 1, 5, 5],
    "cml_tail": [1, 1, 5],
    "cml_tail_nor_vhf": [1, 1, 5],
    "cml_nor_core_vhf": [1, 1, 5, 5, 5],
    "cml_nor_vhf": [1, 1, 1, 1, 5, 5, 5, 5],
    "lo_inv_05_1": [1, 1],
    "lo_inv_1_2": [1, 1],
    "lo_inv_2_4": [1, 1],
    "lo_inv_3_6": [1, 1],
    "lo_inv_45_9": [1, 1],
    "lo_inv_9_18": [1, 1, 1, 1],
    # UHF latch: clk+loads+regen+tail = 4×(2×ng1+2×ng5) wait: 8×ng1 + 7×ng5
    "cml_latch_uhf": [1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5],
    # VHF TL latch: no tail → 6×ng1 + 6×ng5
    "cml_latch_vhf_tl": [1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5],
    # 3×2_4 + 2×05_1 + 3_6 + 9_18(2×45_9) = 8 inv × 2 MOS = 16×ng1
    "cml_conv": [1] * 16,
}


def is_mosfet_leaf(cell) -> bool:
    n = cell.name.lower()
    if n.startswith("nmos") or n.startswith("pmos"):
        return True
    if "sg13_lv_nmos" in n or "sg13_lv_pmos" in n:
        return True
    if "sg13_hv_nmos" in n or "sg13_hv_pmos" in n:
        return True
    return False


def poly_ng(cell) -> int:
    poly = cell.layout().layer(5, 0)
    dbu = cell.layout().dbu
    xs = set()
    for s in cell.shapes(poly).each():
        if not s.is_box():
            continue
        b = s.bbox().to_dtype(dbu)
        if b.width() < 0.2 and b.height() > 0.4:
            xs.add(round(0.5 * (b.left + b.right), 3))
    return len(xs)


def walk_mos_ngs(cell, out: list[int]) -> None:
    """Record ng only on MOSFET leaves; do not count parent poly."""
    if is_mosfet_leaf(cell):
        ng = poly_ng(cell)
        if ng > 0:
            out.append(ng)
        return
    for i in cell.each_inst():
        walk_mos_ngs(i.cell, out)


def main():
    cell = sys.argv[1] if len(sys.argv) > 1 else "cml_clk_pair"
    discover = "--discover" in sys.argv
    gds = os.path.join(OUT, f"{cell}.gds")
    if not os.path.isfile(gds) and os.path.isfile(gds + ".gz"):
        import gzip
        import shutil
        with gzip.open(gds + ".gz", "rb") as z, open(gds, "wb") as f:
            shutil.copyfileobj(z, f)
    ly = pya.Layout()
    ly.read(gds)
    top = ly.top_cell()
    raw: list[int] = []
    walk_mos_ngs(top, raw)
    ngs = sorted(raw)
    if discover or cell not in EXPECT or not EXPECT[cell]:
        print(f"DISCOVER {cell} ngs={ngs} counts={dict(Counter(ngs))}",
              flush=True)
        if discover:
            return 0
    expect = sorted(EXPECT[cell])
    ok = ngs == expect
    gate = "PASS" if ok else "FAIL"
    path = os.path.join(OUT, f"summary_fingers_{cell}.txt")
    open(path, "w").write(
        f"# {cell} fingers [TOOL]\n\n"
        f"ngs={ngs}\n"
        f"expect={expect} (exact equality; MOSFET leaves only)\n"
        f"gate: {gate}\n"
    )
    print(f"fingers {cell} {ngs} expect={expect} {gate}", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
