#!/usr/bin/env python3
"""P2.7.2c vco_top — DRC + KLayout LVS + netgen for a named cell."""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
PDK_DRC = "/foss/pdks/ihp-sg13g2/libs.tech/klayout/tech/drc/run_drc.py"
PDK_LVS = "/foss/pdks/ihp-sg13g2/libs.tech/klayout/tech/lvs/run_lvs.py"
NETGEN_SETUP_PDK = "/foss/pdks/ihp-sg13g2/libs.tech/netgen/ihp-sg13g2_setup.tcl"
# Shared leaf mappings (SVaricap, l2n0 black-box notes) — sources PDK setup [decisions]
NETGEN_SETUP = os.path.join(HERE, "lvs_setup.tcl")
# Sign-off reference: flattened xschem vco_top.sch (not leaf-assembled spice)
SCH_FLAT = os.path.join(OUT, "vco_top_sch_flat.spice")
DENSITY = {"AFil.g", "GFil.g", "M1.j", "M2.j", "M3.j", "M4.j", "M5.j", "M5.k",
           "TM1.c", "TM2.c", "TM1.d", "TM2.d"}
# SVaricap PCell M1.b waived at block level (vco_var); same at top [decisions]
SVARICAP_M1B = {"M1.b"}
# SG13G2 drawn grid — absolute W/L snap for MIM compare [DS / decisions 2026-11-18]
PDK_GRID_UM = 0.01


def _len_to_um(token: str) -> float | None:
    """Parse spice length token to µm (supports 7.87u, 7.874e-06, bare µm)."""
    s = token.strip().rstrip(",")
    if not s:
        return None
    try:
        if s[-1] in "uU" and s[:-1]:
            return float(s[:-1])
        if s[-1] in "nN" and s[:-1]:
            return float(s[:-1]) * 1e-3
        v = float(s)
    except ValueError:
        return None
    # meters if tiny; already µm if around drawn sizes
    if abs(v) < 1e-3:
        return v * 1e6
    return v


def _fmt_len(um: float, style: str) -> str:
    """style='u' → 7.87u; style='m' → 7.870000e-06."""
    g = PDK_GRID_UM
    um = round(um / g) * g
    # avoid float dust (7.8700000001)
    um = round(um, 4)
    if style == "u":
        return f"{um:g}u"
    return f"{um * 1e-6:.6e}"


def strip_extract_only_rhigh_ps(txt: str) -> str:
    """Drop rhigh ps= (poly end-cap) — extract-only; sch has 0 [TOOL/PDK].

    Bent rhigh (b=16) extract reports ps≈0.18 µm; schematic omits it. That
    MatchWithWarning on the device soft-fails the attached nets in KLayout.
    """
    out = []
    for ln in txt.splitlines():
        if " rhigh " in f" {ln.lower()} " or ln.lower().endswith(" rhigh"):
            ln = re.sub(r"\bps=[^\s]+", "", ln, flags=re.I)
            ln = re.sub(r"  +", " ", ln).rstrip()
        out.append(ln)
    return "\n".join(out) + ("\n" if txt.endswith("\n") else "")


def snap_mim_to_pdk_grid(txt: str) -> str:
    """Round MIM w/l to PDK grid and rebuild A/P for KLayout primary params [DS].

    Schematic often keeps ideal sizes (e.g. 7.874 µm) while extract snaps to
    0.01 µm (7.87). DeviceCustomMIM compares primary A/P exactly, so grid
    deltas leave RFCMIM unpaired. Apply the same snap on both netlists.
    """
    def repl_line(ln: str) -> str:
        ll = f" {ln.lower()} "
        if "rfcmim" not in ll and "cap_cmim" not in ll:
            return ln
        wm = re.search(r"\bw=([^\s]+)", ln, re.I)
        lm = re.search(r"\bl=([^\s]+)", ln, re.I)
        if not wm or not lm:
            return ln
        wu = _len_to_um(wm.group(1))
        lu = _len_to_um(lm.group(1))
        if wu is None or lu is None:
            return ln
        style = "u" if wm.group(1).rstrip(",").endswith(("u", "U")) else "m"
        w_s = _fmt_len(wu, style)
        l_s = _fmt_len(lu, style)
        wu2 = _len_to_um(w_s)
        lu2 = _len_to_um(l_s)
        assert wu2 is not None and lu2 is not None
        a_um2 = wu2 * lu2
        p_um = 2.0 * (wu2 + lu2)
        ln2 = re.sub(r"\bw=[^\s]+", f"w={w_s}", ln, count=1, flags=re.I)
        ln2 = re.sub(r"\bl=[^\s]+", f"l={l_s}", ln2, count=1, flags=re.I)
        # Always rewrite A/P from snapped w/l. Extract often truncates A
        # (11.12^2 → 123.654 vs 123.6544); :g would re-truncate [TOOL].
        a_tok = (f"{a_um2:.6f}".rstrip("0").rstrip(".") + "p") if style == "u" \
            else f"{a_um2 * 1e-12:.12e}"
        p_tok = (f"{p_um:.6f}".rstrip("0").rstrip(".") + "u") if style == "u" \
            else f"{p_um * 1e-6:.12e}"
        if re.search(r"\bA=", ln2, re.I):
            ln2 = re.sub(r"\bA=[^\s]+", f"A={a_tok}", ln2, count=1, flags=re.I)
        else:
            ln2 = ln2.rstrip() + f" A={a_tok}"
        if re.search(r"\bP=", ln2, re.I):
            ln2 = re.sub(r"\bP=[^\s]+", f"P={p_tok}", ln2, count=1, flags=re.I)
        else:
            ln2 = ln2.rstrip() + f" P={p_tok}"
        return ln2

    out = [repl_line(ln) for ln in txt.splitlines()]
    return "\n".join(out) + ("\n" if txt.endswith("\n") else "")


