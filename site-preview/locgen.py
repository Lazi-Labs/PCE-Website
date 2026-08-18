#!/usr/bin/env python3
"""
locgen.py — per-city hub (location silo) pages, from the design project's
Location Page template (design pull #5, 2026-08-18).

One page per service area that introduces the business locally and then
routes to all four categories, listing each category's services. It sits
ABOVE the existing city+category pages:

    /areas/<city>-fl.html          <- this file builds these (the city silo)
      -> <city>-fl-swimming-pool-repair.html   (existing, city-specific)
      -> <city>-fl-electrician.html            (existing, city-specific)
      -> ../services/gas-services.html         (silo — no city page yet)
      -> ../services/outdoor-living.html       (silo — no city page yet)

Facts come from the city's existing pages (display name, county) or are
true company-wide (licences, 24/7 dispatch, 5.0 rating).

Every section in the design is built here. Three of them are data-gated,
matching the template's own showNeighborhoods / showReview / showFaq props:
a city renders the Neighborhoods band once it has an entry in
citydata.json, and the review band once it has a real quote there. Nothing
is invented to fill a section — an empty one simply does not render, which
is what the design's toggles are for.

  citydata.json   { "<slug>": { "hoods": [...], "review": {...},
                                "drive": {"miles": n, "minutes": n} } }
  locdata.py      refreshes the drive figures from OSRM (real road miles)
"""
import re, pathlib, html, json

HERE = pathlib.Path(__file__).parent
AREAS = HERE / 'pages' / 'areas'

# Hand-maintained per-city extras. Absent keys just switch their section off.
DATA = json.loads((HERE / 'citydata.json').read_text()) \
    if (HERE / 'citydata.json').exists() else {}

# ── per-city facts, read out of the city's own pages ─────────────────────
def city_facts():
    out = {}
    for f in sorted(AREAS.glob('*-fl-swimming-pool-repair.html')):
        slug = f.name.split('-fl-')[0]
        h = f.read_text()
        t = re.search(r'<title>([^<]*)</title>', h)
        m = re.search(r'in ([^,|]+),\s*FL', t.group(1)) if t else None
        name = m.group(1).strip() if m else slug.replace('-', ' ').title()
        county = 'Pinellas'
        for mm in re.finditer(r'(Pinellas|Hillsborough|Pasco) County', h):
            if 'Proudly Serving' in h[max(0, mm.start() - 90):mm.start()]:
                continue                      # sitewide topbar, not city copy
            county = mm.group(1); break
        out[slug] = dict(name=name, county=county)
    return out

# ── the four categories and the services each card lists ─────────────────
CATS = [
  dict(key='pool', label='Pool Repair', accent='var(--teal)',
       blurb='Pumps, filters, heaters, salt systems, lights and automation — diagnosed '
             'on the pad and quoted flat.',
       city_page='{slug}-fl-swimming-pool-repair.html',
       hub='../services/swimming-pool-repair.html', all_label='All Pool Services',
       links=[('Pool Pump Repair', 'pool-pump-repair-installation'),
              ('Heater &amp; Heat Pump Repair', 'pool-heater-repair-installation'),
              ('Salt System Service', 'salt-water-chlorinator-installation-repair'),
              ('Leak Detection', 'pool-leak-detection')]),
  dict(key='electric', label='Electrical', accent='var(--cream)',
       blurb='Panels, rewiring, EV chargers and outdoor power — permitted under our own '
             'EC licence.',
       city_page='{slug}-fl-electrician.html',
       hub='../services/electrician.html', all_label='All Electrical Services',
       links=[('Panel Upgrades', 'electrical-panel-upgrade-replacement'),
              ('EV Charger Installation', 'ev-charger-installation'),
              ('House Rewiring', 'house-rewiring'),
              ('Whole House Generators', 'whole-house-generator-installation-repair')]),
  dict(key='gas', label='Gas', accent='var(--coral)',
       blurb='New lines, appliance hookups, heater fuel runs and leak testing — pressure '
             'tested every time.',
       city_page=None,
       hub='../services/gas-services.html', all_label='All Gas Services',
       links=[('Gas Line Installation', 'gas-line-installation'),
              ('Gas Leak Detection', 'gas-leak-detection-repair'),
              ('Propane Tank Installation', 'propane-tank-installation'),
              ('Gas Pool Heaters', 'pool-heater-repair-installation')]),
  dict(key='outdoor', label='Outdoor Living', accent='var(--navy)',
       blurb='Outdoor kitchens, pavers, turf, fencing and landscape lighting — built with '
             'the trades already in-house.',
       city_page=None,
       hub='../services/outdoor-living.html', all_label='All Outdoor Services',
       links=[('Outdoor Kitchens', 'outdoor-kitchens'),
              ('Pavers &amp; Driveways', 'pavers-and-driveways'),
              ('Artificial Turf', 'artificial-turf'),
              ('Landscape Lighting', 'outdoor-landscape-lighting-installation')]),
]

