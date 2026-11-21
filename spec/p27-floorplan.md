# P2.7 synthesizer floorplan memo

Status: **D23 accepted (Option A), 2026-11-11** (`decisions.md`). Companion plan: `spec/p27-layout-notes.md` § Plan. Die context: SX1255-compatible MLPQ-W 5 × 5 mm, 32 leads (`spec/rf-frontend.md` §2); digital back end `phase1l` **339 617 µm²** of 340 000 (`decisions.md` 2026-10-19). Pin 3 = **VR_ANA1** (D21).

---

## 1. Constraints that drive placement

| Constraint | Number / rule | Source |
|---|---|---|
| Digital already placed | 339 617 µm²; no area left in back end | `[SCH]` phase1l |
| AFE/LO control (D3) | Separate small digital island next to PLL (MMD, Σ-Δ, bandcal, lockdet, afe_seq) | D3 |
| VR_ANA1 | Pin 3; LDO → 10 Ω → pad → 100 nF; VCO+LO+CP from **pad** side | D21 |
| Loop-filter MOS | C1 30.8 + C2 465 pF ≈ **0.062 mm²** | D19 `[HAND]` |
| LDO Cg | 100 pF ≈ **0.0125 mm²** MOS preferred | D21 / `p27-layout-notes` |
| Tank inductor | Tapped L2n0; keep clear of digital and CP switching | `[EM]` tapped |
| LO RF path | Short VCO → buffer → CML ÷N; retimed CMOS toward mixer (Phase 3) | P2.4 |
| Coupling target | Raw ≤ **−35 dBc** VHF / **−15 dBc** UHF at VCO before the loop | `pll-topology` §13 |
| Local GHz bypass | MIM/MOS at VCO CT and each CML/TSPC supply tap | D21 layout note |

Die aspect for this memo: assume a ~**1.6 × 1.6 mm** active core inside the 5 × 5 package (typical for this class) `[HAND]`; exact die size is Phase 5. Coordinates below are relative: N = pin-1/3 edge (VR_ANA1 / VR_PA), S = RF_IN / RF_OP edge (pins 27–30), E/W = remaining pad sides.

---

## 2. Area sketch for the synthesizer island `[HAND]`

| Block | Area | Notes |
|---|---|---|
| Tapped L2n0 + keep-out | ≈ 0.05–0.06 mm² | Octagon + metal exclusion; tank not redesigned |
| VCO core / bank / var / amp-cal / bypass | ≈ 0.16–0.22 mm² | P2.7.2a compact [HAND]; was 0.10–0.14 |
| **VCO island (L2n0 + VCO analogue)** | **≤ 0.30 mm²** | **D23 amended 2026-11-12** (was 0.15–0.20); compact 0.22–0.28 |
| LO buffer + CML + converter + TSPC | ≈ 0.05–0.08 mm² | Dual chains, one powered |
| PFD + CP + replica + bias + I_cp DAC | ≈ 0.03–0.05 mm² | |
| Loop filter (D19) | ≈ 0.062 mm² | MOS C1/C2 + MIM C3 |
| V_tune hold + window delay + monitors | ≈ 0.01–0.02 mm² | |
| VR_ANA1 LDO + 10 Ω + Cg | ≈ 0.02–0.03 mm² | Cg 0.0125 mm² |
| AFE/LO digital (D3) | ≈ 0.01–0.02 mm² | Outside phase1l budget |
| **Synth analog + AFE digital** | **≈ 0.40–0.52 mm²** | Excludes phase1l; VCO island raised |
| Routing / guard / fill | ≈ 0.08–0.12 mm² | |
| **Synth island total** | **≈ 0.50–0.62 mm²** | Aspect ~1:1 to 1.5:1 |

---

## 3. Option A — “Inductor NW, quiet; digital SE; RF south”

**Placement:** L2n0 in the **NW** corner (near pin 3 / VR_ANA1). VCO core and bank immediately east of the inductor (short CT and tank leads). LO buffer on the south face of the VCO; CML ÷2/÷3 and converter continue south toward the future mixer / RF edge. PFD / CP / bias and the D19 loop filter in a **NE** strip, east of the bank, with V_tune running east–west ≤ ~150 µm. VR_ANA1 LDO sits next to pin 3 (west of inductor or between pad and 10 Ω). **phase1l digital** stays **SE / S** (away from inductor). AFE/LO control abuts the PLL east side.

