#!/usr/bin/env python3
"""Export SVG/PDF (and optional spice) for each LO .sch via xschem batch.

Run inside hpretl/iic-osic-tools:2026.10 from analog/lo/sch:
  python3 -u export_xschem.py | tee out/summary_export_xsch_lo.txt
"""
from __future__ import annotations

import glob
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
EXP = os.path.join(HERE, "exports")
SIM = os.path.join(HERE, "simulations")


def export_one(sch_path: str) -> dict:
    base = os.path.splitext(os.path.basename(sch_path))[0]
    work = os.path.join(SIM, base)
    os.makedirs(work, exist_ok=True)
    os.makedirs(EXP, exist_ok=True)
    rc = os.path.join(HERE, "xschemrc")
    if os.path.exists(rc):
        shutil.copy(rc, os.path.join(work, "xschemrc"))
    svg = os.path.join(EXP, f"{base}.svg")
    pdf = os.path.join(EXP, f"{base}.pdf")
    spice = os.path.join(work, f"{base}.spice")
    env = os.environ.copy()
    env.setdefault("PDK", "ihp-sg13g2")
    # Netlist
    r1 = subprocess.run(
        ["xschem", "-x", "-q", "-n", sch_path],
        cwd=work, env=env, capture_output=True, text=True,
    )
    # SVG / PDF
    tcl = (
        f"xschem zoom_full; "
        f"xschem print svg {svg}; "
        f"xschem print pdf {pdf}; "
        f"exit"
    )
    r2 = subprocess.run(
        ["xschem", "--command", tcl, sch_path],
        cwd=work, env=env, capture_output=True, text=True,
    )
    # Locate spice if produced
    found = glob.glob(os.path.join(work, "**", "*.spice"), recursive=True)
    if found and not os.path.exists(spice):
        shutil.copy(found[0], spice)
    return dict(
        cell=base,
        net_rc=r1.returncode,
        print_rc=r2.returncode,
        svg=os.path.exists(svg),
        pdf=os.path.exists(pdf),
        spice=os.path.exists(spice) or bool(found),
        err=(r1.stderr or r2.stderr or "")[-400:],
    )


def main():
    os.makedirs(OUT, exist_ok=True)
    schs = sorted(glob.glob(os.path.join(HERE, "*.sch")))
    rows = []
    print("# P2.7.4a2 xschem SVG/PDF export\n")
    print("| sch | spice | svg | pdf | rc |\n|---|---|---|---|---|")
    for p in schs:
        info = export_one(p)
        rows.append(info)
        print(f"| {info['cell']}.sch | "
              f"{'yes' if info['spice'] else 'no'} | "
              f"{'yes' if info['svg'] else 'no'} | "
              f"{'yes' if info['pdf'] else 'no'} | "
              f"net={info['net_rc']} print={info['print_rc']} |")
        if info["err"] and (info["net_rc"] or info["print_rc"]):
            print(f"  err: {info['err'][:200]}")
    text = open(os.path.join(OUT, "summary_export_xsch_lo.txt"), "w")
    # rewrite from printed? just dump rows
    lines = ["# P2.7.4a2 xschem SVG/PDF export\n\n",
             "| sch | spice | svg | pdf | rc |\n|---|---|---|---|---|\n"]
    for info in rows:
        lines.append(
            f"| {info['cell']}.sch | "
            f"{'yes' if info['spice'] else 'no'} | "
            f"{'yes' if info['svg'] else 'no'} | "
            f"{'yes' if info['pdf'] else 'no'} | "
            f"net={info['net_rc']} print={info['print_rc']} |\n"
        )
    open(os.path.join(OUT, "summary_export_xsch_lo.txt"), "w").write(
        "".join(lines))
    ok = all(r["svg"] and r["pdf"] for r in rows)
    print(f"\nExport gate: {'PASS' if ok else 'FAIL'} "
          f"({sum(r['svg'] for r in rows)}/{len(rows)} svg, "
          f"{sum(r['pdf'] for r in rows)}/{len(rows)} pdf)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
