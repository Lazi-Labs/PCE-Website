---
entity: pce
domain: servicetitan
vendor: pentair
source: web-research
created: 2026-08-16
status: working
---

# Pentair Equipment Error Codes — Troubleshooting Research

> Research base for Perfect Catch Electric customer-facing troubleshooting content (Largo, FL — licensed pool / electrical / gas contractor). Every entry: exact code or light pattern, technical meaning, plausible causes, SAFE homeowner self-checks, and where the line falls to professional-only work. Items that could not be confirmed against a manual or reputable source are marked **UNVERIFIED**.
>
> **Editorial safety rule for published content:** homeowner steps never include opening sealed compartments, removing heater panels beyond checking the visible display, gas work, or any wiring. Anything involving the control board, gas train, sensors, high-limit switches, or line-voltage wiring is professional-only — in Florida, gas and electrical repairs on pool heaters require licensed trades (PCE holds both).

---

## 1. Pentair MasterTemp Gas Heaters (125 / 200 / 250 / 300 / 400)

### How the indicator system works

- The membrane pad on the front of the heater has status LEDs, including a **"Service System"** light and a **"Service Heater"** light, plus a digital display that can show `E`-codes and `ERR` codes.
- Behind the top access panel, the control board has **five diagnostic LEDs — PS, HLS, AFS, AGS, SFS** — each tied to a safety circuit. When "Service Heater" comes on, one of these board LEDs identifies which safety tripped. (Reading the board LEDs requires removing panels — treat as professional-only in customer content; the customer-facing version should stop at "note which front-panel light is on and call us.")

### Front-panel lights

| Indicator | Technical meaning | Plausible causes | Safe homeowner checks | Professional-only when |
|---|---|---|---|---|
| **Service System light** | The heater's water-side safety chain is open — most commonly the water pressure switch is not detecting flow. Heater will not fire. | Dirty filter, closed/misaligned valves, pump off or on low speed, air lock after cleaning, failed pressure switch, stuck thermal regulator | Confirm the pump is running at normal (high) speed; check filter pressure gauge and clean/backwash a dirty filter; check skimmer/pump baskets; confirm valves feeding the heater are open; check pool water level | If flow is confirmed good and the light stays on — pressure switch adjustment/replacement or internal bypass/thermal regulator work means opening the plumbing/cabinet |
| **Service Heater light** | The control detected a fault in the combustion/safety chain; a specific board LED (PS, HLS, AFS, AGS, SFS) or display code identifies it. Heater locks out. | See individual codes below | Note the display code, power-cycle **once** at the breaker/timer; if it returns, stop | Yes — diagnosing which safety tripped requires panel removal and testing gas-side and 240V components |

### ERR / safety-circuit codes (also shown as board LEDs)

| Code | Technical meaning | Plausible causes | Safe homeowner checks | Professional-only when |
|---|---|---|---|---|
| **ERR PS** (Pressure Switch) | Water pressure switch open — heater doesn't see enough water flow to fire safely. Auto-clears when flow is restored. | Dirty filter, low pump speed, closed valves, clogged baskets, low water level, failed switch | Clean filter (watch the pressure gauge), empty baskets, verify pump on high speed, top off water level | Persistent with good flow → switch calibration/replacement (inside cabinet, near hot exchanger plumbing) |
| **ERR HLS** (High Limit Switch) | Water leaving the first pass of the heat exchanger exceeded ~135°F — overheat safety opened. | Low flow through the heater, scaled/sooted heat exchanger, stuck thermal regulator, failing HLS switch | Same flow checks as ERR PS (filter, baskets, valves); allow heater to cool | Repeated trips → exchanger scaling, thermal regulator, or switch replacement; some models require a manual reset inside the cabinet — professional-only |
| **ERR AFS** (Air Flow Switch) | Blower vacuum switch didn't prove combustion air — the heater refuses to release gas. Auto-clears when airflow is restored. | Blocked exhaust vent, debris/animal nest in air intake, weak blower motor, cracked vacuum tube | Look at the top vent from outside — clear leaves/debris off the exterior grille only; make sure nothing is stacked around the heater blocking airflow | Blower, vacuum tubing, or switch replacement — combustion-side components |
| **ERR AGS** (Automatic Gas Shutoff) | Water temperature after the second exchanger pass exceeded ~140°F — the redundant overheat safety cut the gas. **Front panel is disabled; requires a power cycle.** | Serious flow restriction, failed thermal regulator, scaled exchanger, failed AGS sensor | None beyond confirming flow basics; one power cycle. If it recurs, shut the heater off and call | Yes — a tripping AGS means the primary safeties may also be compromised; gas-side safety diagnosis is licensed-gas work |
| **ERR SFS** (Stack Flue Sensor over-temp) | Exhaust stack temperature exceeded ~480°F — combustion is running dangerously hot. **Front panel disabled; power cycle required.** | Sooted heat exchanger, poor combustion (gas pressure, air mix), blocked flue, low water flow | None. Turn the heater off and call | Yes — flue-temperature faults are a fire/CO risk indicator; combustion analysis is professional gas work |
| **ERR IGN** (Ignition failure) | The ignition module tried to light the burner 3 times and never proved flame; lockout. Reset by pressing HEATER OFF / power cycle. | Gas supply valve closed, low gas pressure (empty LP tank), fouled igniter, bad flame sensor, failed gas valve | Confirm the gas supply valve to the heater is on and (LP) the tank isn't empty; press "Heater Off" then back on **once** | Yes after one retry — igniter, flame rectification, and gas-valve work require a gas license |