| Metric | Estimate `[HAND]` |
|---|---|
| Synth island area / aspect | ≈ 0.50 mm²; ~700 × 700 µm |
| VCO→buffer→CML path | ≈ 80–150 µm differential |
| V_tune line (CP/LF → varactor) | ≈ 100–200 µm |
| Inductor ↔ digital (phase1l) | ≈ 500–800 µm edge-to-edge |
| Inductor ↔ charge pump | ≈ 250–400 µm |
| Guard / DNW | Deep-n-well under VCO+LO; guard ring around inductor; substrate ties dense at VCO/CP boundary; digital on its own ring |
| Supply split | VR_ANA1 pad metal feeds VCO CT, LO, CP star from pad node; LDO output before 10 Ω stays local; VR_DIG only into AFE/phase1l; analog gnd star under VCO |
| Coupling target | Best of the three: max inductor–digital distance; CP switching east of bank shield; LO CMOS edges south, not under coil |
| Post-layout noise | Short tank–buffer helps Amp and kick-back; local CT/CML caps easy; LF large MOS away from coil reduces C2 modulation from digital |

**Pros:** Best isolation for −35/−15 dBc coupling; natural VR_ANA1 adjacency; RF path points to RF pads.  
**Cons:** Synth island spans NW–NE; V_tune crosses bank–LF gap; die may need a tall N strip.

---

## 4. Option B — “Inductor north-centre; synth east of digital”

**Placement:** L2n0 **north-centre**. VCO south of the coil. LO chain continues south-west toward RF. PLL / LF / LDO form a **column on the east**, between phase1l (SE) and the VCO. Pin 3 VR_ANA1 routes north then east into LDO → 10 Ω → pad spur into the east column and west into VCO CT.

| Metric | Estimate `[HAND]` |
|---|---|
| Synth island area / aspect | ≈ 0.48 mm²; ~600 × 800 µm |
| VCO→buffer→CML path | ≈ 100–180 µm |
| V_tune line | ≈ 80–150 µm (LF next to VCO east face) |
| Inductor ↔ digital | ≈ 400–600 µm |
| Inductor ↔ charge pump | ≈ 200–350 µm |
| Guard / DNW | Same idea; CP closer to coil than Option A |
| Supply split | Longer VR_ANA1 spine N→E; more IR and bond-return sharing risk at GHz unless local caps are dense |
| Coupling target | Weaker than A: CP nearer coil; digital still south but closer |
| Post-layout noise | Shorter V_tune helps hold/monitor; LO path slightly longer |

**Pros:** Compact; short V_tune; clear east “PLL street”.  
**Cons:** Worse inductor–CP spacing; VR_ANA1 routing longer; coupling margin tighter.

---

## 5. Option C — “Compact cluster at pin 3 (rejected as primary)”

**Placement:** Entire synth (inductor + VCO + LO + PLL + LF + LDO) packed in the **NW** within ~500 × 500 µm; digital SE.

| Metric | Estimate `[HAND]` |
|---|---|
| Synth island area / aspect | ≈ 0.45 mm²; ~500 × 500 µm |
| VCO→buffer→CML | ≈ 50–100 µm (best) |
| V_tune | ≈ 50–100 µm (best) |
| Inductor ↔ digital | ≈ 600–900 µm (good) |
| Inductor ↔ charge pump | ≈ 100–200 µm (**poor**) |
| Coupling / noise | Fails the spirit of the −35 dBc VHF layout target: CP and Σ-Δ edges sit under or beside the coil |

**Pros:** Shortest RF and V_tune; smallest bounding box.  
**Cons:** Couples CP / digital edges into the tank; hard to meet integer-boundary isolation without exotic shielding. **Not proposed.**

---

## 6. Proposal — **D23: Option A**

Adopt **Option A** (inductor NW near VR_ANA1; VCO east of coil; LO south; PLL/LF NE; phase1l SE; AFE digital on PLL east face).