ROUTE = {
 'Pinellas': 'is on our daily Pinellas route out of the Largo shop',
 'Hillsborough': 'is a regular run for us across the bay from Largo',
 'Pasco': 'is a regular run for us north of the Pinellas line',
}

CSS = """/* loc */
.loc-cats{background:var(--sky);padding:78px 0}
.loc-cats .wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.loc-cats .lede{font-size:16.5px;line-height:1.6;color:var(--body);margin:0 0 34px;max-width:64ch;text-wrap:pretty}
.loc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr));gap:20px}
.loc-card{background:#fff;border-radius:16px;border-top:6px solid var(--navy);padding:26px 24px 22px;box-shadow:0 4px 16px rgba(0,40,70,.1);display:flex;flex-direction:column}
.loc-card h3{font-family:var(--disp);font-weight:700;font-size:21px;text-transform:uppercase;letter-spacing:.4px;color:var(--navy);margin:0 0 10px}
.loc-card>p{font-size:14.5px;line-height:1.55;color:var(--body);margin:0 0 16px}
.loc-links{display:grid;gap:1px;margin:0 0 18px}
.loc-links a{display:flex;align-items:center;gap:10px;padding:9px 2px;border-bottom:1px solid rgba(0,61,106,.12);font-size:14.5px;color:var(--ink);text-decoration:none}
.loc-links a:last-child{border-bottom:0}
.loc-links a::before{content:"";flex:none;width:7px;height:7px;background:var(--coral)}
.loc-links a:hover{color:var(--coral)}
.loc-all{margin-top:auto;font-family:var(--disp);font-size:13px;letter-spacing:.6px;text-transform:uppercase;color:var(--coral);text-decoration:none}
.loc-all:hover{color:var(--navy)}
.loc-hoods{position:relative;background:var(--cream);padding:74px 0;overflow:hidden}
.loc-hoods::before{content:"";position:absolute;right:-120px;top:-110px;width:420px;height:420px;border-radius:50%;background:rgba(0,61,106,.1);pointer-events:none}
.loc-hoods .wrap{position:relative;max-width:1180px;margin:0 auto;padding:0 24px}
.loc-hoods .eyebrow{display:inline-flex;align-items:center;gap:9px;font-family:var(--disp);font-size:13px;letter-spacing:1.6px;text-transform:uppercase;color:var(--red);margin-bottom:10px}
.loc-hoods .lede{font-size:16.5px;line-height:1.6;color:#4A3A28;margin:0 0 30px;max-width:56ch;text-wrap:pretty}
.loc-hoodgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px}
.loc-hoodgrid span{display:flex;align-items:center;gap:10px;background:#fff;border-radius:12px;padding:14px 16px;font-size:15px;font-weight:500;color:var(--ink);box-shadow:0 3px 10px rgba(74,58,40,.12)}
.loc-hoodgrid span::before{content:"";flex:none;width:9px;height:9px;border-radius:50%;background:var(--teal,#42BE9F)}
.loc-near{display:flex;flex-wrap:wrap;align-items:center;gap:6px 14px;margin:26px 0 0;font-size:15px;color:#4A3A28}
.loc-near a{color:var(--red);font-weight:700;text-decoration:none}
.loc-near a:hover{text-decoration:underline}
.loc-near i{color:rgba(74,58,40,.5);font-style:normal}
.loc-review{background:var(--navy-d);color:#fff;padding:70px 0;text-align:center}
.loc-review .wrap{max-width:860px;margin:0 auto;padding:0 24px}
.loc-review .stars{margin:0 0 20px;color:var(--cream);font-size:19px;letter-spacing:2px}
.loc-review blockquote{font-family:var(--disp);font-size:clamp(21px,2.6vw,30px);line-height:1.3;text-transform:uppercase;letter-spacing:.4px;color:#fff;margin:0 0 20px;text-wrap:pretty}
.loc-review cite{display:block;font-size:14.5px;color:#9FB9CC;font-style:normal}
@media(max-width:640px){.loc-hoods{padding:56px 0}.loc-review{padding:54px 0}}
/* /loc */"""

