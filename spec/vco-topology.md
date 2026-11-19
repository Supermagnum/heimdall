# VCO topology memo (P2.3)

Status: **topology accepted (D8–D11; D24 2026-11-12).** P2.3 open items closed. **Layout:** blocks through D22 PASS; chip art PASS. **P2.7.2c** closed. **P2.7.3a–c** VCO post-layout **complete** **[PEX-RC lumped / MODEL]** (2026-11-19): swing / D22 / wake accepted; peak sch-style PASS 1.249 ≤ 1.50. Next: **P2.7.4** (UHF floor with layout C open). See §9.

---

## 1. Requirements

| Item | Value | Source |
|---|---|---|
| Range | 3.12–4.20 GHz (VHF ÷24: 130–175 MHz; UHF ÷8 uses 3.20–3.84 GHz) | `spec/rf-frontend.md` §5 |
| Phase noise at 1 MHz | VHF ≤ −116, UHF ≤ −115 dBc/Hz (at the 600 kHz / 2 MHz duplex offsets: ≤ −108.4 / −117.9) | `spec/phase2-plan.md` §2.1 |
| Current | VCO 2–4 mA of the ≤ 10 mA LO budget (D7) | §2.4 |
| Structure | One VCO, switched-capacitor bank (D2: 5–6 bits), NMOS cross-coupled core first, HBT core as comparison (D1) | §5 |
| Tank | L2n0, L 1.69 nH ± 3 %, Q 14.2 / 15.3 / 16.9 at 3.12 / 3.5 / 4.2 GHz (untapped P2.0); centre-tapped [EM] L 1.685 / 1.690 / 1.703 nH, Q 14.13 / 15.15 / 16.66 at 3.1 / 3.5 / 4.2 GHz, within 2 %, \|V_CT/V_diff\| ≤ 0.0036 | P2.0 / P2.7 tapped |
| Temperature, corners | −40 to +85 °C, PDK corners | `spec/rf-frontend.md` §6 |
| Settling | Band calibration + lock inside 150 µs | §5 |

## 2. Tank budget

Design range 3.00–4.37 GHz (band edges ± 4 % for capacitor spread, parasitic uncertainty and temperature), on top of the ± 3 % L uncertainty:

- Differential tank capacitance needed: **1 717 fF** at the low edge (L − 3 %) down to **762 fF** at the high edge (L + 3 %). Ratio 2.25; the bank and varactor must switch 955 fF.
- **Everything fixed must fit in 762 fF differential** at the high edge: core transistors, inductor self-capacitance, the bank's off-capacitance, the varactor minimum, the buffer input and routing. Rough split `[HAND]`: core ≈ 40, inductor ≈ 45, bank off-state ≈ 320 (for an on/off ratio of 4), varactor ≈ 20, buffer ≈ 15, routing ≈ 25 fF → ≈ 465 fF, leaving ≈ 300 fF margin. **The bank's on/off ratio at an acceptable Q is the main tuning-range risk.**
- Bank Q: each switched unit needs Q ≥ about 80 at 4.2 GHz so the bank costs ≤ 15 % of tank Q (assumed in the estimates below). This sets the switch size and therefore the off-capacitance; step 1 measures the trade-off.

## 3. Proposed topology

```
                VDD_VCO (dedicated LDO, about 1.0–1.2 V, from VR_ANA1)
                          │
                    ┌─────┴─────┐  L2n0 (centre tap to VDD_VCO)
                    │           │
          tank+ ────┤           ├──── tank−    → CML buffer → ÷2 (CML) → dividers (P2.4)
                    │           │
    7-bit cap bank ═╪═══════════╪═  MIM + NMOS switch per bit, differential
    varactor pair  ═╪═══════════╪═  sg13_hv_svaricap, well = Vtune (loop filter)
                    │           │
                M1 ─┴─┐     ┌───┴─ M2      NMOS LV cross-coupled pair (D1)
                      └──┬──┘
                         │ tail node ── C_tail (5–10 pF MIM): shunts tail noise near 2 f0
                         │
                        Mt   NMOS tail, long L (≥ 2 µm), current DAC 4–5 bits (amplitude per band)
                         │
                bias ── RC low-pass (pole ≤ 10 kHz) ── reference current
```

1. **Core: NMOS LV cross-coupled pair** (D1), because the simulation method is validated on exactly this circuit. Swing about 1.0 V differential (0.5 V per side): the peak gate–source, drain–source and gate–drain voltages must stay inside the LV device limits, which step 1 confirms from the PDK documentation. The VCO supply is set from that, not the other way round.
2. **Tail: NMOS current source with two filters**, the two noise paths P2.0 measured:
   - an RC low-pass on the tail bias (pole ≤ 10 kHz, MOS capacitor about 50 pF) against the reference mirror's flicker noise, which put the corner at 615 kHz without it;
   - a capacitor at the tail node (5–10 pF) against the tail transistor's noise near 2 f0, which added 70–90 % on top in P2.0. A resonant 2 f0 tail filter (Hegazi) would do better but needs a second inductor and cannot follow a 30 % tuning range, so it is not proposed.
   - The tail transistor's own flicker is reduced by area (long L); NMOS against PMOS flicker in SG13G2 is checked in step 1.