### E-codes (sensor circuit faults)

| Code | Technical meaning | Plausible causes | Safe homeowner checks | Professional-only when |
|---|---|---|---|---|
| **E01** | Water temperature sensor (thermistor) circuit **open**. Reset via HEATER OFF button. | Disconnected/broken sensor wire, failed thermistor | Press Heater Off to reset once | Yes — sensor and wiring inspection is inside the cabinet |
| **E02 / code 126** | Water temperature sensor circuit **shorted**. (Some sources show this as display code "126.") | Water intrusion into the sensor, failed thermistor | None | Yes — sensor replacement |
| **E05** | Stack flue sensor circuit **open** (sensor reads exhaust temp; trips at ~176°F thresholds). | Broken sensor wire, failed sensor; can accompany clogged exhaust, sooted exchanger, low flow | None | Yes — flue-side component |
| **E06** | Stack flue sensor circuit **shorted**. | Water-damaged or failed sensor element | None | Yes |
| **"ERS"** | **UNVERIFIED** — "ERS" appears frequently in homeowner descriptions but is not a code in Pentair's documented list. It is most likely a misreading of the segmented display showing an `ERR` prefix (e.g., "ERR PS" cycling) or a partially failed display. | — | Note exactly what the display cycles through (photo/video helps the tech) | Treat as a Service Heater fault — diagnose on site |
| **R13 / R+8 / 128-style display codes** | **UNVERIFIED** — homeowners report odd register-style readouts (e.g., "R 8 128"); these are display/diagnostic register views, not standard fault codes. | Display board or firmware quirk | Photo of the display for the tech | Yes |

### Thermal regulator (no code — a recurring root cause)

The internal thermal regulator meters water through the heat exchanger to keep it at operating temperature. When it sticks **closed**, water overheats inside the exchanger → recurring HLS/AGS trips and "Service System" lights even with a clean filter. When it sticks **open**, the heater runs cool, condenses, and soots up (leading to SFS/E05 problems later). There is nothing homeowner-serviceable here; it lives inside the heater's water manifold. Replacing the thermal regulator (often together with the thermistor, HLS, and AGS sensors) is a common, permanent fix for phantom service lights.

**Sources (Section 1):**
- https://greysharkpools.com/guides/equipment/pentair-mastertemp-heater-troubleshooting/
- https://www.pooldial.com/pentair-heater-error-codes
- https://www.epoolsupply.com/blogs/default-blog/pentair-pool-heater-error-codes
- https://www.poolspecialists.com/articles/MasterTemp%20E01%20E02%20E05%20E06%20Error%20Codes.pdf
- https://www.troublefreepool.com/wiki/index.php?title=Pentair_MasterTemp_Heaters (403 to fetcher; thread refs used)
- https://www.troublefreepool.com/threads/pentair-mastertemp-service-heater-light.326532/
- https://heaterfixlab.com/pentair-mastertemp-400-service-heater-light-on/
- https://splashdr.com/how-to-diagnose-and-fix-a-pentair-mastertemp-swimming-pool-heater/

---

## 2. Pentair Variable-Speed Pumps (IntelliFlo / IntelliFlo3 VSF / SuperFlo VS)

### IntelliFlo & IntelliFlo3 VSF — named alarms (red light = pump stops; yellow/warning = pump keeps running)

