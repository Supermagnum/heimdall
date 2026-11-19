# LO divider and phase-generation topology memo (P2.4)

Status: **topology accepted by the owner, 2026-10-20 (§4: D12 VCO capped at 4 mA, D13 and D14 as proposed). Step 1–3 done; P2.4 accepted 2026-10-21.** P2.6 UHF floor −150.1 dBc/Hz [SCH]. **P2.7.4a3 sizing accepted** (D7 PASS 8.18 / 8.66 mA). **P2.7.4b step0 PASS** (VHF ff re-check; MC 0.51° = VHF 8-phase OK vs ~1° HR). First latch GDS **DRC/LVS FAIL** — stop. Numbers are hand estimates `[HAND]` unless marked. Inputs: the simulated VCO (`spec/vco-topology.md` §9), D4 and D7 (`spec/phase2-plan.md` §5), `spec/rf-frontend.md` §3–5, `spec/derived-limits.md` §7.3–7.4.

---

## 1. Requirements

| Item | Value | Source |
|---|---|---|
| Input | VCO 2.90–4.41 GHz (band use 3.12–4.20), differential, about 1.0–1.3 V from the VCO buffer | P2.3 |
| UHF | ÷8: 400–480 MHz from 3.20–3.84 GHz; quadrature (I/Q) | `band_sel` = 0 |
| VHF | ÷24: 130–175 MHz from 3.12–4.20 GHz; **8 phases** (45°) for the harmonic-reject mixer | D4, `band_sel` = 1 |
| Harmonic rejection | VHF 3 × LO response ≥ 60 dB **including board preselection**; the mixer's own share is set in Phase 3 | `spec/rf-frontend.md` §3, `[DER]` §7.3 |
| Image | TX image ≥ 40 dB after host calibration; RX the same order | `spec/rf-frontend.md` §4 |
| Phase noise | The divider chain's own floor well below the divided VCO noise at the duplex offsets: VCO −119 dBc/Hz at 600 kHz ÷ 24 → −147 at the LO; **chain floor ≤ −150 dBc/Hz** at the LO output `[PROP]` | R4 (−136 / −139 dBc/Hz) |
| Speed margin | First stages at up to 4.41 GHz at slow corner, 1.08 V, 125 °C | Risk table, `spec/phase2-plan.md` §6 |
| Current | LO total ≤ 10 mA (D7) with the VCO at 3.4–5 mA (P2.3: the 4 mA cap was not chosen) | D7, P2.3 review |
| Users | RX mixer (passive, quadrature, HR on VHF) and TX IQ modulator, one at a time on this single-chain chip | `spec/rf-frontend.md` §7 |

A correction to an older text: `spec/derived-limits.md` §7.4 says "÷24 built as ÷12 then ÷2" (I/Q only). D4 replaced that with ÷3 then an 8-phase ÷8; the text there is updated with this memo.

## 2. Proposed topology

```
                          ┌─► UHF: CML ÷2 ─► CMOS ÷4 Johnson (2 DFF) ─► 4 phases ─► 25 % duty (AND) ─► I/Q drivers
VCO ─► CML buffer ─┤                (≤ 2.2 GHz)        (≤ 0.96 GHz)          (400–480 MHz)
     (P2.3 stand-in)│
                    ├─► VHF: CML ÷3 ─► CML→CMOS ─► CMOS ÷8 Johnson (4 DFF) ─► 8 phases (45°) ─► HR mixer drivers
                    │      (≤ 4.41 GHz)              (≤ 1.47 GHz)               (130–175 MHz)
                    └─► PLL feedback (multi-modulus divider, P2.5)
```

1. **Shared CML buffer after the VCO** (replaces the P2.3 stand-in): isolates the tank from the dividers and the band switch; its input capacitance is in the VCO budget. One output branch per user (UHF chain, VHF chain, PLL feedback), unused branches off.
2. **UHF: CML ÷2, then a CMOS ÷4 Johnson counter.** The ÷2 runs at up to 4.41 GHz (static CML latch pair, the textbook circuit). A Johnson (twisted-ring) counter of 2 D flip-flops divides by 4 and gives four outputs 90° apart, edge-timed by the same clock, so the quadrature does not depend on the input duty cycle. **25 % duty** pulses (AND of adjacent phases) are the usual LO for a passive quadrature mixer (lower noise and better I/Q isolation than 50 %).
3. **VHF: CML ÷3 at the VCO rate, then a CMOS ÷8 Johnson counter (D4).** A Johnson counter of 4 flip-flops divides by 8 and gives 8 outputs 45° apart, again timed by single clock edges, so the ÷3's output duty cycle does not matter (only its period, which is exact). This is why D4 needs no 50 %-duty ÷3. Whether the HR mixer wants 50 % or 12.5 % non-overlapping phases is a Phase 3 choice; both come from the same 8 outputs with simple logic.
4. **Retiming:** the last stage of each chain is clocked directly by the fast clock, so phase accuracy is set by flip-flop mismatch (a few ps), not by accumulated delays. At 175 MHz, 1° is 15.9 ps.
5. **Band switching:** `band_sel` powers one chain; the other is off (current and spurs). `FILT[4]` (8-phase enable) already exists in the register map.