**Reasons:**
1. Maximises inductor–digital distance while keeping pin-3 adjacency for D21.
2. Keeps the charge pump and large C2 MOS off the coil — needed for the VHF raw ≤ −35 dBc coupling budget (`pll-topology` §13).
3. LO path points toward RF pads for Phase 3 mixer without crossing the digital core.
4. Area (~0.50 mm²) and routing lengths are acceptable `[HAND]`; Option B saves little area and spends isolation.

**Not decided here:** exact die outline, pad-ring abuts, or Phase 3 RX/TX placement (they follow the Phase 2 gate).

---

## 7. Owner decision

**D23 = Option A** recorded in `decisions.md` (2026-11-11). Layout proceeds under P2.7.1+.

---

## 8. Whole-die area tally vs package `[HAND]`

Rough Phase-5 squeeze check against the SX1255-compatible **MLPQ-W 5 × 5 mm** package (`spec/rf-frontend.md` §2). Package outline = **25 mm²**; usable silicon is smaller. Two die-core assumptions: the memo’s ~**1.6 × 1.6 mm** (2.56 mm²) sketch, and a more typical **~2.5 × 2.5 mm** (6.25 mm²) die inside a 5 × 5 MLPQ.

| Block | Area (mm²) | Basis |
|---|---|---|
| VCO island (L2n0 + VCO analogue) | **≤ 0.30** | D23 amended 2026-11-12; compact 0.22–0.28 `[HAND]` / P2.7.2a |
| Rest of synthesizer (LO+PLL+LF+LDO+AFE dig) | **≈ 0.28–0.32** | §2 remainder `[HAND]` |
| Synthesizer island total (D23 Option A) | **≈ 0.55–0.62** | was ≈ 0.50; VCO raise `[HAND]` |
| Digital back end (`phase1l`) | **0.340** | 339 617 µm² `[SCH]` |
| RX (LNA + mixer + TIA/AAF + Σ-Δ ADC) | **0.90** | rf-frontend §7 first-cut; SX1255-class `[HAND]` |
| TX (Σ-Δ DAC + recon filter + IQ mod + PA driver) | **0.65** | same `[HAND]` |
| LDOs (VR_PA, VR_ANA1, VR_ANA2, VR_DIG) + local C | **0.10** | VR_ANA1 alone ≈ 0.02–0.03; four rails `[HAND]` |
| Pad ring / ESD / seal (32 leads) | **0.55** | typical MLPQ pad + ESD strip `[HAND]` |
| **Sum (no routing slack)** | **≈ 3.16–3.23** | |
| Routing / guard / fill / DNW slack (~15 %) | **≈ 0.47** | `[HAND]` |
| **Total estimate** | **≈ 3.6–3.7** | |

| Against | Available | Fit? |
|---|---|---|
| Memo core 1.6 × 1.6 mm = 2.56 mm² | 2.56 | **NO — short ≈ 1.1 mm²** `[HAND]` |
| Typical die 2.5 × 2.5 mm = 6.25 mm² | 6.25 | **YES — ~2.5–2.6 mm² slack** `[HAND]` |
| Package outline 5 × 5 mm = 25 mm² | (die ≪ package) | Package is not the limit; die outline is |

**P2.7.2a2 check:** VCO island ≤ 0.30 mm² (D23 amended) still fits inside ≈ 2.5 × 2.5 mm with pad ring. Die-size squeeze remains RX+TX+pads, not the VCO raise. Exact die size remains a Phase 5 decision.

**P2.7.2b D9 check (2026-11-12, finding — not accepted):** MIM 50 pF `cbf` needs VCO island ≈ 0.33 mm² [HAND/TOOL]. If the owner picks option A (raise D23 to ≤ 0.34 mm²):

| Block | Area (mm²) | Basis |
|---|---|---|
| VCO island | **≤ 0.34** | D9 MIM path [HAND] |
| Rest of synthesizer | **≈ 0.28–0.32** | unchanged |
| Synth island total | **≈ 0.59–0.66** | +0.04 vs amended D23 |
| Other rows (§8 table) | unchanged | |
| **Total estimate** | **≈ 3.64–3.74** | still YES on 2.5 × 2.5 mm (~2.5 mm² slack) |

