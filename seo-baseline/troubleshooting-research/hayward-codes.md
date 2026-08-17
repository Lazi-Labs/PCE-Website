---
entity: pce
domain: website
vendor: hayward
source: web-research
created: 2026-08-16
status: working
---

# Hayward Equipment Error Codes — Troubleshooting Research

Research base for customer-facing troubleshooting content on the PCE website. Perfect Catch Electric is licensed for electrical, pool, and gas work in Pinellas County, FL — the "professional-only" lines below map directly to services we can legally perform that homeowners and unlicensed handymen cannot.

**Editorial rules for anything published from this file:**
- Homeowner self-checks are limited to: breakers/GFCI reset, filter cleaning/backwash, skimmer/pump baskets, water level, valve positions, pump speed schedules, salt level testing, and cell cleaning per manufacturer instructions. Nothing that opens a sealed compartment, touches gas piping, or involves wiring.
- Anything gas, combustion, refrigerant, line-voltage wiring, or board-level = professional-only, with the reason stated.
- Items marked **UNVERIFIED** must be confirmed against the official Hayward manual before publishing.

---

## 1. Hayward Universal H-Series Gas Heaters (H150FDN / H250FDN / H400FDN, NG & LP)

**Primary sources:**
- Hayward Universal H-Series Consumer Troubleshooting Guide (official PDF): https://hayward.com/media/wysiwyg/pdf/heaters/universal-h-series-consumer-troubleshooting-guide.pdf
- Hayward Universal H-Series Troubleshooting Guide TSG-UHS16b (official): https://ca.hayward.com/media/akeneo_connector/asset_files/U/H/UHS16b_UHS_TSG_163f.pdf
- Inyo Pools Universal H-Series fault code guide: https://diy.inyopools.com/article/hayward-universal-h-series-fault-pool-heater-code-troubleshooting-guide/
- PST Pool Supplies error code guide: https://www.pstpoolsupplies.com/blogs/tutorials/hayward-universal-h-series-heater-error-codes-troubleshooting-guide
- Trouble Free Pool — Hayward H-Series wiki: https://www.troublefreepool.com/wiki/index.php?title=Hayward_H-Series_Heaters

General note for content: tell the reader to **write down the code before cycling power** — cycling clears the display but not the cause. Never bypass a safety switch; the limit string exists to prevent a cracked heat exchanger and carbon monoxide hazards.

