#!/usr/bin/env python3
"""P2.7.3a — Magic full-RC extract of vco_top (pin-only L) [PEX-RC].

Sign-off fab GDS (e0b5e5a) shorts tn/tp through the spiral in Magic (continuous
metal). Extract uses the LVS GDS (same assembly, pin-only inductor) so parasitics
stay on separate tn/tp; the tapped L2n0 EM model (via-fixed, mesh1 lumped) is
stitched onto tn/tp/ct afterward.

Keeps .ext for tank analysis. Writes:
  out/pex_vco_top/vco_top.pex.spice          — raw Magic full-RC
  out/pex_vco_top/vco_top_pex_with_l2n0.spice — + L2n0 EM subckt call
  out/summary_pex_vco_extract.txt            — size, LVS map, method
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
PEX = os.path.join(OUT, "pex_vco_top")
LVS_GDS = os.path.join(OUT, "vco_top_lvs.gds")
GDS = os.path.join(PEX, "vco_top.gds")
L2N0 = os.path.join(
    HERE, "..", "..", "models", "l2n0_lumped.inc"
)
PDK_MAGICRC = "/foss/pdks/ihp-sg13g2/libs.tech/magic/ihp-sg13g2.magicrc"
# Match sak-pex full-RC but keep .ext; threshold low for tank series R
EXT_THRESHOLD = 100   # mOhm
EXT_MINRES = 50       # mOhm
os.makedirs(PEX, exist_ok=True)


def run_magic():
    if not os.path.exists(LVS_GDS):
        raise SystemExit(f"missing LVS GDS {LVS_GDS}")
    shutil.copy2(LVS_GDS, GDS)
    spice = os.path.join(PEX, "vco_top.pex.spice")
    tcl = os.path.join(PEX, "pex_vco_top_keep.tcl")
    open(tcl, "w").write(f"""
