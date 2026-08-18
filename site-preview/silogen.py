#!/usr/bin/env python3
"""
silogen.py — category hub (silo) pages, from the design project's Silo Page
template (design pull #5, 2026-08-18).

Each of the four service lines gets a pillar page: hero + proof stats, what
the category covers, a card grid of every service in the silo, an optional
symptom finder, optional brand strip, the four-step process, an FAQ, and a
CTA that cross-links the other silos.

Card names and blurbs are NOT invented here — they are each service page's
own @dsCard name/subtitle, so the hub and the page it points at agree.

Run order after editing: silogen -> headergen -> footergen.
"""
import re, pathlib, html

HERE = pathlib.Path(__file__).parent
SERVICES = HERE / 'pages' / 'services'

# ── the service catalogue, read from the pages themselves ────────────────
def card_meta(slug):
    f = SERVICES / f'{slug}.html'
    first = f.read_text().split('\n', 1)[0]
    name = re.search(r'name="([^"]*)"', first)
    sub = re.search(r'subtitle="([^"]*)"', first)
    if not (name and sub):
        raise SystemExit(f'{slug}: no @dsCard name/subtitle to build a card from')
    # first clause of the subtitle keeps the card tight
    blurb = sub.group(1).split(' — ')[-1] if ' — ' in sub.group(1) else sub.group(1)
    return name.group(1), blurb[0].upper() + blurb[1:]

def cards(slugs):
    return [(s, *card_meta(s)) for s in slugs]

POOL = ['pool-pump-repair-installation', 'pool-filter-repair-and-installation',
        'pool-heater-repair-installation', 'salt-water-chlorinator-installation-repair',
        'pool-light-repair', 'pool-electrical-repair-installation',
        'pool-equipment-installation-upgrades', 'pool-automation-systems-installation-upgrades',
        'pool-leak-detection', 'pool-cleaning', 'pool-acid-wash', 'pool-resurfacing',
        'pool-remodeling', 'emergency-pool-service', 'pool-care-memberships', 'pool-builders']
ELEC = ['electrical-panel-upgrade-replacement', 'house-rewiring', 'surge-protection',
        'whole-house-generator-installation-repair', 'ev-charger-installation',
        'lighting-ceiling-fan-installation', 'smoke-detector-installation',
        'electrical-safety-inspection', 'emergency-electrician', 'commercial-electrician',
        'marine-electricians']
GAS = ['gas-line-installation', 'gas-leak-detection-repair', 'propane-tank-installation',
       'pool-heater-repair-installation', 'whole-house-generator-installation-repair',
       'outdoor-kitchens']
OUT = ['outdoor-kitchens', 'pavers-and-driveways', 'artificial-turf', 'pool-fence',
       'outdoor-landscape-lighting-installation']

# Symptom finder — only the pool silo has guides behind it.
SYMPTOMS = [
    ('Pool pump won&rsquo;t prime', 'pool-pump-loses-prime'),
    ('Pump is loud or grinding', 'pool-pump-loud-grinding'),
    ('Pump hums but won&rsquo;t start', 'pool-pump-humming-not-starting'),
    ('Breaker trips when the pump starts', 'pool-pump-tripping-breaker'),
    ('Heater won&rsquo;t stay lit', 'pool-heater-wont-stay-lit'),
    ('Salt cell not making chlorine', 'salt-cell-not-generating-chlorine'),
    ('Pool light is dark or flickering', 'pool-light-not-working'),
    ('Automation app lost the pad', 'pool-automation-wont-connect'),
]

FAQ_COMMON = [
    ('How fast can you get out here?',
     'Most Pinellas calls are same-day or next-day. Emergencies — no power at the pad, '
     'a gas smell, a flooded equipment area — get dispatched after hours.'),
    ('Do you charge a diagnostic fee?',
     'There is a flat trip and diagnostic charge, quoted when you book. It is credited '
     'toward the repair if you approve the work that visit.'),
    ('Do you pull permits?',
     'Yes — permitted and inspected under our own licenses, never a subcontractor&rsquo;s.'),
    ('Do you use subcontractors?',
     'No. We hold pool, electrical, gas and construction licenses, so the tech who shows '
     'up works here and the whole job runs on one invoice.'),
]