**Alternatives considered:**
- ÷24 as ÷12 then ÷2 (the older text): gives I/Q only, no 8 phases for the HR mixer — excluded by D4.
- SiGe HBT (ECL) first stages: easy at 4.4 GHz and low current, but need ≥ 2.5 V and a level shift to CMOS; kept as the fallback if the CML ÷3 lacks speed margin at the slow corner.
- Injection-locked dividers: low power but narrow locking range; cannot cover 30 %.

## 3. Estimates `[HAND]`

| Item | Estimate | Comment |
|---|---|---|
| CML ÷2 at 4.41 GHz | 1.0–1.5 mA | Static CML in 130 nm toggles well above 10 GHz at typical; the slow corner is checked in step 1 |
| CML ÷3 at 4.41 GHz | 1.5–2.5 mA | The tightest stage: three latches plus logic in the loop. **Main speed risk** |
| CML buffer | about 1 mA | |
| CMOS Johnson ÷4 at ≤ 2.2 GHz / ÷8 at ≤ 1.47 GHz | 0.2–0.5 mA (C·V²·f) | True single-phase-clock flip-flops; margin at slow corner and 125 °C checked in step 1; CML if not enough |
| Phase accuracy | about 0.2–0.5° (1σ) from flip-flop mismatch | Monte Carlo in step 3. Untrimmed, about 1° phase and 1 % gain mismatch give roughly 40 dB HR3, so the 60 dB needs board preselection as well (Phase 3 split) |
| Chain noise floor | −155 to −160 dBc/Hz typical for CMOS dividers at the output | Checked with pnoise/noise in step 3 |
| Mixer drivers | 1–3 mA, depending on the mixer switch size (C·V²·f at 130–480 MHz) | Counted with the mixer in Phase 3, not here |

**LO current (D7 ≤ 10 mA), VHF worst case (before D12):** VCO 5 mA (bottom band) + buffer 1 + CML ÷3 2 + Johnson 0.5 + PLL (PFD, CP, MMD, Σ-Δ) about 1.5 mA = **about 10 mA, at the limit**; UHF about 8.5 mA. With the mixer drivers on top, the receive chain's 25 mA budget is affected. After D12 (VCO ≤ 4 mA): about 9 mA VHF, 8 mA UHF.

## 4. Decisions (2026-10-20)

| # | Decision | Proposal | Reason |
|---|---|---|---|
| **D12** | LO current budget | **Decided: cap the VCO at 4 mA**; the LO budget stays ≤ 10 mA (proposed was 11 mA or the cap) | The VHF chain plus a 5 mA VCO reaches the 10 mA of D7 before any margin; the 4 mA cap costs about 2 dB of phase noise at the band bottom (still 6 dB margin) |
| **D13** | UHF LO waveform | **4 phases, 25 % duty** | Standard for passive quadrature mixers; no extra divider stage |
| **D14** | Flip-flop style after the first stage | **CMOS (true single-phase clock)**, CML if step 1 shows less than 1.3× speed margin at slow corner / 1.08 V / 125 °C | Lowest current; the speed check decides |

Interface consequences: none for the register map (`band_sel`, `FILT[3:4]` exist). `spec/derived-limits.md` §7.4 is corrected to the D4 structure.

## 5. Step 1 — device checks before the schematic

Small VACASK transients, typical and slow corner (1.08 V, 125 °C):
1. **CML latch / ÷2:** maximum input frequency against tail current and load; pick the current for ≥ 1.3 × 4.41 GHz at the slow corner.
2. **CML ÷3:** the same at 4.41 GHz.
3. **TSPC flip-flop:** maximum toggle frequency against size at the slow corner, for the 1.47 GHz (VHF) and 2.2 GHz (UHF) clocks.
4. **CML→CMOS converter:** duty cycle and delay at 1.47 GHz.

## 6. After the review

| Step | Work | Gate |
|---|---|---|
| 1 | Device checks (§5) | Result review: confirms or changes §2 |
| 2 | Schematic of both chains with the VCO buffer; transient with the P2.3 VCO | — |
| 3 | Corners and temperature: maximum frequency, duty cycle, I/Q and 8-phase errors (Monte Carlo), noise floor, current | Result review against §1 |

## 7. Step 1 results (2026-10-20)

Source: `analog/lo/step1/` (VACASK, PDK `a49358cc`) `[SCH]`. Ideal clocks and supplies; tails ideal current sources.