def build(slug, f, facts):
    name, county = f['name'], f['county']
    d = DATA.get(slug, {})
    drive = d.get('drive') or {}
    cards = ''
    for c in CATS:
        # the city-specific page when one exists, else the category silo
        target = c['city_page'].format(slug=slug) if c['city_page'] else c['hub']
        all_label = (f"{c['all_label']} in {name}" if c['city_page'] else c['all_label'])
        links = ''.join(f'<a href="../services/{s}.html">{t}</a>' for t, s in c['links'])
        cards += (f'<div class="loc-card" style="border-top-color:{c["accent"]}">'
                  f'<h3>{c["label"]}</h3><p>{c["blurb"]}</p>'
                  f'<div class="loc-links">{links}</div>'
                  f'<a class="loc-all" href="{target}">{all_label} &rarr;</a></div>')

    # The design leads on distance from the shop. Use the real road figure
    # where locdata.py has measured one; fall back to the licence count so
    # the panel never shows an invented number.
    eyebrow = (f'{drive["minutes"]} Minutes From Our Largo Shop' if drive.get('minutes')
               else f'{county} County &middot; Licensed Pool, Electric &amp; Gas')
    lead = ((f'{drive["miles"]} mi', 'From our Largo shop — no travel surcharge')
            if drive.get('miles')
            else ('4', 'Active licences — pool, electric, gas, construction'))
    proof = ''.join(f'<div class="silo-stat"><b>{v}</b><span>{t}</span></div>' for v, t in [
        lead,
        ('4', 'Service lines under one roof, one invoice'),
        ('24/7', 'Emergency dispatch for power and gas calls'),
        ('5.0', 'Google rating from Pinellas homeowners')])

    # ── Neighborhoods band — renders only for cities with a real list ────
    hoods = d.get('hoods') or []
    near = [n for n in (d.get('near') or []) if n in facts]
    hood_html = ''
    if hoods:
        chips = ''.join(f'<span>{html.escape(n)}</span>' for n in hoods)
        nearline = ''
        if near:
            links = '<i>&middot;</i>'.join(
                f'<a href="{n}-fl.html">{html.escape(facts[n]["name"])}</a>' for n in near)
            nearline = f'<p class="loc-near">Nearby cities we also cover: {links}</p>'
        hood_html = f'''
<section class="loc-hoods"><div class="wrap">
<span class="eyebrow">Inside {name}</span>
<h2 class="silo-h2">Neighborhoods We Cover</h2>
<p class="lede">If you are inside the city limits or just over the line, you are on the route.</p>
<div class="loc-hoodgrid">{chips}</div>{nearline}
</div></section>
'''

    # ── Review band — a real quote or nothing at all ─────────────────────
    rev = d.get('review') or {}
    rev_html = ''
    if rev.get('quote'):
        rev_html = f'''
<section class="loc-review"><div class="wrap">
<p class="stars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</p>
<blockquote>&ldquo;{html.escape(rev["quote"])}&rdquo;</blockquote>
<cite>{html.escape(rev.get("source", f"Verified Google review — {name}, FL"))}</cite>
</div></section>
'''

    faqs = [
      (f'How soon can someone get to {name}?',
       f'{name} {ROUTE[county]}, so most calls are same-day or next-day. No power at the '
       f'equipment pad, a gas smell, or a flooded pad gets dispatched after hours.'),
      (f'Do you pull {county} County permits?',
       f'Yes. Heater installs, panel work, gas lines and outdoor builds are permitted and '
       f'inspected under our own licences, never a subcontractor&rsquo;s.'),
      ('Can one visit cover pool and electrical work?',
       'That is the point of holding four licences. A pump replacement plus a bonding '
       'correction or a new sub-panel happens on one visit, on one invoice.'),
      ('Do you use subcontractors?',
       'No. The tech who shows up works here, and the same company carries the pool, '
       'electrical, gas and construction licences the job needs.'),
    ]
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)

    jump = ''.join(
        f'<a href="{(c["city_page"].format(slug=slug) if c["city_page"] else c["hub"])}">'
        f'{c["label"]}<span>&rarr;</span></a>' for c in CATS)

    return f'''<section class="silo-hero"><div class="silo-hin"><div>
<p class="silo-crumb"><a href="../../index.html">Home</a><span>/</span><a href="index.html">Service Areas</a><span>/</span><b>{name}</b></p>
<span class="silo-eyebrow">{eyebrow}</span>
<h1>Pool, Electrical &amp; Gas Service in {name}, FL</h1>
<p class="silo-lede">One licensed crew for the whole property — pool equipment, panels and
wiring, gas lines, and outdoor living builds. {name} {ROUTE[county]}, so most calls land
same-day or next-day.</p>
<div class="cta-row" style="justify-content:flex-start">
<a class="btn btn-primary" href="tel:7273165206">Call 727-316-5206</a>
<a class="btn btn-white" href="../../index.html#contact">Request Service</a></div>
</div>
<div class="silo-proof"><h2>{name} At A Glance</h2><div>{proof}</div></div>
</div></section>

<section class="loc-cats"><div class="wrap">
<h2 class="silo-h2">What We Do In {name}</h2>
<p class="lede">Four service lines, four licences, one crew. Pick the category that matches
your project and you will land on the full service list.</p>
<div class="loc-grid">{cards}</div></div></section>

<section class="silo-covers"><div class="silo-cin"><div>
<h2 class="silo-h2">Why {name} Homeowners Call Us</h2>
<p>Most jobs here start as one problem and turn out to be two — a dead pump that is really a
tripped bonding circuit, a heater that will not fire because of the gas run rather than the
board. We test the whole system before quoting, so the second problem does not become a
second trip.</p>
<p>{county} County requires permits for gas work and most electrical work. We pull them under
our own licences, which is why a heater install or a panel change does not turn into a second
contractor and a second week of waiting.</p>
<ul class="silo-ticks">
<li>{name} {ROUTE[county]} — same-day and next-day appointments</li>
<li>Pool, electrical, gas and construction licences all in-house</li>
<li>Permits pulled and inspected under our own licences</li>
<li>Flat pricing quoted before any work starts</li></ul>
</div>
<img class="silo-photo" src="../../assets/photo-van-home.jpg" alt="Perfect Catch service van on a {name} job" loading="lazy">
</div></section>

{hood_html}{rev_html}
<section class="silo-faq"><div class="wrap"><h2 class="silo-h2">{name} Service Questions</h2>{faq}</div></section>

<section class="silo-cta" id="contact"><div class="silo-wave"><svg viewBox="0 0 1440 120" preserveAspectRatio="none"><path d="M0,14 C170,74 330,92 530,66 C710,42 870,100 1070,88 C1230,78 1350,42 1440,24 L1440,0 L0,0 Z" fill="#fff" opacity=".35"></path><path d="M0,50 C180,18 340,70 540,78 C740,86 900,48 1080,40 C1240,33 1360,58 1440,44 L1440,0 L0,0 Z" fill="#fff"></path></svg></div>
<div class="silo-ctain"><div>
<span class="eyebrow">{name} &middot; Same-Day Dispatch</span>
<h2>Book A {name} Tech Today</h2>
<p class="sub">Tell us what the equipment is doing. A licensed tech — not a sub — shows up with the truck stocked.</p>
<div class="cta-row" style="justify-content:flex-start">
<a class="btn btn-white" href="tel:7273165206">Call 727-316-5206</a>
<a class="btn btn-ghost" href="../../index.html#contact">Request Service</a></div>
</div>
<div class="silo-jump"><h3>Jump To A Service Line</h3>{jump}
<p class="silo-hours"><b>Mon&ndash;Fri 8&ndash;5</b>24/7 emergency dispatch</p></div>
</div></section>
'''