| Alarm | Technical meaning | Plausible causes | Safe homeowner checks | Professional-only when |
|---|---|---|---|---|
| **Blocked System / Suction Blockage** | The drive detected the pump dead-heading or a blocked suction and shuts off within ~1 second (SVRS-equipped models). | Blocked skimmer/main drain, closed valve, full pump basket, entrapment-detection trip | Open/verify suction valves, empty skimmer and pump baskets, clear visible debris from skimmer, restart | Recurring trips with clear plumbing → flow sensor / drive diagnosis |
| **Priming Failure / Priming Alarm** | Pump couldn't verify prime within "Max Priming Duration"; alarms for 10 min, retries, and after 5 consecutive failures locks out until Reset is held. | Low water level, air leak at pump lid o-ring, suction-side air leak, closed valve, empty pump basket housing | Top off pool water; check pump lid is hand-tight and the o-ring is seated/clean; empty baskets; open valves; press/hold Reset once | Persistent air leaks (union/valve gland/suction plumbing) or seal replacement |
| **Overheat / Drive Temperature** | Drive electronics exceeded ~130°F (54.4°C); the pump first **derates** (slows itself), then stops if it can't shed heat. | Direct afternoon sun, blocked fan/vents, dead cooling fan, high ambient (equipment room), wiring issues | Clear leaves/objects blocking the drive vents; it often runs normally after cooling in the evening — note the pattern | Fan replacement, wiring, or persistent thermal derating |
| **Over-Current** | Drive tripped to protect itself from excess motor current. | Debris jamming the impeller, bearing/part interference, low or bad supply voltage, aging motor | Power-cycle at the breaker once; empty baskets | Yes if it recurs — impeller access and voltage testing are pro tasks (opening the wet end / electrical testing) |
| **Over-Voltage** | Supply voltage above range — or the pump is being **spun backward by water flow** while off (water flowing downhill through it turns the motor into a generator). | Utility voltage spike, wiring problem, elevated-pool backflow through the pump | Note when it happens (storms? pump off?) for the tech | Yes — voltage measurement and check-valve/wiring corrections are electrician work |
| **Under-Voltage / Power Out** | Supply voltage below required range; drive shuts down. | Voltage drop on the circuit, loose lugs, brown-outs, undersized wiring | Check whether other equipment on the same panel is affected; note time of day | Yes — anything at the breaker panel or pump terminals is licensed electrical work |
| **Internal Error / Internal Fault** | Drive's software self-monitoring caught an inconsistency. | Firmware glitch, failing drive hardware | Clear the alarm and restart once | Recurring → drive service/replacement (Pentair support 1-800-831-7133) |
| **Derating Alarm / Exceeded and Cut Off** (IntelliFlo3) | Motor couldn't reduce speed enough to protect itself and stopped. | Sustained heat or load condition | Same as Overheat checks | Yes if recurring |
| **Thermal Mode** (warning) | Pump self-runs based on drive temperature to prevent freeze damage — **normal protective behavior**, not a fault. | Cold snap (yes, even in Florida) | None needed; don't switch the pump off at the breaker during a freeze | — |
| **Speed / Pressure / Flow Limit** (warnings) | Pump hit a programmed maximum and is self-limiting; keeps running. | Dirty filter raising pressure (pressure limit), aggressive schedule settings | Clean the filter if pressure-limited; note which limit shows | Reprogramming limits / hydraulic evaluation |
| **Weak Wi-Fi / Offline** (IntelliFlo3) | App-connectivity warnings only — pump still runs its schedule. | Router distance, antenna obstruction, power/Wi-Fi outage | Reboot router; move obstructions; re-pair in Pentair Home app | — |

### SuperFlo VS — numeric fault codes (shown on the drive keypad)

