# Why-Us Card Rollout Spec

Apply the design-system "Why-us card" to EVERY service page in `/Users/yramos/yr/10-active/pce/pce-website/site-preview/pages/services/` (all *.html except index.html), replacing each page's existing "Why … Choose Us"-style section.

## CSS to add (once per page, before `</style>`; skip if `.why-band` already present)
```
.why-wrap{padding:26px 0 8px}
.why-band{position:relative;background:url('../../assets/beach-bg.jpeg') center bottom/cover no-repeat,linear-gradient(180deg,#F2544B,#F7A458);color:#fff;text-align:center;padding:60px 36px 66px;overflow:hidden;border-radius:20px;box-shadow:0 18px 44px rgba(0,40,70,.18)}
@media(max-width:640px){.why-band{padding:46px 18px 52px;border-radius:16px}}
.why-band h2{font-family:'Burbank Big',Impact,sans-serif;font-weight:700;color:#fff;font-size:clamp(26px,3.6vw,40px);line-height:1.05;text-transform:uppercase;max-width:860px;margin:0 auto 16px;letter-spacing:.5px;text-shadow:2px 2px 0 rgba(167,19,12,.35)}
.why-band .sub{max-width:780px;margin:0 auto 32px;font-size:16.5px;color:#FFF3E8}
.why-card{background:linear-gradient(180deg,#fff,#FFF7EA);border:2px solid #F24E45;border-radius:16px;box-shadow:0 14px 34px rgba(120,20,10,.25);margin:0 auto 34px;padding:30px 32px;text-align:left}
.why-card ul{list-style:none;margin:0;padding:0;columns:2;column-gap:44px}
.why-card li{break-inside:avoid;display:flex;gap:13px;align-items:flex-start;font-size:15.5px;line-height:1.55;color:#001E33;padding:10px 0}
.why-card .wico{width:24px;height:24px;flex:0 0 auto;color:#F24E45;margin-top:3px}
.why-band .outro{max-width:720px;margin:0 auto 28px;font-size:16.5px;line-height:1.75;color:#001E33}
@media(max-width:860px){.why-card ul{columns:1}.why-card{padding:24px 20px}}
.why-band .cta-row{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.why-band .btn-call{background:#003D6A;color:#fff;border-color:#062F4F}
```
(Pages already define `.btn`/`.btn-primary`; `.btn-call` added here.)

## Section markup (replaces the existing why-us section INSIDE the article column, same position)
```
<div class="why-wrap"><section class="why-band">
<h2>Why {AUDIENCE_GEO} Choose Perfect Catch Swimming Pool Repair, Gas, &amp; Electric for {SERVICE}</h2>
<p class="sub">{SUBLINE}</p>
<div class="why-card"><ul>
{6 × <li><svg class="wico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.7 6.3a4.2 4.2 0 0 0-5.9 5.9L3 18v3h3l5.8-5.8a4.2 4.2 0 0 0 5.9-5.9l-3 3-2-2 3-3z"/></svg>{PROOF POINT}</li>}
</ul></div>
<p class="outro">{OUTRO}</p>
<div class="cta-row">
<a class="btn btn-primary" href="../../contact-us.html">Request Service</a>
<a class="btn btn-call" href="tel:7273165206">☎ Call 727-316-5206</a>
</div>
</section></div>
```

## Slot rules (per page)
- {AUDIENCE_GEO}: "Largo Pool Owners" for pool services; "Largo Homeowners" for electrical/gas/outdoor residential; "Pinellas Business Owners" for commercial-electrician; "Tampa Bay Boat Owners" for marine; "Pinellas Pool Builders" for pool-builders.
- {SERVICE}: short natural service phrase from the page's H1 (e.g. "Pump Repair", "Panel Upgrades", "Gas Leak Repair").
- {SUBLINE}: one sentence: "{Service} requires a licensed contractor. Here is what Perfect Catch Swimming Pool Repair, Gas, & Electric brings to the job." (adapt naturally per page).
- 6 proof points: REUSE the page's existing why-us bullets (they're already service-specific). Rules: exactly 6 items; item #1 must carry the relevant license number(s) (merge from existing bullets — pool: CPC1459998 (+EC13011994 where electrical scope); electrical: EC13011994; gas pages: LI4527 (+EC13011994); outdoor structural: CGC1531306); "zero subcontractors" appears once; pad from these standards if the page has <6: upfront pricing before work begins / best-in-class warranty / full-system diagnosis finds the actual cause / honest repair-vs-replacement guidance.
- {OUTRO}: "If your {equipment/problem} is not working correctly, contact Perfect Catch … today. We will tell you exactly what is wrong and what it costs to fix it." (adapt per service; for install-type services: "Ready to plan your {project}? … We will tell you exactly what it takes and what it costs.")
- DELETE the old why-us section (typically `<h2 class="disp">Why …</h2>` + its `ul.checks`) — the new band takes its place. Keep every other section untouched.
- Membership/builders/emergency pages: keep the pattern, adapt phrasing sensibly (e.g. emergency outro: "…call now — priority urgent dispatch.").

Return per-page confirmation list.
