# P2.7.2c vco_top shared LVS setup (KLayout + netgen)
# Source of truth for leaf mappings — do not hand-edit reference netlists.
# Used with: flattened xschem export (vco_top_sch_flat.spice) vs flattened extract.
#
# netgen: source this as the setup file (loads PDK setup first).

# --- PDK base (netgen) ---
if {[info exists ::env(PDK_ROOT)]} {
  set _pdk_setup "$::env(PDK_ROOT)/ihp-sg13g2/libs.tech/netgen/ihp-sg13g2_setup.tcl"
} else {
  set _pdk_setup "/foss/pdks/ihp-sg13g2/libs.tech/netgen/ihp-sg13g2_setup.tcl"
}
if {[file exists $_pdk_setup]} {
  source $_pdk_setup
}

# --- Leaf mappings (identical intent for KLayout + netgen) [decisions 2026-11-18] ---
# 1) SVaricap: schematic model sg13_hv_svaricap_fx → extract sg13_hv_svaricap
#    (flatten_sch_spice.py MODEL_MAP). Pins G1/G2 = cell-local vgp/vgn; well W↔vt.
# 2) Inductor l2n0: omitted from flat LVS sch (same as leaf core spice); layout
#    LVS GDS is pin-only (no spiral / no extract device). Fab GDS keeps spiral.
# 3) Bank LSB b0..b2: schematic cap_cmim; b3+ and dummies rfcmim [GDS].
# 4) Bias R: schematic rhigh (bank 5.0/60.8, core 2/15.2, var 0.5/42.095 b=16,
#    d9 0.5/21.285 b=16) [GDS leaf].
# 5) Unmatched devices: listed in summary_place_compare.txt — never edit netlists
#    to force a match.

# Equate fx model name if both sides appear
catch {equate classes {-circuit1 sg13_hv_svaricap_fx} {-circuit2 sg13_hv_svaricap}}
catch {equate classes {-circuit1 sg13_hv_svaricap} {-circuit2 sg13_hv_svaricap_fx}}

puts "lvs_setup.tcl: vco_top flatten-sch mappings loaded"