| Block | Result | Consequence |
|---|---|---|
| TSPC flip-flop (D14) | Toggles up to 6–7 GHz typical, **4.0 GHz at slow corner** (1.08 V, 125 °C) for all three sizes: 2.7× margin for the VHF Johnson clock (1.47 GHz), 1.8× for UHF (2.2 GHz) | **CMOS TSPC confirmed** (≥ 1.3×); smallest size is enough |
| CML-to-CMOS converter | Duty 50–51 % typical, 45–46 % slow corner, full CMOS levels at 1.47 and 2.2 GHz | Adequate: the Johnson counters use one clock edge |
| CML ÷2 | 0.5 mA per latch, **1.0 mA**; with enough clock swing divides 2–8 GHz at slow corner, 2–12+ GHz typical | UHF first stage as proposed |
| CML ÷3 (two CML flip-flops + single-level NOR) | 0.5 mA per latch, **2.5 mA**; with enough clock swing divides 2–6.5 GHz at slow corner, 2–8 GHz typical | VHF first stage as proposed; 1.3× margin over 4.41 GHz at slow corner holds |
| **Clock swing** | With 0.27 V per side both fail below about 5 GHz at the slow corner (they free-run instead of following the input). Minimum swing for the whole window (÷2 2.9–5.0, ÷3 2.9–5.7 GHz): slow 0.35 V (÷2) / **0.40 V (÷3)**, typical and fast (1.32 V, −40 °C) 0.30 V; values at a 1.2 V scale (×0.9 at 1.08 V) | **Requirement for the VCO buffer: ≥ 0.5 V per side** (25 % over the ÷3 minimum) at a common mode about 0.55 V below V_DD |
| Variants rejected | A latch pair twice as wide adds nothing; a tail-less latch is starved at the slow corner (fails everywhere) | Keep the plain CML latch with a tail source |

**LO current with D12** `[HAND]`: VHF ≈ VCO 4 + buffer 1 + ÷3 2.5 + Johnson and converter 0.6 + PLL 1.5 = **9.6 mA**; UHF ≈ 4 + 1 + 1.0 + 0.6 + 1.5 = **8.1 mA** (D7: ≤ 10 mA). The VHF margin is small; the buffer is the item to watch.

**Buffer note for step 2:** the VCO tank swings about 0.41 V per side at the bottom band with the 4 mA cap, so a capacitor-coupled tap of the tank alone does not reach 0.5 V with margin. Step 2 designs the buffer for ≥ 0.5 V per side into the divider inputs at all corners.

## 8. Step 2 — buffer and chains with the VCO (2026-10-20)

Source: `analog/lo/step2/` (VCO from P2.3, 4 mA cap, D12) `[SCH]`, typical (1.2 V, 27 °C) and slow corner (mos_ss, 1.08 V, 125 °C). Buffer: per side 100 fF from the tank, self-biased CMOS inverter 2/4 µm, inverter 6/12 µm (final: 3/6 then 4/8 µm, see below), cross-coupled anti-phase inverters; CML ÷2 / ÷3 (step 1), enabled after VCO start-up (D15); converter with a tapered clock driver (to 9/18 µm); TSPC flip-flops size 2; every output retimed by a TSPC flip-flop on the divided clock.

| Case | Phase error (max) | Duty | Buffer per side | Currents: buffer / CML / converter / logic (mA) |
|---|---|---|---|---|
| UHF typ 3.20 GHz | 0.21° | 24.2–24.3 % | 0.62 V | 0.76 / 1.00 / 0.63 / 0.24 |
| UHF typ 3.84 GHz | 0.25° | 23.9–24.1 % | 0.63 V | 0.83 / 1.00 / 0.69 / 0.28 |
| UHF slow 3.20 GHz | 0.36° | 23.3–23.6 % (24.7–25.0 with `pq=2`) | 0.52 V | 0.51 / 1.00 / 0.59 / 0.21 |
| UHF slow 3.84 GHz | 0.46° | **20.6–21.4 %** (22.6–23.7 with `pq=2`) | 0.54 V | 0.62 / 1.00 / 0.62 / 0.23 |
| VHF typ 3.12 GHz | 0.07° | 49.1–50.0 % | 0.62 V | 0.88 / 2.49 / 0.58 / 0.26 |
| VHF typ 4.20 GHz | 0.09° | 48.9–50.1 % | 0.63 V | 1.07 / 2.50 / 0.69 / 0.35 |
| VHF slow 3.12 GHz | 0.10° | 48.9–49.9 % | **0.43 V** (target 0.45), clock duty 43.7 %, skew −20 ps | 0.55 / 2.50 / 0.55 / 0.22 |
| VHF slow 4.20 GHz | 0.12° | 48.7–49.6 % | 0.47 V | 0.77 / 2.51 / 0.63 / 0.30 |

