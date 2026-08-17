---
entity: pce
domain: servicetitan
source: web-research (manufacturer manuals, TFP, vendor guides)
created: 2026-08-16
status: working
---

# Pool Equipment Troubleshooting Research — Raypak, AquaCal, Universal Symptoms

> Research base for Perfect Catch Electric's customer-facing troubleshooting content (website / Ads landing pages). Every entry: exact code → technical meaning → plausible causes → SAFE homeowner self-checks → professional-only trigger. **House rule for all published content: ALL gas work, ALL refrigerant work, and ALL electrical work is professional-only. Homeowner checks are limited to: looking, listening, cleaning baskets/filters, checking water level, valve positions, app/router settings, and power-cycling at the breaker.** Perfect Catch is licensed for electrical, pool, and gas in Pinellas County — that trio is the trust angle for every "call a pro" block.
>
> Items marked **UNVERIFIED** could not be confirmed against a manufacturer source during this research pass — verify against the unit's own manual before publishing as fact.

---

## PART 1 — RAYPAK GAS HEATERS

### Model-family orientation (matters — codes differ by family)

| Family | Display style | Code set |
|---|---|---|
| **206A / 266A / 336A / 406A "Digital"** (P-M/P-R series) | 2-digit LED + 3-letter fault code, "SERVICE" flashes | `PRS, HL1, HL2, SNS, IGN, ILO, ROL, FAN, GVC, GVO, FFL, VNT, BD1, EEP` (Raypak 206A I&O manual, diagnostics p.35) |
| **106A / 156A** (atmospheric, current manual 241519) | LCD with **full-word messages** | "Water Sw Open," "Hi Limit 1/2 Fault," "Rollout Sw Open," "Ignition Lockout," "Ignition Failure," "Sensor Open/Short," "Clock/Fireman Sw," "Vent/Field Sw #1," "Low Temp Lockout," "Flame w/o CFH," "PV/MV Output Fault," "Internal Fault," "EEPROM Fault" |
| **Avia** (current gas line, 264A/404A) | Backlit LCD, **full-word fault messages** | See Avia table below (Avia I&O manual, Tables O/P/Q) |

**E-codes (E01/E02/E03/E05/E06):** Several consumer guides attribute E-codes to Raypak: E01 = ignition failure/lockout, E05 = flame loss, E06 = faulty high limit switch (Medallion Energy Raypak error-code guide). **E02, E03, and the "E01 (ILO)" / "E02 (IHO)" pairing are UNVERIFIED** — they do not appear in the current 106A/156A manual (241519) or the Avia I&O manual, both of which use full-word messages. "IHO" appears in no manufacturer source found. Treat E-codes as legacy/regional display variants; on the website, map them to the equivalent full-word fault ("E01 → Ignition Lockout," "E06 → High Limit Fault") and tell the reader to confirm against their model's manual.

### 1A. Digital-series 3-letter codes (206A–406A)

Source of record: Raypak 206A Installation & Operating manual, "Diagnostics — Reading a Fault" (manualslib.com/manual/1114914, p.35); supplemented by Inyo Pools Raypak Fault Code Guide and Florida's Best Pools code library.