CATS = {
  'swimming-pool-repair': dict(
    key='pool', label='Pool Repair', title='Pool Repair',
    license='Licensed Pool Contractor · CPC1459998',
    h1='Pool Repair in Largo &amp; All of Pinellas County',
    lede='Pumps, filters, heaters, salt systems, lights and automation — diagnosed and '
         'repaired by our own techs, under our own licenses. Flat pricing quoted before '
         'the work starts.',
    covers_h='What Pool Repair Covers',
    covers=['Most calls start the same way: something stopped running, or the water stopped '
            'looking right. We diagnose the whole equipment pad — not just the part that '
            'failed — so you are not paying twice when the next weak link goes.',
            'Because we hold the electrical and gas licenses too, a bad breaker, a corroded '
            'bonding wire, or a gas line to the heater gets handled on the same visit '
            'instead of turning into a second contractor and a second week.'],
    bullets=['Same-day and next-day appointments across Pinellas',
             'Flat-rate quote before any work begins',
             'Factory-trained on Pentair, Hayward, Jandy and Gulf Stream',
             'Equipment tested and running before we leave'],
    photo='photo-pool-repair.webp', photo_alt='Technician servicing pool equipment',
    services=POOL, symptoms=True, brands=True,
    process_h='How A Repair Call Runs',
    cta_h='Let&rsquo;s Get That Pool Running',
    seo_title='Pool Repair in Largo & Pinellas County, FL | Perfect Catch',
    seo_desc='Licensed pool repair across Pinellas — pumps, filters, heaters, salt systems, '
             'lights and automation. Flat pricing, four licenses, zero subcontractors. '
             'Call 727-316-5206.'),

  'electrician': dict(
    key='electric', label='Electrical', title='Electrical',
    license='Licensed Electrical Contractor · EC13011994',
    h1='Electricians in Largo &amp; All of Pinellas County',
    lede='Panels, rewiring, EV chargers, generators and outdoor power — permitted, '
         'inspected and warrantied under our own electrical licence. No subs, no '
         'hand-offs, one invoice.',
    covers_h='What Our Electrical Work Covers',
    covers=['From a tripping breaker to a full service change, the same licensed crew does '
            'the diagnosis, the repair and the permit. We test the whole system rather than '
            'swapping the one part that announced itself.',
            'Holding the pool and gas licences alongside the electrical one means the jobs '
            'that usually need three contractors — a sub-panel for a heater, bonding at the '
            'pool pad, a generator fuel line — happen on a single visit.'],
    bullets=['Permits pulled and inspected under EC13011994',
             'Flat-rate quote before any work begins',
             'Emergency dispatch for sparking, burning smells and dead power',
             'Every circuit tested and labelled before we leave'],
    photo='photo-ev-charger.jpg', photo_alt='Electrician installing a home EV charger',
    services=ELEC, symptoms=False, brands=False,
    process_h='How An Electrical Call Runs',
    cta_h='Get A Licensed Electrician Out',
    seo_title='Electrician in Largo & Pinellas County, FL | Perfect Catch',
    seo_desc='Licensed electricians in Largo — panel upgrades, rewiring, EV chargers, '
             'generators, surge protection and emergency service. EC13011994, zero '
             'subcontractors. Call 727-316-5206.'),

  'gas-services': dict(
    key='gas', label='Gas', title='Gas',
    license='Licensed Gas Contractor · LI4527',
    h1='Gas Line &amp; Appliance Services in Pinellas County',
    lede='New gas lines, appliance hookups, pool heater fuel runs, propane tanks and leak '
         'testing — sized, permitted and pressure-tested by the crew that installs them.',
    covers_h='What Our Gas Work Covers',
    covers=['Gas work is sizing and safety before it is anything else. We calculate the BTU '
            'load for every appliance on the run, size the pipe for it, and pressure-test '
            'the line before it is signed off.',
            'Because the pool and electrical licences sit in-house, a heater install is one '
            'job — gas line, electrical tie-in and startup — instead of three trades trying '
            'to find the same week.'],
    bullets=['NG and LP lines sized to the real appliance load',
             'Pressure tested and permitted on every install',
             'Electronic leak detection, not just a soap test',
             'Same crew handles the heater&rsquo;s gas and electric'],
    photo='photo-gas-heater.webp', photo_alt='Gas pool heater installation',
    services=GAS, symptoms=False, brands=False,
    process_h='How A Gas Job Runs',
    cta_h='Get Your Gas Work Scheduled',
    seo_title='Gas Line Installation & Leak Detection, Largo FL | Perfect Catch',
    seo_desc='Licensed gas contractor in Largo — gas line installation, appliance hookups, '
             'propane tanks, pool heater fuel runs and leak detection. Pressure tested and '
             'permitted. Call 727-316-5206.'),

  'outdoor-living': dict(
    key='outdoor', label='Outdoor Living', title='Outdoor Living',
    license='Licensed General Contractor · CGC1531306',
    h1='Outdoor Living Builds Across Pinellas County',
    lede='Outdoor kitchens, pavers, turf, safety fencing and landscape lighting — built by '
         'the same company that already holds the gas and electrical licences the backyard '
         'needs.',
    covers_h='What Outdoor Living Covers',
    covers=['An outdoor kitchen is rarely just cabinetry — it is a gas line, a dedicated '
            'circuit, lighting and a paver base, all of which have to be permitted. We do '
            'all four, so the project does not stall between trades.',
            'The same is true of a pool deck: pavers, deck drains, fence and lighting are '
            'one scope for us, quoted flat and scheduled as one build.'],
    bullets=['Built under our own general contractor licence',
             'Gas and electrical handled in-house, not subbed out',
             'Flat pricing quoted before the build starts',
             'One crew from base prep through final lighting'],
    photo='photo-vans.jpg', photo_alt='Perfect Catch crew on an outdoor living build',
    services=OUT, symptoms=False, brands=False,
    process_h='How An Outdoor Build Runs',
    cta_h='Start Your Backyard Project',
    seo_title='Outdoor Living Contractor in Largo, FL | Perfect Catch',
    seo_desc='Outdoor kitchens, pavers, artificial turf, pool fencing and landscape '
             'lighting across Pinellas — gas and electrical in-house under CGC1531306. '
             'Call 727-316-5206.'),
}