- **All 8 cases divide correctly**, systematic phase errors ≤ 0.46° (UHF) and ≤ 0.12° (VHF); random mismatch follows in step 3.
- **UHF 25 % duty:** the TSPC output rises one gate later than it falls, so the pulses come out short at the slow corner. A 2× output PMOS (`pq=2`, now the default) gives 22.6–25.0 %. A 2 % short pulse costs a passive mixer about 0.1–0.2 dB of conversion gain and no overlap; accepted for now, final check with the mixer in Phase 3.
- **Buffer at the bottom band, slow corner:** 0.43 V per side, just below the 0.45 V target (the ÷3 still divides; step 1 minimum 0.36 V at 1.08 V). **Final buffer:** an extra 3/6 µm gain inverter per side and the last inverter shrunk to 4/8 µm: VHF all four cases correct (≤ 0.12°), **0.53–0.56 V per side at the slow corner**, 0.64–0.65 V typical; buffer current 0.74–1.25 mA (worst VHF typical 4.20 GHz, +0.18 mA against the table above).
- **LO current, worst case (VHF typ 4.20 GHz, final buffer):** buffer 1.25 + CML 2.49 + converter 0.70 + logic 0.36 = 4.80 mA; with the VCO (3.59 mA there) and the PLL (about 1.5 mA, `[HAND]`) **about 9.9 mA**; bottom band 4.30 + 4.00 + 1.5 = 9.8 mA. Against D7 ≤ 10 mA: inside, but only about 0.1 mA margin, and the PLL share is still a hand estimate; the converter (0.6–0.7 mA, mostly its clock driver) and the buffer are the places to save in layout-aware sizing. UHF about 8.3 mA.

**Start-up trap (finding).** A CML divider that is on while its clock is absent free-runs (here about 2.2–3.1 GHz at 0.15–0.17 V). Step-1 check `div3s` at the slow corner: with the clock ramping up (5 or 20 ns) the ÷3 stays in that state at 4.41 GHz, even with 0.6 or 0.75 V final swing; enabled after the clock is up it divides at 3.12, 4.21 and 4.41 GHz. Clock shape, duty cycle (40–50 %), converter load and latch current were ruled out first (`div3x`).

**D15 (owner, 2026-10-20): sequenced divider enable.** `en_lodiv` is raised by the AFE sequencer about 1 µs after `en_vco` (VCO start-up is tens of ns), and pulsed low again after a band change (`BAND`, `VCO_BAND` writes) and when the PLL fails to lock within its window. Applies to both chains (the ÷2 showed no trap, but the cost is nil). No extra current; a few gates in the AFE block (`spec/analog-digital-interface.md` §6).

Step 3: §9.

## 9. Step 3 — corners, temperature, Monte Carlo (2026-10-21)

Source: `analog/lo/step3/` `[SCH]`. The VCO replaced by an ideal sine on the tank nodes at the **lowest VCO swing** for that frequency (0.27 V per side at 3.12 GHz … 0.52 V at 4.20 GHz), so every corner sees a pessimistic clock. Corners: tt 1.2 V 27 °C; ss 1.08 V 125 / −40 °C; ff 1.32 V −40 / 125 °C; sf, fs 1.2 V 27 °C. Monte Carlo: PDK mismatch (σV_T 3.9 / 2.2 mV·µm, σβ 0.5 / 0.33 %·µm, σW 4 nm, σL 2 nm) on every LO transistor, as gate offset sources and width changes; 25 samples per case.

**Problems found and fixed** (five runs; each fix costs no extra current):

| # | Problem | Cause | Fix |
|---|---|---|---|
| 1 | VHF ÷3 divides by 2 (2.10 GHz, 0.05–0.17 V) at ff 125 °C and in 8 of 12 slow-corner samples, despite D15 | Weak latch regeneration: a low-swing mode locked to f/2 is stable; which mode the ÷3 lands in depends on start-up | Regenerative pair **1.5×** wider and CML swing **0.5 V** (was 0.4); the ÷3 reference follows the swing (V_DD − I·R_L/2). Each alone passes; both kept. No start-up pulse needed |
| 2 | UHF counter miscounts in 5 of 12 slow-corner samples | The CML-to-CMOS converter's output duty fell to 23–37 % at 1.92 GHz, too short a clock-high time for the TSPC flip-flops (larger flip-flops or a stronger clock driver made it worse) | **Converter built like the buffer:** CML outputs AC-coupled (50 fF) into self-biased 2/4 µm inverters (50 kΩ), anti-phase cross-coupling, a second AC-coupled self-biased stage, then the 3/6 → 9/18 µm clock driver. Clock duty now 47–52 %; converter current 0.32–0.80 mA (was 0.55–0.80) |
| 3 | Bottom of the band: buffer duty drifts to 58–69 % with a small tank swing | The middle buffer inverter's fixed threshold | **Middle buffer stage AC-coupled and self-biased** (50 fF, 50 kΩ) |
| 4 | VHF ff 125 °C: no DC operating point | Simulation only (floating TSPC nodes) | Supplies ramp from 0 in the testbench |

**Corners (final circuit):** all 28 cases divide except the bottom band at ss −40 °C (UHF 3.20, VHF 3.12 GHz) with the pessimistic 0.27–0.29 V tank swing. Minimum tank swing per side at the bottom of the band:

| Corner | Minimum swing | VCO gives (P2.3, 4 mA) | Margin |
|---|---|---|---|
| ss 125 °C | < 0.25 V (both bands) | ≈ 0.29–0.30 V (from 0.32 V at 85 °C) | > 15 % |
| ss −40 °C | 0.33 V (both bands) | ≈ 0.43 V (0.87 V differential, MIM worst case) | ≈ 30 % |

So the ss −40 °C failures come from combining the cold slow corner with the hot fast-corner VCO swing; with the VCO's own swing there it passes. Systematic errors: UHF phase ≤ 0.49°, duty 24.0–25.8 %; VHF phase ≤ 0.13°, duty 47.9–51.1 %.

**Monte Carlo (final circuit): 100 of 100 samples divide.**

| Case | Largest phase σ | Quadrature error (Q+ vs I+) | Raw image rejection at 3σ (phase only) | Duty σ |
|---|---|---|---|---|
| UHF tt, 3.84 GHz | 0.47° (2.7 ps) | −0.11° ± 0.37° | 39.5 dB | ≤ 0.19 % |
| UHF ss 125 °C | 0.77° (4.5 ps) | −0.12° ± 0.61° | 35.4 dB | ≤ 0.28 % |
| VHF tt, 4.20 GHz | 0.17° (2.7 ps) | — | — | ≤ 0.25 % |
| VHF ss 125 °C | 0.28° (4.4 ps) | — | — | ≤ 0.10 % |

The UHF image target (≥ 40 dB) applies after host I/Q calibration, which removes this static error; raw 35–40 dB is in line with the estimate in §3 (0.2–0.5° typical). For VHF, about 0.2–0.3° σ is the input to the harmonic-reject mixer budget in Phase 3 (§3: about 1° gives about 40 dB HR3 untrimmed).

**Chain current (buffer + CML + converter + logic):**

| Corner | UHF 3.20 / 3.84 GHz | VHF 3.12 / 4.20 GHz |
|---|---|---|
| tt 1.2 V 27 °C | 2.53 / 2.79 mA | 4.14 / **4.56 mA** |
| ss 1.08 V 125 °C | 2.16 / 2.41 mA | 3.68 / 4.11 mA |
| ff 1.32 V −40 / 125 °C | 2.98–3.36 mA | 4.65–**5.23 mA** |

LO total at typical, VHF 4.20 GHz: 4.56 + VCO 3.59 + PLL ≈ 1.5 (`[HAND]`) ≈ **9.65 mA** (D7 ≤ 10 mA). At the fast corner with 1.32 V the CMOS parts draw more: ≈ 10.3 mA. Whether D7 is a typical or worst-case limit, and whether the LO supply really reaches 1.32 V (it comes from an LDO, `VR_ANA1`), was settled 2026-10-21 (owner, `decisions.md`): D7 is a typical figure and is met; the fast-corner figure is a maximum; the margin is checked again with the real PLL in P2.5.

**Noise floor (target ≤ −150 dBc/Hz at the LO output, §1).** A driven pss/pnoise of the edge-setting path (buffer, CML ÷N, converter, one TSPC flip-flop as ÷2; `run_step3.py noise`) gave results that are **not usable**: flat from 0.1 to 20 MHz, at −107 / −126 dBc/Hz (UHF tt / ss) and −113 / −130 dBc/Hz (VHF tt / ss), typical 17–20 dB *worse* than slow, the same at a floating and at a driven output node. That pattern (white, corner-inverted, far above any physical source in the path) points at the method — pss/pnoise on dynamic CMOS logic with 1 GΩ-held nodes, at loosened tolerances — not at the circuit. The validated use of pnoise (P2.0) is LC oscillators.

Hand estimate instead `[HAND]`: edge jitter of the path ≈ 25 fs per CMOS gate (about 10 gates incl. buffer, converter, driver, flip-flop) and ≈ 50 fs per CML latch (2), σ ≈ 0.1 ps rms, white. With one sampled edge per LO period, L ≈ 4π² f_LO σ²: **≈ −157 dBc/Hz at 480 MHz (UHF), ≈ −161 dBc/Hz at 175 MHz (VHF)**; with twice the jitter −151 / −155. Below the target, and 9–16 dB under the divided VCO noise at the 1 MHz and duplex offsets (UHF −139.7, VHF −147.6 dBc/Hz at 1 MHz); beyond about 5–10 MHz the divider floor dominates the LO. The kT/C noise of the 50 fF / 50 kΩ AC-coupled stages adds about 45 fs (−158 dBc/Hz at 480 MHz alone). **Verification by simulation moves to P2.6** (closed loop with transistor-level dividers), with a sampled-edge jitter method or transient noise on the edge path.