| Code | Technical meaning | Plausible causes (ranked) | Safe homeowner checks | Pro-only — why |
|---|---|---|---|---|
| **PRS** ("PS open") | Water pressure switch open — heater sees insufficient water pressure/flow | 1. Pump off or on low speed 2. Dirty filter / full baskets 3. Low pool water level 4. Valves diverting flow 5. Mis-adjusted or failed pressure switch | Confirm pump is running at high speed; clean skimmer/pump baskets; clean or backwash filter; check water level; verify valves send water through the heater | Adjusting or replacing the pressure switch, or any internal bypass work — mis-set switches let the heater fire without flow and can soot or destroy the exchanger |
| **HL1 / HL2** ("HLS") | High-limit switch 1 or 2 open — water in the exchanger exceeded ~135°F | 1. Restricted water flow (filter, baskets, valves) 2. Scaled/blocked heat exchanger tubes 3. Stuck unloader/bypass valve 4. Failed high-limit switch | Same flow checks as PRS; power-cycle at breaker once after flow is restored | Exchanger descaling, bypass valve, and switch replacement — an overridden high limit is a scald and exchanger-failure hazard |
| **SNS** ("Sns") | Temperature sensor out of range (reads below 36°F or above 110°F) or thermistors disagree | 1. Failed thermistor 2. Corroded/loose sensor wiring (fast in coastal FL air) 3. Poorly seated sensor | Power-cycle once; note whether displayed water temp is obviously wrong | Sensor and harness replacement is electrical work inside a gas appliance |
| **IGN** ("IF") | Ignition failure — 3 trials, no flame proven (IGN alone during startup is the normal purge/light sequence, not a fault) | 1. Air in gas line / gas shut off 2. Low inlet gas pressure (undersized line, low LP tank) 3. Dirty igniter or corroded flame rod 4. Condensate dripping on burner 5. Failed ignition control | Confirm the gas supply valve is on and (LP) tank is above ~30%; power-cycle once | Everything else — gas pressure testing, igniter/flame-rod service, and burner work are licensed-gas-only tasks (explosion/CO risk) |
| **ILO / IGN LOCKOUT** | Ignition lockout — heater has stopped trying to light after repeated failed attempts (flagged on propane units) | 1. Same causes as IGN, now persistent 2. Pilot/igniter assembly fault 3. Control board fault | One breaker reset only. If it locks out again, stop | Repeat lockouts mean a real gas-supply or combustion problem; retry-spamming a lockout is a fire hazard |
| **ROL** | Rollout safety switch / thermal fuse open — flame left the combustion chamber | 1. Downdraft/wind blowing flame out of the burner tray 2. Blocked heat exchanger (soot/scale) forcing flame out 3. Burned wiring at the switch | None beyond noting wind exposure. Do not reset repeatedly | Flame rollout is an active fire event — combustion chamber inspection is strictly professional |
| **FAN** ("AFS") | Combustion blower air-pressure switch didn't close (fan-assisted models) | 1. Vent/flue obstruction (nests, debris) 2. Failed blower motor 3. Kinked/clogged pressure-tap tubing 4. Failed air switch | Visually check the vent top for obvious blockage (from the ground) | Blower and vent service — bad combustion air = carbon monoxide risk |
| **GVC / GVO** | Gas valve output not in commanded state (GVC = no voltage when commanded on; GVO = voltage present when commanded off) | 1. Board fault 2. Wiring/connection fault 3. Weak transformer 4. Failed gas valve | Power-cycle once | Any gas-valve or board diagnosis — a valve stuck open is an explosion hazard |
| **FFL** ("Flame w/o CFH") | Flame sensed while both gas valves are commanded shut | 1. Gas valve leaking through / stuck 2. Flame-sense circuit or board fault | **Shut the heater off and stop using it** | Gas leaking past a closed valve is an emergency-level gas defect |
| **VNT** | Vent switch open (factory-jumped on outdoor units) | 1. Vent spill switch tripped (indoor installs) 2. Jumper/wiring fault | None | Venting diagnosis = CO safety |
| **BD1 / EEP** | Control board failure / memory (EEPROM) fault | 1. Power surge or brown-out 2. Failed board | One full power cycle (off at breaker 30 s). If code returns, done | Board replacement inside a gas appliance |
| **spk** | Displayed while the unit is sparking to ignite — **status, not a fault** on most displays (Avia shows "Spark"). A display frozen on spark that ends in IF/ILO = ignition failure path. **UNVERIFIED as a standalone fault code** | See IGN causes | Watch whether it progresses to a lockout code | Same as IGN |
| **FLo** | Flow-related display. On Avia this maps to "Low Flow Fault" (low flow detected in heater — possible scaling); on digital units flow problems present as PRS/HLS. **Exact "FLo" rendering UNVERIFIED per model** | 1. Dirty filter 2. Low pump speed 3. Scaled exchanger | Flow checks as PRS | Scale/exchanger service |
| **IHO** | **UNVERIFIED** — no manufacturer source found. Field guides pair it with high-limit/ignition-high lockout on older E-code displays. Publish only as "see your manual; treat as a lockout — call for service" | — | Power-cycle once | Unknown lockout = professional diagnosis |