# ── CSS, once per page (design's inline styles, folded into classes) ─────
CSS = """/* silo */
.silo-hero{position:relative;background:linear-gradient(105deg,#041C30 0%,var(--navy) 60%,#0A4A7A 100%);color:#fff;padding:56px 0 74px;overflow:hidden}
.silo-hero::after{content:"";position:absolute;right:-150px;top:-130px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(66,190,159,.2),transparent 68%);pointer-events:none}
.silo-hin{position:relative;max-width:1180px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:1.25fr minmax(300px,.75fr);gap:52px;align-items:center}
.silo-crumb{display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:13px;color:#9FB9CC;margin:0 0 18px}
.silo-crumb a{color:var(--teal);text-decoration:none;font-weight:500}
.silo-crumb a:hover{color:var(--cream)}
.silo-crumb b{color:#fff;font-weight:400}
.silo-eyebrow{display:inline-flex;align-items:center;gap:9px;font-family:var(--disp);font-size:13px;letter-spacing:1.6px;text-transform:uppercase;color:var(--teal);margin-bottom:12px}
.silo-hero h1{font-family:var(--disp);font-weight:700;font-size:clamp(34px,4.6vw,54px);line-height:1.04;text-transform:uppercase;letter-spacing:.5px;margin:0 0 16px}
.silo-lede{font-size:17px;line-height:1.6;color:#C9DCEA;margin:0 0 26px;max-width:52ch;text-wrap:pretty}
.silo-proof{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:18px;padding:26px 28px 22px}
.silo-proof h2{font-family:var(--disp);font-weight:700;font-size:17px;letter-spacing:.6px;text-transform:uppercase;color:#fff;margin:0 0 18px}
.silo-proof div{display:grid;gap:15px}
.silo-stat{display:grid;grid-template-columns:56px 1fr;gap:13px;align-items:baseline}
.silo-stat b{font-family:var(--disp);font-size:27px;color:var(--cream);line-height:1}
.silo-stat span{font-size:13.5px;line-height:1.45;color:#C9DCEA}
.silo-covers{background:#fff;padding:78px 0}
.silo-cin{max-width:1180px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:1.15fr 1fr;gap:56px;align-items:start}
.silo-h2{font-family:var(--disp);font-weight:700;font-size:clamp(26px,3.4vw,38px);line-height:1.06;text-transform:uppercase;letter-spacing:.5px;color:var(--ink);margin:0 0 18px}
.silo-covers p{font-size:16.5px;line-height:1.7;color:var(--body);margin:0 0 16px;text-wrap:pretty}
.silo-ticks{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:12px}
.silo-ticks li{display:flex;gap:12px;align-items:flex-start;font-size:15.5px;line-height:1.5;color:var(--ink)}
.silo-ticks li::before{content:"";flex:none;width:8px;height:8px;background:var(--coral);margin-top:7px}
.silo-photo{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:16px;border:2px solid var(--teal);display:block;box-shadow:0 6px 22px rgba(0,40,70,.15);position:sticky;top:24px}
.silo-svc{background:var(--sky);padding:78px 0}
.silo-svc .wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.silo-svc .lede{font-size:16px;line-height:1.6;color:var(--body);margin:0 0 34px;max-width:62ch}
.silo-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px}
.silo-card{background:#fff;border-radius:16px;border-bottom:5px solid var(--navy);padding:24px 24px 20px;text-decoration:none;display:block;box-shadow:0 4px 16px rgba(0,40,70,.1);transition:transform .15s,box-shadow .15s,border-color .15s}
.silo-card:hover{transform:translateY(-3px);box-shadow:0 12px 26px rgba(0,40,70,.18);border-bottom-color:var(--coral)}
.silo-card h3{font-family:var(--disp);font-weight:700;font-size:19px;text-transform:uppercase;letter-spacing:.4px;color:var(--navy);margin:0 0 9px}
.silo-card p{font-size:14.5px;line-height:1.55;color:var(--body);margin:0 0 14px}
.silo-card span{font-family:var(--disp);font-size:13px;letter-spacing:.6px;text-transform:uppercase;color:var(--coral)}
.silo-sym{position:relative;background:var(--cream);padding:74px 0;overflow:hidden}
.silo-sym::after{content:"";position:absolute;right:-120px;top:-110px;width:420px;height:420px;border-radius:50%;background:rgba(242,78,69,.14);pointer-events:none}
.silo-sym .wrap{position:relative;max-width:1180px;margin:0 auto;padding:0 24px}
.silo-symhead{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:20px;margin-bottom:32px}
.silo-sym .eyebrow{display:inline-flex;font-family:var(--disp);font-size:13px;letter-spacing:1.6px;text-transform:uppercase;color:var(--red);margin-bottom:10px}
.silo-sym h2{font-family:var(--disp);font-weight:700;font-size:clamp(28px,3.6vw,42px);line-height:1.04;text-transform:uppercase;letter-spacing:.5px;color:var(--ink);margin:0 0 10px}
.silo-sym .sub{font-size:16.5px;line-height:1.6;color:#4A3A28;margin:0;max-width:52ch;text-wrap:pretty}
.silo-symgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(272px,1fr));gap:14px}
.silo-symcard{display:flex;align-items:center;justify-content:space-between;gap:14px;background:#fff;border-radius:14px;border-bottom:4px solid var(--navy);padding:18px 18px 16px;font-size:15.5px;font-weight:500;line-height:1.35;color:var(--ink);text-decoration:none;box-shadow:0 4px 14px rgba(74,58,40,.13);transition:transform .15s,box-shadow .15s,border-color .15s}
.silo-symcard:hover{transform:translateY(-3px);box-shadow:0 10px 22px rgba(74,58,40,.2);border-bottom-color:var(--coral)}
.silo-symcard>span:first-child{display:flex;align-items:flex-start;gap:12px}
.silo-symcard .dot{flex:none;width:10px;height:10px;border-radius:50%;background:var(--teal);margin-top:6px}
.silo-symcard .arw{font-family:var(--disp);color:var(--coral);flex:none}
.silo-symnote{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:26px 0 0;font-size:15px;color:#4A3A28}
.silo-symnote a{color:var(--red);font-weight:700;text-decoration:none}
.silo-brands{background:#fff;padding:76px 0;text-align:center}
.silo-brands .wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.silo-brands h2{font-family:var(--disp);font-weight:700;font-size:26px;letter-spacing:1px;text-transform:uppercase;color:var(--ink);margin:0 0 8px}
.silo-brands p{font-size:15.5px;line-height:1.6;color:var(--body);margin:0 auto 34px;max-width:52ch}
.silo-brandrow{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:22px 48px;border-top:1px solid rgba(0,61,106,.14);border-bottom:1px solid rgba(0,61,106,.14);padding:26px 0}
.silo-brandrow img{height:62px;width:auto;max-width:100%;object-fit:contain;display:block}
.silo-proc{background:var(--navy-d);color:#fff;padding:74px 0}
.silo-proc .wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.silo-proc h2{font-family:var(--disp);font-weight:700;font-size:clamp(26px,3.4vw,38px);line-height:1.06;text-transform:uppercase;letter-spacing:.5px;color:#fff;margin:0 0 34px}
.silo-steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(216px,1fr));gap:28px}
.silo-step{border-top:3px solid var(--teal);padding-top:18px}
.silo-step b{display:block;font-family:var(--disp);font-size:14px;letter-spacing:1.2px;color:var(--teal);margin-bottom:9px}
.silo-step h3{font-family:var(--disp);font-weight:700;font-size:20px;text-transform:uppercase;letter-spacing:.4px;color:var(--cream);margin:0 0 9px}
.silo-step p{font-size:14.5px;line-height:1.6;color:#C9DCEA;margin:0}
.silo-faq{background:#fff;padding:74px 0}
.silo-faq .wrap{max-width:900px;margin:0 auto;padding:0 24px}
.silo-faq details{background:var(--sky);border-radius:14px;padding:18px 22px;margin-bottom:12px}
.silo-faq summary{font-family:var(--disp);font-size:17px;text-transform:uppercase;letter-spacing:.4px;color:var(--navy);display:flex;justify-content:space-between;gap:16px;align-items:center;list-style:none;cursor:pointer}
.silo-faq summary::-webkit-details-marker{display:none}
.silo-faq summary::after{content:"+";color:var(--coral)}
.silo-faq details[open] summary::after{content:"–"}
.silo-faq p{font-size:15px;line-height:1.65;color:var(--body);margin:12px 0 0}
.silo-cta{position:relative;background:linear-gradient(112deg,var(--coral) 0%,#CE231B 52%,var(--red) 100%);color:#fff;padding:132px 0 84px;overflow:hidden}
.silo-wave{position:absolute;top:-1px;left:0;width:100%;line-height:0;pointer-events:none}
.silo-wave svg{width:100%;height:104px;display:block}
.silo-ctain{position:relative;max-width:1180px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:1.1fr minmax(300px,.9fr);gap:52px;align-items:center}
.silo-cta .eyebrow{display:inline-flex;font-family:var(--disp);font-size:13px;letter-spacing:1.6px;text-transform:uppercase;color:var(--cream);margin-bottom:12px}
.silo-cta h2{font-family:var(--disp);font-weight:700;font-size:clamp(30px,4.2vw,48px);line-height:1.04;text-transform:uppercase;letter-spacing:.5px;color:#fff;margin:0 0 14px}
.silo-cta .sub{font-size:16.5px;line-height:1.6;color:#FFE7E3;margin:0 0 26px;max-width:44ch}
.silo-jump{background:#fff;color:var(--ink);border-radius:18px;border-bottom:5px solid var(--navy);padding:28px 28px 24px;box-shadow:0 22px 46px rgba(80,8,4,.3)}
.silo-jump h3{font-family:var(--disp);font-weight:700;font-size:21px;text-transform:uppercase;letter-spacing:.5px;color:var(--navy);margin:0 0 16px}
.silo-jump a{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:13px 2px;border-bottom:1px solid rgba(0,61,106,.14);font-family:var(--disp);font-size:15.5px;text-transform:uppercase;letter-spacing:.4px;color:var(--navy);text-decoration:none}
.silo-jump a:last-of-type{border-bottom:0}
.silo-jump a:hover{color:var(--coral)}
.silo-jump a span{color:var(--coral)}
.silo-hours{display:flex;align-items:center;gap:10px;background:var(--sky);border-radius:12px;padding:13px 15px;font-size:13px;line-height:1.45;color:var(--navy);margin:18px 0 0}
.silo-hours b{font-family:var(--disp);font-size:14px;letter-spacing:.3px}
@media (max-width:900px){.silo-hin,.silo-cin,.silo-ctain{grid-template-columns:1fr;gap:34px}.silo-photo{position:static}}
/* /silo */"""