| Code | Technical meaning | Plausible causes / notes | Safe homeowner checks | Professional-only when |
|---|---|---|---|---|
| **0021** | Communication link lost between the keypad (HMI) and the motor-control board. | The classic cause is **moisture intrusion or a loose 5-pin connector** on the jacketed cable behind the keypad, under the drive top cover; also corrosion on the pins. Very common on SuperFlo VS. | Power-cycle at the breaker (off until keypad LEDs go dark, then on). If it returns, stop | Yes — fixing it means opening the drive cover with power secured; connector cleaning/reseating and gasket sealing are tech work |
| **0002** | Absolute phase current limit exceeded (internal). | Internal drive error | One hard power cycle | Recurs → drive service |
| **0004** | Power module temperature limit exceeded. | Drive overheating internally | Clear vents of debris; one power cycle | Recurs → drive service |
| **0006** | PFC temperature limit exceeded. | Internal thermal | One power cycle | Recurs |
| **0008** | Diode bridge temperature limit exceeded. | Internal thermal | One power cycle | Recurs |
| **0009** | DC bus over-voltage. | Supply spike / internal | One power cycle | Voltage testing = electrician |
| **000A** | DC bus under-voltage. | Supply sag / internal | One power cycle; note brown-out timing | Voltage testing = electrician |
| **000F** | Absolute AC under-voltage — supply dropped below ~99V. | Utility sag, loose connections, undersized circuit | May self-clear; note pattern | Yes — supply-side diagnosis |
| **0016** | Phase current imbalance detected. | Internal diagnostic | Hard power cycle | Recurs |
| **0017** | Phase current offset out of range. | Internal diagnostic | Hard power cycle | Recurs |
| **001A** | Power module over-current. | Rotating-assembly problem — impeller jam or mechanical seal drag | Empty baskets; one power cycle | Yes — wet-end disassembly |

**RS-485 "Comm Error" (any Pentair VS pump on automation):** pump display or automation shows a communication error with EasyTouch/IntelliTouch/IntelliCenter. Causes: loose or reversed green/yellow RS-485 wires, damaged comm cable, electrical noise, failed comm port. Homeowner check: none beyond power-cycling the automation panel breaker once — comm wiring lands inside the load center next to line voltage, so it's professional-only.

**Sources (Section 2):**
- https://www.pooldial.com/resources/articles/pentair/intelliflo/pentair-intelliflo-troubleshooting-guide
- https://www.epoolsupply.com/blogs/default-blog/how-to-identify-alarms-and-warnings-on-pentair-home-app-for-intelliflo3-vsf
- https://www.epoolsupply.com/blogs/default-blog/pentair-superflo-vs-error-codes
- https://www.manualslib.com/manual/121631/Pentair-Intellitouch-Screenlogic.html?page=103 (IntelliFlo alarms via ScreenLogic)
- https://www.troublefreepool.com/threads/error-0021-on-pentair-superflo-vs.258252/
- https://techfaultfix.com/pool-pumps/pentair/error-comm-error-intelliflo-intellipro-vs-or

---

## 3. Pentair IntelliChlor Salt Cells (IC15 / IC20 / IC40 / IC60)

### Reading the panel

- **Sanitizer output LEDs (5 green):** bar graph of output setting. 20–100% = solid LEDs; 2–10% = **blinking** LED (normal, not a fault). All lights **scrolling in sequence = Boost/Superchlorinate mode** (100% for 24 hrs) — cancel by holding "More" + "Less."
- **Flow light:** **Green** = adequate flow, chlorine being produced. **Red** = insufficient flow, production stopped.
- **Salt lights:** green = OK (roughly 2,800–4,500 ppm band); red LOW SALT and red VERY LOW SALT below thresholds.
- **Cell light:** green = cell energized and producing; flashing = needs attention (inspection/cleaning); off with LOW SALT = production suspended.

### Light patterns