**Final circuit** (step-3 defaults in `analog/lo/step3/run_step3.py`, on top of `analog/lo/step2/run_step2.py`): buffer 2/4 → AC-coupled self-biased 3/6 → 4/8 µm per side, anti-phase cross-coupling; CML ÷2 / ÷3 0.5 mA per latch, swing 0.5 V, regenerative pair 1.5×, enabled after VCO start-up (D15); AC-coupled self-biased converter with 3/6 → 9/18 µm clock driver; TSPC flip-flops size 2; all outputs retimed (UHF retiming output PMOS 2×).

## 10. P2.7.4a — divider inventory and layout gate (2026-11-19)

### Hierarchy completeness [TOOL]

| Item | Status |
|---|---|
| xschem `.sch` hierarchy | **Missing** — only Python netlist builders (`step1/2/3`) |
| Sim netlist source | Flat VACASK decks from those scripts [SCH] |
| Ideal parts (list) | CML latch **isource** tails; step3 **ideal tank sine**; TSPC **1 GΩ** node holds; ideal VDD domains; step1 `clk.va`; start-up kick **off** (`nokick`) |
| Real MOSFET tails / LO buffers to mixers | Not yet — tails stay ideal until xschem + bias cell |

**Found, not done:** capture hierarchical xschem (prompt 06 / P2.7.4) so layout
LVS matches a flattened sch, as for the VCO.

### Sub-block inventory

Counts from `cml_latch` / `cml_dff` / `tspc` / `buffer` / `converter_ac` source
templates [SCH]. Multifinger `ng` not used (single finger widths).

| Sub-block | MOS | R / C / I (on-chip) | Accepted performance |
|---|---:|---|---|
| CML latch | 6 NMOS | 2×RL, 1×Itail | building block |
| CML ÷2 (1 MS DFF) | **12** NMOS | 4×RL, 2×Itail (1.0 mA) | Slow: divides with ≥0.5 V/side; f_max ≫ 4.41 GHz [SCH] §7 |
| CML ÷3 (2 DFF + NOR) | **27** NMOS | ~6×RL, 5×I (2.5 mA) | Same; regenerative k=1.5, swing 0.5 V [SCH] §9 |
| LO buffer (final) | ≈ **16–20** | 100 fF + 50 kΩ AC; anti-phase | ≥0.5 V/side into CML; duty fixed by AC middle [SCH] §8–9 |
| CML→CMOS converter (AC) | ≈ **20–24** | 50 fF / 50 kΩ stages; ck drv 3/6→9/18 | Duty 47–52 % [SCH] §9 |
| TSPC FF (size 2) | **9** | — | Toggle ≥4 GHz slow [SCH] §7 |
| UHF Johnson ÷4 + 25 % + retimes | 2×TSPC + 2 inv + 4×(NAND+TSPC) ≈ **70** | 20 fF loads | Phase err ≤0.46°; duty ~24–26 % [SCH] §8–9 |
| VHF Johnson ÷8 + retimes | 4×TSPC + invs + 8×TSPC ≈ **120** | 10 fF loads | Phase ≤0.13°; duty ~48–51 % [SCH] §8–9 |
| Bias / enables | D15 `en_lodiv` in deck | Ideal Itail until bias cell | Sequencer 1 µs after `en_vco` [D15] |
| LO output buffers to mixers | **not sized** | Phase 3 | — |

**Noise floors (pre-layout):** UHF **−150.1** dBc/Hz (3–10 MHz) [SCH]; VHF
**−154.0 … −155.5** [SCH]; P2.4 HAND −157 / −161. I/Q phase ≤0.46°; 8-phase
σ ≤0.28° ss [SCH] §9.

### UHF floor with layout parasitics [HAND / SCH]

See `analog/lo/step3/out/summary_p274a_uhf_floor_layout_c.txt`. Compact C_ck ≈
12–15 fF/side → scaled floor **≈ −147.8 dBc/Hz FAIL** vs ≤ −150 (P2.7.4a).

### P2.7.4a2 — xschem capture + floor fix (2026-11-19) [SCH]

| Item | Status |
|---|---|
| xschem hierarchy | **`lo_bias` / `lo_uhf_top` / `lo_vhf_top`** + SVG/PDF; netlists from sch [`analog/lo/sch/`] |
| Ideal parts removed | CML MOSFET tails on `nb_lo`; TSPC Q-only keepers + 100 Meg on a/b (no 1 GΩ) |
| Remaining TB inputs | `tp`/`tn` VCO; split supplies; `nbias` stand-in; `en_lodiv`; VHF `vref` |
| Equiv tt | UHF/VHF PASS; phase ≤0.24° / ≤0.08° [SCH] |
| Equiv ss | UHF PASS at I_latch=0.75 mA + RL sync [SCH]. VHF ss **FAIL** with MOSFET tails (CML ÷3 dead at 1.08 V); **PASS** with ideal `isource` tails [SCH]. Headroom-limited — owner redesign before VHF GDS |
| MC / f_max slow | **Not completed** (docker races) |
| Per-stage noise C_ck=15 fF | ZOH→TIE L(f) avg 3–10 MHz (p26 HAND scale): UHF **−154.7 PASS**; VHF **−158.6** [SCH] |
| Dominant stage | **logic** (−157.5 → LO) [SCH] |
| Fix | I_latch **0.5 → 0.75 mA**; B2 unchanged; keepers as above |
| D7 | UHF LO ≈ **8.44 mA OK**; VHF LO ≈ **10.69 mA over** by ~0.69 mA [HAND] |
| Peak MC N=20 | VCO ampcal sch-style **PASS** 1.249+3σ ≤1.50 [PEX-RC lumped] (re-check after floor knobs) |

