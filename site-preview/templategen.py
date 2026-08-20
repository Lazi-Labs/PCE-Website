#!/usr/bin/env python3
"""Upgrade all /pages/services/ pages to the Claude Design 'Service Page Template':
hero badges box + wave, sticky sidebar (qform + category service list), two
alternating .media photo blocks, sticky mobile call bar. Idempotent: each
transform strips its previous output before re-injecting. Header/footer are
owned by headergen/footergen and are never touched (HDR/FOOT markers).
Run from site-preview root: python3 templategen.py
"""
import re, glob, html, os

POOL = [("Pool Repair","swimming-pool-repair.html"),("Pool Pump Repair & Installation","pool-pump-repair-installation.html"),
("Pool Heater & Heat Pump Repair","pool-heater-repair-installation.html"),("Pool Cleaning Service","pool-cleaning.html"),
("Pool Leak Detection","pool-leak-detection.html"),("Pool Filter Repair & Replacement","pool-filter-repair-and-installation.html"),
("Salt System & Salt Cell Repair","salt-water-chlorinator-installation-repair.html"),("Pool Automation","pool-automation-systems-installation-upgrades.html"),
("Pool Light Replacement & Repair","pool-light-repair.html"),("Pool Electrician","pool-electrical-repair-installation.html"),
("Pool Equipment Installation & Upgrades","pool-equipment-installation-upgrades.html"),("Pool Resurfacing","pool-resurfacing.html"),
("Pool Remodeling","pool-remodeling.html"),("Pool Acid Wash","pool-acid-wash.html"),("Emergency Pool Repair","emergency-pool-service.html"),
("Pool Maintenance Plans","pool-care-memberships.html"),("For Pool Builders","pool-builders.html")]
ELEC = [("Electrician","electrician.html"),("Panel Upgrades & Replacement","electrical-panel-upgrade-replacement.html"),
("Surge Protection","surge-protection.html"),("Emergency Electrician","emergency-electrician.html"),
("Lighting & Ceiling Fans","lighting-ceiling-fan-installation.html"),("Smoke Detector Installation","smoke-detector-installation.html"),
("House Rewiring","house-rewiring.html"),("Electrical Safety Inspection","electrical-safety-inspection.html"),
("EV Charger Installation","ev-charger-installation.html"),("Whole House Generators","whole-house-generator-installation-repair.html"),
("Commercial Electrician","commercial-electrician.html"),("Marine & Dock Electrician","marine-electricians.html")]
GAS = [("Gas Services","gas-services.html"),("Gas Leak Detection & Repair","gas-leak-detection-repair.html"),
("Gas Line Installation & Hookups","gas-line-installation.html"),("Propane Tank Installation","propane-tank-installation.html")]
OUTD = [("Landscape Lighting","outdoor-landscape-lighting-installation.html"),("Outdoor Living","outdoor-living.html"),
("Pavers & Driveways","pavers-and-driveways.html"),("Outdoor Kitchens","outdoor-kitchens.html"),
("Pool Fence","pool-fence.html"),("Artificial Turf","artificial-turf.html")]

CATS = [("Pool Repair Services", POOL, "photo-equipment-pad.webp", "Equipment-pad diagnostics — Largo, FL"),
        ("Electrical Services",  ELEC, "photo-ev-charger.jpg",     "Licensed electrical work — Pinellas County"),
        ("Gas Services",         GAS,  "photo-gas-heater.webp",    "Gas appliance & line work — LI4527 licensed"),
        ("Outdoor Services",     OUTD, "photo-pool-repair.webp",   "Outdoor project work — Largo, FL")]

def esc(t): return t.replace("&","&amp;")

def category_for(fname):
    for cap, items, photo, photocap in CATS:
        if any(h == fname for _, h in items):
            return cap, items, photo, photocap
    return CATS[0]