### 1B. Raypak 106A / 156A full-word messages (manual 241519)

Displayed faults: **Water Sw Open** (pressure switch — see PRS above) · **Vent/Field Sw #1** (vent spill switch) · **Hi Limit 1/2 Fault** · **Rollout Sw Open** · **Flow/Field Sw #2** · **Ignition Lockout** (alternates with "No pilot sensed" — pilot not established in 15/90 s — or "Main Ign Failure" — pilot lost during 8-s main-burner trial) · **Ignition Failure** and **Ign 6min Delay** (non-propane: 4 pilot losses → 6-minute lockout before retry) · **Sensor Failure / Sensor Open / Sensor Short** (thermistors disagree >2°F; open below −20°F; short above 217°F) · **Flame w/o CFH** · **PV/MV Output Fault** (pilot/main gas valve not in commanded state) · **Internal Fault / EEPROM Fault** (board) · **Clock/Fireman Sw** (external interlock circuit open) · **Low Temp Lockout** (water below 36°F). Causes/homeowner-checks/pro triggers mirror the digital-series table above.

### 1C. Raypak Avia fault messages (Avia I&O manual, Tables O/P/Q)

Status (normal): `No Demand · Pre-Purge · Spark · Heating · Post-Purge`.

Key faults: **Water Sw Open** · **Hi Limit 1/2 Fault** (press MODE to clear after fixing flow) · **Air SW Open** / **Diff Sw Open/Closed/Fault** (combustion air pressure switch) · **Fan Lockout** (3 air-switch faults in one heat cycle; power-cycle to clear) · **Ign Try Failure** (failed 1st/2nd try) · **Ign 60 min Delay** (gas valve failed 3× in one call — 60-min lockout) · **Ignition Lockout** (power-cycle to clear) · **Flame Lost** · **Flame w/o CFH** · **Gas Valve Fault** (valve sensed ON when commanded OFF — 60-min soft lockout) · **In/Out Sensor Fault/Open/Short** (inlet thermistors disagree >3°F; open below 6°F; short above 188°F) · **Flue Sensor Open/Shrt**, **Flue Over Temp** (>390°F, power-cycle to clear), **Flue Low Temp** (<175°F, condensation warning), **Flue Extreme Low** (<140°F — service required) · **Low Flow Fault** (possible scaling) / **High Flow Fault** (possible condensation) · **Cabinet Temp Lm** · **Low Voltage** (<17 VAC to controller) · **Low Temp Lockout** (<36°F) · **Clock/Fireman Sw** · **Pump Ctl Fail / WChem Brd Fail / Remote Wire Err** (accessory boards not responding) · **Internal Fault / EEPROM Fault** · **Call Service** (Fan Lockout, Ignition Lockout, or Flue Extreme Low occurred 3× in 48 h — contact service).

Homeowner-safe on an Avia: flow checks (filter, baskets, valves, pump speed), one power cycle, MODE-key reset where the display instructs. Everything flue-, gas-, or sensor-related is licensed-gas work — the Avia manual itself warns service "requires certain expertise, mechanical skills, tools, and equipment."