Detail: `analog/lo/sch/out/summary_equiv_lo.txt`, `summary_stage_noise.txt`,
`summary_floor_fix.txt`.

### Floorplan sketch [HAND] (Option A)

LO buffer input faces VCO tank south; CML ÷2/÷3 next; converter + TSPC south
toward mixers; away from inductor and V_tune (NE). Symmetric clock trees for
I/Q and 8-phase. Area estimate with I_latch=0.75 mA: buffer+CML+conv+TSPC
**≈ 0.05–0.09 mm²** [HAND] (`p27-floorplan` §8); die re-total unchanged until GDS.

## 11. P2.7.4a3 — VHF ÷3 diagnosis before topology (2026-11-19) [SCH]

Decision recorded: `decisions.md` “VHF ÷3: diagnosis before topology”. No production
schematic change this run (TB / knobs only). Source:
`analog/lo/sch/out/summary_vhf_freq_diag.txt` (`run_vhf_freq_diag.py`).
mos_ss / 125 °C; I_latch=0.75 mA; swing=0.5; real buffer B2=4; MOSFET NOR tail.
TD = stacked tailed latches; TL = `VARIANT['tailless']` (clock→gnd).

#### Frequency sweep (VCO rate)

| Mode | VDD | 3.12 | 3.40 | 3.70 | 4.00 | 4.20 | Class |
|---|---:|---|---|---|---|---|---|
| TD | 1.108 | FAIL | FAIL | FAIL | FAIL | FAIL | **headroom** (all f) |
| TD | 1.080 | FAIL | FAIL | FAIL | FAIL | FAIL | **headroom** (all f) |
| TL | 1.108 | OK | OK | OK | OK | OK | all PASS (buf 0.42–0.48 V/side) |
| TL | 1.080 | OK | OK | FAIL | FAIL | FAIL | **drive/BW** (fails ≥ ~3.70 GHz) |

At TD fail points buffer is still 0.40–0.50 V/side and tail V_DS ≈ 0.07–0.10 V
(triode) [SCH]. Higher VCO swing not allowed (D22). Detail table in the summary.

#### Re-ordered chain (÷2 → ÷3 → ÷4)

- **8-phase VHF required** for the harmonic-reject mixer: **D4** (`decisions.md`
  2026-10-19; `spec/phase2-plan.md` §5; §1 above). Phase 3 still sizes the mixer's
  HR share; D4 is not revoked.
- ÷2×÷3×÷4 = ÷24 (ratio OK) but Johnson ÷4 → **4 phases only** — fails D4.
  Eight phases need dual-edge / interleaved ÷4 on a **50 %-duty** ÷3 at f_VCO/6
  (cost [HAND]: duty constraint, edge-matched dual counters, phase-error risk).
- ÷3 at ≤ 2.1 GHz [SCH]: **TD FAIL** all points at 1.08 and 1.05 V (buf ≥ 0.54 V/side)
  — still headroom. **TL PASS** all ≤ 2.1 GHz at 1.08 and 1.05 V. Re-order alone
  does not revive the stacked latch.

#### Option table (owner pick; not implemented)

| Opt | Corners / 30 mV margin | Extra I vs D7 | Area [HAND] | 8-ph / duty | Schematic change |
|---|---|---|---|---|---|
| **a** Tail-less + faster buffer (≥0.5 V/side @ 4.20 ss) | Full band PASS @ 1.108 [SCH]; @ 1.08 FAIL ≥3.70; prior 1.05@3.12 FAIL; B2=8 + default tank FAIL 4.20 ss; B2=6 + tank 0.75 PASS [SCH prior] — **not closed without D22** | Buf +0.5–1.5 mA [HAND]; VHF LO already 10.69 mA over D7 [HAND a2] | +buffer small | Keep ÷3→÷8; TL match/noise open | `tailless` + buffer redesign |
| **b** Folded PMOS-load ÷3 | Not sim'd here; targets stack headroom (ideal `isource` PASS [SCH a2]) [PROP] | ÷3 ~2.5–3.5 + bias ~0.2–0.5 mA [HAND] | New cell +20–40 % | Keep D4; re-check MC | New folded latch + bias; xschem redo |
| **c** Re-order ÷2→÷3→÷4 | TL ÷3 PASS ≤2.1 @ 1.08/1.05 [SCH]; TD still FAIL — still needs TL or folded | +÷2 ~1 mA if not shared [HAND] | +÷2 / dual-edge | **4 ph** unless dual-edge 50 %-duty path | Re-wire VHF; phase-gen if 8 ph |