| Pattern | Technical meaning | Plausible causes | Safe homeowner checks | Professional-only when |
|---|---|---|---|---|
| **Green flow light + green salt + solid output LEDs** | Normal operation | — | — | — |
| **Red FLOW light** | Flow switch doesn't see enough water; chlorine production stopped | Pump off/low speed, dirty filter, full baskets, air in system, failed flow switch, debris on the switch paddle | Verify pump running at adequate speed, clean filter, empty baskets; production resumes when flow returns | Flow-switch replacement or persistent red light with good flow |
| **Solid red LOW SALT** | Salinity has dropped into the low band (~2,600–2,900 ppm area); cell still produces at reduced efficiency | Rain/backwash dilution, splash-out, aging salt reading | Test salt independently (test strips or a pool-store sample); add salt per pool volume; run the pump 24 hrs before re-reading | If the panel still reads low after independent test confirms 3,200+ ppm → cell reading drift; recalibration/cell evaluation |
| **Flashing red LOW/VERY LOW SALT** | Salinity below ~2,600 ppm — **cell stops producing chlorine** and the CELL light goes blank | True low salt; OR cold water (cold water reads as lower salinity); OR a worn cell under-reading | Independent salt test first — don't dump salt in on the panel's word; add only the calculated amount; allow 24 hrs circulation | Reading stays wrong after verified salt level → cell nearing end of life (typ. 3–5 yr) |
| **Flashing green salt light** | Salt too high (above ~4,500 ppm) | Over-salting, evaporation concentration | Independent test; partial drain/refill dilutes (in FL summer, rain often fixes it) | — |
| **Green and red salt lights flashing together** | Inconsistent salinity readings / sensor confusion | Scale on cell blades, temperature swing, failing cell electronics | Independent salt test; visual check of the cell window for scale | Cell cleaning beyond a rinse, or replacement |
| **Flashing green CELL / STATUS light** | "Inspect cell" — the unit is asking for the cell blades to be checked for calcium scale or debris | Calcium buildup (very common with FL hard fill water), debris lodged between plates; also comes on automatically after ~500 hrs as a maintenance reminder | Looking through the cell's clear body for white flaky deposits is fine. **We recommend leaving acid-washing to us**: removal is simple, but the cleaning solution is diluted muriatic acid | Acid cleaning (chemical handling), and any case where cleaning doesn't clear the light — hold the reset per manual or replace cell |
| **Red COLD WATER light** | Water below the production threshold (~52°F) — chlorine output suspended to protect the cell | Winter water temps | Nothing wrong — normal protective behavior; supplement with liquid chlorine while cold | — |
| **No lights at all** | Cell not receiving power/communication | Power center fuse, transformer, cable damage, automation COM LINK failure | Confirm the power center's power switch/breaker is on | Yes — fuse/board work inside the power center is electrical |

**Note for content:** IntelliChlor thresholds vary slightly by source (2,600 vs 2,800 ppm low-salt trip). Pentair's ideal is ~3,400 ppm; the operating band commonly cited is 2,800–4,500 ppm. Use "target ~3,400 ppm" in customer copy and avoid hard cut-offs.

**Sources (Section 3):**
- https://www.pentair.com/content/dam/extranet/nam/pentair-pool/residential/sanitizers/intellichlor/intellichlor-installation-users-guide-ic15-ic20-ic40-ic60.pdf
- https://www.pentair.com/content/dam/extranet/nam/pentair-pool/pool-manuals/intellichlor/IntelliChlor_Quick_Start_Guide_and_Tips_English.pdf
- https://support.aqua-tech.ca/support-posts/intellichlor-flashing-lights/
- https://www.funcenterpools.com/en/help/pentair/intellichlor/what-does-a-red-low-salt-light-and-a-flashing-green-cell-light-mean-on-an-intellichlor
- https://www.poolspecialists.com/articles/Pentair%20Salt%20Cell%20Troubleshooting%20Guide.pdf
- https://www.inyopools.com/HowToPage/how_to_recalibrate_the_salt_level_on_a_pentair_intellichlor.aspx

---

## 4. Pentair Automation (EasyTouch / IntelliTouch / IntelliCenter / ScreenLogic)

### Common fault messages

| Message | Technical meaning | Plausible causes | Safe homeowner checks | Professional-only when |
|---|---|---|---|---|
| **COM LINK ERROR** (EasyTouch/IntelliTouch display) | Panel lost communication with the IntelliChlor salt cell / IntelliChlor power center | Damaged or loose 4-wire cable from cell to motherboard, corroded connector, failed power center board | Power-cycle the panel breaker once | Yes — the connection lands on the motherboard inside the live load center |
| **Comm Error / no pump communication** | Automation lost RS-485 comms with an IntelliFlo/VS pump | Loose or reversed green-yellow comm wires, cable damage (landscapers, rodents), electrical noise, failed port | Power-cycle panel and pump once | Yes — comm terminals are inside the load center |
| **"No Comm" / "Address Lock" (wired EasyTouch remote / indoor panel)** | Remote panel can't talk to the main board, or two devices conflict on the same address | RS-485 wiring fault to the remote, address conflict after adding a device | Power cycle once | Yes — wiring and address configuration |
| **Air Err** (air temp sensor) | Ambient air sensor open/shorted — **freeze protection may not work** | Unplugged/damaged sensor on the board, corrosion | None (sensor is inside the enclosure). In a FL cold snap, run the pump manually overnight until repaired | Yes — sensor replacement at the board |
| **Water Err / Water Sensor Error** | Water temp sensor fault — heater control and displays misread | Failed/miswired thermistor at the plumbing | Note whether displayed water temp is obviously wrong (e.g., 32°F in summer) | Yes |
| **Solar Err** | Solar temp sensor fault (only matters if solar is configured) | Failed roof sensor, cut wire | None | Yes |
| **Freeze protection active / equipment turning on by itself at night** | Not a fault — the panel runs pumps (and rotates valves) when air temp nears ~36°F | Cold weather; can also trigger falsely if the air sensor fails or sits in sun/shade badly | Nothing to fix; don't kill the breaker in cold weather. If it triggers on a 70°F night, the air sensor is suspect → service call | Sensor relocation/replacement |
| **Circuits stuck on after power interruption** | Freeze-protect/aux states can be inconsistent after an outage | Power blip mid-cycle | One clean power cycle of the panel breaker | Persistent relay chatter or stuck relays |
| **EasyTouch "Error Code 4" (Compool-to-EasyTouch upgrades)** | **UNVERIFIED** — reported on upgrade kits; Pentair partner KB covers it but exact meaning not confirmed in this research pass | — | — | Yes |