**P2.7.2b running island tally (2026-11-14) [GDS]:** core+tank 0.1102 + bank 0.1514 + `dac_array` 0.0073 + `tail_mt` 0.0058 + `ota_vds` 0.0017 + `d9_rc` 0.0039 + `cbf` (7× cmim) **0.0431** ≈ **0.3234 mm²**. That sum is **laid-out cells only** — it does **not** include the hand forecast for varactor + D22 + top routing (≈ **0.017 mm²** [HAND]). With forecast: **≈ 0.340 mm²**, at the ≤ 0.34 limit (not 0.0166 under). ≤ 0.36 die re-total not opened unless join packing or forecast grows. `tail_block` join bbox **0.2352 mm²** [GDS] (not added on top of the cell-sum tally). **tail_block join PASS** (DRC density waived; KLayout LVS; netgen uniquely) — see `spec/p27-layout-notes.md`.

**P2.7.2b reshape stop (2026-11-14) [GDS/HAND]:** cells reshaped (d9 fold / mt 2×2 / cbf 3×3) PASS. Place-only tail **0.0805**; island sum **0.1102+0.1514+0.0805+0.017 ≈ 0.359** at ≤ 0.36. Power corridors → join ≈ 0.091 → island ≈ **0.370 > 0.36**. Filter join WIP. Owner decides (further squeeze vs raise D23). Die re-total if raised to ≈ 0.38: total ≈ 3.68–3.78; still fits 2.5×2.5.

**D23 final ≤ 0.38 mm² (2026-11-14)** (`decisions.md`). **tail_block join PASS** footprint **0.0950 mm²** [GDS]. **Island outline GDS** (core+tank + bank + tail, reserved pocket, no inter-block routing): bbox **0.3906 mm²** [GDS] — **over** ≤ 0.38 by **0.0106**. Cell-sum+forecast **0.3737** still under. Finding accepted as die-level gate at P2.7.2c (`spec/p27-floorplan.md` §8 re-total with inter-block routing). Die re-total at 0.3906: synth ≈ +0.01 vs 0.38 case; still fits ≈ 2.5 × 2.5 mm [HAND].

**P2.7.2b varactor (2026-11-16) [GDS]:** hierarchical `vco_var` **0.0066 mm²**, width **41.3 µm** — over the reserved **1/3 strip** area (0.0062 mm²) by **0.0004**; width YES vs 43.2 µm; under full pocket **0.0187 mm²**. Join **PASS** (DRC dens.+SVaricap M1.b waived; KLayout; netgen). Island cell-sum+forecast still uses pocket 0.0187 until D22 lands; die-level gate unchanged (P2.7.2c).

**P2.7.2b D22 (2026-11-17) [GDS] — layout PASS:** ampcal_det join DRC dens. waived; KLayout Congrats; netgen uniquely; fingers OK; bbox **0.0186** > pocket **0.0121** after vco_var [GDS]. Footprint carried to P2.7.2c die-level gate. Peak MC accepted.

**Chip art (2026-11-17) [GDS] — chip-floorplan / Phase 5 item:** standalone TopMetal2 cell `chip_art` **0.8706 mm²** (884.35 × 984.40 µm); TM2 dens. **30.7 %**; accepted as overlay (`decisions.md` 2026-11-17). **Reserved:** a **TM2-free region ≈ 0.9 × 1.0 mm** on the chip floorplan (no TM2 power straps, inductors, or RF under the art). Checked at **synthesizer top / Phase 5**, not inside the VCO island. Text-only ≈ 0.17 mm² [HAND] if that region cannot be kept.

**P2.7.2c STOP (2026-11-17) [SCH/GDS]:** re-pack outline **0.5743 mm²** [GDS] not accepted. Band-margin gate FAIL: island 59.4 + bank 40 + core 30 fF/side → top margin **−29 MHz** vs ≥ 40 MHz [SCH]. Direct bank–core re-pack plan in `spec/p27-layout-notes.md` (island ≈32–37 fF [HAND]; still tight vs gate). Die still fits ≈ 2.5 × 2.5 mm at 0.5743 [HAND]. Art TM2 keep-out: Phase 5 (reserved above).

