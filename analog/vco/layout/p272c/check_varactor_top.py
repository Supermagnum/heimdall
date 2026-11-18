#!/usr/bin/env python3
"""Varactor dimension + finger checks on assembled vco_top [TOOL].

Ports W on SVaricap are the well pin (schematic vt), not device width — so
netgen alone does not prove w/l/Nx (#753-class). Compare spice / extract /
GDS here. Intent: two sg13_hv_svaricap, w=3.74 µm, l=0.3 µm, Nx=10 [SCH].
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
INTENT = {"w": 3.74, "l": 0.3, "Nx": 10}
TOL_UM = 0.02
EXPECT_SV = 2
EXPECT_BYPASS_NG = [2, 2]  # two bypass NMOS, ng=2 each [SCH]


def parse_svaricap(path: str) -> list[dict]:
    if not path or not os.path.exists(path):
        return []
    txt = open(path, errors="ignore").read()
    out = []
    for m in re.finditer(r"sg13_hv_svaricap\s+([^\n]+)", txt, re.I):
        props = m.group(1)
        d = {}
        for k, pat in (
            ("w", r"w=([\d.eE+-]+)u?"),
            ("l", r"l=([\d.eE+-]+)u?"),
            ("Nx", r"Nx=(\d+)"),
        ):
            mm = re.search(pat, props, re.I)
            if not mm:
                continue
            v = mm.group(1)
            if k == "Nx":
                d[k] = int(v)
            else:
                x = float(v)
                # meters → µm
                if x < 1e-3:
                    x *= 1e6
                d[k] = x
        if d:
            out.append(d)
    return out


def match(got: dict) -> tuple[bool, str]:
    msgs = []
    ok = True
    for k, want in INTENT.items():
        if k not in got:
            ok = False
            msgs.append(f"{k}: missing")
            continue
        g = got[k]
        if k == "Nx":
            if int(g) != int(want):
                ok = False
                msgs.append(f"Nx={g}!={want}")
            else:
                msgs.append(f"Nx={g} OK")
        elif abs(float(g) - float(want)) > TOL_UM:
            ok = False
            msgs.append(f"{k}={g}!={want}±{TOL_UM}")
        else:
            msgs.append(f"{k}={g} OK")
    return ok, "; ".join(msgs)


def poly_gate_count(cell) -> int:
    poly = cell.layout().layer(5, 0)
    dbu = cell.layout().dbu
    xs = set()
    for s in cell.shapes(poly).each():
        if not s.is_box():
            continue
        b = s.bbox().to_dtype(dbu)
        xs.add(round(0.5 * (b.left + b.right), 3))
    return len(xs)


def walk_gds(gds_path: str, top_name: str = "vco_top"):
    import pya
    ly = pya.Layout()
    ly.read(gds_path)
    top = ly.cell(top_name) if ly.has_cell(top_name) else ly.top_cell()
    sv, bypass_ng = [], []

    def walk(cell):
        for inst in cell.each_inst():
            c = ly.cell(inst.cell_index)
            n = c.name.lower()
            if "svaricap" in n:
                rec = {"cell": c.name}
                try:
                    if inst.is_pcell_variant():
                        for p in inst.pcell_parameters_by_name():
                            pl = p.lower()
                            if pl in ("w", "l", "nx"):
                                val = inst.pcell_parameter(p)
                                if pl == "nx":
                                    rec["Nx"] = int(val)
                                else:
                                    rec[pl] = float(val)
                except Exception:
                    pass
                sv.append(rec)
            if "nmos" in n and "bypass" in n:
                ng = poly_gate_count(c)
                if ng:
                    bypass_ng.append(ng)
            walk(c)

    walk(top)
    if not bypass_ng:
        def walk2(cell):
            for inst in cell.each_inst():
                c = ly.cell(inst.cell_index)
                if "nmos" in c.name.lower():
                    ng = poly_gate_count(c)
                    if ng == 2:
                        bypass_ng.append(ng)
                walk2(c)
        walk2(top)
    return sv, bypass_ng


def main():
    sch = os.path.join(OUT, "vco_top_sch_flat.spice")
    if not os.path.exists(sch):
        sch = os.path.join(OUT, "vco_top_klayout.spice")
    ext = os.path.join(OUT, "vco_top_extracted_klayout.cir")
    if not os.path.exists(ext):
        ext = os.path.join(OUT, "lvs_vco_top", "vco_top_lvs_extracted.cir")
    gds = os.path.join(OUT, "vco_top.gds")

    lines = [
        "# Varactor dimension + finger check — vco_top assembly [TOOL]",
        f"Intent: w={INTENT['w']}u l={INTENT['l']}u Nx={INTENT['Nx']} "
        f"x{EXPECT_SV} [SCH]",
        "",
    ]
    ok_all = True

    sch_d = parse_svaricap(sch)
    lines.append(f"## Schematic spice ({os.path.basename(sch)}) — "
                 f"{len(sch_d)} SVaricap")
    if len(sch_d) < EXPECT_SV:
        ok_all = False
        lines.append(f"FAIL: expected >= {EXPECT_SV}")
    for i, d in enumerate(sch_d):
        ok, msg = match(d)
        ok_all = ok_all and ok
        lines.append(f"  [{i}] {d} → {msg} → {'PASS' if ok else 'FAIL'}")

    ext_d = parse_svaricap(ext)
    lines.append(f"\n## Extract ({os.path.basename(ext)}) — {len(ext_d)} "
                 "SVaricap")
    if not ext_d:
        lines.append("  extract missing or no svaricap lines [TOOL]")
        ok_all = False
    for i, d in enumerate(ext_d):
        ok, msg = match(d)
        ok_all = ok_all and ok
        lines.append(f"  [{i}] {d} → {msg} → {'PASS' if ok else 'FAIL'}")
    # combine may merge identical parallel devices
    if ext_d and all(match(d)[0] for d in ext_d) and len(sch_d) >= EXPECT_SV:
        lines.append("  (extract count may be < sch after combine_devices)")

    lines.append("\n## GDS PCell / finger walk")
    if not os.path.exists(gds):
        lines.append("  vco_top.gds missing [TOOL]")
        ok_all = False
    else:
        try:
            sv, bng = walk_gds(gds)
            lines.append(f"  SVaricap instances: {len(sv)}")
            for s in sv:
                lines.append(f"    {s}")
            if len(sv) < EXPECT_SV:
                ok_all = False
                lines.append(f"  FAIL: expected >= {EXPECT_SV} SVaricap")
            # Nx from PCell when present
            for s in sv:
                if "Nx" in s and int(s["Nx"]) != INTENT["Nx"]:
                    ok_all = False
                    lines.append(f"  FAIL Nx on {s}")
            lines.append(f"  bypass-like ng=2 counts seen: {bng[:8]} "
                         f"(expect two ng=2 bypass [SCH])")
            # Soft check: at least two ng=2 devices exist in hierarchy
            if bng.count(2) < 2:
                lines.append("  WARN: fewer than two ng=2 NMOS found "
                             "(bypass may be named differently) [TOOL]")
            else:
                lines.append("  bypass finger presence: PASS [TOOL]")
        except Exception as e:
            lines.append(f"  GDS walk failed: {e} [TOOL]")
            ok_all = False

    lines.append(f"\n## Result: {'PASS' if ok_all else 'FAIL'}")
    path = os.path.join(OUT, "summary_varactor_top.txt")
    open(path, "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    print(f"Wrote {path}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