**Part 1 sources:**
- Raypak Avia Installation & Operation Manual (PDF): https://www.eztestpools.com/content/raypak-avia-heater-installation-and-operation-manual-eztestpools.pdf
- Raypak 106A/156A I&O Manual 241519 (PDF): https://s3.amazonaws.com/AWSProd/sites/raypakcom/documents/241519.pdf
- Raypak 206A manual diagnostics page: https://www.manualslib.com/manual/1114914/Raypak-206a.html?page=35
- Inyo Pools — Raypak Heater Fault Code Guide: https://diy.inyopools.com/article/raypak-heater-fault-code-guide/
- Florida's Best Pools — Raypak error codes (IF, IGN, OS1, ILO, AFS, HLS): https://floridasbestpools.com/training/library/equipment/raypak-pool-heater-error-codes
- Medallion Energy — Raypak error codes (incl. Avia/Crosswind families): https://www.medallionenergy.com/raypak-pool-heater-error-codes/
- Shasta Pool Supply — Raypak code meanings: https://shastapoolsupply.com/blogs/news/what-raypak-heater-error-codes-mean
- Raypak official Avia troubleshooting (JS page, content not fetchable — link for readers): https://www.raypak.com/support/tech-corner/avia-troubleshooting/
- TFP Raypak wiki (403 to bots; known-good reader link): https://www.troublefreepool.com/wiki/index.php?title=RayPak_Heaters

---

## PART 2 — AQUACAL HEAT PUMPS (HeatWave SuperQuiet, TropiCal, etc.)

Source of record: AquaCal HeatWave SuperQuiet SQ120R Installation Manual §6 fault codes (manualslib pp.37–38), Medallion Energy AquaCal error-code guide, Aqua Terra Backyard HP/LP/HP5/LP5 explainer, AquaCal official blog. SuperQuiet flow spec: **30 GPM min / 70 GPM max**.

