---
entity: pce
domain: website
topic: jandy-error-codes
source: web-research (manufacturer manuals via ManualsLib, Trouble Free Pool, INYO Pools, PoolDial, JustAnswer)
created: 2026-08-16
status: working
audience: customer-facing troubleshooting content, Perfect Catch Electric (licensed pool/electrical/gas contractor, Largo FL)
---

# Jandy Equipment Error Codes — Troubleshooting Research

Research base for customer-facing troubleshooting pages. Every entry: exact code → meaning → causes → SAFE homeowner checks → when it's pro-only. "Homeowner-safe" is limited to: breakers/switches, valves, water level, filter cleaning, salt level, visible cell cleaning, app/router steps. Anything behind a sealed panel, gas-related, or involving wiring/boards is flagged professional-only — PCE holds electrical, pool, and gas licenses, which is the selling point of these pages.

> Sourcing note: primary sources are Jandy installation/operation manuals (via ManualsLib transcriptions), INYO Pools' AquaPure code guide, Trouble Free Pool threads, and PoolDial reference pages. Items marked **UNVERIFIED** could not be confirmed against a manufacturer manual and should be verified against the printed manual before publishing.

---

## 1. Jandy JXi / LXi Gas Heaters

Two diagnostic layers: **display fault messages** on the control panel, and **ignition control LED blink codes** on the Fenwal ignition module (visible through the access panel — homeowners should read them through the window only, not open the cabinet).

### Display fault messages