def page(slug, f, shell, silo_css):
    """Wrap the body in the city pool page's own shell (head + header + footer)."""
    name = f['name']
    s = shell
    s = re.sub(r'<title>.*?</title>', f'<title>Pool, Electrical &amp; Gas Service in '
               f'{html.escape(name)}, FL | Perfect Catch</title>', s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description" content="[^"]*"',
               '<meta name="description" content="Licensed pool, electrical, gas and outdoor '
               f'living services in {html.escape(name)}, FL. Four licences, zero '
               'subcontractors, flat pricing. Call 727-316-5206."', s, count=1)
    # keep the shell's <head>, header and footer; swap the body
    foot = s.index('<!--FOOT-->')
    mm = s.index('<div class="mmenu"')
    start = s.index('<section class="hero"', mm)   # the page body proper
    s = s[:start] + build(slug, f, None) + s[foot:]
    if '/* silo */' not in s:
        s = s.replace('</style>', silo_css + '\n</style>', 1)
    s = re.sub(r'/\* loc \*/.*?/\* /loc \*/', '', s, flags=re.S)
    s = s.replace('</style>', CSS + '\n</style>', 1)
    return s

if __name__ == '__main__':
    import silogen
    facts = city_facts()
    n = 0
    for slug, f in facts.items():
        shell = (AREAS / f'{slug}-fl-swimming-pool-repair.html').read_text()
        (AREAS / f'{slug}-fl.html').write_text(page(slug, f, shell, silogen.CSS))
        n += 1
    print(f'{n} location hub pages built')