def run(cmd, log, timeout=3600):
    print("+", " ".join(cmd), flush=True)
    with open(log, "w") as fh:
        r = subprocess.run(cmd, stdout=fh, stderr=subprocess.STDOUT, timeout=timeout)
    print(f"  exit {r.returncode}; log {log}", flush=True)
    return r.returncode


def parse_violated(log_path):
    txt = open(log_path, errors="ignore").read()
    m = re.search(r"Violated rules are : (\{[^}]+\})", txt)
    if not m:
        return set()
    return set(re.findall(r"'([^']+)'", m.group(1)))


def render(cell):
    py = os.path.join(OUT, f"_klayout_shot_{cell}.py")
    open(py, "w").write(r'''
import pya, os
gds = os.path.join(out, name + ".gds")
ly = pya.Layout(); ly.read(gds)
bb = ly.top_cell().bbox()
lv = pya.LayoutView()
lv.show_layout(ly, False)
lv.max_hier()
lv.zoom_fit()
png = os.path.join(out, name + ".png")
try:
    lv.save_image(png, 1600, 1200)
except Exception as e:
    open(os.path.join(out, name + "_png_err.txt"), "w").write(str(e))
w = max(bb.width(), 1); h = max(bb.height(), 1)
scale = min(780.0 / w, 560.0 / h)
ow, oh = w * scale, h * scale
open(os.path.join(out, name + ".svg"), "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600">'
    f'<rect x="10" y="20" width="{ow:.1f}" height="{oh:.1f}" '
    f'fill="none" stroke="black" stroke-width="1"/>'
    f'<text x="10" y="14" font-size="12">{name} bbox {bb} dbu</text>'
    f'</svg>\n')
print("rendered", name, "bbox", bb)
''')
    run(["klayout", "-b", "-r", py, "-rd", f"out={OUT}", "-rd", f"name={cell}"],
        os.path.join(OUT, f"render_{cell}.log"), timeout=120)