CSS = """/* v3 svc template */
.badges{display:inline-flex;background:rgba(1,36,62,.65);border:1px solid var(--teal);border-radius:12px;padding:12px 8px;flex-wrap:wrap;justify-content:center;margin-bottom:26px;box-shadow:0 6px 18px rgba(0,0,0,.25);backdrop-filter:blur(3px)}
.badges span{font-family:var(--disp);font-weight:700;font-size:14px;text-transform:uppercase;letter-spacing:.5px;padding:4px 18px;display:inline-flex;align-items:center;gap:8px}
.badges .ico{fill:currentColor;color:var(--teal);width:18px;height:18px;flex:0 0 auto}
.hero{position:relative;overflow:hidden}
.hero>*{position:relative}
.wave{position:absolute;bottom:-2px;left:0;width:100%;line-height:0}
.wave svg{width:100%;height:60px;display:block}
.media{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:30px;align-items:center;margin:40px 0 18px}
.media>figure{grid-column:1;margin:0;position:relative;border-radius:14px;overflow:hidden;border:1px solid rgba(0,61,106,.1);border-bottom:4px solid var(--coral);box-shadow:0 10px 28px rgba(0,40,70,.16)}
.media.flip>figure{grid-column:2;grid-row:1}
.media img{display:block;width:100%;height:100%;aspect-ratio:4/3;object-fit:cover}
.media figcaption{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(rgba(0,30,51,0),rgba(0,30,51,.88));color:#fff;font-family:var(--disp);font-weight:700;font-size:12.5px;text-transform:uppercase;letter-spacing:.6px;line-height:1.35;padding:28px 14px 11px}
.media .txt>h2{margin-top:0}
.media .txt>p:last-child,.media .txt>ul:last-child,.media .txt>ol:last-child{margin-bottom:0}
@media(max-width:700px){.media{grid-template-columns:1fr;gap:20px}.media>figure,.media.flip>figure{grid-column:1;grid-row:1}}
aside{display:flex;flex-direction:column;gap:22px}
.side-sticky{position:sticky;top:120px;display:flex;flex-direction:column;gap:22px}
.side-card{background:#fff;border-radius:14px;box-shadow:0 8px 26px rgba(0,40,70,.12);overflow:hidden;border:1px solid rgba(0,61,106,.08)}
.side-card .cap{background:var(--navy);color:#fff;padding:14px 18px 11px}
.side-card .cap h3{font-family:var(--disp);font-weight:700;font-size:18px;text-transform:uppercase;margin:0}
.side-list{list-style:none;margin:0;padding:8px 0}
.side-list a{display:block;padding:10px 18px;font-size:14.5px;color:var(--body);text-decoration:none;border-left:3px solid transparent;transition:background .15s;font-weight:400}
.side-list a:hover{color:var(--coral);background:var(--sky)}
.side-list a.cur{color:var(--navy);font-weight:700;border-left-color:var(--coral);background:var(--sky)}
.qform{background:linear-gradient(180deg,var(--navy),var(--navy-d));color:#fff;border-radius:14px;padding:24px;box-shadow:0 8px 26px rgba(0,40,70,.2)}
.qform h3{font-family:var(--disp);font-weight:700;font-size:22px;text-transform:uppercase;margin:0 0 4px;color:#fff}
.qform p{font-size:13.5px;color:#C9DCEA;margin:0 0 14px}
.qform input,.qform select{width:100%;font-family:var(--txt);font-size:15px;color:var(--ink);border:1px solid var(--teal);border-bottom-width:4px;border-radius:12px;padding:11px 14px 9px;margin-bottom:10px;background:#fff}
.qform input:focus,.qform select:focus{outline:2px solid var(--cream)}
.qform .btn{width:100%}
.phone-line{text-align:center;margin-top:12px;font-size:13.5px;color:#C9DCEA}
.phone-line b{font-family:var(--disp);font-size:20px;color:var(--cream);display:block}
.phone-line a{color:var(--cream);text-decoration:none}
.mbar{display:none;position:fixed;left:0;right:0;bottom:0;z-index:150;background:var(--navy-d);box-shadow:0 -4px 18px rgba(0,10,25,.35);padding:10px 12px calc(10px + env(safe-area-inset-bottom));grid-template-columns:1fr 1fr;gap:10px}
.mbar .btn{font-size:13px;padding:13px 8px;width:100%}
.mbar .btn-white{background:#fff;color:var(--navy);border-color:transparent}
@media(max-width:900px){.mbar{display:grid}body{padding-bottom:76px}}
@media(max-width:640px){.side-sticky{position:static}}
/* /v3 svc template */"""