STEPS = {
 'pool': [('You Describe It', 'A real person answers, asks what the equipment is doing, and books a window.'),
          ('We Test The Pad', 'Pump, filter, heater, bonding and power all get checked — not just the symptom.'),
          ('You Approve A Price', 'Flat rate, in writing, before a wrench moves. No hourly surprises.'),
          ('Fixed And Warrantied', 'We run the system, show you it works, and stand behind parts and labor.')],
 'electric': [('You Describe It', 'A real person answers and books a window — same day when it is unsafe.'),
              ('We Test The System', 'Panel, circuit, grounding and bonding get checked, not just the dead outlet.'),
              ('You Approve A Price', 'Flat rate, in writing, before any work begins.'),
              ('Permitted And Tested', 'Inspected under our own licence, labelled, and warrantied.')],
 'gas': [('You Describe It', 'Tell us the appliance and the run; we size the load over the phone.'),
         ('We Size And Permit', 'BTU load calculated, pipe sized for it, permit pulled before we dig.'),
         ('You Approve A Price', 'Flat rate, in writing, before any work begins.'),
         ('Pressure Tested', 'Every line is pressure tested and inspected before it is signed off.')],
 'outdoor': [('You Describe It', 'Tell us the space and how you want to use it — we scope it on site.'),
             ('We Quote The Whole Build', 'Base, gas, electric and lighting in one number, not four.'),
             ('You Approve A Price', 'Flat rate, in writing, before the build starts.'),
             ('Built And Warrantied', 'One crew start to finish, permitted under our own licence.')],
}
OTHER = [('swimming-pool-repair', 'Pool Repair'), ('electrician', 'Electrical'),
         ('gas-services', 'Gas'), ('outdoor-living', 'Outdoor Living')]