**P2.7.2c direct pack (2026-11-17 later) [GDS/HAND/TOOL]:** outline as built **0.5225 mm²** [GDS] (bbox −208.78…394.7 × 0…865.835). Island routing C ≈ 27.9/28.9 fF/side [HAND] under ≤ 37. DRC clean through controls; unique LVS still FAIL (tail mega-short — `summary_p272c_step345_stop.txt`). Die re-total vs §8 table: VCO island row uses **0.5225** [GDS] in place of 0.5743; synth island still fits ≈ 2.5 × 2.5 mm [HAND]. Art keep-out unchanged (Phase 5).

**P2.7.2c tail escape STOP (2026-11-17) [GDS/HAND/TOOL]:** core east pin PASS; corridor/north-ring M3 stub LVS-clean; pin entry into `tail_block` → `gnd|tn`. Hold die row **0.5225 mm²** [GDS] until unique LVS. Tail C≈110 fF [HAND] for attempted path. Detail: `summary_p272c_tail_escape_stop.txt`.

**P2.7.2c rfcmim / join STOP (2026-11-18) [GDS/SCH/TOOL]:** island outline **0.4029 mm²** [GDS] (tail-next pack, tn_tp); island C **35.6/35.6 fF** [HAND]; tail L 91 µm, C≈9.1 fF [PDK/HAND]. rfcmim 24=24 and g1/g2 unique PASS; band@35.6 PASS (104/92 MHz) [SCH]. Unique LVS still FAIL at tn_tp (144 vs 145 nets) — see `summary_p272c_rfcmim_join_stop.txt`. Die row uses **0.4029** [GDS]; still fits ≈ 2.5 × 2.5 mm [HAND].

**P2.7.2c flat-sch LVS STOP (2026-11-18) [GDS/SCH/TOOL]:** outline still **0.4029 mm²** [GDS]; die row unchanged. Flattened-sch reference wired; placement-only PASS; unique LVS FAIL at power (1 NMOS) — `summary_p272c_flat_sch_lvs_stop.txt`. tn/tp C / PEX not re-run.

**P2.7.2c varactor bypass / vvb_bias STOP (2026-11-18) [TOOL/HAND]:** outline still **0.4029 mm²** [GDS]. Drains of M$888/M$899 separate; merge from orphan `$589` / hold `$551`/`$564` [TOOL]. vvb_bias requirement written (open). Unique LVS still FAIL — `summary_p272c_varactor_bypass_stop.txt`.

**P2.7.2c close vbp / unique LVS STOP (2026-11-18) [GDS/TOOL]:** outline still **0.4029 mm²** [GDS]; die row unchanged. vbp join PASS; intermediate net groups PASS; unique LVS FAIL (Mtail on tn) — `summary_p272c_close_vbp_unique_lvs_stop.txt`. vvb_bias requirement accepted (PLL bias gen). Still fits ≈ 2.5 × 2.5 mm [HAND].

**P2.7.2c tail + fan-out / KLayout unique STOP (2026-11-18) [GDS/TOOL]:** outline still **0.4029 mm²** [GDS]; die row unchanged. Tail south-via route clear of tn; L=99 µm R125=2.35 Ω C≈9.9 fF [HAND/PDK/GDS]; pin fan-out gate PASS all groups; netgen unique 239/144 PASS; KLayout unique FAIL — `summary_p272c_tail_fanout_unique_lvs_stop.txt`. Still fits ≈ 2.5 × 2.5 mm [HAND].

**P2.7.2c KLayout + step-2 PASS (2026-11-18) [GDS/TOOL/SCH]:** assemble outline still **0.4029 mm²** [GDS] (full cell bbox measures 0.4624 — reconcile later). KLayout unique PASS + netgen unique PASS after case/grid/`ps` setup; varactor scripts PASS; step-2 @35.6 overlap/boundary/D20 PASS; PN [HAND] (PSS no converge). Die row holds **0.4029**. Still fits ≈ 2.5 × 2.5 mm [HAND]. Next: P2.7.3 PEX.