WAVE = '<div class="wave"><svg viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true"><path d="M0,50 C240,90 480,10 720,40 C960,70 1200,20 1440,55 L1440,90 L0,90 Z" fill="#ffffff"></path></svg></div>'

def badges_html():
    fish = '<svg class="ico" aria-hidden="true"><use href="#i-fish"/></svg>'
    return ('<!--BDG--><div><div class="badges">'
            f'<span>{fish} Upfront Pricing</span>'
            f'<span>{fish} Four Licenses, Zero Subs</span>'
            f'<span>{fish} Best in Class Warranty</span>'
            '</div></div><!--/BDG-->')

def aside_html(fname):
    cap, items, _, _ = category_for(fname)
    cur_name = next(n for n, h in items if h == fname)
    opts = [cur_name] + [n for n, h in items if h != fname][:2]
    options = ''.join(f'<option>{esc(n)}</option>' for n in opts)
    lis = ''.join(
        f'<li><a href="{h}" class="cur" aria-current="page">{esc(n)}</a></li>' if h == fname
        else f'<li><a href="{h}">{esc(n)}</a></li>' for n, h in items)
    return ('<!--SIDE--><aside><div class="side-sticky">'
            '<div class="qform" id="form">'
            '<h3>Request Service</h3>'
            "<p>Tell us what's going on &mdash; we'll call you back fast.</p>"
            '<input placeholder="Full name" aria-label="Full name">'
            '<input placeholder="Phone number" aria-label="Phone number">'
            f'<select aria-label="Service needed">{options}</select>'
            '<a class="btn btn-primary" href="../../contact-us.html">Send Request</a>'
            '<div class="phone-line">or call us now<b><a href="tel:7273165206">727-316-5206</a></b></div>'
            '</div>'
            f'<div class="side-card"><div class="cap"><h3>{esc(cap)}</h3></div>'
            f'<ul class="side-list">{lis}</ul></div>'
            '</div></aside><!--/SIDE-->')

MBAR = ('<!--MBAR--><div class="mbar">'
        '<a class="btn btn-primary" href="#form">Request Service</a>'
        '<a class="btn btn-white" href="tel:7273165206">&#9742; Call Now</a>'
        '</div><!--/MBAR-->')

def media_wrap(section_html, photo, caption, alt, flip):
    cls = 'media flip' if flip else 'media'
    return (f'<div class="{cls}"><figure>'
            f'<img src="../../assets/{photo}" alt="{alt}" loading="lazy" decoding="async">'
            f'<figcaption>{caption}</figcaption></figure>'
            f'<div class="txt">{section_html}</div></div>')

def split_sections(article):
    """Split article body into [(pre, [(h2start, h2end_or_articleend)...])] by <h2 positions."""
    idxs = [m.start() for m in re.finditer(r'<h2', article)]
    secs = []
    for n, i in enumerate(idxs):
        j = idxs[n+1] if n+1 < len(idxs) else len(article)
        secs.append((i, j))
    return idxs, secs