def build(slug, c):
    S = lambda p: f'{p}.html'
    svc = ''.join(
        f'<a class="silo-card" href="{S(s)}"><h3>{html.escape(n)}</h3>'
        f'<p>{b}</p><span>View Service &rarr;</span></a>'
        for s, n, b in cards([x for x in c['services'] if x != slug]))

    proof = ''.join(f'<div class="silo-stat"><b>{v}</b><span>{t}</span></div>' for v, t in [
        ('4', 'Active licenses — pool, electric, gas, construction'),
        ('0', 'Subcontractors — the tech on site works here'),
        ('5.0', 'Google rating across Pinellas County'),
        ('30', 'Service areas, dispatched daily out of Largo')])

    sym = ''
    if c['symptoms']:
        cardsx = ''.join(
            f'<a class="silo-symcard" href="../help/{g}.html">'
            f'<span><span class="dot"></span>{t}</span><span class="arw">&rarr;</span></a>'
            for t, g in SYMPTOMS)
        sym = (f'<section class="silo-sym"><div class="wrap"><div class="silo-symhead"><div>'
               f'<span class="eyebrow">Symptom Finder</span>'
               f'<h2>What Is Your Pool Doing?</h2>'
               f'<p class="sub">Pick the symptom and we&rsquo;ll tell you what usually causes it '
               f'— and whether it is a fix you can do yourself.</p></div>'
               f'<a class="btn btn-primary" href="../help/index.html">All Troubleshooting Guides</a>'
               f'</div><div class="silo-symgrid">{cardsx}</div>'
               f'<p class="silo-symnote">Symptom not listed? '
               f'<a href="tel:7273165206">Call 727-316-5206</a> and describe it — '
               f'we diagnose over the phone first.</p></div></section>')

    brands = ''
    if c['brands']:
        imgs = ''.join(f'<img src="../../assets/brand-{b}.webp" alt="{a}" loading="lazy">'
                       for b, a in [('pentair', 'Pentair'), ('hayward', 'Hayward'),
                                    ('jandy', 'Jandy'), ('amp', 'AMP Lighting'),
                                    ('gulfstream', 'Gulf Stream')])
        brands = (f'<section class="silo-brands"><div class="wrap">'
                  f'<h2>Equipment We Service Daily</h2>'
                  f'<p>Factory-trained and stocked with the parts these brands actually fail on.</p>'
                  f'<div class="silo-brandrow">{imgs}</div></div></section>')

    steps = ''.join(
        f'<div class="silo-step"><b>Step {i:02d}</b><h3>{h}</h3><p>{p}</p></div>'
        for i, (h, p) in enumerate(STEPS[c['key']], 1))

    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ_COMMON)

    jump = ''.join(f'<a href="{S(s)}">{n}<span>&rarr;</span></a>'
                   for s, n in OTHER if s != slug)
    jump += '<a href="../areas/index.html">Service Areas<span>&rarr;</span></a>'

    return f'''<section class="silo-hero"><div class="silo-hin"><div>
<p class="silo-crumb"><a href="../../index.html">Home</a><span>/</span><a href="index.html">Services</a><span>/</span><b>{c['label']}</b></p>
<span class="silo-eyebrow">{c['license']}</span>
<h1>{c['h1']}</h1>
<p class="silo-lede">{c['lede']}</p>
<div class="cta-row" style="justify-content:flex-start">
<a class="btn btn-primary" href="tel:7273165206">Call 727-316-5206</a>
<a class="btn btn-white" href="../../index.html#contact">Request Service</a></div>
</div>
<div class="silo-proof"><h2>Why This Crew</h2><div>{proof}</div></div>
</div></section>

<section class="silo-covers"><div class="silo-cin"><div>
<h2 class="silo-h2">{c['covers_h']}</h2>
{''.join(f'<p>{p}</p>' for p in c['covers'])}
<ul class="silo-ticks">{''.join(f'<li>{b}</li>' for b in c['bullets'])}</ul>
</div>
<img class="silo-photo" src="../../assets/{c['photo']}" alt="{c['photo_alt']}" loading="lazy">
</div></section>

<section class="silo-svc"><div class="wrap">
<h2 class="silo-h2">{c['label']} Services</h2>
<p class="lede">Every service in this silo. Pick the one that matches your job, or call and we&rsquo;ll sort it out on the phone.</p>
<div class="silo-grid">{svc}</div></div></section>

{sym}{brands}

<section class="silo-proc"><div class="wrap"><h2>{c['process_h']}</h2>
<div class="silo-steps">{steps}</div></div></section>

<section class="silo-faq"><div class="wrap"><h2 class="silo-h2">{c['label']} Questions</h2>{faq}</div></section>

<section class="silo-cta" id="contact"><div class="silo-wave"><svg viewBox="0 0 1440 120" preserveAspectRatio="none"><path d="M0,14 C170,74 330,92 530,66 C710,42 870,100 1070,88 C1230,78 1350,42 1440,24 L1440,0 L0,0 Z" fill="#fff" opacity=".35"></path><path d="M0,50 C180,18 340,70 540,78 C740,86 900,48 1080,40 C1240,33 1360,58 1440,44 L1440,0 L0,0 Z" fill="#fff"></path></svg></div>
<div class="silo-ctain"><div>
<span class="eyebrow">Serving All 30 Pinellas Areas</span>
<h2>{c['cta_h']}</h2>
<p class="sub">Tell us what you need done. A licensed tech — not a sub — shows up with the truck stocked.</p>
<div class="cta-row" style="justify-content:flex-start">
<a class="btn btn-white" href="tel:7273165206">Call 727-316-5206</a>
<a class="btn btn-ghost" href="../../index.html#contact">Request Service</a></div>
</div>
<div class="silo-jump"><h3>Other Service Lines</h3>{jump}
<p class="silo-hours"><b>Mon&ndash;Fri 8&ndash;5</b>24/7 emergency dispatch</p></div>
</div></section>
'''

