#!/usr/bin/env python3
"""Divider wiring-C method (decisions 2026-11-20) [PEX-RC].

Headline per net:
  C_wiring = substrate/node C + sum(coupling to other nets)
           = wire-to-substrate + coupling.

Device gate / junction C is carried by PDK MOSFET models in the schematic
and is **not** added here. Magic device recognition keeps intrinsic Cgg/Cj
in the device; the `.ext` node C + `cap` lines are interconnect.

VCO bank previously dropped substrate node C because it was mixed with MIM
plate area. Divider cells have no MIM, so the substrate term stays.

Units: Magic `.ext` aF / 1000 = fF.
"""
from __future__ import annotations

from collections import defaultdict


def to_ff(af: float) -> float:
    return af / 1000.0


def parse_ext(path: str, port_pref: tuple[str, ...]):
    parent: dict[str, str] = {}

    def find(a: str) -> str:
        parent.setdefault(a, a)
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def rank(n: str) -> int:
        if n in port_pref:
            return port_pref.index(n)
        return 100 + len(n)

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank(rb) < rank(ra):
            ra, rb = rb, ra
        parent[rb] = ra

    node_c: dict[str, float] = {}
    caps: list[tuple[str, str, float]] = []
    substrate_names: set[str] = set()
    ports: set[str] = set()
    for ln in open(path):
        toks = ln.split()
        if not toks:
            continue
        if toks[0] == "node" and len(toks) >= 4:
            name = toks[1].strip('"')
            try:
                c = float(toks[3])
            except ValueError:
                continue
            node_c[name] = node_c.get(name, 0.0) + c
        elif toks[0] == "substrate" and len(toks) >= 4:
            # Magic substrate ref: C to substrate is 0 on this node; other
            # nodes' node-C includes C to this name [PEX-RC].
            name = toks[1].strip('"')
            substrate_names.add(name)
            try:
                c = float(toks[3])
            except ValueError:
                c = 0.0
            node_c[name] = node_c.get(name, 0.0) + c
        elif toks[0] == "port" and len(toks) >= 2:
            ports.add(toks[1].strip('"'))
        elif toks[0] in ("merge", "equiv") and len(toks) >= 3:
            union(toks[1].strip('"'), toks[2].strip('"'))
        elif toks[0] == "cap" and len(toks) >= 4:
            caps.append((toks[1].strip('"'), toks[2].strip('"'),
                         float(toks[3])))
    return find, node_c, caps, substrate_names, ports


def wiring_per_net(ext_path: str, interest: tuple[str, ...],
                   port_pref: tuple[str, ...] | None = None,
                   alias: dict[str, str] | None = None) -> dict:
    """Return per-net sub/coup/all (= wiring) in fF.

    alias maps logical name -> .ext root (e.g. ta -> a_n5476_0#).

    If a port (typically gnd) is Magic's substrate reference, its own node C
    is 0; C from other nets to it lives in those nets' substrate terms. We
    then set that port's coupling = sum of the other interest nets' substrate
    C so the row is non-zero and assembly-usable [PEX-RC].
    """
    pref = port_pref or interest + ("vdd", "gnd", "sub!", "0")
    find, node_c, caps, substrate_names, ports = parse_ext(ext_path, pref)
    alias = dict(alias or {})
    for p in interest:
        alias.setdefault(p, p)
    roots = {p: find(alias[p]) for p in interest}

    sub: dict[str, float] = defaultdict(float)
    for n, c in node_c.items():
        r = find(n)
        for p, root in roots.items():
            if r == root:
                sub[p] += c

    coup: dict[str, dict[str, float]] = {p: defaultdict(float) for p in interest}
    for a, b, c in caps:
        ra, rb = find(a), find(b)
        if ra == rb:
            continue
        for p, root in roots.items():
            if ra == root:
                coup[p][rb] += c
            elif rb == root:
                coup[p][ra] += c

    # Ports that Magic declared as substrate (or equiv to one)
    sub_roots = {find(n) for n in substrate_names}
    rows = {}
    for p in interest:
        coup_sum = sum(coup[p].values())
        note = ""
        sub_af = sub[p]
        if find(alias[p]) in sub_roots:
            # Bound as substrate ref: recover C-to-this-net from others' sub
            for q in interest:
                if q == p:
                    continue
                if sub[q] > 0:
                    coup[p][f"{q}(sub)"] += sub[q]
            coup_sum = sum(coup[p].values())
            sub_af = 0.0
            note = "substrate_ref"
        rows[p] = {
            "ext_name": alias[p],
            "sub_ff": round(to_ff(sub_af), 4),
            "coup_ff": round(to_ff(coup_sum), 4),
            "wire_ff": round(to_ff(sub_af + coup_sum), 4),
            "bound": alias[p] in ports or p in ports or find(alias[p]) in sub_roots,
            "note": note,
            "top_partners": [
                (k, round(to_ff(v), 4))
                for k, v in sorted(coup[p].items(), key=lambda x: -abs(x[1]))[:12]
            ],
        }
    return rows


METHOD_BLURB = (
    "- **Wiring C** = substrate/node C + coupling to other nets "
    "(wire-to-substrate + coupling). Device gate/junction C stays in PDK "
    "MOSFET models and is excluded [PEX-RC / decisions 2026-11-20].\n"
    "- If Magic declares a port as `substrate` (typical for gnd+ptap), that "
    "port's node C is 0 by definition; its wiring C is recovered as the sum "
    "of other interest nets' substrate terms (C to that ref) [PEX-RC].\n"
    "- Units: Magic `.ext` aF / 1000 = fF. `extresist` not run unless noted "
    "[TOOL].\n"
)
