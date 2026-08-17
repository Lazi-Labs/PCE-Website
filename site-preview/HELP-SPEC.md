# Help Center Build Spec (Pool Equipment Troubleshooting)

Output dir: `/Users/yramos/yr/10-active/pce/pce-website/site-preview/pages/help/`
Content source files (AUTHORITATIVE — use ONLY these, no new research): `/Users/yramos/yr/10-active/pce/pce-website/seo-baseline/troubleshooting-research/{hayward-codes.md, pentair-codes.md, jandy-codes.md, raypak-aquacal-symptoms.md}`
Template base for chrome (header pill + dropdown nav, fonts, sticky call bar, CTA band, footer): copy from `pages/blog/3-signs-you-have-a-bad-circuit-breaker.html` (a blog post — same two-dir depth, article layout). Widen article to max-width 860px.

## Hard rules
- **EXCLUDE every item marked UNVERIFIED** in the research files. Publish only verified codes. Never include the "never-publish" repair categories (capacitor work, gas train, refrigerant, opening light fixtures, bypassing safeties).
- Phone 727-316-5206 only. Licenses: CPC1459998 (pool), EC13011994 (electrical), LI4527 (gas).
- No HowTo or FAQPage schema. JSON-LD = Article (author Person "Yanni Ramos" → https://callperfectcatch.com/about-us/, publisher #organization, mainEntityOfPage https://callperfectcatch.com/help/<slug>/) + BreadcrumbList (Home → Troubleshooting (https://callperfectcatch.com/help/) → title).
- Visible breadcrumb: Home → Troubleshooting (index.html) → title. Byline: "By Yanni Ramos, Licensed Pool, Electrical & Gas Contractor".
- NO @dsCard comments.

## Page anatomy (every guide)
1. H1 (see per-page titles below) + byline + 1-paragraph GEO lead: what this page covers, ≤60 words, mentioning we're the Pinellas company licensed for the electrical/gas side of these repairs.
2. "Jump to a code" anchor list (links to each code's H3 id).
3. Per code: `<h3 id="<code-slug>">` "[CODE] — [plain-English meaning]" → 2-3 sentence self-contained explanation (what it means + most likely cause) → "Try this first" ul.checks of ONLY the safe homeowner steps from the research → a one-line safety stop in a callout div ("If that doesn't clear it: this is a [gas/electrical/sealed-component] repair — stop here.") Where the research notes a code as urgent/stop-now, lead with the warning.
4. After each brand-section or every ~4 codes: a compact local CTA box: "[Brand] [equipment] repair in Largo, St. Pete, Clearwater & all of Pinellas — we service it under our own [licenses]. Priority dispatch: 727-316-5206" linking the matching service page + ../areas/index.html.
5. Closing section "Why homeowners across Pinellas call us for [brand/equipment]": 3 bullets (relevant license angle from research editorial notes — e.g. E23 undersized wiring, PFC-Hi voltage, gas ignition faults), CTA band.
6. Mention Florida/Pinellas context naturally where research supports it (salt air, lightning, year-round runtime) — do not fabricate stats.
7. Attribute facts softly in prose ("per Hayward's service documentation", "Jandy's JXi manual") — no external links.

## Pages

### Agent H (source: hayward-codes.md) — 4 pages
- hayward-heater-error-codes.html — H1 "Hayward Pool Heater Error Codes: LO, IF, CE & More Explained" (PRIORITY: LO/IF/CE get the richest treatment — 1,200 searches/mo)
- hayward-aquarite-salt-system-codes.html — H1 "Hayward AquaRite Codes & Lights: No Flow, Check Salt, Inspect Cell"
- hayward-vs-pump-error-codes.html — H1 "Hayward Variable-Speed Pump Error Codes Explained" (PFC-Hi voltage angle)
- hayward-omnilogic-troubleshooting.html — H1 "Hayward OmniLogic & OmniHub Troubleshooting Guide"

### Agent P (source: pentair-codes.md) — 4 pages
- pentair-mastertemp-error-codes.html — H1 "Pentair MasterTemp Error Codes: Service Heater Light, ERR & E-Codes"
- pentair-intelliflo-error-codes.html — H1 "Pentair IntelliFlo & SuperFlo VS Alarm Codes Explained" (0021 comm error featured)
- pentair-intellichlor-light-codes.html — H1 "Pentair IntelliChlor Lights: What Every Color & Flash Means"
- pentair-automation-screenlogic-troubleshooting.html — H1 "Pentair Automation & ScreenLogic Troubleshooting Guide"

### Agent J (source: jandy-codes.md) — 4 pages
- jandy-heater-fault-codes.html — H1 "Jandy JXi & LXi Heater Fault Codes: Check Ign, High Limit & More"
- jandy-aquapure-error-codes.html — H1 "Jandy AquaPure Error Codes 120–194 Explained"
- jandy-vs-pump-error-codes.html — H1 "Jandy Variable-Speed Pump Error Codes Explained" (E23 undersized-wiring angle)
- jandy-aqualink-troubleshooting.html — H1 "Jandy AquaLink & iAquaLink Troubleshooting Guide"

### Agent R (source: raypak-aquacal-symptoms.md Parts 1-2 + symptoms a-d) — 6 pages
- raypak-heater-error-codes.html — H1 "Raypak Pool Heater Codes Explained (Digital, 106A/156A & Avia)" (note the three code families)
- aquacal-heat-pump-error-codes.html — H1 "AquaCal Heat Pump Codes: FS, HP, LP & More Explained"
- pool-pump-humming-not-starting.html — H1 "Pool Pump Humming But Not Turning On: What It Means"
- pool-pump-tripping-breaker.html — H1 "Pool Pump Keeps Tripping the Breaker? Here's Why"
- pool-pump-loses-prime.html — H1 "Pool Pump Losing Prime: Causes & Fixes"
- pool-pump-loud-grinding.html — H1 "Why Is My Pool Pump So Loud? Grinding, Screaming & Humming Decoded"

### Agent S (source: raypak-aquacal-symptoms.md Part 3 symptoms e-h) — 4 pages
- pool-light-not-working.html — H1 "Pool Light Not Working: What's Safe to Check (and What Never Is)" — SAFETY-FIRST page per the research's CPSC/GFCI/NEC 680 framing; the homeowner section is deliberately short; this page's job is safe diagnosis + call.
- pool-heater-wont-stay-lit.html — H1 "Gas Pool Heater Won't Stay Lit: Short-Cycling Causes Explained"
- salt-cell-not-generating-chlorine.html — H1 "Salt Cell Not Generating Chlorine: A Step-by-Step Check"
- pool-automation-wont-connect.html — H1 "Pool Automation Won't Connect to Wi-Fi or App: Fix Guide"

Symptom pages: same anatomy but H3s are causes ranked by likelihood instead of codes; cross-link the relevant brand code guides ("Seeing a specific code? → Hayward heater codes / Pentair MasterTemp codes…").

Return list of files written per agent.