**P2.7.3a die row (2026-11-18) [GDS]:** decisions closed P2.7.2c with **full-cell bbox 0.4624 mm²** [GDS] (−219.28…409.40 × −15.20…720.26 µm). Assemble outline 0.4029 remains the place-pack figure; **§8 VCO island die tally uses 0.4624**. Synth island still fits ≈ 2.5 × 2.5 mm [HAND]. Art TM2 keep-out unchanged (Phase 5). Detail: `layout/p272c/out/summary_pex_vco_die.txt`.

**P2.7.4a LO plan (2026-11-19) [HAND]:** divider placement south of VCO (buffer
input faces tank; CML next; LO outs toward mixers; away from tank / V_tune).
Sub-block areas still §2: LO buffer+CML+conv+TSPC **≈ 0.05–0.08 mm²** [HAND] —
no GDS yet (UHF floor with C_ck FAIL; stop before layout). Die re-total:
VCO island row still **0.4624** [GDS]; rest-of-synth **≈ 0.28–0.32** unchanged;
still fits ≈ 2.5 × 2.5 mm [HAND].

**P2.7.4a2 floor fix (2026-11-19) [SCH/HAND]:** xschem captured; I_latch 0.75 mA;
UHF floor with C_ck=15 fF **−154.7 PASS** [SCH]. Area with fix: LO
buffer+CML+conv+TSPC **≈ 0.05–0.09 mm²** [HAND] (slightly larger CML). No
divider GDS yet. Die re-total unchanged (VCO **0.4624** [GDS]); still fits
≈ 2.5 × 2.5 mm [HAND]. VHF LO current ≈ 10.69 mA vs D7 ≤ 10 — owner decision.

**P2.7.4a3 tail-less ÷3 (2026-11-19) [SCH/HAND]:** VHF ÷3 latches tail-less; B2
stays **4 µm** (0.516 V/side @ 4.20 / V_min 1.181 V [SCH]). LO area still
**≈ 0.05–0.09 mm²** [HAND] (no buffer growth; fewer ÷3 tail devices). No
divider GDS. Die re-total unchanged. D7 VHF **10.69 mA** over — STOP (superseded below).

**P2.7.4a3 current sizing (2026-11-19) [SCH/HAND]:** VHF I_latch **0.30 mA**
(UHF 0.75 mA); LO area still **≈ 0.05–0.09 mm²** [HAND] (narrower VHF CML).
D7 **PASS** VHF 8.66 / UHF 8.18 mA. Final corners + MC 20/20; f_max_ss ≈
4.8 GHz. Ready for P2.7.4b layout.

**P2.7.4b step0 (2026-11-19) [SCH]:** VHF ff/−40 & ff/125 PASS at final
currents; MC 0.51° = VHF 8-phase OK vs ~1° HR. First latch GDS WIP —
DRC/LVS FAIL (M1 shorts); area ≈ 0.00087 mm² [GDS]; clock C leaf ≈ 2.5 fF
of 15 fF/side. Die re-total unchanged.

**P2.7.4b latches + NOR (2026-11-20) [GDS/SCH+PEX-RC]:** `cml_latch_uhf`
**0.01286**, `cml_latch_vhf_tl` **0.01019**, `cml_nor_vhf` **0.00669** mm²
[GDS]; running divider cell-sum **≈ 0.0297 mm²** (buffer/conv/TSPC/Johnson
not drawn). Floors with extracted C on ck/qp/qn/ta: UHF **−155.6** / VHF
**−159.7** PASS vs ≤ −151. LO area still inside **≈ 0.05–0.09 mm²** [HAND]
sketch. Die re-total unchanged (VCO **0.4624** [GDS]).

**P2.7.4b `cml_conv` (2026-11-21) [GDS/TOOL]:** area **0.01591 mm²** [GDS];
DRC (density waived) / KLayout LVS / netgen / fingers / render **PASS**.
Running divider cell-sum **0.04565 mm²** [GDS]
(0.01286 + 0.01019 + 0.00669 + 0.01591); TSPC/Johnson/buffer not drawn.
Die re-total unchanged (VCO **0.4624** [GDS]).

**Flag:** the §1 sketch of a **1.6 × 1.6 mm** active core **does not fit** the Phase 3/4 RX+TX + synth + digital + pads tally. Before Phase 5, plan on a die closer to **≥ ~2.2 × 2.2 mm** (≈ 4.8 mm²) or tighten RX/TX area after topology.