#### CHECK FLOW (JXi) / FAULT-NO FLOW (LXi)
- **Meaning:** The water pressure switch inside the heater detects insufficient water flow. Heater will not fire.
- **Causes:** Pump off or not primed; dirty/clogged filter; closed or misaligned valves; variable-speed pump running too slow (below the heater's minimum flow); pressure switch out of adjustment or failed.
- **Homeowner-safe checks:** Confirm the pump is running and primed; empty pump and skimmer baskets; clean/backwash the filter; confirm valves are open; if a VS pump, raise the speed while heating.
- **Pro-only:** Pressure switch adjustment or replacement — it's a gas-appliance safety device inside the cabinet.

#### FAULT-HIGH LIMIT
- **Meaning:** Water temperature inside the heater exceeded the internal safety limit and a high-limit switch opened.
- **Causes:** Insufficient flow through the heater (dirty filter, low pump speed); stuck/failed thermal regulator valve in the water header (a known JXi cause — check before condemning sensors, per Trouble Free Pool); failed high-limit switch; blocked exhaust vent.
- **Homeowner-safe checks:** Clean/backwash filter; verify pump speed is adequate; visually check the top vent for leaves/debris/bird nests from outside; power-cycle at the panel (off, wait 30 s, on).
- **Pro-only:** Repeated high-limit trips mean bypass/thermal-regulator or limit-switch diagnosis inside the water header — overheating a gas heater is a safety issue, not a nuisance.

#### FAULT-CHECK IGN CONTROL
- **Meaning:** The ignition control module reports a fault — the heater tried to light and could not, or the module itself faulted.
- **Causes:** Gas valve turned off; air in the gas line (common after new install or propane refill); low gas pressure or undersized gas line; broken/weak hot-surface igniter; no flame at burner; failed gas valve; faulty wiring to the module.
- **Homeowner-safe checks:** Confirm the external gas shutoff valve is ON; confirm propane tank isn't empty; power-cycle the heater once. That's it.
- **Pro-only:** Everything else. Gas pressure testing, igniter replacement, gas valve work, and combustion diagnosis legally and practically require a licensed gas contractor. This is PCE's core "call us" code.

#### FAULT-SHORTED H2O SENSOR / FAULT-OPEN WATER SENSOR
- **Meaning:** The water temperature sensor circuit reads shorted (SHORTED) or disconnected (OPEN).
- **Causes:** Failed water temp sensor; chafed/corroded sensor wiring; loose connection at the power interface board.
- **Homeowner-safe checks:** Power-cycle. Nothing else — the sensor and its wiring live inside the cabinet.
- **Pro-only:** Sensor testing (resistance vs. temperature) and replacement involve opening the heater and working at the control board.

#### FAULT-HIGH FLUE TEMPERATURE (JXi)
- **Meaning:** Flue/vent gas temperature exceeded its limit switch setting.
- **Causes:** Restricted airflow or blocked vent (bird/insect nests are called out in the manual); fan not running or running slow; broken tubing; sooted heat exchanger.
- **Homeowner-safe checks:** Look at the vent/top of heater from outside for obvious obstruction; ensure required clearances around the heater aren't blocked by pool toys, planters, etc.
- **Pro-only:** Flue temperature faults can indicate poor combustion or exhaust restriction — carbon-monoxide territory. Blower and switch replacement is licensed-gas work.

#### FAULT-FUSELINK/FIELD (LXi)
- **Meaning:** The roll-out (fusible link, ~152 °C) or vent-temperature limit (~240 °C) safety opened — flame or heat escaped where it shouldn't.
- **Causes:** Flame roll-out, blocked heat exchanger, loose connection in the safety circuit, failed switch.
- **Homeowner-safe checks:** None. Leave the heater off.
- **Pro-only:** Roll-out trips mean flame outside the combustion chamber. Do not reset and retry — this is an immediate service call.

#### FAULT-PUMP / AUX MONITOR (status line)
- **Meaning (per JXi manual):** Status message — the filter pump is OFF while the heater is programmed in Maintain Temp mode. The manual lists "no service required; normal operation."
- **Homeowner-safe checks:** Turn the pump on or wait for its schedule.
- **Note:** Distinct from CHECK AUX MONITOR below.

#### CHECK AUX MONITOR
- **Meaning:** Fault in the auxiliary monitor circuit on the power interface board — the circuit that watches external safety/control devices (e.g., fireman's-switch-style interlocks from an automation system). **UNVERIFIED** as to exact trigger conditions per model; field reports (Trouble Free Pool, JustAnswer) associate it with the aux safety-circuit input or board issue.
- **Homeowner-safe checks:** Power-cycle heater and automation system once.
- **Pro-only:** Board-level diagnosis on a gas appliance.

#### SERVICE AGS / FAULT AGS (older Laars/LX lineage; some Jandy displays)
- **Meaning:** Automatic Gas Shutoff activated — the safety chain closed the gas valve, commonly on loss of flame sense or water-side overheat.
- **Causes:** Low water flow, high incoming water temp, faulty pressure switch, flame-sense failure.
- **Homeowner-safe checks:** Clean filter, confirm valves open and pump running, one power-cycle.
- **Pro-only:** Anything recurring — AGS exists specifically to stop unsafe gas operation. **UNVERIFIED** whether current-production JXi displays this exact text; confirm per model before publishing.

### Ignition control LED codes (JXi and LXi — read through the window, don't open the panel)

| LED pattern | Meaning | Notes |
|---|---|---|
| Continuous ON | Ignition control fault | Pro-only: module diagnosis/replacement |
| 1 flash | Air flow fault | Blower/air pressure switch circuit — homeowner can check vent for obstruction from outside; the rest is pro-only |
| 2 flashes | Flame detected when there is NO call for heat | Gas valve leaking through or flame-sense fault. Turn the heater OFF and call immediately — uncontrolled gas/flame condition |
| 3 flashes | Ignition lockout — three failed ignition attempts (soft lockout) | Auto-retries after ~1 hour. Homeowner: verify gas valve on / propane level, power-cycle once. Repeated lockouts = licensed gas service |

**Blower/fan faults:** The JXi manual attributes HIGH FLUE TEMP and ignition air-flow faults to "fan not operating / fan running slow," remedy "correct fault or replace fan" — there is no standalone "FAULT BLOWER" display text confirmed in the manual pages reviewed. **UNVERIFIED** as a distinct display code; treat blower failure under the air-flow/flue-temp entries.

**Sources (heaters):**
- JXi manual, Service Diagnostic Messages + Ignition Control LED Service Codes: https://www.manualslib.com/manual/1959645/Jandy-Jxi-200.html?page=41 and https://www.manualslib.com/manual/1166078/Jandy-Jxi-200.html?page=38
- LXi manual, Table 12 Service Codes + Table 10 LED codes: https://www.manualslib.com/manual/737177/Zodiac-Jandy-Lxi.html?page=40 (and page 42)
- Trouble Free Pool JXi wiki (thermal regulator → high-limit note): https://www.troublefreepool.com/wiki/index.php?title=Jandy_JXI_Heaters
- PoolDial JXi/LXi code reference: https://pooldial.com/jandy-heater-error-codes
- CHECK AUX MONITOR field reports: https://www.troublefreepool.com/threads/jandy-heater-error-message-check-aux-monitor.161401/ , https://www.justanswer.com/pool-and-spa/ap4lr-pool-heater-code-that-s-reads-check-aux-monitor.html
- AGS meaning: https://www.justanswer.com/pool-and-spa/5txgj-does-mean-jandy-heater-flashing-service.html

---

## 2. Jandy AquaPure / TruClear Salt Systems

AquaPure shows numeric service codes. **Level 1 codes (120–175)** are the customer-visible codes; **Level 2 codes (180–195)** are the underlying diagnostic that *generates* a Level 1 code (a tech reads them from the service menu). TruClear reports faults on its panel/iAquaLink app; several of the same numeric codes (172, 185, 186) plus plain-text "No Flow" / "Check Cell" / low-salt indications.

### Level 1 service codes

| Code | Meaning | Causes | Homeowner-safe checks | Pro-only when |
|---|---|---|---|---|
| **120** | Low current to cell, forward direction | Scaled/worn cell; DC cord connection | Inspect cell for white scale; clean per Jandy acid-wash procedure; verify salt ~3.0–3.5 gpl with test strips | Persists after clean cell + cord check → board/DC output measurement (live electrical diagnosis) |
| **121** | Low current to cell, reverse direction | Same as 120 | Same as 120 | Same as 120 |
| **123** | Extremely low current to cell | Severely scaled or end-of-life cell; DC cord | Clean cell; check cord ends for corrosion (unplug at cell only) | If new cell + cord doesn't clear it, back board diagnosis |
| **124** | Higher-than-normal current to cell | Back board fault | None meaningful | Board fault — electrical service |
| **125** | Cell needs cleaning (low output) | Scaled cell; tri-sensor issue; end-of-life cell (see 194) | Clean cell; verify salt level; power-cycle | Recurs immediately after cleaning → cell replacement or sensor/board test |
| **126** | Low forward current + low voltage | Supply voltage / transformer / back board | Check breaker; confirm nothing else tripping | Voltage/transformer testing is live electrical work |
| **127** | Low reverse current + low voltage | Same as 126 | Same as 126 | Same as 126 |
| **144** | Low salinity (below 2.0 gpl) | Not enough salt; splash-out/rain dilution; cold water reading low | Test salt independently with strips; add pool salt toward 3.0–3.5 gpl (dissolve fully, retest before adding more); note water under ~60 °F reads artificially low | Salt tests fine but code persists → sensor/board diagnosis |
| **145** | High salinity (above 4.0 gpl) | Over-salting; sensor drift | Test independently; partially drain and refill to dilute | Reading clearly wrong vs. test kit → tri-sensor replacement |
| **170** | Front board service condition / unit not wired to correct 115 VAC | Low AC voltage from back board; transformer | Check the breaker feeding the system | Wiring/transformer/board — licensed electrical work (PCE specialty) |
| **171** | Back board service condition | Defective back board; relay failure (see 189/190) | Power-cycle once | Board replacement |
| **172** | Flow sensor not detecting flow / sensor fault | Pump off; valves; dirty flow sensor; sensor failure; loose sensor cable | Confirm pump running, valves open, filter clean; check that the sensor cable is plugged in (external connector only) | Sensor replacement or board test |
| **173** | Low input voltage or wiring error | Wrong supply voltage tap; loose supply wiring | Breaker check only | Supply-voltage verification is electrician work |
| **174** | High water temperature (>108 °F at sensor) | Spa mode overshoot; sensor error | Let water cool; verify actual water temp with a thermometer | Persistent false reading → tri-sensor |
| **175** | Flow sensor airlock or very low salinity | Air trapped at sensor; near-zero salt | Run pump to purge air; verify salt with strips | Recurring airlock → plumbing/sensor orientation check |

### Level 2 service codes (tech-level; each "generates" the Level 1 code shown)

| Code | Meaning | Generates | Disposition |
|---|---|---|---|
| **180** | Heating element of the sensor not heating (sensor's internal heater failed) | 172 | Tri-sensor replacement — pro |
| **181** | Temperature sensor malfunction | 172 | Tri-sensor replacement — pro |
| **182** | Salinity sensor reads < 0.2 gpl | 175 | No salt present or sensor airlock; homeowner can verify salt, rest is pro |
| **183–186** | Temperature probe errors (out-of-range readings) | 172 | Board test / tri-sensor replacement — pro |
| **187** | Front power supply out of range | 173 or 170 | Electrical — pro |
| **188** | VAC input voltage too low | 173 | Supply wiring/voltage — pro |
| **189** | Forward relay failure | 171 | Back board replacement — pro |
| **190** | Reverse relay failure | 171 | Back board replacement — pro |
| **191** | High cell current + low voltage | 170 | Front board service — pro |
| **192** | High cell current + low voltage | 171 | Back board service — pro |
| **193** | Unexpected cell current | 170 | Front board service — pro |
| **194** | Cell current 85% below target with cell voltage above 19 V | 125 | Classic end-of-life salt cell — replacement (homeowner may swap a plug-in cell on some models; confirm model before advising) |
| **195** | Invalid salinity reading | 170 | Front board service — pro |

### TruClear-specific
- **No Flow:** Flow switch not detecting ≥ ~20 GPM. Homeowner: pump on, baskets/filter clean, valves open. Persisting → flow switch cleaning/replacement (pro).
- **Check Cell:** Scaled or failing cell. Homeowner: breaker off, inspect/clean cell, restore power. Recurs → cell or board.
- **Low salt with good test-strip result:** Usually flow switch or scaled cell, not salt. Cold water (< ~50 °F) also suppresses output legitimately.
- Numeric codes 172/185/186 appear on TruClear via panel/app with the same sensor/communication meanings as AquaPure. **UNVERIFIED** — confirm against the TruClear manual before publishing TruClear-specific numeric-code claims.

**Sources (salt systems):**
- INYO Pools complete AquaPure code guide (primary for both tables): https://diy.inyopools.com/article/jandy-aquapure-error-codes/
- Trouble Free Pool alternating 123/125/194 thread: https://www.troublefreepool.com/threads/jandy-aqua-pure-alternating-error-codes-123-125-194-already-replaced-port-sensor.143162/
- PoolDial AquaPure troubleshooter: https://pooldial.com/jandy-aquapure-troubleshooter
- PoolDial TruClear guide: https://pooldial.com/resources/articles/jandy/truclear/jandy-truclear-troubleshooting-guide
- TruClear field Q&A: https://www.justanswer.com/pool-and-spa/t75kg-jandy-truclear-salt-cell-check-error.html

---

## 3. Jandy VS FloPro / ePump Variable-Speed Pumps

Jandy VS pumps report E-prefixed drive fault codes (on the JEP-R controller display or via iAquaLink). Jandy publishes fewer codes publicly than Pentair/Hayward; the list below is assembled from third-party references and field reports — **treat codes not confirmed in the JEP-R/VS FloPro manual as UNVERIFIED before publishing.**

| Code | Meaning | Causes | Homeowner-safe checks | Pro-only when |
|---|---|---|---|---|
| **E01** (UNVERIFIED vs. manual) | Stuck rotor | Debris jamming impeller | Breaker OFF, remove pump lid, clear basket; do NOT reach into the volute | Impeller/diffuser disassembly |
| **E02** (UNVERIFIED vs. manual) | Overcurrent — drive sensed excessive draw | Binding motor, shorted winding, debris | Power-cycle 5 min | Recurs → motor/drive diagnosis (live electrical) |
| **E22** | DC bus over-voltage | Supply voltage high/unstable; wiring; older AquaLink RS board revision (pre-Rev O) interaction | Power-cycle 5 min | Wire-gauge/voltage correction and board-rev check — electrician |
| **E23** | DC bus under-voltage | Undersized wire on long runs (most common per field references — #10 AWG recommended beyond ~100 ft); loose connections; utility sag | Power-cycle; note whether it happens when other big loads start | Wiring upgrade — electrician (PCE core work) |
| **E2E** | Drive overheat | Poor ventilation, sun exposure, clogged heatsink fins, blocked side/rear clearance | Clear vegetation/objects around pump; add shade; hose dirt off exterior fins with power OFF | Persistent overheat → drive service |
| **E2F** | Motor phase fault | Internal motor/drive fault; condensation in high-humidity climates (Florida explicitly cited) | One 5-minute power cycle | Returns immediately → motor/drive assembly replacement |
| **FAULT: PUMP NOT CONNECTED** (JEP-R display) | Controller can't reach pump over RS-485 | Broken/miswired RS-485 (red/black/yellow/green order), corroded connections, wrong DIP address | Power-cycle controller and pump | Comm wiring and DIP switches are inside energized enclosures |

Non-code drive symptoms worth a page section: pump enabled on the panel but motor never spins = likely failed drive board; won't prime = suction air leak/lid o-ring/pump too high above water (homeowner can clean and re-seat the lid o-ring).

**Sources (pumps):**
- ProTuff VS pump fault code comparison (E22/E23/E2E/E2F): https://www.protuffproducts.com/equipment-use/variable-speed-pump-fault-codes/
- PoolDial VS FloPro troubleshooting guide (RS-485, DIP, priming, thermal): https://pooldial.com/resources/articles/jandy/vs-flopro/jandy-vs-flopro-troubleshooting-guide
- E01/E02 and general Jandy pump troubleshooting: https://www.poolsparepairs.com/troubleshooting-jandy-pool-pump/
- JEP-R manual (Jandy doc H0412200) for verification: https://www.jandy.com/en/products/pool-pumps/pump-controls/jep-r

---

## 4. Jandy AquaLink RS / iAquaLink Automation

AquaLink doesn't use numeric fault codes; it surfaces text states and connectivity failures. Most service calls are comm-wiring or board-level.

### Common fault states

| Displayed state | Meaning | Causes | Homeowner-safe checks | Pro-only when |
|---|---|---|---|---|
| **Waiting for Connection** (iAquaLink app/antenna) | The iAquaLink web device can't reach the router/Jandy cloud | Wi-Fi credentials/band issues (older iAquaLink antennas need 2.4 GHz and, on early units, 802.11b/mixed-mode compatibility); weak signal; ISP/router change | Power-cycle router and the AquaLink at the breaker; check signal strength (OneTouch: Menu → Help → Diagnostics shows bars out of 5); move router closer or add an extender; re-run Wi-Fi setup in the app | Antenna replacement or hardwiring the jbox |
| **No Operations Allowed Here** | Power center is in Service or Timeout mode — remote control is intentionally locked out | Someone set Service mode at the power center | Set the Service/Timeout/Auto switch back to AUTO at the power center door panel | If it won't leave Service mode, board diagnosis |
| **System offline in app, local control works** | Antenna ↔ board or antenna ↔ internet link down | Loose/miswired RS-485 4-wire connector (red/black/yellow/green — and it must be on the RS-485 header, not the "RS4/RS8 ONLY" header, a documented field mistake); failed antenna; no 12 V DC to antenna | Full power-cycle at the breaker; router reboot | RS-485 wiring inside the power center is behind the dead-front — electrician |
| **Aux equipment won't respond / relay doesn't click** | Relay, actuator, or board output failure | Failed relay, tripped GFCI on that circuit, actuator unplugged | Check the equipment's own breaker/GFCI; listen for the relay click when toggling | Relay/board replacement, actuator wiring |
| **Frozen or garbled display / random behavior** | Board or comm corruption; surge damage (common after lightning in Tampa Bay) | Surge, corroded connections, failing PPD/board | One full power-cycle at the breaker | Board-level repair; recommend surge protection |
| **Temp sensors reading wrong (air/water/solar)** | Open/shorted 10k sensor | Sensor or wiring failure | Compare against a real thermometer to confirm it's the sensor | Sensor swap at the board terminals — inside the power center |

### Connectivity notes for content
- Early iAquaLink antennas are 2.4 GHz-only and can require the router in b/g mixed mode; modern mesh systems that force band steering are a recurring cause of "Waiting for Connection." (Trouble Free Pool threads, JustAnswer.)
- The antenna needs stable 12 V DC from the board; corrosion at that connector mimics antenna failure.
- Firmware/board revision matters for VS pump integration (Rev O+ for some pump features) — a good upsell note for PCE board-upgrade services. **UNVERIFIED** exact revision matrix; confirm with Jandy docs before publishing specifics.

**Sources (automation):**
- Trouble Free Pool — iAquaLink offline: https://www.troublefreepool.com/threads/iauqalink-is-offline.51083/
- Trouble Free Pool — online but "Waiting for connection": https://www.troublefreepool.com/threads/iaqualink-online-operating-correctly-but-always-waiting-for-connection.287370/
- Trouble Free Pool — AquaLink RS comm issue: https://www.troublefreepool.com/threads/aqualink-rs-issue.266401/
- JustAnswer antenna/RS-485 header mistake: https://www.justanswer.com/pool-and-spa/pg401-2nd-opinion-please-not-close-i-no-red-power-light.html
- JustAnswer "Waiting for connection" loop: https://www.justanswer.com/home-security-systems/trm3j-jandy-aqualink-3-0-waiting-for-connection-loop.html

---

## Editorial guardrails for the published pages

1. **Never instruct** opening the heater cabinet, touching gas piping, opening the AquaLink dead-front, or probing any board. The homeowner-safe column above is the outer limit.
2. Every code section should end with the same CTA logic: one power-cycle + the listed safe checks → if the code returns, it's a licensed-repair item (gas: JXi/LXi ignition/flue/AGS; electrical: boards, E22/E23 wiring, 170-series AquaPure codes).
3. Two codes warrant "stop and call now" language: **heater LED double-flash** (flame with no call for heat) and **FAULT-FUSELINK/FIELD** (roll-out).
4. Resolve all UNVERIFIED flags against printed Jandy manuals (JXi H0574200, LXi, AquaPure PLC1400, TruClear, VS FloPro/JEP-R H0412200) before publishing.