### LO — Limit String Open (THE priority keyword: "hayward heater lo code")
- **Meaning:** One of the safety switches wired in series (the "limit string") is open, so the control shuts the heater down. The string includes the **water pressure switch, temperature limit switches, exhaust gas temperature limit, and vent pressure switch**. LO is NOT simply "low water" — it's any open safety in that chain, but low water flow is by far the most common trigger.
- **Plausible causes:** Dirty/clogged filter; variable-speed pump running too slow when the heater calls; heater bypass valve open or valves misdirecting flow; low water level at the skimmer; stuck skimmer weir door; clogged pump basket; failing internal bypass cartridge (drives high-limit trips); genuinely failed pressure/limit switch.
- **Safe homeowner self-checks:** Clean or backwash the filter; empty skimmer and pump baskets; top up pool water level; make sure all valves feeding the heater are open; if a variable-speed pump is installed, raise the speed while the heater runs and see if the code clears; power-cycle once after fixing flow.
- **Professional-only:** Multimeter diagnostics across the limit-string terminals, replacing pressure/limit/vent switches, or the internal bypass cartridge — this means opening the heater cabinet next to gas and line-voltage components.
- Sources: TFP wiki, Airlucent (https://airlucent.com/hayward-heater-lo-code/), FireplaceHubs (https://fireplacehubs.com/hayward-pool-heater-lo-code/).

### IF — Ignition Failure
- **Meaning:** The heater exceeded its maximum ignition attempts without proving a flame; it locks out (auto-resets after ~60 minutes per Inyo's read of the Hayward guide).
- **Plausible causes:** Gas supply valve off; empty propane tank / low gas pressure; dirty flame sensor; ignition/flame-sense wiring; failing gas valve.
- **Safe homeowner self-checks:** Confirm the manual gas shutoff to the heater and at the meter/tank is fully open; confirm the propane tank isn't empty; confirm other gas appliances work. Stop there.
- **Professional-only:** Anything past the shutoff valve — gas pressure testing, flame sensor cleaning inside the combustion cabinet, gas valve testing. This is combustion/gas work; wrong pressure or a leak is a fire and CO hazard. (Some retail guides suggest DIY flame-sensor cleaning; for our audience we route this to a gas-licensed tech.)

### IO — Igniter Open / Ignition Lockout
- **Meaning:** Igniter circuit reads open during the blower run; control shuts down and locks out (auto restart ~2 minutes after correction per Inyo). PST describes IO as lockout after 3 consecutive IF events. Both readings agree it's an ignition-circuit fault.
- **Causes:** Failed hot-surface igniter, igniter wiring, control board.
- **Homeowner:** Power-cycle once; if it returns, call.
- **Professional-only:** Igniter replacement is inside the combustion compartment — gas work.

### CE — Communication Error
- **Meaning:** Ignition control board and display board aren't talking (not established within 3 s at startup, or lost for 30+ s).
- **Causes:** Loose ribbon/harness between boards, moisture/corrosion, failing board.
- **Homeowner:** Power-cycle at the breaker once. If CE returns, call.
- **Professional-only:** Reseating internal harnesses and board diagnosis — line voltage inside the cabinet.

### AO — Blower Vacuum Switch Open
- **Meaning:** The blower (air prover) vacuum switch didn't close after the combustion blower started, so ignition is aborted.
- **Causes:** Blocked vent/exhaust, kinked or cracked vacuum tubing, failed blower, failed vacuum switch or relay.
- **Homeowner:** Visually confirm nothing is sitting on or blocking the heater's exhaust vent (leaves, covers, animal nests) — from outside only.
- **Professional-only:** Vacuum tubing, switch resistance testing, blower replacement — combustion air system.

### AC — Blower Vacuum Switch Closed (when it should be open)
- **Meaning:** The vacuum switch reads closed before the blower starts, so the control refuses to start the blower.
- **Causes:** Stuck vacuum switch, welded relay contact.
- **Homeowner:** Power-cycle once; nothing else safe.
- **Professional-only:** Switch/relay diagnosis inside the cabinet.
- Note: PST's guide describes AC as an "AC voltage" fault — the official Hayward guide (and Inyo's reading of it) defines it as the blower vacuum switch closed error. Use the Hayward definition; flag PST's variant only as a conflicting retail description.

### HF — Flame Present With Gas Valve Off
- **Meaning:** Flame is sensed while the gas valve is de-energized — a serious condition. Control locks out and keeps the blower running to purge.
- **Causes:** Leaking/failed gas valve, board fault.
- **Homeowner:** None. If HF displays repeatedly, shut the heater's power off and call immediately. Do not keep resetting it.
- **Professional-only:** Gas valve testing/replacement — an uncontrolled gas valve is a fire hazard. Gas license required.

### SF — Thermistor / Temperature Sensor Fault
- **Meaning:** Per the official guide (via Inyo): excessive disagreement between the two water thermistors (5°F or more). Some retail guides gloss SF as "stack flue sensor" — the official H-Series definition is the thermistor comparison error.
- **Causes:** Damaged sensor wiring (rodents, corrosion), drifted/failed thermistor.
- **Homeowner:** Power-cycle once.
- **Professional-only:** Sensor wiring and replacement are behind the panels next to line voltage.

### HS — Water Temperature Sensing Error (rapid rise / overheat)
- **Meaning:** Inlet temp exceeds 104°F, or temperature rises ≥6°F in 60 seconds while firing — a low-flow signature. Three occurrences in an hour = lockout requiring a power cycle.
- **Causes:** Restricted flow (dirty filter, low pump speed, valve position), scaled heat exchanger, internal bypass problem.
- **Safe homeowner self-checks:** Same flow checklist as LO — clean filter, baskets, water level, valves open, raise VS pump speed. Then power-cycle.
- **Professional-only:** Heat exchanger descaling/inspection, bypass cartridge — sealed water/gas assemblies.

### bD — Bad Board / Secondary High-Voltage Fault
- **Meaning:** The ignition control board's self-diagnostic failed (secondary high-voltage circuit fault).
- **Causes:** Blown FC4 fuse, failed transformer, failed fuse board or control module.
- **Homeowner:** One power cycle. If bD returns, it's component-level.
- **Professional-only:** Fuse/transformer/board testing and replacement — line-voltage electrical work.

### sB — Stuck Button (keypad)
- **Meaning:** A keypad button has been closed/pressed for more than 30 seconds. Heater keeps operating; the code clears when the button releases.
- **Causes:** Debris or water on the keypad, warped bezel, failed keypad membrane.
- **Homeowner:** Wipe the keypad, make sure nothing is pressing on it. Totally safe.
- **Professional-only:** Keypad/display assembly replacement if it persists.

### EE — EEPROM Error
- **Meaning:** Control module memory failure — the board is defective.
- **Homeowner:** One power cycle to rule out a glitch.
- **Professional-only:** Control module replacement.

### PF — Power/Polarity Fault
- **Meaning:** 120V polarity reversed, low supply voltage, or inadequate ground path. Clears immediately when corrected.
- **Homeowner:** If the heater was just serviced or rewired, don't touch it — call. Check nothing tripped at the panel.
- **Professional-only:** Correcting polarity/grounding is electrical work — exactly PCE's electrical license.

### bO — Bypass Operation
- **Meaning:** Not a fault. The heater is being controlled by an external/remote thermostat (automation). If unintended, hold DOWN + MODE for 3 seconds to exit.
- **Homeowner:** Fully safe to clear per the manual.

### "F1–F4" — UNVERIFIED as display codes
- On the Universal H-Series, **F1/F2/F3/FC4 are board fuses referenced in the diagnostics manual, not codes shown on the display**. We found no authoritative source showing F1–F4 as H-Series display codes; they may be confused with Hayward heat-pump fan faults or with fuse callouts in repair guides. **Do not publish F1–F4 as H-Series display codes without confirming against the Hayward diagnostics manual (TSG-UHS16b).** Blown-fuse diagnosis is professional-only regardless (board-level, line voltage).

### Codes seen in retail guides but not in the official consumer guide
- **PS ("pressure switch")** and **AS ("sensor short")** appear in the PST guide. Plausible but **UNVERIFIED** against Hayward's own code table — confirm before publishing.

---

## 2. Hayward AquaRite / TurboCell Salt Chlorination Systems

**Primary sources:**
- Inyo Pools "How To Troubleshoot a Hayward Aqua Rite": https://www.inyopools.com/HowToPage/how_to_troubleshoot_a_hayward_aqua_rite.aspx
- Inyo Pools AquaRite error code guide: https://diy.inyopools.com/hayward-aqua-rite-error-code-guide/
- Inyo Pools "Read and Adjust the Aqua Rite SCG Operational Values": https://www.inyopools.com/HowToPage/how-to-read-and-adjust-the-hayward-aqua-rite-scg-operational-values.aspx
- Hayward Aqua Rite Diagnostics Manual (mirror): https://images.inyopools.com/cloud/documents/aquarite-troubleshooting-guide.pdf
- Trouble Free Pool AquaRite wiki: https://www.troublefreepool.com/wiki/index.php?title=Hayward_Aquarite_SWG
- Leslie's AquaRite troubleshooting: https://lesliespool.com/blog/how-to-troubleshoot-a-hayward-aquarite-salt-system.html

**Key numbers (verified across Inyo + Hayward diagnostics manual):**
- Salt range **2,700–3,400 ppm, ideal 3,200 ppm**.
- Generation stops when water is too cold (~<50–60°F depending on source/model) or above ~140°F.
- Diagnostic button sequence: pool temp → cell voltage → cell current → output % → instant salinity (shown with a leading "−") → product name → software rev → cell type (t-3/t-5/t-9/t-15). Display reverts after 30 s.
- Healthy cell voltage **22–25 V while generating** (30–35 V when idle). Generating amperage by cell: **T-15: 3.1–8.0 A, T-9: 2.3–6.7 A, T-5: 1.9–5.7 A, T-3: 1.3–4.5 A**.
- The configured cell type MUST match the installed cell or salinity readings and output are wrong.

### No Flow LED
- **Meaning:** Flow switch isn't detecting adequate water movement; chlorine generation stops as a safety measure. (Normal for ~60 s at pump start and whenever the pump is off.)
- **Causes:** Pump off/not primed; dirty filter; closed or diverted valves (spa mode); flow switch installed backwards or without 12" of straight pipe upstream; cut flow-switch wire; failed switch.
- **Safe homeowner self-checks:** Confirm the pump is running and primed; clean/backwash the filter; empty baskets; check valve positions (especially spa diverters); check the flow-switch cable is plugged into the box and undamaged (visual only).
- **Professional-only:** Replacing/repositioning the flow switch (plumbing cut-in) or wiring repairs.

### Check Salt LED
- **Flashing (with Inspect Cell flashing):** salt marginal (~2,500–2,600 ppm) — generation continues at reduced efficiency.
- **Solid (with Inspect Cell solid):** salt read below ~2,300 ppm — generation stops.
- **Causes:** Genuinely low salt (rain dilution, splash-out, backwashing); scaled or aged cell reading artificially low; wrong cell type configured.
- **Safe homeowner self-checks:** Test salt independently (test strips or a pool store) BEFORE adding salt — the unit's reading can be wrong when the cell is old or dirty. If truly low, add pool salt toward 3,200 ppm. If the store test says salt is fine, the cell likely needs cleaning or is near end of life.
- **Professional-only:** Recalibration decisions, board diagnosis, cell replacement verdicts where readings conflict.

### High Salt LED
- **Meaning:** Salinity (or cell amperage) above limits — generation stops to protect the cell.
- **Causes:** Over-salting; wrong cell type configured (a T-15 setting with a smaller cell over-reads); amperage above the cell's max.
- **Safe homeowner self-checks:** Independently test salt; if genuinely high, partially drain and refill with fresh water. No other fix is DIY.
- **Professional-only:** Cell-type reconfiguration and amperage diagnosis.

### Inspect Cell LED
- **Flashing:** 500-hour maintenance timer — inspect/clean the cell, then hold the diagnostic button 3–5 s to reset the timer.
- **Solid:** the unit believes the cell is scaled or depleted (can't reach target current).
- **Safe homeowner self-checks:** With the **pump off and system off**, remove the cell (union fittings — hand tools, no wiring) and look through it; if plates have white scale, clean per Hayward's instructions using a diluted muriatic acid soak (acid-into-water, gloves and eye protection, outdoors) or use a commercial cell cleaner. Reinstall, reset the timer. If a clean cell with correct salt still shows solid Inspect Cell, the cell is likely depleted (typical life 3–5+ seasons).
- **Professional-only:** Confirming depletion vs. board fault (voltage/current readings), replacement cell selection/config. Note for content: many homeowners are uncomfortable with acid handling — offer cell cleaning as a service.

### Power LED off
- **Homeowner:** Check the breaker feeding the unit. That's it.
- **Professional-only:** The 20 A fuse on the main PCB and input-voltage verification are inside the wired enclosure — electrical work.

### Generating LED flashing
- **Meaning:** Water temperature outside generating range (usually cold water in winter — common even in FL). Not a fault.
- **Homeowner:** None needed; Super Chlorinate can override cold cutoff temporarily. Consider liquid chlorine supplementation in cold months.

### Display: "COLD" / "HOT"
- **COLD:** water below ~50°F, or the cell's temperature sensor misreading. If displayed when water obviously isn't cold, clean the cell; if it persists, the in-cell sensor has failed → cell replacement.
- **HOT:** water above ~140°F reading — almost always a **failed/shorted temperature sensor in the cell** (real 140°F pool water doesn't happen). No override exists for HOT. → cell replacement.
- **Professional-only:** Sensor/cell verdict and replacement config.
- Source: Inyo error-code guide; JustAnswer thread corroborates HOT = sensor failure (https://www.justanswer.com/pool-and-spa/e2q2d-pool-aquarite-salt-generator-keeps-giving-hot-error.html).

### Display: "-PCB-" (with all four red/yellow LEDs lit)
- **Meaning:** Main printed-circuit-board fault self-detected.
- **Homeowner:** Power-cycle at the breaker once.
- **Professional-only:** If it returns, main board replacement — inside a line-voltage enclosure.
- Source: Inyo + TFP board-repair thread (https://www.troublefreepool.com/threads/aquarite-diagnose-troubleshoot-your-own-main-board.167903/).

### Diagnostic reading: 0 cell amps with normal voltage
- **Meaning:** No current through the cell — depleted/scaled cell, unplugged cell cord, or board current-sensing fault. **Professional-only** beyond checking the cell cord is plugged in.

### Salinity recalibration
- When the displayed average salinity disagrees with an independent test, the unit can be re-synced to instant salinity (procedure: with the unit generating, display instant salinity, then cycle the main switch Auto → Super Chlorinate → Auto — **UNVERIFIED exact sequence, confirm against the AquaRite manual before publishing**). Safe (switch-flipping only) once verified.

---

## 3. Hayward Variable-Speed Pumps (TriStar VS, MaxFlo VS, Super Pump VS, EcoStar)

**Primary sources:**
- ProTuff VS pump fault code reference: https://www.protuffproducts.com/equipment-use/variable-speed-pump-fault-codes/
- PoolDial EcoStar troubleshooting guide: https://pooldial.com/resources/articles/hayward/ecostar/hayward-ecostar-troubleshooting-guide
- Hayward Technical Service Bulletin — PFC Hi error: https://www.totallyhayward.com/techservices/attachments/Technical%20Service%20Bulletin%20PFC%20Hi%20error%20code.pdf
- Hayward EcoStar SP3400VSP Owner's Manual error-code pages: https://www.manualslib.com/manual/609555/Hayward-Ecostar-Sp3400vsp.html?page=29
- Leslie's Hayward VS troubleshooting: https://lesliespool.com/blog/how-to-troubleshoot-hayward-variable-speed-pumps.html

These drives mostly show **plain-English display messages** rather than two-letter codes. When a TriStar VS is wired to a Hayward automation control, some faults surface as **numeric codes — e.g., 64 = DC voltage low, 65 = DC voltage high** (source: TFP thread https://www.troublefreepool.com/threads/hayward-tristar-2-7hp-vs-pump-error.207656/; treat other numeric codes as UNVERIFIED).

### "Prime Failed"
- **Meaning:** Pump couldn't establish prime within 15 minutes.
- **Causes:** Low water level; empty/loose pump basket lid or o-ring; suction-side air leak; closed suction valve; clogged skimmer line.
- **Safe homeowner self-checks:** Top up water level; clean skimmer and pump baskets; make sure the pump lid is seated (lube the o-ring with pool lube); open all suction valves; retry.
- **Professional-only:** Pressure-testing suction plumbing for leaks, replacing shaft seal.

### "Drive Is Overheated" / "Heat Sink Overheat"
- **Meaning:** Drive electronics exceeded safe temperature.
- **Causes:** Debris blocking motor/drive cooling fins or fan; enclosure too tight (needs ~12" rear clearance); direct Florida sun on the drive; failing drive.
- **Safe homeowner self-checks:** Power off at the breaker, then clear leaves/debris from the fan and cooling fins; ensure ventilation clearance; provide shade. Restore power.
- **Professional-only:** Recurring heat-sink faults usually mean drive replacement — wiring work.

### "PFC-Hi" (also "PFC Circuit Hi/Low")
- **Meaning:** Per Hayward's own service bulletin, the drive detected an incoming AC voltage spike (>~280 VAC) and latched itself off to protect the electronics. **Not a pump defect.**
- **Safe homeowner self-checks:** Reset by cycling the breaker off/on. If it recurs frequently, that points at supply-power quality.
- **Professional-only:** Investigating recurring surges (panel connections, utility supply) — electrical license work, squarely PCE territory.

### "DC Voltage Too High / Too Low" (codes 65/64 via automation)
- **Meaning:** Incoming power outside the safe window (~207–253 VAC on 230 V models; EcoStar flags "AC Mains Low" below ~185 VAC).
- **Causes:** Undersized wire for the run, loose lugs, utility voltage problems.
- **Homeowner:** Breaker cycle once; nothing else.
- **Professional-only:** Voltage measurement at the pump, conductor upsizing, utility coordination — licensed electrical work.

### "Drive Overload" / "Over Current"
- **Meaning:** Motor drawing excessive current.
- **Causes:** Jammed impeller (debris/pebbles), failing bearings/shaft seal, drive fault.
- **Safe homeowner self-checks:** Power off, clean pump basket; nothing further — do not open the wet end housing.
- **Professional-only:** Impeller/diffuser/seal inspection and replacement.

### "Pump has Stalled" / "Drive Failed to Start" (Stall Error)
- **Meaning:** Motor failed to spin up after (typically 3) start attempts.
- **Causes:** Seized shaft, water intrusion into the drive, loose motor leads.
- **Homeowner:** One breaker cycle.
- **Professional-only:** Everything else — usually a motor/drive replacement decision.

### "Motor Phase Lost"
- **Meaning:** One motor winding phase is gone — internal failure (water ingress, winding, or drive transistor). Power cycling won't fix it.
- **Professional-only:** Motor/drive assembly replacement.

### "Memory Failure"
- **Meaning:** Drive control memory fault (EcoStar). **Professional-only** if it survives a power cycle — board-level.

### "Check System"
- **Meaning:** Generic drive protective stop (voltage out of range, overcurrent, overheat, or stall) — often after multiple auto-restart attempts.
- **Homeowner:** Note conditions (hot day? storm?), cycle the breaker once, watch for a more specific message.

### "Warning No Comm" / blank display
- **Meaning:** Display and drive not communicating, or no power to display (healthy display supply is ~9–15 VDC per PoolDial).
- **Homeowner:** Confirm breaker on. Nothing else.
- **Professional-only:** RS-485 wiring and harness checks — inside the wired drive enclosure.

### "SVRS Tripped" (SVRS models only)
- **Meaning:** Safety Vacuum Release System detected a suction anomaly (possible entrapment/blockage).
- **Homeowner:** Check and clean baskets and filter; make sure drain covers are intact. If it trips repeatedly, stop using the pump and call — SVRS is a life-safety system.

### Pump repeatedly tripping the breaker
- **Meaning/causes:** Wiring fault, drive failure, or GFCI compatibility/sensitivity.
- **Homeowner:** Do NOT keep resetting a breaker that immediately re-trips.
- **Professional-only:** Fault isolation (disconnecting motor leads to localize) is live electrical diagnosis.

### When replacement beats repair (per PoolDial, good content angle)
Water inside the drive enclosure, drive revision reading 0.00, recurring Heat Sink Overheat, seized shaft, or burnt/corroded PCB → replace, don't chase parts.

---

## 4. Hayward OmniLogic / OmniHub / OmniPL Automation

**Primary sources:**
- PoolDial OmniLogic troubleshooting guide: https://pooldial.com/resources/articles/hayward/omnilogic/hayward-omnilogic-troubleshooting-guide
- GreyShark Pools Omni HL troubleshooting: https://greysharkpools.com/guides/equipment/hayward-omni-hl-troubleshooting/
- Hayward OmniPL Troubleshooting Guide TSG-OPL42a (official PDF): https://hayward.com/media/akeneo_connector/asset_files/O/m/OmniPL_Troubleshooting_Guide___TRR_7804.pdf
- Trouble Free Pool OmniLogic wiki: https://www.troublefreepool.com/wiki/index.php?title=Hayward_OmniLogic
- TFP alarms thread: https://www.troublefreepool.com/threads/hayward-omnilogic-alarms.243148/

Omni alarms are plain-text messages on the touchscreen (MSP). Screen color matters: **yellow = warning, red = critical fault**. The subpanel carries up to 100 A at 240 VAC — Hayward's own guide restricts internal service to qualified personnel, which is our framing for the whole section.

### "Comm Loss" (e.g., "MPP – Comm Loss", VS pump comm loss)
- **Meaning:** The Main Panel Processor lost communication with a component (VS pump on the Low-Speed Bus, wall remote on the High-Speed Bus, smart relay, etc.).
- **Causes:** Loose/damaged comm wiring, corroded terminals, failed device, board fault.
- **Safe homeowner self-checks:** Power-cycle the whole system at the breaker once (many comm losses clear); note WHICH device is named for the service call.
- **Professional-only:** Comm-bus wiring lives inside the load center next to 240 V — wiring diagnosis is licensed electrical work.

### "T-CELL Cable/Sensor Open"
- **Meaning:** The chlorinator cell cord reads open — cut cable or cell not plugged in.
- **Safe homeowner self-checks:** Visually confirm the cell cord is plugged in snugly at the cell end (accessible, low-voltage plug) and undamaged.
- **Professional-only:** Board-end connection and cable replacement.
- Source: TFP alarms thread.

### "T-CELL Current Sensor Short"
- **Meaning:** Current-sense circuit fault — typically the main board.
- **Professional-only:** Board diagnosis/replacement.
- Source: TFP alarms thread. Mark exact wording **UNVERIFIED** against the Hayward manual before publishing.

### Chlorinator alarms — Low Salt / High Salt / Cell fault
- Same physics and same homeowner guidance as the AquaRite section above (Omni units drive the same TurboCell; 2,700–3,400 ppm, ideal 3,200): independently test salt before adding; clean the cell per instructions; everything else is professional.

### Flow alarm / "FLOW"
- **Meaning:** Flow switch not closing while equipment (esp. chlorinator) should run; the system suspends chlorination and may shut the pump down after 15–20 minutes when flow monitoring is enabled.
- **Safe homeowner self-checks:** Same flow checklist as AquaRite No Flow: pump running, filter clean, baskets empty, valves open.

### Temperature sensor faults (open / short / out-of-range)
- **Meaning:** Water or air thermistor reading open, shorted, or impossible.
- **Symptoms:** Wrong displayed temps, heater refusing to run.
- **Professional-only:** Sensor replacement terminates inside the panel.

### Blank touchscreen / dead panel
- **Causes:** No 120 VAC to the main board, power-supply failure, tripped breaker/GFCI.
- **Safe homeowner self-checks:** Check the breaker and any GFCI feeding the automation panel. Stop there.
- **Professional-only:** Everything inside the enclosure.

### Valve actuator not rotating
- **Causes:** Comm/wiring fault, power supply, failed actuator, jammed valve.
- **Homeowner:** Nothing safe (actuator wiring is in the panel). Note which valve for the call.

### Wi-Fi / app connectivity issues (very common; good SEO content)
- **Symptoms:** OmniLogic app can't reach the system; "system offline."
- **Causes:** Weak Wi-Fi at the equipment pad (pads are far from routers), router changes (new SSID/password), outdated firmware, Hayward cloud outages.
- **Safe homeowner self-checks:** Reboot home router; reboot the Omni at its breaker; move a Wi-Fi extender/mesh node closer to the pad; re-run the network setup from the touchscreen if the router password changed; check firmware updates from the MSP; verify the system shows connected on the local touchscreen before blaming the panel (if local works and app doesn't, it's network/cloud, not wiring).
- **Professional-only:** Antenna/wired-Ethernet retrofits into the panel, board replacement.

### Maintenance step techs use: clear the DDT (Device Discovery Table)
- Refreshes component communications after device changes. Menu-level operation but easy to misuse — treat as tech-level in published content. Source: TFP wiki/threads. **UNVERIFIED exact menu path.**

---

## Content strategy notes (not for publication)

1. **Priority page:** "Hayward Heater LO Code" (590/mo) — lead with the flow checklist (filter, baskets, water level, valves, VS pump speed), because that resolves the majority of LO calls without parts, then pivot to "if the code returns, the limit string needs meter diagnostics — that's us."
2. Every code page gets the same skeleton: What the code means → 5-minute safe checks → why the rest is licensed work (gas/electrical) → CTA. The gas-license angle is a genuine differentiator vs. pool-only competitors.
3. HF deserves an explicit safety callout box (flame with gas valve off = stop resetting, call now).
4. AquaRite "HOT/-PCB-" and VS "PFC-Hi" are high-intent, low-competition long-tails worth their own FAQ entries.
5. Before publishing, verify every item marked UNVERIFIED against: Hayward Universal H-Series TSG-UHS16b, AquaRite Diagnostics Manual, EcoStar owner's manual pp. 28-30, OmniPL TSG-OPL42a (links above).