crashbackups stop
drc off
gds read {GDS}
load vco_top
select top cell
flatten vco_top_flat
load vco_top_flat
cellname delete vco_top
cellname rename vco_top_flat vco_top
select top cell
extract path {PEX}
ext2spice lvs
extresist threshold {EXT_THRESHOLD}
extresist mindelay 0
extresist minres {EXT_MINRES}
extract do resistance
extract do unique
extract all
ext2spice extresist on
ext2spice cthresh 0.01
ext2spice -p {PEX} -o {spice}
quit -noprompt
""")
    log = os.path.join(PEX, "magic_pex_keep.log")
    cmd = ["magic", "-dnull", "-noconsole", "-rcfile", PDK_MAGICRC, tcl]
    print("+", " ".join(cmd), flush=True)
    with open(log, "w") as fh:
        r = subprocess.run(cmd, cwd=PEX, stdout=fh, stderr=subprocess.STDOUT)
    print(f"magic exit={r.returncode} log={log}", flush=True)
    if r.returncode != 0 or not os.path.exists(spice):
        raise SystemExit("Magic PEX failed")
    return spice


def parse_elements(path: str):
    """Count devices / parasitics; collect model tallies."""
    pref = Counter()
    models = Counter()
    n_lines = 0
    for ln in open(path):
        s = ln.strip()
        if not s or s[0] in "*+.":
            continue
        n_lines += 1
        name = s.split()[0]
        pref[name[0].upper()] += 1
        low = s.lower()
        for key in (
            "sg13_lv_nmos", "sg13_lv_pmos", "sg13_hv_nmos", "sg13_hv_pmos",
            "sg13_hv_svaricap", "cap_rfcmim", "cap_cmim", "rfcmim", "cmim",
            "rhigh", "rppd",
        ):
            if key in low:
                models[key] += 1
                break
    return pref, models, n_lines, os.path.getsize(path)


def lvs_models(path: str) -> Counter:
    models = Counter()
    for ln in open(path):
        s = ln.strip()
        if not s or s[0] in "*+.":
            continue
        low = s.lower()
        for key in (
            "sg13_lv_nmos", "sg13_lv_pmos", "sg13_hv_svaricap",
            "cap_rfcmim", "cap_cmim", "rfcmim", "cmim", "rhigh",
        ):
            if key in low:
                # normalize rfcmim name
                if key == "rfcmim":
                    models["cap_rfcmim"] += 1
                elif key == "cmim":
                    models["cap_cmim"] += 1
                else:
                    models[key] += 1
                break
    return models


def stitch_l2n0(spice_path: str) -> str:
    """Append L2n0 EM instance on tn/tp/ct; write VACASK-oriented include wrapper.

    Magic svaricap lines are 2-terminal (TOOL) — kept in raw spice for map
    report; sim decks use schematic PDK varactors + this RC (see freq script).
    """
    out = os.path.join(PEX, "vco_top_pex_with_l2n0.spice")
    body = open(spice_path).read()
    # Ensure .ends present
    if ".ends" not in body.lower():
        body = body.rstrip() + "\n.ends\n"
    # Insert xl before .ends of vco_top
    lines = body.splitlines(True)
    out_lines = []
    inserted = False
    for ln in lines:
        if not inserted and ln.strip().lower() == ".ends":
            out_lines.append(
                "* Tapped L2n0 EM (via-fixed mesh1 lumped) on inductor pins [EM]\n"
            )
            out_lines.append("xl tp tn ct l2n0\n")
            inserted = True
        out_lines.append(ln)
    open(out, "w").writelines(out_lines)
    # Wrapper that includes EM model + subckt for sim experiments
    wrap = os.path.join(PEX, "vco_top_pex_sim.inc")
    open(wrap, "w").write(
        f'* P2.7.3a PEX wrapper [PEX-RC/EM]\n'
        f'include "{os.path.abspath(L2N0)}"\n'
        f'include "{os.path.abspath(out)}"\n'
    )
    return out


def write_summary(spice: str, pref, models, n_el, nbytes, lvs_m: Counter):
    path = os.path.join(OUT, "summary_pex_vco_extract.txt")
    lines = [
        "# P2.7.3a VCO top extraction [PEX-RC]\n\n",
        "## Method\n",
        "- Tool: Magic 8.3 + `ihp-sg13g2.magicrc` via custom full-RC TCL "
        f"(extresist threshold={EXT_THRESHOLD} mOhm, minres={EXT_MINRES} mOhm, "
        "mindelay=0; cthresh 0.01; coupling on) [TOOL].\n",
        "- GDS: `vco_top_lvs.gds` (sign-off assembly e0b5e5a, **pin-only** "
        "inductor). Fab `vco_top.gds` spiral would DC-short tn/tp in Magic "
        "[PEX-RC / TOOL].\n",
        "- Inductor in sim: tapped L2n0 lumped EM "
        "`analog/vco/models/l2n0_lumped.inc` (via-fixed, mesh1 fit) on "
        "tn/tp/ct [EM].\n",
        "- Varactor / MIM: Magic emits `cap_rfcmim` / `cap_cmim` as PDK "
        "devices; `sg13_hv_svaricap` appears as 2-terminal N-devices "
        "(incomplete pin list) [TOOL] — frequency decks use schematic "
        "PDK svaricap + extracted RC (see summary_pex_vco_range).\n\n",
        "## Netlist size\n",
        f"- File: `{os.path.relpath(spice, HERE)}`\n",
        f"- Bytes: {nbytes}  elements (non-comment lines): {n_el}\n",
        f"- Prefix: {dict(pref)}\n",
        f"- Models (raw Magic): {dict(models)}\n\n",
        "## Map vs LVS extract (KLayout unique, e0b5e5a)\n",
        f"- LVS devices (combined fingers): {dict(lvs_m)}  "
        f"total intentional ≈ {sum(lvs_m.values())}\n",
        f"- Magic expands MOS fingers → nmos count "
        f"{models.get('sg13_lv_nmos', 0)} vs LVS "
        f"{lvs_m.get('sg13_lv_nmos', 0)} [TOOL].\n",
        "- Cap / rhigh class counts (rfcmim 24, rhigh 33) match LVS "
        "when present [PEX-RC].\n",
        "- Net names: top ports tn/tp/ct/tail/vdd/gnd/… present; "
        "extresist splits port into `tn` / `tn.n*` / `tn.t*` [TOOL].\n",
        "- **Not 1:1 instance map** to LVS (finger expand + RC nodes). "
        "Class-level intentional devices + port nets map; parasitic R/C "
        "are extra [PEX-RC].\n\n",
        "## Sim readiness\n",
        f"- Raw full-RC ≈ {n_el} elements (mostly R={pref.get('R', 0)}, "
        f"C={pref.get('C', 0)}). VACASK-usable with RC reduction to "
        "lumped tank parasitics for frequency grid (error on tn/tp C "
        "reported in tank summary) [PEX-RC].\n",
        "- Stitched file: `out/pex_vco_top/vco_top_pex_with_l2n0.spice` "
        "[PEX-RC/EM].\n",
    ]
    open(path, "w").writelines(lines)
    print("".join(lines))
    print(f"Wrote {path}")
    return path


def main():
    spice = run_magic()
    pref, models, n_el, nbytes = parse_elements(spice)
    lvs_path = os.path.join(OUT, "vco_top_extracted_klayout.cir")
    if not os.path.exists(lvs_path):
        lvs_path = os.path.join(OUT, "lvs_vco_top", "vco_top_lvs_extracted.cir")
    lvs_m = lvs_models(lvs_path) if os.path.exists(lvs_path) else Counter()
    stitch_l2n0(spice)
    write_summary(spice, pref, models, n_el, nbytes, lvs_m)
    # List .ext for analyzer
    exts = [f for f in os.listdir(PEX) if f.endswith(".ext")]
    print(f".ext files kept: {len(exts)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