def process(slug):
    f = SERVICES / f'{slug}.html'
    s = f.read_text()
    c = CATS[slug]
    body = build(slug, c)

    # body = from the first page section after the mobile menu, up to <!--FOOT-->
    foot = s.index('<!--FOOT-->')
    mm = s.index('<div class="mmenu"')
    start = s.index('<section class="hero"', mm)
    s = s[:start] + body + s[foot:]

    # refresh the silo CSS block (idempotent), then add it once
    s = re.sub(r'/\* silo \*/.*?/\* /silo \*/', '', s, flags=re.S)
    s = s.replace('</style>', CSS + '\n</style>', 1)

    # these pages shipped with no <title>/description at all
    s = re.sub(r'<title>.*?</title>\s*', '', s, flags=re.S)
    s = re.sub(r'<meta name="description"[^>]*>\s*', '', s)
    head = (f'<title>{html.escape(c["seo_title"])}</title>'
            f'<meta name="description" content="{html.escape(c["seo_desc"])}">')
    s = s.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + head, 1)
    f.write_text(s)
    return len(re.findall(r'silo-card', body))

if __name__ == '__main__':
    for slug in CATS:
        n = process(slug)
        print(f'  {slug:24} silo page — {n} service cards')
    print(f'{len(CATS)} silo pages built')
