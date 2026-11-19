#!/usr/bin/env python3
"""P2.7.4a2: hierarchical xschem capture of LO dividers / buffers.

Flat band tops are the LVS / sim source (step-3 + MOSFET tails + keepers).
Leaf cells document the hierarchy in spec/lo-divider-topology.md §10.
"""
from __future__ import annotations

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "analog", "vco", "sch"))

from xsch_lib import Sch, write_sym  # noqa: E402
import circuit as C  # noqa: E402


def place_devs(sch: Sch, devs):
    for d in devs:
        if d.kind == "nmos":
            sch.nmos(d.name, *d.nodes, d.params["w"], d.params["l"],
                     int(d.params.get("ng", 1)), model=d.params["model"])
        elif d.kind == "pmos":
            sch.pmos(d.name, *d.nodes, d.params["w"], d.params["l"],
                     int(d.params.get("ng", 1)), model=d.params["model"])
        elif d.kind == "res":
            sch.res(d.name, d.nodes[0], d.nodes[1], d.params["r"])
        elif d.kind == "capa":
            sch.capa(d.name, d.nodes[0], d.nodes[1], d.params["c"])


def write_from_body(name, ports, body, title=None):
    devs = C.parse_body(body)
    sch = Sch(name, os.path.join(HERE, f"{name}.sch"))
    for p in ports:
        sch.iopin(p)
    sch.title(title or name)
    place_devs(sch, devs)
    sch.write()
    write_sym(os.path.join(HERE, f"{name}.sym"), name, ports)
    C.write_vacask(os.path.join(HERE, "netlists", f"{name}.vacask"),
                   f"P2.7.4a2 {name}", devs)
    return sch, devs


def gen_lo_bias():
    body = C.lo_bias_netlist("vdd")
    return write_from_body(
        "lo_bias", ["nbias", "en_lodiv", "nb_lo", "vdd", "0"], body,
        "lo_bias_nbias_en")


def gen_band(band):
    import re
    body, names, ideal, ndiv, duty = C.build_band_body(band, 1.2)
    # On-chip sch: drop TB-only ideal vref source (pin remains for VHF).
    body = re.sub(r"^vref \(vref 0\) vsource .*\n", "", body, flags=re.M)
    if band == "uhf":
        ports = ["tp", "tn", "nbias", "en_lodiv",
                 "x_p0", "x_p1", "x_p2", "x_p3",
                 "vbuf", "vdv", "vcv", "vdg", "vdd", "0"]
    else:
        ports = ["tp", "tn", "nbias", "en_lodiv", "vref",
                 "x_r1", "x_r2", "x_r3", "x_r4",
                 "x_r1b", "x_r2b", "x_r3b", "x_r4b",
                 "vbuf", "vdv", "vcv", "vdg", "vdd", "0"]
    sch, devs = write_from_body(f"lo_{band}_top", ports, body,
                                f"lo_{band}_top_flat")
    C.write_vacask(os.path.join(HERE, "netlists", f"lo_{band}_flat.vacask"),
                   f"P2.7.4a2 lo_{band} flat", devs)
    return sch, devs, dict(names=names, ideal=ideal, ndiv=ndiv, duty=duty)


def write_xschemrc():
    dst = os.path.join(HERE, "xschemrc")
    vco_rc = os.path.join(REPO, "analog", "vco", "sch", "xschemrc")
    src = "/foss/pdks/ihp-sg13g2/libs.tech/xschem/xschemrc"
    if os.path.exists(src):
        shutil.copy(src, dst)
    elif os.path.exists(vco_rc):
        shutil.copy(vco_rc, dst)
    if os.path.exists(dst):
        txt = open(dst).read()
        if "file dirname [info script]" not in txt[:400]:
            open(dst, "w").write(
                "set XSCHEM_LIBRARY_PATH "
                "[file normalize [file dirname [info script]]]\n"
                "append XSCHEM_LIBRARY_PATH "
                ":$env(PDK_ROOT)/$env(PDK)/libs.tech/xschem\n" + txt
            )


def main():
    os.makedirs(os.path.join(HERE, "netlists"), exist_ok=True)
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    write_xschemrc()
    cells = []
    sch, devs = gen_lo_bias()
    cells.append(("lo_bias", len(devs), len(sch.ports)))
    # Leaf documentation cells: buffer / latch excerpts via band parse counts
    for band in ("uhf", "vhf"):
        sch, devs, meta = gen_band(band)
        cells.append((f"lo_{band}_top", len(devs), len(sch.ports)))

    lines = [
        "# P2.7.4a2 xschem LO divider capture\n\n",
        "Generated from step-3 defaults with MOSFET CML tails (nbias TG) and "
        "TSPC weak Q keepers + 100Meg on a/b (no 1 GOhm). "
        f"I_latch={C.I_LATCH*1e3:g} mA, swing via step3, k={C.K_REGEN:g}.\n\n",
        "## Hierarchy\n\n| Cell | Devices | Ports |\n|---|---:|---:|\n",
    ]
    for n, nd, np_ in cells:
        lines.append(f"| `{n}` | {nd} | {np_} |\n")
    lines += [
        "\n## Remaining test-bench inputs (not on-chip)\n\n",
        "| Input | Why |\n|---|---|\n",
        "| `tp`/`tn` | VCO tank or ideal sine (VCO is a separate block) |\n",
        "| `vbuf`/`vdv`/`vcv`/`vdg`/`vdd` | Split supplies for current metering; "
        "on-chip share VR_ANA1 |\n",
        "| `nbias` | PLL bias generator; TB uses diode+I stand-in |\n",
        "| `en_lodiv` | D15 sequencer enable |\n",
        "| `vref` (VHF) | CML NOR reference = V_DD − I·R_L/2 |\n",
        "\n## Ideal parts removed vs Python decks\n\n",
        "- CML `isource` tails → MOSFET mirrors on `nb_lo`\n",
        "- TSPC `resistor r=1G` → weak Q keepers + 100Meg on a/b\n",
        "\nExports: `exports/*.svg`, `exports/*.pdf`. Netlists: `netlists/`.\n",
    ]
    summary = "".join(lines)
    open(os.path.join(HERE, "out", "summary_xsch_lo.txt"), "w").write(summary)
    open(os.path.join(HERE, "README.md"), "w").write(
        "# P2.7.4a2 xschem LO dividers\n\n" + summary.split("\n", 2)[-1])
    print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