**Recommendation: (b) folded PMOS-load.** TD is headroom at every frequency
(including ≤2.1 GHz). (a) already failed 4.20 ss with B2=8 and production tank
[SCH prior] under D22; VHF is over D7. (c) does not fix TD headroom and breaks
simple D4 8-phase unless dual-edge logic is added.

**Decision needed:** owner chooses a / b / c (or hybrid). Next run implements the
chosen option, then finishes a3 sizing / floor / D7 / peak.

## 12. P2.7.4a3 — tail-less ÷3 implemented (2026-11-19)

Owner: `decisions.md` “VHF ÷3 topology: tail-less CML”. Folded / re-order not taken.
Chain order kept (÷3 → Johnson ÷8). Sources:
`analog/vco/ldo/out/summary_vrana1_corner_vmin.txt`,
`analog/lo/sch/out/summary_vhf_buffer_size.txt`,
`summary_vhf_a3_corners.txt`, `summary_a3_floor_d7.txt`.

| Item | Result | Tag |
|---|---|---|
| VR_ANA1 V_min (ss/125, VHF load − route IR) | **1.181 V** (pad 1.186 − 5.3 mV) | [SCH/HAND] |
| VR_ANA1 V_max (ff/−40, UHF load) | **1.208 V** | [SCH/HAND] |
| LO-enable step ΔVpk (ss VHF) | −83 mV | [SCH] |
| ÷3 topology | Tail-less CML latches; NOR MOSFET tail; UHF ÷2 stacked | xschem |
| Buffer @ 4.20 ss V_min | B2=**4** µm → **0.516 V/side**; divide OK | [SCH] |
| Corners tt/ss UHF+VHF | All divide; UHF φ ≤ 0.33°; VHF φ ≤ 0.11° | [SCH] |
| f_max ss | ≈ **5.2 GHz** | [SCH] |
| MC N=20 VHF ss 4.20 | **20/20**; φ mean/σ/max 0.32/0.10/0.51° | [SCH] |
| Floor C_ck=15 fF | UHF **−154.7 PASS**; VHF **−158.6 PASS** | [SCH] |
| LO current vs D7 | UHF 8.44 OK; VHF **10.69** (−0.69 mA) | [HAND] |
| Peak MC N=20 | Prior PASS (VCO unchanged) | [PEX-RC] |

**Was STOP:** D7 overrun at HAND 10.69 mA — superseded by §13 sizing (**D7 PASS**).

## 13. P2.7.4a3 — measured current, sizing, D7 PASS (2026-11-19)

Owner: `decisions.md` “Tail-less ÷3 accepted, D7 deferred”. Sources:
`summary_lo_stage_currents.txt`, `summary_vhf_cml_jitter_fix.txt`,
`summary_a3_current_size.txt`, `summary_vhf_a3_final_corners.txt`.

### Measured stage currents [SCH]

At I_latch=0.75 mA / B2=4 / tailless, VHF I_CML (vdvs) is **3.96–5.52 mA**
across corners — above HAND 5×0.75=3.75 mA (tailless clocks to gnd are not
tail-limited). UHF I_CML ≈ 1.04–1.27 mA. TB `I_bias` 0.75 mA is the nbias
stand-in (counted in PLL HAND, not added again).

Corrected LO total @ 0.75 mA: UHF tt **8.18 mA**; VHF ss **11.08 mA** (over D7).

### VHF CML noise jitter

60 ps rms was a TB bug: stacked VARIANT in `stage_cml` + TIE rate locked to
assumed f_out. After fix: CML jit **43 fs**, L→LO **−176.5** [SCH].

### Sizing

| Knob | Value |
|---|---|
| I_latch UHF | **0.75 mA** |
| I_latch VHF | **0.30 mA** |
| B2 | 4 µm |

Floor aims (requirement + ≈1 dB): UHF ≤ −152 (req ≤ −151); VHF ≤ −151
(req ≤ −150 [PROP] §1). At selected knobs: UHF **−154.7**, VHF **−159.1** PASS
[SCH]. Buffer @ 4.20 ss V_min: **0.619 V/side**. LO totals: UHF **8.18**,
VHF **8.66 mA** → **D7 PASS**.

### Final corners / MC [SCH] (`summary_vhf_a3_final_corners.txt`)

All UHF/VHF tt+ss band-edge cases divide. Duty filled: UHF ~24–26 %, VHF
~48–51 %. UHF I/Q max **0.33°** ≤ 0.46°. VHF 8-phase corner max **0.11°**;
MC 20/20 at ss 4.20, max|φ| **0.51°** (mean 0.32°). f_max_ss ≈ **4.8 GHz**
(FAIL at 5.2; was ≈5.2 GHz at I=0.75 mA).