def process(path):
    fname = os.path.basename(path)
    s = open(path).read()
    if '<article' not in s or '<section class="hero"' not in s:
        return False
    cap, items, photo, photocap = category_for(fname)

    # --- strip previous injections (idempotent) ---
    s = re.sub(r'<!--BDG-->.*?<!--/BDG-->', '', s, flags=re.S)
    s = re.sub(r'<!--SIDE-->.*?<!--/SIDE-->', '@@ASIDE@@', s, flags=re.S)
    s = re.sub(r'<!--MBAR-->.*?<!--/MBAR-->', '', s, flags=re.S)
    s = re.sub(r'<div class="media(?: flip)?"><figure>.*?<div class="txt">(.*?)</div></div>\n?', r'\1', s, flags=re.S)
    s = re.sub(r'/\* v3 svc template \*/.*?/\* /v3 svc template \*/', '', s, flags=re.S)

    # --- hero: crumb -> nav, drop emoji trust row, badges after </h1>, wave ---
    s = re.sub(r'<div class="crumb">(.*?)</div>',
               r'<nav class="crumb" aria-label="Breadcrumb">\1</nav>', s, count=1, flags=re.S)
    s = re.sub(r'\s*<div class="trust">.*?</div>\s*(?=\s*<h1)', '\n  ', s, count=1, flags=re.S)
    hero_m = re.search(r'<section class="hero".*?</section>', s, flags=re.S)
    if hero_m:
        hero = hero_m.group(0)
        hero2 = hero.replace('</h1>', '</h1>\n  ' + badges_html(), 1)
        if '<!--WAVE-->' not in hero2:
            hero2 = hero2.replace('</section>', '<!--WAVE-->' + WAVE + '<!--/WAVE--></section>')
        s = s.replace(hero, hero2, 1)
    s = re.sub(r'<!--WAVE-->.*?<!--/WAVE-->', WAVE, s, flags=re.S)  # refresh

    # hero CTA -> in-page form anchor
    s = s.replace('href="../../index.html#contact"', 'href="#form"')
    s = s.replace('href="../../contact-us.html#form"', 'href="#form"')

    # --- sidebar: replace legacy mm-cta aside (or previous SIDE) ---
    if '@@ASIDE@@' not in s:
        s2 = re.sub(r'<aside class="mm-cta">.*?</aside>', '@@ASIDE@@', s, count=1, flags=re.S)
        if '@@ASIDE@@' in s2:
            s = s2
        else:  # no aside at all: insert after </article>
            s = s.replace('</article>', '</article>\n@@ASIDE@@', 1)
    s = s.replace('@@ASIDE@@', aside_html(fname), 1)

    # --- media blocks in article ---
    am = re.search(r'(<article[^>]*>)(.*?)(</article>)', s, flags=re.S)
    if am:
        body = am.group(2)
        idxs, secs = split_sections(body)
        h1txt = re.search(r'<h1[^>]*>(.*?)</h1>', s, flags=re.S)
        svc_alt = re.sub(r'<[^>]+>|&amp;', lambda m: '&' if m.group(0)=='&amp;' else ' ',
                         h1txt.group(1)).strip() if h1txt else cap
        svc_alt = re.sub(r'\s+', ' ', svc_alt)
        new_parts, wrapped = [], 0
        # pick section 2 (index 1) for media#1; the "Process" h2 for media#2
        proc_idx = None
        for n, (i, j) in enumerate(secs):
            h2txt = re.sub(r'<[^>]+>', '', body[i:body.find('</h2>', i)])
            if 'process' in h2txt.lower():
                proc_idx = n
                break
        pos = 0
        for n, (i, j) in enumerate(secs):
            new_parts.append(body[pos:i])
            sec = body[i:j]
            if n == 1 and 'Frequently Asked' not in sec and n != proc_idx:
                sec = media_wrap(sec, photo, photocap, svc_alt, flip=False); wrapped += 1
            elif n == proc_idx:
                sec = media_wrap(sec, 'photo-van-home.jpg',
                                 'Our crew, our trucks — zero subcontractors', svc_alt, flip=True); wrapped += 1
            new_parts.append(sec)
            pos = j
        new_parts.append(body[pos:])
        s = s.replace(am.group(0), am.group(1) + ''.join(new_parts) + am.group(3), 1)

    # --- sticky mobile call bar, before the footer marker or </body> ---
    anchor = '<!--FOOT-->' if '<!--FOOT-->' in s else '</body>'
    s = s.replace(anchor, MBAR + anchor, 1)

    # --- css ---
    s = s.replace('</style>', CSS + '</style>', 1)
    open(path, 'w').write(s)
    return True

def run():
    n = 0
    for p in sorted(glob.glob('pages/services/*.html')):
        if os.path.basename(p) == 'index.html':
            continue
        if process(p):
            n += 1
        else:
            print('skipped:', p)
    print('v3 template applied to', n, 'service pages')

if __name__ == '__main__':
    run()