| Code | Technical meaning | Plausible causes (ranked) | Safe homeowner checks | Pro-only — why |
|---|---|---|---|---|
| **FLO** | Low or no water flow detected through the heat pump | 1. Pump off / VS pump speed too low 2. Dirty filter, full baskets 3. Valves diverting water around the unit 4. Failed flow/pressure sensing device | Run filter pump on high; clean/backwash filter; empty baskets; verify valve positions | Flow-switch replacement and internal plumbing — and a heat pump run dry cooks the titanium exchanger |
| **FS** | Fan/flow switch fault. AquaCal's blog describes FS appearing when the **fan does not start when heat is called** (shown after the compressor starts). Some field references read FS as "flow switch" on newer boards — **which sensor FS names varies by board revision; UNVERIFIED — treat either way as a no-run condition** | 1. Fan motor/capacitor failure 2. Fan obstruction 3. Switch/board fault | Look (don't reach) — is the top fan spinning when the unit calls for heat? Clear leaves/debris from the top grille with unit OFF | Fan motor, capacitor, and switch work is electrical; capacitors hold a charge even with power off |
| **HP** | High-pressure switch open — refrigerant head pressure too high (in heating this is almost always the water side not carrying heat away) | 1. Low water flow (dirty filter, low pump speed) 2. Valves bypassing the unit 3. External bypass mis-set (>70 GPM or <30 GPM) 4. Mis-calibrated/failed HP switch 5. Refrigerant overcharge (rare) | Same water-flow checks as FLO; confirm filter pressure isn't 7–10+ psi over clean baseline | Pressure-switch calibration and anything touching the sealed refrigerant circuit — EPA-certified refrigerant work only |
| **HP5 / HPC** | High-pressure **lockout** — 5 consecutive HP faults in one heating/cooling cycle; unit locks itself out ("HPC" appears on some displays for the same lockout family — **HPC label UNVERIFIED**) | Underlying HP cause was never fixed | Power off at breaker, restore water flow, power on once. If it locks again, stop | Repeat lockouts risk compressor damage; diagnosis requires gauges on the refrigerant circuit |
| **LP** | Low-pressure switch open — refrigerant suction pressure too low (in heating, the **air side** isn't feeding enough heat) | 1. Fan not running 2. Blocked airflow (shrubs, fences, debris on coil) 3. Dirty/blocked evaporator coil 4. Ice on coil (cold nights) 5. Refrigerant leak/undercharge | Clear 24"+ around the unit; gently rinse leaves off the coil with a hose, power OFF; look for ice — if iced, leave it off and let it thaw | Refrigerant leak search/recharge is EPA 608 work; running a leaking unit destroys the compressor |
| **LP5 / LPC** | Low-pressure **lockout** — 5 consecutive LP faults in one cycle ("LPC" label **UNVERIFIED**, same lockout family) | Underlying LP cause persists — often an actual refrigerant leak | One power cycle after airflow is cleared. Repeat = stop | Same as LP |
| **dPo / dPc** | **Defrost sensor** open (dPo) / shorted (dPc) — the sensor that tells the board when to run defrost is disconnected, open, or shorted | 1. Failed defrost thermistor 2. Chafed/corroded sensor wiring 3. Board input fault | Power-cycle once | Sensor replacement inside the cabinet is electrical service |
| **PO / PC** | **Water temperature sensor** open (PO) / shorted (PC) | Same pattern as dPo/dPc, water-side sensor | Power-cycle once | Same |
| **CEr** | Communication error — display-to-control-board cable loose or damaged (this is the "board comms" fault) | 1. Loose/corroded comm cable 2. Damaged cable 3. Failed display or board | Power-cycle once | Opening the control cabinet to reseat boards/cables is live-electrical work |
| **CSE** | Control system error — internal controls fault | 1. Power glitch 2. Board fault | Power off at breaker, wait 1–2 min, restart | Board diagnosis/replacement |
| **OtA** | Over-temperature — incoming water above 110°F; unit locks out | 1. Another heater upstream 2. Sensor error 3. Very hot return line | Check if a gas heater upstream is overshooting; power-cycle | Sensor verification and plumbing-sequence correction |
| **Defrost** (display) | Not a fault — unit is in defrost mode on a cold night; fan/compressor behavior changes and heating pauses | Normal below ~50°F air temp | Wait it out. If it defrosts constantly in mild weather, note it | Constant defrost in warm air suggests low refrigerant — pro |

**Part 2 sources:**
- AquaCal SQ120R Installation Manual §6 fault codes: https://www.manualslib.com/manual/1249519/Aquacal-Heatwave-Superquiet-Sq120r.html?page=37 (and ?page=38)
- Medallion Energy — AquaCal error codes: https://www.medallionenergy.com/aquacal-heat-pump-error-codes/
- Aqua Terra Backyard — HIGH PRESSURE / LOW PRESSURE / HP5 / LP5 explained: https://www.aquaterrabackyard.com/blogs/pool-and-patio-blog/aquacal-superquiet-high-pressure-low-pressure-hp5-and-lp5-faults-explaine
- AquaCal blog — heat pump will not start (FS/fan behavior): https://www.aquacal.com/troubleshooting-my-swimming-pool-heat-pump-will-not-start/
- AquaCal official error-code index: https://www.aquacal.com/error-codes/

---

## PART 3 — UNIVERSAL SYMPTOM GUIDES (brand-agnostic; primary Ads landing content)

### (a) Pool pump humming but not turning on

**Meaning:** motor is energized but the rotor isn't spinning — a start-circuit or mechanical-bind problem. A humming motor is overheating in real time; don't leave it energized.

**Causes, ranked:** 1. Failed **start capacitor** (the classic — motor hums, won't kick) 2. **Jammed impeller** (debris packed in the volute) 3. **Seized bearings/shaft** (corrosion, age) 4. Low/uneven supply voltage.

**Safe homeowner checks:** turn the pump OFF; with power off, open the pump lid and clear the basket; check for visible debris at the impeller eye through the basket housing (fingers out of the impeller); turn breaker off if humming persists.

**Pro-only:** capacitor testing/replacement (capacitors store a lethal charge even unplugged), motor teardown, and any wiring/voltage diagnosis — this is 230 V equipment next to water.

### (b) Pool pump tripping breaker (~210 searches/mo)

**Meaning:** the pump is drawing more current than the circuit allows, or leaking current to ground (GFCI trip). *When* it trips is the diagnostic: instantly = short/ground fault or seized motor; 5–15 s in = capacitor/bearing; 30+ min = thermal overload.

**Causes, ranked:** 1. Failing capacitor pulling excess start current 2. **Shorted motor windings** (insulation breakdown from years of heat cycling) 3. **Ground fault from moisture** — failed shaft seal letting water into the motor, or rain/irrigation intrusion 4. Undersized/aged breaker 5. Bound/seized rotor.

**Safe homeowner checks:** reset the breaker **once** and note how long it holds; note whether it started after rain; make sure nothing else shares the circuit. That's it.

**Pro-only:** everything past one reset. A GFCI that keeps tripping is doing its job — it may be the only thing between a fault and energized water. Megger/winding tests, seal replacement, and breaker work are licensed-electrician tasks.

### (c) Pool pump loses prime / won't prime

**Meaning:** the pump can't hold water — almost always a **suction-side air leak** or no water reaching the pump, not a motor problem.

**Causes, ranked:** 1. **Low pool water level** (skimmer gulping air — the single most common cause) 2. **Worn pump-lid O-ring** (cheapest fix, extremely common) 3. Clogged skimmer/pump basket 4. Suction-side air leak — union O-rings, valve stems, cracked fittings 5. Check-valve/valve issue draining the system on shutdown 6. Clogged impeller.

**Safe homeowner checks:** top up water to mid-skimmer; clean both baskets; inspect/lubricate or replace the lid O-ring; hand-tighten unions; refill the pump pot with a bucket before restart; watch the basket — steady bubbles after 30 s of running = ongoing air leak.

**Pro-only:** pressure-testing lines, underground leak location, impeller/seal replacement, and any repeat prime-loss you can't trace — running dry destroys the shaft seal and melts PVC.

### (d) Pool pump very loud / grinding (~170 searches/mo)

**Meaning:** sound identifies the fault. **Screech/grind = motor bearings.** **Gurgle/rumble like gravel = cavitation** (pump starving for water). **Rattle = debris or loose mount.**

**Causes, ranked:** 1. Worn motor bearings (heat, age, water past the seal) 2. Cavitation from suction restriction or air leak (see symptom c) 3. Debris rattling in the impeller 4. Loose mounting bolts / vibration transfer.

**Safe homeowner checks:** clean baskets and filter; restore water level; check for the bubble-stream that signals cavitation; note *which* noise it makes for the service call.

**Pro-only:** bearing/seal replacement or motor swap-vs-replace decision. Timing matters: once grinding starts, bearings typically finish failing within days to weeks — waiting converts a repair into a full pump replacement.

### (e) Pool light not working (~210 searches/mo) — SAFETY-FIRST PAGE

**Never open, reseat, or rewire a pool light yourself. Water + electricity is the one place a DIY save can be fatal.** The CPSC identifies electrocution from faulty pool wiring, bonding, and lighting among leading causes of pool electrical fatalities. A pool light that stopped working — or worse, one that trips the GFCI — may be signaling water inside the fixture or a compromised bond, and the GFCI is the only device standing between that fault and a swimmer.

**Causes, ranked:** 1. Tripped GFCI (may itself be caused by a real fault — don't just keep resetting) 2. Burned-out lamp/failed LED driver 3. Water intrusion into the fixture (failed lens gasket) 4. Corroded splice in the junction box 5. Failed switch/relay/automation output 6. Broken bond/ground path (invisible and the most dangerous).

**Safe homeowner checks (all dry-land):** press TEST then RESET on the GFCI **once**; check the breaker panel; check whether the automation/switch is actually calling the light on. **If the GFCI trips again — stop and keep everyone out of the pool until it's inspected.**

**Pro-only — everything else, with why:** fixture removal, bulb/lamp changes on wet-niche lights, junction-box work, and bonding verification require a licensed electrician per NEC 680 — stray voltage in a pool cannot be seen, and improper reassembly of a wet-niche light seals a future fault underwater. (Perfect Catch angle: licensed electrical + pool contractor — this exact scenario is the company's home turf.)

### (f) Gas pool heater won't stay lit / short cycles

**Meaning:** heater ignites, then loses flame or shuts down on a safety. Two families: **flame-side** (ignition/flame-sense/gas pressure/venting) and **water-side** (flow and high-limit trips).

**Causes, ranked:** 1. **Low water flow** — dirty filter is the #1 cause of short cycling (most heaters need ~25–30+ GPM) 2. Dirty/corroded flame sensor failing to confirm flame 3. Low gas pressure (undersized line, low LP tank, utility issue) — lights briefly, can't sustain 4. Wind/downdraft or rain intrusion blowing out the flame 5. High-limit trips from scaled exchanger or internal bypass 6. Failing thermocouple (millivolt/pilot models — needs ~600 mV) 7. Venting/air-intake restriction.

**Safe homeowner checks:** clean filter and baskets; run pump on high while heating; confirm gas supply valve on / LP tank level; redirect sprinklers away from the heater; power-cycle once.

**Pro-only — with why:** **all gas work, full stop** — gas pressure testing, flame-sensor/thermocouple service, burner and venting work carry explosion and carbon-monoxide risk and require a licensed gas contractor. **Never bypass or jumper a safety switch** — those switches are the only thing preventing overheat, fire, and CO events.

### (g) Salt cell not generating chlorine

**Meaning:** the salt chlorine generator (SWG) isn't converting salt to chlorine — a chemistry, flow, or cell-life problem far more often than a "broken" unit.

**Causes, ranked:** 1. **Scale buildup on cell plates** (very common in hard Florida water) 2. **Low salt level** (system cuts output; verify with an independent test, not just the display) 3. **Cold water** — most SWGs reduce/stop below ~60°F and cut off near 50°F (a winter non-issue that generates service calls) 4. **Worn-out cell** at end of life (typically 3–7 seasons) 5. No-flow condition — pump off, dirty filter, flow switch unsatisfied 6. Low stabilizer/CYA letting chlorine burn off (looks like the cell "isn't making enough") 7. Board/power fault.

**Safe homeowner checks:** confirm the pump runs long enough and the "generating" light is on; check the no-flow indicator; clean filter/baskets; test salt with strips and compare to the display; **visually** inspect the cell for white scale; verify percentage/output setting; check water temp.

**Pro-only — with why:** acid-washing the cell (muriatic acid handling + cells crack when over-etched), electrical diagnosis of the board/cell voltage, and cell replacement wiring. Also: chronic scaling means the water balance (CH/pH/CYA) needs a professional reset, or the new cell dies the same way.

### (h) Pool automation won't connect to Wi-Fi / app

**Meaning:** the pad controller (Pentair ScreenLogic/IntelliCenter, Hayward OmniLogic/OmniHub, Jandy iAquaLink) has lost its link to the router or the vendor cloud. This is the one symptom that's mostly homeowner-fixable.

**Causes, ranked:** 1. **2.4 GHz vs 5 GHz band confusion** — most pool controllers are 2.4 GHz-only; mesh routers broadcasting one SSID for both bands break them 2. Router changed/replaced (new SSID/password never re-entered) 3. Weak signal to the equipment pad 4. Corroded/loose antenna connection at the pad 5. Stale firmware / app-firmware mismatch 6. Vendor cloud outage 7. Failed comm module.

**Safe homeowner checks:** power-cycle the automation and the router; create/confirm a dedicated 2.4 GHz SSID; re-run the app's pairing flow; stand at the pad and check phone signal strength as a proxy; update the app, then firmware if the interface offers it; ScreenLogic: paperclip-reset the Protocol Adapter (3 presses in 5 s → DHCP reset); iAquaLink: unplug the antenna module 30 s.

**Pro-only — with why:** opening the control panel to reseat antenna/comm boards (line-voltage compartments live alongside the low-voltage side), replacing comm modules, and any wiring at the pad — automation panels feed pumps, heaters, and lights at 230 V.

**Part 3 sources:**
- Leslie's — pool pump troubleshooting guide: https://lesliespool.com/blog/pool-pump-troubleshooting-guide.html
- ABC Home & Commercial — pump humming but not working: https://www.abchomeandcommercial.com/blog/pool-pump-humming-but-not-working/
- TFP thread — humming with new capacitor: https://www.troublefreepool.com/threads/pump-motor-humming-and-not-starting-with-new-capacitor.195695/
- Globo Pool — 10 causes a pump trips the breaker: https://globopool.com/pool-pump-trips-breaker/
- PoolPumpFix — tripping breaker (trip-timing diagnostic): https://poolpumpfix.com/pool-pump-tripping-breaker/
- Inyo Pools — why a pool pump won't prime: https://www.inyopools.com/HowToPage/how_to_determine_why_a_pool_pump_won_t_prime.aspx
- Swimming Pool Steve — why pumps lose prime: https://www.swimmingpoolsteve.com/pages/loses-prime.html
- AquaDoc — pump noise diagnostic walkthrough: https://www.mavaquadoc.com/blogs/pool-maintenance-blog/pool-pump-making-noise-a-diagnostic-walkthrough
- PoolPartsToGo — noisy pool pump fixes: https://poolpartstogo.com/blogs/articles/noisy-pool-pump-heres-how-to-fix-it
- In The Swim — inground pool electrical safety (CPSC electrocution warning, GFCI, bonding): https://www.intheswim.com/blog/inground-pool-electrical-safety.html
- Sonoma County EH — underwater pool/spa light GFCI operation: https://sonomacounty.gov/health-and-human-services/health-services/divisions/public-health/environmental-health/programs-and-services/pools-and-spas/underwater-poolspa-light-gfci-operation
- In The Swim — gas pool heater troubleshooting (thermocouple 600 mV, wind/pilot): https://www.intheswim.com/eguides/gas-pool-heater-troubleshooting.html
- Mini Bucket Test — pool heater short cycling: https://minibuckettest.com/blogs/news/pool-heater-short-cycling-causes-and-fixes-for-a-warmer-more-reliable-pool
- Discount Salt Pool — salt cell symptom checker: https://www.discountsaltpool.com/effective-troubleshooting-for-salt-chlorine-generator-problems-tips-and-solutions
- Dog Days Pools — salt cell not producing chlorine: https://www.dogdayspools.com/poolserviceblog/why-is-my-salt-cell-not-producing-chlorine
- Pentair ScreenLogic2 official troubleshooting guide (PDF): https://www.pentair.com/content/dam/extranet/nam/pentair-pool/residential/automation/screenlogic2/screenlogic2-troubleshooting-guide-2024.pdf
- TFP thread — OmniLogic app connectivity (2.4 GHz SSID issue): https://www.troublefreepool.com/threads/hayward-omnilogic-app-connectivity-issues.203091/
- Pool Chemical Calculator — automation troubleshooting (antenna, firmware, resets): https://poolchemicalcalculator.com/news/pool-automation-system-not-working/

---

## Editorial notes for the website build

1. **Every symptom page ends the same way:** one power-cycle is the homeowner's last move; the licensed-for-all-three (electrical + pool + gas) positioning is the CTA. No competitor in Largo/Pinellas can claim all three on one truck.
2. **Never publish instructions that involve:** opening electrical compartments, testing capacitors, gas pressure, refrigerant gauges, pool light fixtures, or bypassing any safety switch.
3. **UNVERIFIED items to resolve before publishing Part 1 E-code content:** obtain the legacy Raypak digital-display manual that actually prints E01–E06 (Raypak tech support, 805-278-5300, or the raypak.com document library) and confirm the IHO label. Same for AquaCal FS (fan vs flow switch by board revision) and HPC/LPC labels — AquaCal support 727-823-5642.
4. Raypak's own AVIA troubleshooting page and TFP's Raypak wiki are strong reader-facing outbound links even though they blocked automated fetch.