### ScreenLogic / app connectivity issues (not equipment faults — the pool still runs)

| Symptom | Meaning | Plausible causes | Safe homeowner checks |
|---|---|---|---|
| **"Looking for controller…" (>60 sec)** | App can't reach the Protocol Adapter, or the adapter can't reach the load center | Adapter unplugged, router rebooted onto a new IP for the adapter, ISP/router change, adapter firmware | Check the Protocol Adapter (small black box near the router) is powered; reboot router, then adapter; reopen app |
| **"ERROR: Address Invalid" / can't connect remotely** | App's stored address for the system is stale | Adapter's IP changed on the LAN; DHCP reassignment is the most frequent real-world cause | Delete and re-add the system in the app while on the home Wi-Fi; reboot router |
| **Adapter present but unresponsive** | Adapter hung | Firmware lockup, power blip | Reset: press the adapter's recessed reset button 3 times (~half-second presses) with a paperclip; or unplug 30 sec |
| **App works at home, not away** | Remote relay/port issue | Pentair cloud relay hiccup, router firewall, double-NAT | Update app; reboot adapter and router; if persistent, note ISP/router model for the tech |
| **IntelliCenter offline in Pentair Home app** | Panel's Wi-Fi/wireless link down; local control at the panel still works | Weak Wi-Fi at the equipment pad (very common — pad is far from the house), router change, firmware | Re-run Wi-Fi setup at the outdoor panel screen if signal shows; consider a Wi-Fi extender near the pad |

**Line for customer content:** connectivity problems are usually router/IP issues the homeowner can safely reset; anything with an actual fault message on the outdoor panel (COM LINK, sensor Err, comm errors) lives inside an energized load center and is licensed-electrician territory.

**Sources (Section 4):**
- https://www.troublefreepool.com/threads/pentair-screenlogic-app-and-easytouch-remote-cannot-connect-error-address-invalid.247051/
- https://www.pooldial.com/resources/articles/pentair/screenlogic2/pentair-screenlogic2-troubleshooting-guide
- https://www.trunetto.com/troubleshooting/smart-pool-spa/pentair/pentair-screenlogic-app-cannot-find-connect-system
- https://pooldial.com/resources/articles/pentair/intellicenter/pentair-intellicenter-sensor-errors
- https://techfaultfix.com/pool-pumps/pentair/error-comm-error-intelliflo-intellipro-vs-or
- https://www.pentair.com/content/dam/extranet/nam/pentair-pool/residential/automation/archive/archive-intelliconnect-firmware/intelliconnect-customer-freeze-protection-11042019.pdf
- https://partners.pentair.com/s/article/What-Does-Error-Code-on-the-Compool-to-EasyTouch-Upgrade-Mean

---

## Research gaps / follow-ups

1. **TFP wiki pages** (MasterTemp, IntelliChlor) return 403 to automated fetchers — worth a manual browser pass to cross-check thresholds.
2. **"ERS"** on MasterTemp remains UNVERIFIED as a real code — treat as display artifact of ERR codes in published content.
3. **IntelliFlo3 numeric codes** (if any beyond named alarms in Pentair Home) not enumerated — Pentair Home app shows named alarms only.
4. IntelliChlor **low-salt cutoff** varies by source (2,600 vs 2,800 ppm) — use soft language in customer copy.
5. EasyTouch **Error Code 4** (Compool upgrade) — needs Pentair partner KB access to verify.
