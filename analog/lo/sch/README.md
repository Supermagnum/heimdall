# P2.7.4a2 xschem LO dividers

Generated from step-3 defaults with MOSFET CML tails (nbias TG) and TSPC
Q-only keepers + 100 Meg on a/b (no 1 GOhm). I_latch=0.75 mA, swing via step3, k=1.5.

## Hierarchy

| Cell | Devices | Ports |
|---|---:|---:|
| `lo_bias` | 5 | 5 |
| `lo_uhf_top` | 221 | 14 |
| `lo_vhf_top` | 369 | 19 |

## Remaining test-bench inputs (not on-chip)

| Input | Why |
|---|---|
| `tp`/`tn` | VCO tank or ideal sine (VCO is a separate block) |
| `vbuf`/`vdv`/`vcv`/`vdg`/`vdd` | Split supplies for current metering; on-chip share VR_ANA1 |
| `nbias` | PLL bias generator; TB uses diode+I stand-in |
| `en_lodiv` | D15 sequencer enable |
| `vref` (VHF) | CML NOR reference = V_DD − I·R_L/2 |

## Ideal parts removed vs Python decks

- CML `isource` tails → MOSFET mirrors on `nb_lo`
- TSPC `resistor r=1G` → Q-only weak keepers + 100 Meg on a/b

Exports: `exports/*.svg`, `exports/*.pdf`. Netlists: `netlists/`.
Summaries: `out/summary_*.txt`.