3. **Amplitude (D22):** 5-bit `VCO_BIAS` DAC, **I_tail = 1.52 mA + code × 0.08 mA** (≤ 4 mA, D12). Peak detector + SE comparator on the tank; digital search with band cal (`en_vco_tail_bp` closed during search), then hold. Target 1.25 V ± 0.10 V; steady ≤ 1.40 V, search transient ≤ 1.50 V. **Step 1 done 2026-11-11; interim A2 retired** (`spec/vco-amplitude-cal.md` §10).
4. **Capacitor bank: 7 bits, binary, differential MIM + NMOS switch** (proposed change from D2's 5–6 bits, §5 D8).
5. **Varactor: `sg13_hv_svaricap`** (accumulation-mode, thick oxide, PDK device), gates on the tank, well on the tuning line. Small: about 10 fF swing with 7 bits. Its C–V curve and Q set the usable tuning window, assumed 0.6 V here; a wider window lowers KVCO further.
6. **Supply: a dedicated LDO for the VCO.** Frequency pushing turns supply noise into phase noise exactly like tail noise; the LDO's own noise is budgeted in step 3.
7. **Buffer:** a differential CML buffer between the tank and the first ÷2, so divider kick-back and the load change between ÷8 and ÷24 do not pull the tank. Its input capacitance is in the 762 fF budget.

**Variant for comparison (D1): SiGe HBT cross-coupled core** (`npn13G2`), larger swing (≈ 1.6 V differential), low flicker. It is about 5 dB better on paper but needs 4–6 mA at the low edge (above the 4 mA VCO share of D7) and a higher supply. It is simulated in P2.3 as the comparison, not as the baseline.

**Not proposed:**
- Complementary (NMOS + PMOS) core: half the current for the same swing, but the PMOS pair adds capacitance that the 762 fF budget cannot spare at 30 % tuning range.
- Two VCO cores: rejected in D2 (twice the inductor area).

## 4. Estimates

Leeson, tank Q × 0.85 for bank and varactor loss, current-limited swing (`analog/vco/tank_budget.py`) `[HAND]`:

| Core | 3.12 GHz | 3.65 GHz | 4.20 GHz | Current |
|---|---|---|---|---|
| A: NMOS, 1.0 V swing, F = 3 | −124.8 | −123.1 | −121.7 dBc/Hz | 3.9 / 3.1 / 2.5 mA |
| A′: same, F = 4 (residual tail and bias noise) | −123.5 | −121.9 | −120.4 dBc/Hz | same |
| C: HBT, 1.6 V swing, F = 2.5 | −129.7 | −128.0 | −126.5 dBc/Hz | 6.3 / 4.9 / 3.9 mA |

Against the ≤ −116 / −115 dBc/Hz targets, core A has about 4–9 dB of margin before the losses this estimate leaves out (varactor AM-to-PM, supply pushing, buffer loading, corners). The worst case is the high edge: phase noise scales with (f0 / Q)², and f0 rises faster than Q across the range.

## 5. Decisions (accepted as proposed, 2026-10-20)

| # | Decision | Proposal | Reason |
|---|---|---|---|
| **D8** | Capacitor-bank size (changes D2) | **7 bits** instead of 6 | P2.2 rerun: the band step grows as f³ across the range, so a 6-bit bank needs KVCO 29–94 MHz/V. At 94 MHz/V the loop-filter resistor noise fails the VHF duplex limit (−135.3 dBc/Hz against −136) unless the charge-pump current rises to 50 µA, which needs about 950 pF of loop filter (2.4×; ≈ 0.12 mm² instead of ≈ 0.05 mm² as MOS capacitors). 7 bits needs 14–47 MHz/V; at 48 MHz/V with 42 µA the model passes with the original ≈ 400 pF. Cost: one more calibration step and one more register bit (`VCO_BAND` [6:0]; [7] stays manual) |
| **D9** | Tail treatment | **NMOS tail + RC-filtered bias + tail capacitor** (§3 item 2) | Removes both noise paths measured in P2.0 with standard parts; class-C biasing (gates biased below threshold through coupling capacitors, large tail capacitor) is evaluated as a variant in P2.3, not chosen now |
| **D10** | VCO supply | **Dedicated LDO**, voltage set by the LV device limits (about 1.0–1.2 V) | Supply pushing; isolation from the dividers and the digital blocks |

Interface consequences (applied to `spec/analog-digital-interface.md` on 2026-10-20): `VCO_BAND` becomes 7 bits; a new register for the VCO tail-current DAC (proposed 0x2C, `VCO_BIAS` [4:0]), written per band by the host or by the calibration; the charge-pump current code in `PLL_CTRL` [5:3] (25–200 µA) is also set per band to keep the loop bandwidth constant while KVCO varies about 3× across the range.

## 6. Step 1 — device checks before the schematic

All in VACASK on the pinned PDK, each a small testbench:

1. **LV NMOS voltage limits** from the PDK documentation, and the resulting swing and VCO supply.
2. **`sg13_hv_svaricap`:** C–V and Q at 3–4.4 GHz against tuning voltage; sets the varactor size and the tuning window.
3. **Bank unit cell** (MIM + NMOS switch): on/off capacitance ratio against Q for a few switch widths; decides whether the 762 fF budget holds.
4. **Flicker of NMOS against PMOS** current sources of equal area (tail choice).
5. **Inductor model:** a lumped broadband model fitted to the de-embedded EM data (2.0–4.5 GHz), so pss/pnoise can use it; checked against the EM L and Q within 1 %.

## 7. P2.3 after the review

| Step | Work | Gate |
|---|---|---|
| 1 | Device checks (§6) | Result review: confirms or changes §2–3 |
| 2 | Core schematic with the EM inductor model; bank, varactor, tail, buffer | — |
| 3 | `pnoise` (16 000 points, offsets ≥ 30 kHz) across bands, PDK corners, −40/27/85 °C; tuning range and KVCO per band; supply pushing; HBT comparison | Result review against §1 |

Simulation settings and method: `analog/pn-validation/README.md`. Offsets below 30 kHz need `pss_minpts` × offset ≥ 5·10⁸.

## 8. Step 1 results (2026-10-20) and what they change

Source: `analog/vco/step1/` (`run_step1.py`, results in its README). Typical corner, 27 °C.

| Item | Result | Change to §2–3 |
|---|---|---|
| Swing `[DS]` | LV `VGS ≤ 1.65 V @ 125 °C` (process spec). With 10 % margin and drain headroom over a 0.35 V tail node: **1.5 V differential at a 1.1 V centre tap** | D10 LDO at about 1.1 V. Swing is current-limited at the low edge (about 1.05 V at 4 mA) and voltage-limited at the high edge (1.5 V at 3.3 mA) |
| Bank cell `[SCH]` | 2 × `cap_rfcmim` 9 × 9 µm + LV NMOS switch, bottom plates to the switch. **About 100 µm of switch per 60 fF, 200 kΩ bias resistors**: whole 7-bit bank keeps 0.89 (all on, 3.12 GHz) / 0.97 (all off, 4.2 GHz) of tank Q; 391 fF off-state capacitance, **+226 fF** left in the 762 fF budget. 20 kΩ bias resistors made the off state lossy (Q_off 6–50) | Bias resistors ≥ 200 kΩ |
| Tail `[SCH]` | At the real 0.35 V tail voltage the HV NMOS keeps 74 % of its current (no headroom), LV NMOS 85 %. **LV NMOS 160/4 µm**: flicker corner 0.14–0.32 MHz, at 600 kHz within 1.5× of the white floor; LV PMOS worst (3.2 MHz corner at 80/2 µm) | Tail: LV NMOS ≥ 160/4 µm |
| Inductor `[EM]→[SCH]` | Lumped model `analog/vco/models/l2n0_lumped.inc`, L and Q within 0.71 % of EM (3.0–4.37 GHz); self-capacitance 30 fF. The EM layout has **no centre tap**; the model assumes one at the electrical midpoint | Tapped layout needs EM before P2.7 |
| Varactor `[SCH]` | Per finger (3.74 × 0.3 µm per side): 3.7 → 2.1 fF differential from V_G − V_W = +1.2 to −1.2 V; steepest about 1.4 fF/V near **V_G − V_W ≈ −0.3 V**; Q 110–190 at 4.2 GHz. Needed: about 10 fF over the tuning window → **about 12 fingers** (two instances, `nx` = 6) for a 0.7 V window | See D11 |

Phase noise with these numbers (Leeson, bank loss as measured, F = 3–4, 4 mA at the low edge): about −124 to −126 dBc/Hz at 1 MHz across the range, 8–10 dB under the targets `[HAND]`.

**D11 — varactor bias: option A accepted by the owner, 2026-10-20.** With the varactor gates at the tank DC (1.1 V), its steep region sits at a tuning voltage of about 1.4 V, above what a charge pump on the 1.2 V domain can deliver. Two common ways:

| Option | How | Cost |
|---|---|---|
| **A (proposed): AC-coupled varactor** | Varactor gates connected to the tank through MIM capacitors (about 5× the varactor capacitance), gates DC-biased to about 0 V through large resistors, so the steep region falls at a tuning voltage of about 0.3–1.0 V; charge pump and loop filter stay on 1.2 V LV devices | Coupling MIMs and bias resistors (their noise reaches the varactor, so ≥ 100 kΩ, checked in step 3); about 30 % less varactor swing through the coupling capacitors (so about 17 fingers instead of 12) |
| B: high-voltage charge pump | Charge pump and loop filter on the 2.7–3.6 V supply with HV devices; tuning window about 1 V or more | The ≈ 400 pF loop filter needs HV capacitors (lower density than LV MOS caps, or MIM at 1.5 fF/µm²): roughly 2× the filter area; KVCO halves, which helps noise |

Note on the PDK: the VACASK conversion of `sg13_hv_svaricap` does not elaborate (`v(2,4)` in its well resistance); step 1 uses a local copy with those zero-coefficient terms removed. To be reported upstream.

## 9. Steps 2–3 results (2026-10-20): first schematic, bands, corners

**D20 (2026-10-25, P2.6 step 1): the bank becomes 8 bits** (same 2.90–4.41 GHz range, LSB about 5.8 fF on-state) so that one band step is 0.23–0.30 V of V_tune instead of 0.45–0.59 V (`spec/pll-topology.md` §13). The step-2/3 scripts build 8 bits by default (`bits=7` gives the results below); first rerun 2026-10-25 `[SCH]`:
- Sizing: LSB 5.71 fF (on-state), fixed 203 fF. Range 2.910–4.408 GHz typical; at all 15 corner / temperature cases 2.77–3.05 GHz bottom and 4.34–4.55 GHz top (covers); peak V_GS / V_GD ≤ 1.48 V; KVCO 13.1–38.6 MHz/V; tail current per band as before (3.4–4.0 mA).
- Phase noise in five bands, typical: −124.4 / −123.4 / −122.7 / −121.5 / −119.9 dBc/Hz at 1 MHz (3.12–4.20 GHz), worst margin +3.9 dB — the same as with 7 bits to within 0.1 dB.
- **Band steps not uniform:** at the carries the step grows towards the MSB — 3→4: 1.07 ×, 63→64: 1.38 ×, **127→128: about 2.8 × a normal step (0.72 V of V_tune)**, 191→192: 1.45 × (ratios against the local mean, which includes the carry itself). Small cells switch relatively less capacitance (perimeter and switch parasitics in the off state do not scale with the cell), so a plain binary weighting is not enough. Fix: each bit trimmed in size so the step at its carry equals the single-LSB steps beside it (`trim()` in `run_step2.py`, bottom-up, two passes, then re-sizing for the range); systematic, so it holds over corners to first order.
- **Second run (with the trim):** trims 0.971 (bit 1) … 0.933 (bit 7), i.e. the larger cells 3–7 % smaller than plain binary; after re-sizing LSB 6.07 fF, fixed 202 fF. Range 2.914–4.414 GHz, KVCO 13.1–38.8 MHz/V, swing and tail currents unchanged. **Band steps even:** every carry within 0.94–1.07 × the neighbouring steps, steps 3.3 MHz (bottom) to 11.2 MHz (top), **0.24–0.29 V of V_tune** everywhere (7 bits: 0.45–0.59 V), as assumed in the P2.6 closed-loop model. Corner range with the trimmed bank: all 15 cases cover; bottom 2.77–3.05 GHz (least margin 3.054 GHz, MIM best case, 66 MHz below 3.12 GHz), top 4.35–4.55 GHz; peak V_GS / V_GD ≤ 1.48 V — the same as before the trim. **D20 bank done.**

Source: `analog/vco/step2/`, `analog/vco/step3/` (VACASK, PDK `a49358cc`) `[SCH]`. Ideal still: supplies (LDO — noise budget from pushing, § open point 4), reference current, bias-filter R and C, tail capacitor. Stand-in buffer replaced for PN by the P2.4 LO buffer (CML ÷N on the tank still breaks PSS).

**Circuit as simulated:** L2n0 lumped model, centre tap at 1.1 V; LV NMOS pair 32/0.13 µm; tail LV NMOS 160/4 µm, mirror 1:8, bias RC 1 MΩ / 50 pF, tail capacitor 8 pF; 7-bit bank, on-state LSB 11.5 fF after the review (10.9 fF before; sized automatically: the bank switches C_on − C_off, and the fixed capacitance without a fixed capacitor was only about 420 fF), about 100 µm of switch per 60 fF, plus a 204 fF fixed MIM (224 fF before the review); varactor 20 fingers AC-coupled through MIMs of about 5×, gates at 0.3 V; **2 MΩ** bank and varactor bias resistors.

**Start-up bias bypass (P2.6 open point 2, 2026-10-31; P2.7.1c binary bank 2026-11-11):** LV NMOS across `rbf` (20 µm / 0.13 µm, ng=4); bank `rba*`/`rbb*` **W_k = max(0.15 µm, 5 µm × 2^(k−7))** (MSB w=5u ng=2; PDK `nmos_minW`); var `rvp`/`rvn` unchanged (5 µm / 0.13 µm, ng=2). Gates `vbp` / `vbp_tail` / digital `en_vco_bias_bp`. Closed ≥ 0.4 µs at wake by `afe_seq` (36 ref cycles = 1.00 µs at 36 MHz). Stand-alone VCO range/pnoise runs keep `vbp` tied low. See `spec/analog-digital-interface.md` §6.

**SCH re-run 2026-10-31:** range pass (`summary_range_rerun.txt`). PSS abort root cause: off-state **bank** bypass NMOS on the tank bottom plates (`summary_pss_bypass_parts.txt`; tail and varactor bypasses OK). Bank-omitted PN accepted for layout start: tt 3.65 GHz −122.7 dBc/Hz @ 1 MHz (+6.7 dB); ss 85 °C 4.20 GHz −119.4 (+3.4 dB) (`summary_pn_nobank.txt`). Linear bank equivalent abandoned. Switch-noise bound vs bank bias R **closed 2026-11-01** (`summary_bound_bank_switch.txt`): tt +0.59 dB worst-case bound (margin +6.1 dB); ss85 Δ +0.006 dB; owner gate (positive margin everywhere; worst-point move < 0.5 dB).

**Bypass on-resistance `[SCH]`** (V_GS = 1.2 V, V_DS = 50 mV): tail switch Ron ≈ 29–34 Ω (tt/ss, −40/27 °C); bank MSB Ron ≈ 131–162 Ω (ss/−40, ff/125); smaller bits higher Ron as W shrinks (floor 0.15 µm → ~3 kΩ). With C_tail = 50 pF, τ ≈ 1.5–1.6 ns and 7 τ ≈ 11 ns. Bank plates: worst wake nτ in 1.00 µs ≈ **3800** (bit 4, ff/125) — PASS ≫ 6–7 (`summary_wake_bank_bypass.txt`). Ron ≪ R_bias (1 MΩ / 2 MΩ).

| Result | Value |
|---|---|
| Range, typical 27 °C | **2.90–4.41 GHz** after the review (2.95–4.41 before) |
| Range at 5 corner combinations × −40 / 27 / 85 °C | Covered everywhere: top 4.34–4.55 GHz, bottom 2.77–3.05 GHz. Least margin at the bottom: MIM best-case corner, 3.036–3.047 GHz, 73–84 MHz below 3.12 GHz (32–45 MHz before the review), enough for the ± 3 % inductance uncertainty (about ± 47 MHz) |
| KVCO | 13.1–38.6 MHz/V (D8 target 14–47) |
| Peak V_GS / V_GD | ≤ 1.48 V at all corners (limit 1.5 V with margin, 1.65 V in the process specification) |
| Tail current for about 1.3 V | 3.4–3.6 mA at the top; **capped at 4 mA** (D12) from about 3.65 GHz down (5 mA before D12) |
| Swing at the bottom (4 mA) | 0.92 V differential typical; lowest 0.59 V (fast MOS, MIM worst case, 85 °C) and 0.64 V (slow, 85 °C) |
| pss tolerance | reltol 1e-6 gives the same result as 1e-7 on the validated level 2 (0.00 dB); 1e-7 does not converge on the full VCO |

Phase noise, typical, 27 °C (dBc/Hz), with the 4 mA cap (D12, rerun 2026-10-20; codes 97 / 67 / 45 / 28 / 11). In brackets: before D12 (5 mA cap).

| VCO | I_tail | 600 kHz | 1 MHz | 2 MHz | Worst margin |
|---|---|---|---|---|---|
| 3.12 GHz | 4.0 mA (5.0) | −119.1 | −124.4 (−124.7) | −130.9 | +8.4 dB (VHF 1 MHz) (+8.7) |
| 3.40 GHz | 4.0 mA (4.8) | −117.8 | −123.4 (−123.5) | −130.2 | +7.4 dB (+7.5) |
| 3.65 GHz | 3.96 mA (4.3) | −116.6 | −122.3 (−122.7) | −129.1 | +6.3 dB (+6.7) |
| 3.90 GHz | 3.87 mA | −115.6 | −121.6 | −128.6 | +5.6 dB |
| 4.20 GHz | 3.59 mA | −113.7 | −120.0 | −127.3 | **+4.0 dB** |

Slow MOS corner, 85 °C, 4 mA cap: 3.12 / 3.65 / 4.20 GHz at 1 MHz −122.8 / −122.0 / −119.6 dBc/Hz (before D12 −123.5 / −122.1 / −119.6), worst margin **+3.6 dB** unchanged (4.20 GHz, VHF 1 MHz). The 4 mA cap costs 0.3–0.7 dB at the bottom, less than the 2 dB estimated. The UHF limits (3.20–3.84 GHz) have at least 8 dB margin. Noise contributions at 3.65 GHz, 1 MHz: core pair 50 %, inductor 20 %, varactor bias 9 %, bank bias about 10 %, tail 3 % (at 200 kΩ the bias resistors were 36 % and the stand-in buffer 26 %).

**Open points for the result review:**
1. **Current at the bottom of the band:** 5 mA is above the 4 mA VCO share of D7. At 4 mA the swing at 3.12 GHz falls to about 0.82 V and the phase noise by roughly 2 dB, still about 6 dB inside the limit. Proposal: cap `VCO_BIAS` at 4 mA. **Decided 2026-10-20 (D12, with P2.4): capped at 4 mA**; rerun done (`analog/vco/step3/out/summary_4ma.txt`): range and corners unchanged, phase noise 0.3–0.7 dB worse at the bottom, bottom margin +6.8 dB at slow 85 °C.
2. **Bottom-edge margin (accepted and done 2026-10-20: now 73–84 MHz):** with the MIM best-case corner the bottom edge sits 32 MHz below 3.12 GHz. Combined with the ± 3 % inductance uncertainty it could miss by about 10 MHz. Proposal: about 5 % more switched capacitance (design range down to about 2.9 GHz); the top edge keeps ≥ 4.3 GHz at the worst MIM corner.
3. **Amplitude per corner:** **D22 accepted 2026-11-02; step 1 closed 2026-11-11** (`spec/vco-amplitude-cal.md` §10): SE-cmp end-to-end search PASS (steady ≤1.40 / transient ≤1.50); **interim A2 retired**. Bottom bands code 31 / tnr=1 expected.
4. **Supply pushing / LDO budget `[SCH]+[HAND]` (2026-11-01):** K_push ≈ −30 / −50 MHz/V → S_v ≤ ~11 nV/√Hz @ 1 MHz (`summary_supply_push.txt`). First D10 LDO SCH: ~86 nV/√Hz bare (**miss**). **D21 (owner):** VR_ANA1 = LDO → 10 Ω → pad → 100 nF; VCO+LO+CP from pad; RX→VR_ANA2; pad worst-case ≥1.08 V; no option (1). Prior S_v≈9.5 nV/√Hz **UNVERIFIED** (OP did not hold). Fixed LDO (Rz=500 + Cg=100 p to gnd): HOLD; PM ≥ 60° with/without 100 nF; S_v(pad)≈**3.0 nV/√Hz** @ 10 mA (**PASS**). `summary_ldo_verify.txt`. **Real P2.4 LO buffer:** −122.6 / −119.3 (Δ +0.14 / +0.08 dB). Buffer + CML ÷N: PSS aborts.
5. **Centre-tapped L2n0 `[EM]` (2026-11-01):** done. L 1.685 / 1.690 / 1.703 nH, Q 14.13 / 15.15 / 16.66 at 3.1 / 3.5 / 4.2 GHz; all within 2 % of untapped; \|V_CT / V_diff\| ≤ 0.0036 (`spec/provisional-tank-q.md`, `tapped/review/em_summary.md`). **[HAND]** 1.4 % lower Q at 4.2 GHz → ≈ 0.1 dB worse PN at ss 85 °C; remaining margin ≈ +3.5 dB (was +3.6).
6. **Real LO buffer + CML load — closed 2026-11-11** (`analog/vco/step3/out/summary_real_load.txt`, landing `analog/pll/p26/step1/out/summary_land_scaled.txt`):
   - Full real load (P2.4 buffer + CML ÷2/÷3 + converter), D22 bias: max |Δf| vs same-Vtune stand-in **0.285 %** `[SCH]`; worst bottom 3.057 GHz (ss/bcs/−40) → **63.3 MHz** margin to 3.12 GHz (was 66 MHz / 3.054 GHz); carries 63→64 / 127→128 / 191→192 even (4.5–8.5 MHz) `[SCH]`.
   - Shift > 0.2 % → closed-loop landing with **scaled behavioural bank** (+0.285 %), not transistor bank `[MODEL]`: D20 8-bit / f/4P / nearest outside-% unchanged within 0.1 pt; V_tune stays in 0.25–0.95 V (ss 0.25–0.85 V).
   - Divider pulling: |Δf| ≤ 55 ppm, |ΔAmp| ≤ 0.0001 V (tt 3.65 / ss85 4.20) `[SCH]`. Kick-back (coherent |Δ|mag) f0/2 and f0/3 ≤ **−107 dBc**; sidebands ≤ −95 dBc `[SCH]`. Buffer reverse isolation **67.8 dB** `[SCH]`.
   - PSS with CML: still aborts (tolerances + longer warm + lower maxharm + CML always-on; no separate autonomous-shooting option in VACASK) `[SCH]`.
   - **[HAND] PN bound:** buffer SCH +0.14 dB + CML ≤ +0.3 dB → total real-load ΔL(1 MHz) ≤ **+0.5 dB** gate (limit met). Open point closed.
7. **HBT core comparison (D1) — closed 2026-11-11** (`analog/vco/step3/out/summary_hbt_compare.txt`): comparison only; **keep NMOS**.
   - Model: `npn13G2` op/tran PASS; PSS converges but L ~35 dB optimistic vs Leeson — **HBT PSS L untrusted** `[SCH]`/`[HAND]`. BVCEO 1.4/1.6 V, BVCBO 3.8/4.8 V, BVEBO 1.0/1.6 V `[DS]`. Flicker params present in VBIC.
   - Same tank / 8-bit bank / D21 1.2 V / D12 4 mA / nx=8: Amp ≈ **0.99 V** (NMOS 1.16 V) `[SCH]`; VCE peaks OK at that Amp; paper 1.6 V swing would exceed BVCEO min and needs ≈ 1.8–2.5 V CT (D21 unchanged → not proposed).
   - Fair Leeson (Q=15, F_HBT=2.5 / F_NMOS=3): ΔL(1 MHz) ≈ **+0.1…+0.6 dB** (HBT not better) `[HAND]`. NMOS SCH duplex −122.6 / −119.3 still the design numbers.
   - Range: top **4.10 GHz < 4.20 GHz** (HBT Cje); bottom 2.91 GHz OK; KVCO ≈ 21 MHz/V; start-up ≈ 1 ns `[SCH]`. Core area smaller (`[HAND]`) — not the cost driver.
   - **Conclusion:** paper ≈ 5 dB win not realised under D21/D12; band top misses; no switch.

### P2.7.1b (2026-11-11) — range shift cause, re-baseline, coverage finding

**Cause of miss vs `range_2026-10-25.json`:** off-state start-up **bank** bypass NMOS C on the tank plates (≈ −15 MHz at code 0), plus var bypass (≈ −3 MHz). Tail bypass ≈ 0. Sum of parts matches the full-bypass shift. Not PDK/tool (pinned `a49358cc`); not xschem. D22 det/DAC are ampcal-only. Details: `analog/vco/sch/out/summary_range_shift.txt`, `summary_p271b.txt` `[SCH]`.

**Re-baseline:** new `analog/vco/step2/out/range.json` (LSB 7.25 fF, cfix 190 fF, trims ≈ 0.87–0.93); archive kept as `range_2026-10-25.json`. tt span 2.796–4.302 GHz.

**Coverage [SCH]** (`step3/out/summary_8bit_range.txt`): all **15** MOS/CAP/T cases cover 3.12–4.20 GHz; peak V_GS/V_GD ≤ 1.46 V. Worst top margin **39 MHz** (mos_ss / cap_wcs / −40 °C, f_top 4.239 GHz). Worst bottom margin **186 MHz** (f_bot 2.934 GHz).

**Band steps [SCH]** (`step2/out/summary_steps.txt`): **FAIL** — 127→128 is **1.060 V** of V_tune (need 0.24–0.29 V). Off-state bypass C breaks the prior trim. **Do not start P2.7.2 layout until steps are fixed.**

**Proposal:** re-trim / re-size with bypass C in the model; or shrink / move bank bypass so off-C does not dominate MSB carries; or keep RF-plate bypass off if wake RC still meets 0.4 µs.

**D22 search** tt/27: PASS (top code 16, Amp 1.261; bottom 31). **D20 landing [MODEL]** with new ends: 8-bit / f/4P / nearest still ~0 % outside.

### P2.7.1c (2026-11-11) — binary bank bypass, re-trim, coverage

**Change:** bank bypass W tracks bit weight (`bank_bypass_geom` in `run_step2.py`; same in `vco_bank.sch`). Var/tail bypass unchanged. Details: `sch/out/summary_p271c.txt` `[SCH]`.

**Wake:** ≥ 3800 τ in 1.00 µs at ss/−40 and ff/125 — PASS.

**Re-trim:** LSB 6.18 fF, cfix 198 fF, trims ≈ 0.93–0.97; tt **2.903–4.404 GHz**.

**Steps tt:** ratios **0.97–1.02** PASS; 127→128 **0.273 V** (was 1.060 V). Max step **0.296 V** (three top LSBs) — **strict FAIL vs 0.24–0.29** by ≤ 6 mV; within original D20 0.23–0.30 wording.

**15-corner:** all cover; worst top margin **140 MHz**; worst bottom **77 MHz**; peak V_GS/V_GD ≤ 1.48 V. D22 tt/27 PASS (top code 14). D20 landing ~0 % outside with new ends.

**Amp +0.06 V:** remains with bypass off in plain step2 — not bypass C; sizing/trim vs 25-Oct archive. D22 sets Amp in operation.

**Decision:** accept 0.296 V LSB steps or nudge before **P2.7.2**.

### P2.7.2b / D24 (2026-11-12) — segmented bank

**Change:** MSBs become 7 identical thermometer unit cells (32 × LSB each) + 5 binary LSB cells; AFE `vco_band_dec` maps `VCO_BAND[7:5]` → thermometer. Bypass W tracks cell weight (unit = weight 32). D18 offset off during V_tune hold (`afe_seq.en_cp_offset`): held **tt 0.577 / ss 0.512 / ff 0.649 V** [SCH] (`summary_hold_d24.txt`).

**Re-size/trim [SCH]:** LSB 6.19 fF, cfix 192 fF; `trim_bin` ≈ 0.94–0.96, `trim_unit` 0.9347. Range **2.905–4.406 GHz** covers 3.12–4.20.

**Steps tt:** max **0.298 V** (≤ 0.30) PASS; ratios 0.96–1.02 except **95→96 = 0.90** (sole miss vs 0.94–1.07). Unit nudges worsened high-code ratios — kept first trim.

**Gate [MODEL]** (`summary_p272b_gate.txt`): tt PASS (0.355–0.942 V); **ss FAIL** (max 0.882 vs 0.85); **ff FAIL** (max 0.997 vs 0.95). ss85 127→128 ratio 1.01 (MSB blow-up gone). Layout blocked pending pad-supply re-run.

**15-corner / D22:** not re-run at 1.08/1.32 (gate stop). xschem bank regenerated (84 devices); inventory-vs-deck diffs class as P2.7.1.

### P2.7.2c (2026-11-12) — gate at VR_ANA1 pad supplies

**Supplies [HAND]** (`summary_vrana1_pad_corners.txt`): ss = 1.108 V (min pad), tt = 1.200 V, ff = 1.295 V (max pad from ±5 % LDO and light-load IR). Prior 1.08/1.32 V results for VR_ANA1 blocks listed there; not re-run.

**Hold [SCH]** (`summary_hold_vrana1.txt`, D24 offset off): tt 0.577 / ss 0.524 / ff 0.636 V.

**Compliance window [SCH]** (`summary_compliance_vrana1.txt`, 10 % fall of I_up/I_dn at mid-rail): tt 0.265–1.150 V; ss 0.202–1.050 V; ff 0.341–1.250 V.

**Carries [SCH]** (`summary_p272c_carries.txt`): ss85 max dV 0.352 V, worst ratio 1.05; ff−40 max dV 0.254 V, worst ratio 0.86 (159→160).

**D20 landing [MODEL]** (`summary_p272c_gate.txt`): **PASS** all corners — tt 0.361–0.936 V; ss 0.244–0.897 V; ff 0.457–0.970 V. No cal-target bias, no K=512. Spread parts (½ largest step / counting / curvature asym / hold−mid) in that summary.

**15-corner [SCH]** (`summary_p272c_cover.txt`): all 15 cover; worst top margin **130 MHz**; worst bottom **76 MHz**; peak V_GS/V_GD ≤ 1.49 V (ss cap_bcs −40 °C). **D22** tt/27: top code 14 / bottom 31 PASS. Next: **P2.7.2 VCO layout**.

### P2.7.2c (2026-11-17) — band plan with parasitics (PEX + trim)

**PEX [PEX-RC]** (`layout/p272b/out/summary_pex_core_tank.txt`,
`layout/p272b_bank/out/summary_pex_bank.txt`):

| term | C/side (fF) | vs HAND used |
|---|---:|---|
| core (max; spiral omitted) | 23.66 | ≤ 30 |
| bank wiring (coupling-only) | 36.87 | ≤ 40 |
| island direct pack | 37.00 | [HAND] use 37 |
| **total** | **97.53** | was 129.4 HAND |

**Fixed C trim [SCH]** (`step3/out/summary_p272c_trim_fixed_c.txt`):
2× `rfcmim` **14.5 µm** → `cfix` **157.7 fF** (was 192 / 16 µm).
With parasitics: top margin **102 MHz**, bot **93 MHz** (both ≥ 40) [SCH].
Overlap monotonic at carries: PASS [SCH].
D20 landing and worst-corner pnoise: **not re-run** this job [TOOL].

**Core layout:** stage d rebuild; TM1.b notches in cell; DRC / KLayout LVS /
netgen PASS (`summary_assemble_trim.txt`).

### P2.7.2c direct pack join (2026-11-17) [TOOL/GDS/HAND]

D20 ff landing 0.955 V accepted vs ff window 0.457–0.970 V [MODEL/SCH].
Pin-only inductor LVS GDS: place/power extract clean (no ct|tn|tp or cmp|gnd|vdd
pipes) [TOOL]. Full assembly **DRC clean** (density + SVaricap M1.b waived)
[TOOL]. Island C ≈ 27.9/28.9 fF/side, ΔL 9.8 µm [HAND]; outline **0.5225 mm²**
[GDS]. **Unique LVS/netgen FAIL** — extract mega-short
`W|gnd|tail|tn|tp|vbp|vdd|vt` from tail parent routing through core/bank metals
[TOOL] (`summary_p272c_step345_stop.txt`). ct H-strap raise fixed prior ct|tn.
Inductor fab/LVS diff PASS; varactor fingers PASS [TOOL].

### P2.7.2c rfcmim / g1g2 / band@35.6 (2026-11-18) [TOOL/SCH/GDS]

rfcmim 24→23 at power fixed (ampcal_det.gnd M3 west of bank). g1/g2 unique
(SVaricap G1/G2 stripped; W→vt; bank bb* stripped). Band at island 35.6 fF:
top **104.0** / bot **92.1** MHz [SCH]; no cfix change. Outline **0.4029 mm²**,
island C 35.6/35.6 fF, tail L 91 µm [GDS/HAND]. Unique LVS still FAIL at tn_tp
(144 vs 145 nets; mismatch already at place) —
`summary_p272c_rfcmim_join_stop.txt`.

### P2.7.2c flattened sch LVS reference (2026-11-18) [TOOL/SCH]

Sign-off reference = flattened `vco_top.sch` (`vco_top_sch_flat.spice` +
`lvs_setup.tcl`), not leaf-assembled spice [decisions]. Sch LVS alignment:
bank b0..b2 cmim + rhigh; tail = dac_array units; l2n0 omitted in LVS flat.
Placement-only m-weighted PASS. Unique LVS FAIL at power: 239 vs 238 devices
(1 NMOS after merge), 829 vs 831 nets [TOOL]. Band/D20 **not re-sim’d** after
cmim sch change. Stop: `summary_p272c_flat_sch_lvs_stop.txt`.

### P2.7.2c varactor bypass merge / vvb_bias (2026-11-18) [TOOL/HAND]

M$888/M$899 drains **$507 ≠ $571** in extract — not a drain short; SVaricap
remap not the cause. Orphan gate `$589` (duplicate `vbp` pin text vs bank)
+ shared S drives netgen false merge; PDK 65 vs 64 also from hold mdtp/mdtn
orphan S (`$551`/`$564` vs tp/tn). Place+power unique LVS still **FAIL**.
Stop: `layout/p272c/out/summary_p272c_varactor_bypass_stop.txt`.

**vvb_bias (0.3 V) requirement — accepted** (2026-11-18 decisions): supply from
PLL bias generator at synthesizer top (`spec/pll-topology.md` §12 open item):

| Item | Requirement | Tag |
|------|-------------|-----|
| Biases | SVaricap gates through rvp/rvn (D11 AC-coupled) | [SCH] |
| Nominal | 0.3 V | [SCH] |
| Load | ≈ 0 DC; wake transient when bypasses close | [HAND] |
| Accuracy | ±30 mV | [HAND] |
| Noise | ≤ 8 nV/√Hz @ 100 kHz and @ 1 MHz (PN add ≤ 0.2 dB at K_VCO 38.8 MHz/V vs L_tot −119.6 dBc/Hz @ 1 MHz) | [HAND]/[SCH] |

### P2.7.2c close vbp / unique LVS (2026-11-18) [TOOL/GDS]

bank.vbp↔var.vbp joined (strip hierarchical texts; pin→bus M2 bridge; west
strap). Intermediate net groups: DRC clean, no named-net `|` merge.
M$888/M$899 on `vbp`, drains separate. Unique LVS **FAIL**: `M$934` (Mtail)
`D=tn`; core.tail open from Mtail. Stop:
`layout/p272c/out/summary_p272c_close_vbp_unique_lvs_stop.txt`.

### P2.7.2c tail fix + pin fan-out (2026-11-18) [TOOL/GDS/PDK/HAND]

vbp join accepted. Tail: south via stack clear of tn; face lands on child vias
only; L=99 µm, R125=2.35 Ω, J=0.80 mA/µm, C≈9.9 fF [HAND/PDK/GDS]. Intermediate
gate adds pin fan-out (`check_pin_fanout.py`). All groups: DRC + no `|` + fan-out
PASS. Full join: ports clean incl. ct; **netgen unique 239/144 PASS**; KLayout
initially FAIL — cleared below. Outline assemble 0.4029 mm² [GDS].

### P2.7.2c KLayout LVS difference + step-2 @35.6 (2026-11-18) [TOOL/DS/SCH]

KLayout setup: spice↔spice via `--layout_netlist` (case); MIM w/l snap to PDK
grid 0.01 µm with A/P rebuild; strip extract-only rhigh `ps`; Status-table pass
detect (`run_drc_lvs.py`, `lvs_setup.tcl`). **KLayout unique PASS** + netgen
unique PASS [TOOL]. Varactor w/l/Nx + fingers on assembly PASS
(`summary_varactor_top.txt`) [TOOL/SCH]. Step-2 @ island 35.6 fF: overlap PASS;
boundary ≤½ LSB (local mean) PASS; D20 margins 105/92 MHz PASS; PN PSS no
converge → [HAND] PASS (`summary_p272c_step2_island35p6.txt`) [SCH/HAND].
Stop/pass: `summary_p272c_klayout_diff_step2_pass.txt`. Next: P2.7.3 PEX.

### P2.7.3a — VCO extraction + frequency (2026-11-18) — accepted

**Extract** (`layout/p272c/out/summary_pex_vco_extract.txt`): Magic full-RC on
LVS GDS (pin-only L); ~17.5k elements; L2n0 EM on tn/tp/ct [EM]. Class map vs
LVS: rfcmim 24 / rhigh 33 match; MOS fingers expanded (1103 vs 67) [TOOL].
Svaricap extract 2-terminal [TOOL].

**Tank** (`summary_pex_vco_tank.txt`): wiring add **62.5 / 68.2 fF** tn/tp
(headline **68.22**); series R **0.24 Ω**; hand side was **96.2 fF** (−28 fF)
[PEX-RC/HAND].

**Frequency [PEX-RC lumped]** (`summary_pex_vco_range.txt`): **not** a full
post-layout run of the 17.5k spice. Schematic PDK devices + extracted wiring
C/R lumped per tank net. 15 corners PASS (worst top **143 MHz**, bot **78 MHz**);
overlap PASS; boundary ≤½ LSB PASS; D20 proxy PASS [PEX-RC lumped].

**Die** (`summary_pex_vco_die.txt`): full-cell bbox **0.4624 mm²** [GDS] →
`spec/p27-floorplan.md` §8.

### P2.7.3b — post-layout VCO phase noise (2026-11-18) — PASS

**Parasitics** (`layout/p272c/out/summary_pex_vco_pn_parasitics.txt`) [PEX-RC]:
- Tail for PN separated from cbf/filter: **C_tail_pn = 9.55 fF** (wiring-all
  31.4 fF; anon ≥5 fF 21.84 fF treated as filter-like, excluded). Hand 9.9 fF.
- Pad residual after sub−Σ(MIM plates): **0 / 0 fF**; pad C carried by L2n0 EM
  `cp` + wiring add, not a separate term [PEX-RC/EM].
- Couplings ≥1 fF: tn−tp 29.2; tp−vbp 10.8; tn/tp−tail 4.4/4.0; tp−vt 2.8 fF.

**PN netlist [PEX-RC lumped]:** schematic PDK devices + L2n0 EM + lumped C_side
68.22 fF / R 0.24 Ω + C_tail_pn + couplings ≥1 fF. Bank bypass omitted (PSS);
tail+var bypass on. Magic 2-terminal svaricap **not** used — schematic
4-terminal PDK svaricap kept [TOOL].

**PSS / pnoise** (`summary_pex_vco_pn.txt`) [PEX-RC lumped]: all five points
converge. With bank +0.59 [SCH] + det 0 [HAND] + CML +0.5 [HAND]:

| point | L@100 kHz | L@1 MHz (→w/ bounds) | limit | margin |
|---|---:|---:|---:|---:|
| ss85 4.20 | −88.1 | −119.3 → −118.2 | −116 | **+2.2** |
| tt 3.65 | −92.6 | −122.4 → −121.3 | −116 | +5.3 |
| tt 4.20 | −87.9 | −119.3 → −118.2 | −115 | +3.2 |
| tt 3.12 | −97.8 | −125.1 → −124.0 | −116 | +8.0 |
| tt 3.20 | −96.8 | −124.8 → −123.7 | −115 | +8.7 |

**Duplex** (`summary_pex_duplex_pn.txt`) [MODEL]: post-layout VCO curve + D19 /
CP FoM −203.8 / LO floors. Worst **VHF 175 MHz −137.8 dBc/Hz, +1.8 dB** vs −136
(was +2.8 SCH). PASS.

**Hand bounds:** not re-simulated in the PEX netlist (bank omitted for PSS);
kept [SCH]/[HAND] as above [TOOL].

### P2.7.3c — swing / D22 / peak / wake (2026-11-18) — PASS

**Netlist [PEX-RC lumped]:** sch PDK + L2n0 EM + lumped C_side 68.22 fF /
R 0.24 Ω + C_tail_pn (Rtail=10 Ω) + couplings. D22 det/cmp on. vbp C folded
to gnd when vbp ideal/absent; SAR omits C(tail−tn/tp) (fold → C_tail_pn);
`Rtb_op`=1 MΩ on det `tb` for VACASK OP @ 85 °C [TOOL].

**Swing** (`summary_pex_vco_swing.txt`) [PEX-RC lumped]: 30 corners at accepted
fab-retune codes. Bottom ff/wcs/85 code 31 **0.658 V ≥ 0.54 V**; all steady
≤ 1.40 V. Det tank load ≤10 fF/side (tn 4.59 / tp 4.54 fF) [PEX-RC]. **PASS.**

**D22 SAR** (`summary_pex_vco_d22_search.txt`) [PEX-RC lumped]: 30 cases
tt/ss/ff × CAP × −40/27/85 × top/bottom. Tops in 1.25±0.10 or tnr; bottoms
code 31 + tnr; steady ≤1.40; peak ≤1.50. Several 85 °C tops land code 31 /
tnr=1 with Amp still in window (cmp soft with PEX). **PASS.**

**Peak MC (prior)** (`summary_pex_vco_peak_mc.txt`) [PEX-RC lumped]: 1.250 V at
bit=−1 / code 31 with Cctl omitted — final Amp, not SCH mid-SAR peak.

**Peak MC sch-style re-run** (`summary_pex_vco_peak_mc_schstyle.txt`) [PEX-RC
lumped]: Cctl included; Rtb_op=1 MΩ on det SF bias `tb` only (not hold/rep/tank;
OP at 85 °C [TOOL]); peak = max over SAR trials. Nominal trail Amp 1.153→1.249
(monotonic; bit3/c24 = 1.214, not SCH 1.493). N=5 Vos: peak+3σ **1.249 ≤ 1.50 V**.
**PASS.** **P2.7.3 VCO complete.**

**Wake** (`summary_pex_vco_wake.txt`) [MODEL]: max **130 µs ≤ 150 µs**. **PASS.**

Next: **P2.7.4** LO divider layout (floor with layout C first).

### D9 filter capacitor notes (2026-11-13) — MIM kept; MOS swing cause

**Device:** `cbf` = 50 pF **rfcmim** W=L=182.574 µm (cmim PCell clamps; side ≥ 7 µm → rfcmim) [PDK]. MOS rejected (`decisions.md` 2026-11-13); D23 island ≤ 0.34 mm².

**MOS swing 1.20 → 0.93 V — cause [SCH/HAND]** (`layout/p272b_tail/out/summary_mos_swing_cause.txt`):

- Ig @ 0.6 V ≈ 42 nA → Ig×1 MΩ ≈ 42 mV [SCH]. OTA raises `nb` by that order and **holds `nbf` / Itail** (OP ΔItail −0.1 % with forced V(tail)=0.35 V) [SCH].
- Therefore DC Ig×1 MΩ alone does **not** explain the −22.5 % swing drop.
- Retained mechanism: thin-ox moscap C(V) + channel conductance under the large-signal bias filter, with bias Sid +3.2 dB @ 100 kHz and VCO ΔL +0.516 dB @ 100 kHz vs ideal [SCH `summary_d9_finding`]. MIM restores the filter; no design change for MOS.