def prove(cell: str) -> dict:
    gds = os.path.join(OUT, f"{cell}.gds")  # fab (spiral) — DRC
    gds_lvs = os.path.join(OUT, f"{cell}_lvs.gds")  # pin-only inductor — LVS
    if not os.path.exists(gds_lvs):
        gds_lvs = gds
    # Prefer flattened sch export for vco_top; else cell.spice [decisions 2026-11-18]
    spice = SCH_FLAT if (cell == "vco_top" and os.path.exists(SCH_FLAT)) \
        else os.path.join(OUT, f"{cell}.spice")
    res = {"cell": cell, "gds_lvs": gds_lvs, "spice": spice}
    print(f"  LVS netlist={os.path.basename(spice)}", flush=True)
    drc_dir = os.path.join(OUT, f"drc_{cell}")
    os.makedirs(drc_dir, exist_ok=True)
    res["drc"] = run([
        "python3", PDK_DRC, f"--path={gds}", f"--topcell={cell}",
        "--minimum_drc", f"--run_dir={drc_dir}", "--mp=2",
    ], os.path.join(OUT, f"drc_{cell}.log"))
    res["drc_rules"] = parse_violated(os.path.join(OUT, f"drc_{cell}.log"))
    res["drc_non_density"] = sorted(res["drc_rules"] - DENSITY)
    leftover = set(res["drc_non_density"]) - SVARICAP_M1B
    res["drc_svaricap_m1b"] = "M1.b" in res["drc_non_density"]
    res["drc_clean"] = len(leftover) == 0

    lvs_dir = os.path.join(OUT, f"lvs_{cell}")
    os.makedirs(lvs_dir, exist_ok=True)
    # PDK run_lvs names the log from the layout basename (vco_top_lvs.gds →
    # vco_top_lvs.log), not always {topcell}.log [TOOL].
    gds_stem = os.path.splitext(os.path.basename(gds_lvs))[0]
    cell_logs = [
        os.path.join(lvs_dir, f"{gds_stem}.log"),
        os.path.join(lvs_dir, f"{cell}.log"),
    ]
    for cell_log in cell_logs:
        if os.path.exists(cell_log):
            open(cell_log, "w").close()
    # Cumulative compare log retains old ERROR lines; clear before this run [TOOL]
    dummy_log = os.path.join(lvs_dir, "__layout_netlist_dummy__.log")
    if os.path.exists(dummy_log):
        open(dummy_log, "w").close()
    # KLayout spice reader uppercases model names (rfcmim→RFCMIM) while GDS
    # extract keeps lowercase → false class splits [TOOL]. Fix: extract once,
    # then compare both sides as spice (--layout_netlist) so the reader
    # normalizes case on both. Also snap MIM w/l to PDK grid 0.01 µm [DS].
    def for_klayout_sch(txt: str) -> str:
        txt = txt.replace(" cap_rfcmim ", " rfcmim ")
        out = []
        for ln in txt.splitlines():
            s = ln.lstrip()
            if s.startswith("X") and " sg13_hv_svaricap " in f" {s} ":
                i = len(ln) - len(s)
                ln = ln[:i] + "C" + s[1:]
            # rhigh A/B are physically symmetric; extract port order can
            # oppose the schematic. Swap var bias R ends to match GDS extract
            # (vvb first) so KLayout net xref does not soft-fail [TOOL/GDS].
            if s.startswith("R") and " rhigh " in f" {s} ":
                parts = s.split()
                # Rname n1 n2 sub rhigh ...
                if len(parts) >= 5 and parts[3].lower() == "gnd" and \
                        parts[1].lower().startswith("var_vg") and \
                        parts[2].lower() == "var_vvb":
                    parts[1], parts[2] = parts[2], parts[1]
                    pad = ln[:len(ln) - len(s)]
                    ln = pad + " ".join(parts)
            out.append(ln)
        return strip_extract_only_rhigh_ps(snap_mim_to_pdk_grid(
            "\n".join(out) + ("\n" if txt.endswith("\n") else "")))

    spice_kl = spice
    if cell == "vco_top" and os.path.exists(spice):
        spice_kl = os.path.join(OUT, f"{cell}_klayout.spice")
        open(spice_kl, "w").write(for_klayout_sch(open(spice).read()))
        res["spice_klayout"] = spice_kl
        res["pdk_grid_um"] = PDK_GRID_UM

    # 1) extract-only from pin-only inductor GDS [TOOL]
    res["klayout_extract"] = run([
        "python3", PDK_LVS, f"--layout={gds_lvs}", f"--netlist={spice_kl}",
        f"--topcell={cell}", f"--run_dir={lvs_dir}",
        "--disable_tap_extraction", "--ignore_top_ports_mismatch",
        "--combine_devices", "--top_lvl_pins", "--net_only",
    ], os.path.join(OUT, f"lvs_klayout_{cell}_extract.log"))
    print(f"  LVS layout={os.path.basename(gds_lvs)}", flush=True)

    ext = None
    for root, _, files in os.walk(lvs_dir):
        for f in files:
            if f.endswith("_extracted.cir"):
                # Prefer pin-only stem
                path = os.path.join(root, f)
                if ext is None or gds_stem in f:
                    ext = path
    res["extracted"] = ext

    # Snap extract MIM to the same PDK grid; drop extract-only rhigh ps [DS/TOOL]
    ext_kl = ext
    if ext and os.path.exists(ext) and cell == "vco_top":
        ext_kl = os.path.join(OUT, f"{cell}_extracted_klayout.cir")
        open(ext_kl, "w").write(strip_extract_only_rhigh_ps(
            snap_mim_to_pdk_grid(open(ext).read())))
        res["extracted_klayout"] = ext_kl

    # 2) compare: both netlists through spice reader (case + grid) [TOOL]
    res["klayout_pass"] = False
    if ext_kl and os.path.exists(ext_kl):
        res["klayout_lvs"] = run([
            "python3", PDK_LVS, f"--layout_netlist={ext_kl}",
            f"--netlist={spice_kl}", f"--topcell={cell}",
            f"--run_dir={lvs_dir}",
            "--disable_tap_extraction", "--ignore_top_ports_mismatch",
            "--combine_devices", "--top_lvl_pins",
        ], os.path.join(OUT, f"lvs_klayout_{cell}.log"))
        # PDK appends to __layout_netlist_dummy__.log across runs and then
        # reprints old ERROR lines in the summary *after* a new PASS — so
        # rfind(ERROR) alone false-fails. Prefer the Status table; fall back
        # to Congratulations vs ERROR only in the compare-phase slice [TOOL].
        wrap = open(os.path.join(OUT, f"lvs_klayout_{cell}.log"),
                    errors="ignore").read()
        kl_cell = ""
        for cell_log in cell_logs:
            if os.path.exists(cell_log):
                txt = open(cell_log, errors="ignore").read()
                if txt.strip():
                    kl_cell = txt
                    break
        blob = wrap if wrap.strip() else kl_cell
        st_pass = blob.rfind("| Status           | PASS")
        st_fail = blob.rfind("| Status           | FAIL")
        if st_pass >= 0 or st_fail >= 0:
            res["klayout_pass"] = st_pass > st_fail
        else:
            last_ok = blob.rfind("Congratulations! Netlists match")
            last_bad = blob.rfind("ERROR : Netlists don't match")
            res["klayout_pass"] = last_ok > last_bad and last_ok >= 0
    else:
        res["klayout_lvs"] = None
    res["netgen_pass"] = False
    res["netgen"] = None
    ng_setup = NETGEN_SETUP if os.path.exists(NETGEN_SETUP) else NETGEN_SETUP_PDK
    if ext and os.path.exists(ng_setup):
        # rfcmim extract uses C-prefix + name "rfcmim"; netgen setup wants
        # cap_rfcmim and X-prefix for 3-terminal devices [PDK / assemble].
        def for_netgen(txt: str) -> str:
            txt = txt.replace(" rfcmim ", " cap_rfcmim ")
            txt = txt.replace(" cmim ", " cap_cmim ")
            out = []
            for ln in txt.splitlines():
                s = ln.lstrip()
                # C-prefix 3-terminal (rfcmim / svaricap) and R-prefix rhigh
                # need X-prefix for netgen multi-terminal parse [PDK]
                if ((s.startswith("C") and (
                        " cap_rfcmim " in f" {s} " or
                        " cap_cmim " in f" {s} " or
                        " sg13_hv_svaricap " in f" {s} ")) or
                        (s.startswith("R") and " rhigh " in f" {s} ")):
                    i = len(ln) - len(s)
                    ln = ln[:i] + "X" + s[1:]
                out.append(ln)
            return "\n".join(out) + ("\n" if txt.endswith("\n") else "")

        spice_ng = os.path.join(OUT, f"{cell}_netgen.spice")
        ext_ng = os.path.join(OUT, f"{cell}_extracted_netgen.cir")
        open(spice_ng, "w").write(for_netgen(open(spice).read()))
        open(ext_ng, "w").write(for_netgen(open(ext).read()))
        tcl = os.path.join(OUT, f"netgen_{cell}.tcl")
        json_out = os.path.join(OUT, f"netgen_{cell}.json")
        open(tcl, "w").write(
            f'lvs {{{spice_ng} {cell}}} {{{ext_ng} {cell}}} '
            f'{ng_setup} {json_out}\n')
        res["netgen"] = run(
            ["netgen", "-batch", "source", tcl],
            os.path.join(OUT, f"netgen_{cell}.log"), timeout=600)
        ng = open(os.path.join(OUT, f"netgen_{cell}.log"), errors="ignore").read()
        res["netgen_pass"] = "Circuits match uniquely" in ng or \
            "Final result: Circuits match" in ng

    try:
        render(cell)
    except Exception as e:
        print(f"  render fail: {e}")
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cell", required=True)
    args = ap.parse_args()
    r = prove(args.cell)
    print("\n# Summary")
    print(f"cell={r['cell']}")
    print(f"DRC clean (density waived): {r['drc_clean']}  "
          f"non-density={r['drc_non_density']} "
          f"svaricap_M1.b={r.get('drc_svaricap_m1b')}")
    print(f"KLayout LVS: {'PASS' if r['klayout_pass'] else 'FAIL'}")
    print(f"netgen: {'PASS' if r['netgen_pass'] else 'FAIL'}")
    open(os.path.join(OUT, f"summary_prove_{args.cell}.txt"), "w").write(
        f"drc_clean={r['drc_clean']} non_density={r['drc_non_density']} "
        f"svaricap_M1.b={r.get('drc_svaricap_m1b')}\n"
        f"klayout={r['klayout_pass']} netgen={r['netgen_pass']}\n"
        f"lvs_gds={os.path.basename(r.get('gds_lvs') or '')}\n"
        f"spice={os.path.basename(r.get('spice') or '')}\n"
    )
    ok = r["drc_clean"] and r["klayout_pass"] and r["netgen_pass"]
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
