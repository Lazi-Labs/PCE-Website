#!/usr/bin/env python3
"""Inject the full dropdown service menu into every staging page.
Idempotent: strips any previous <nav>…</nav> in the .pill header and prior dropdown CSS, then injects fresh.
Run from site-preview root: python3 navgen.py
"""
import re, glob, os

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
ABOUT = [("About Us","about-us.html"),("Reviews","reviews.html"),("Specials","specials.html"),
("Referral Program","referral-program.html"),("Giving Back","giving-back.html"),("Blog","pages/blog/index.html")]
OUTD = [("Landscape Lighting","outdoor-landscape-lighting-installation.html"),("Outdoor Living","outdoor-living.html"),
("Pavers & Driveways","pavers-and-driveways.html"),("Outdoor Kitchens","outdoor-kitchens.html"),
("Pool Fence","pool-fence.html"),("Artificial Turf","artificial-turf.html")]

DD_CSS = """/* dropdown menu */
  .hdr-zone{position:relative;z-index:60}
  .pill nav .has-mega>a::after{content:' \\25BE';font-size:9px;color:#F24E45}
  .pill nav .has-mega .mega{position:absolute;left:24px;right:24px;top:calc(100% - 6px);background:radial-gradient(680px 320px at 82% 0%,rgba(87,200,242,.18),transparent 62%),linear-gradient(160deg,#0A4A7A,#003D6A 55%,#052B49);border-radius:18px;box-shadow:0 20px 46px rgba(0,20,40,.38);padding:24px 30px 26px;display:none;z-index:99;text-align:left}
  .pill nav .has-mega:hover .mega,.pill nav .has-mega:focus-within .mega{display:block}
  .pill nav .mega h4{font-family:'Burbank Big',Impact,sans-serif;font-weight:700;font-size:19px;letter-spacing:.6px;text-transform:uppercase;color:#FEDFAE;margin:0 0 14px}
  .pill nav .mega-in{display:grid;grid-template-columns:1fr 1fr minmax(210px,.85fr);gap:2px 40px;align-items:center}
  .pill nav .mega-col{display:flex;flex-direction:column}
  .pill nav .mega a{display:flex;align-items:flex-start;gap:10px;font-family:'Sofia Sans',Arial,sans-serif;font-size:14.5px;font-weight:500;color:#fff;text-transform:none;text-decoration:none;padding:6px 8px;border-radius:8px}
  .pill nav .mega a::before{content:"";flex:none;width:7px;height:7px;background:#F24E45;margin-top:7px}
  .pill nav .mega a:hover{background:rgba(255,255,255,.08);color:#FEDFAE}
  .pill nav .mvan{width:100%;height:auto;display:block;filter:drop-shadow(0 14px 22px rgba(0,10,25,.45))}
  @media(max-width:1180px){.pill nav .mega-in{grid-template-columns:1fr 1fr}.pill nav .mvan{display:none}}
  .pill nav{position:relative}
  .pill nav .dd{position:relative;display:inline-block}
  .pill nav .dd>a::after{content:' \\25BE';font-size:9px;color:#F24E45}
  .pill nav .dd-menu{display:none;position:absolute;top:100%;left:50%;transform:translateX(-50%);background:#fff;border:1px solid #DCE8F1;border-radius:12px;box-shadow:0 14px 34px rgba(0,20,40,.22);padding:0;z-index:99;min-width:470px;overflow:hidden}
  .pill nav .dd-links{flex:1;min-width:255px;padding:10px 0;max-height:64vh;overflow-y:auto}
  .pill nav .dd:hover .dd-menu,.pill nav .dd:focus-within .dd-menu{display:flex}
  .pill nav .dd-art{width:225px;background:linear-gradient(180deg,#E6F4FF 0%,#9FD4F5 100%);display:flex;flex-direction:column;justify-content:space-between;align-items:center;padding:16px 10px 0}
  .pill nav .dd-cta{text-align:center;font-family:'Burbank Big',Impact,sans-serif;text-transform:uppercase;color:#003D6A;font-size:13px;line-height:1.25}
  .pill nav .dd-cta a{display:block;margin-top:6px;padding:7px 10px 5px;background:#F24E45;color:#fff!important;border-radius:9px;font-size:14px;text-decoration:none}
  .pill nav .dd-cta a:hover{background:#A7130C}
  .pill nav .dd-art img{width:150%;max-width:none;display:block;margin:8px 0 -6px}
  .pill nav .dd:hover .dd-menu,.pill nav .dd:focus-within .dd-menu{display:block}
  .pill nav .dd-menu a{display:block;padding:7px 18px;font-family:'Sofia Sans',Arial,sans-serif;font-size:14px;font-weight:600;text-transform:none;color:#001E33;white-space:nowrap}
  .pill nav .dd-menu a:hover{background:#E6F4FF;color:#A7130C}
  .pill nav .dd-menu .dd-head{display:block;padding:8px 18px 3px;font-family:'Burbank Big',Impact,sans-serif;font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:#3F444B}
  @media(max-width:920px){.pill nav{display:none}}
"""
MARK_A, MARK_B = "<!--NAV-->", "<!--/NAV-->"

def esc(t): return t.replace("&","&amp;")

def nav_html(root, svc):
    def links(items, pre):
        return "".join(f'<a href="{pre}{h}">{esc(t)}</a>' for t, h in items)
    def mega(label, top, title, col1, col2):
        van=f'<img class="mvan" src="{root}assets/van-side.png" alt="" loading="lazy">'
        return (f'<span class="has-mega"><a href="{top}">{label}</a>'
                f'<div class="mega"><h4>{title}</h4><div class="mega-in">'
                f'<div class="mega-col">{col1}</div><div class="mega-col">{col2}</div>{van}</div></div></span>')
    def dd(label, top, inner):
        return (f'<span class="dd"><a href="{top}">{label}</a>'
                f'<div class="dd-menu"><div class="dd-links">{inner}</div></div></span>')
    hub=f"{svc}index.html"
    p1=links(POOL[:9], svc)
    p2=links(POOL[9:], svc)+f'<a href="{root}pages/help/index.html">Troubleshooting Guides</a>'
    e1=links(ELEC[:6], svc); e2=links(ELEC[6:], svc)
    g1=links(GAS, svc)+f'<a href="{svc}pool-heater-repair-installation.html">Gas Pool Heaters</a>'
    g2=(f'<a href="{svc}whole-house-generator-installation-repair.html">Generators + Gas Line</a>'
        f'<a href="{svc}outdoor-kitchens.html">Outdoor Kitchen Gas Lines</a>'
        f'<a href="{svc}gas-line-installation.html">Fire Pits &amp; Grill Hookups</a>'
        f'<a href="{svc}propane-tank-installation.html">Whole-Home Propane</a>')
    about_dd="".join(f'<a href="{root}{h}">{esc(t)}</a>' for t, h in ABOUT)
    return (f'{MARK_A}<nav>'
        + mega('Pool Repair', f'{hub}#pool', 'Pool Repair Services', p1, p2)
        + mega('Electrical', f'{hub}#electric', 'Electrical Services', e1, e2)
        + mega('Gas', f'{hub}#gas', 'Gas Services', g1, g2)
        + dd('Outdoor', f'{hub}#outdoor', links(OUTD, svc))
        + dd('About', f'{root}about-us.html', about_dd)
        + f'<a href="{root}pages/areas/index.html">Service Areas</a>'
        + f'<a href="{root}contact-us.html">Contact</a>'
        + f'</nav>{MARK_B}')

def process(path, root, svc):
    s = open(path).read()
    # strip previous injected nav
    s = re.sub(re.escape(MARK_A)+r'.*?'+re.escape(MARK_B), '@@NAV@@', s, flags=re.S)
    # or replace first plain <nav>…</nav> inside pill header
    if '@@NAV@@' not in s:
        s = re.sub(r'<nav[^>]*>.*?</nav>', '@@NAV@@', s, count=1, flags=re.S)
    if '@@NAV@@' not in s:
        return False
    s = s.replace('@@NAV@@', nav_html(root, svc), 1)
    # refresh dropdown css (strip any prior injected block, then insert current)
    s = re.sub(r'/\* dropdown menu \*/.*?@media\(max-width:920px\)\{\.pill nav\{display:none\}\}\n?', '', s, flags=re.S)
    s = s.replace('</style>', DD_CSS + '</style>', 1)
    open(path, 'w').write(s)
    return True

def run():
    count = 0
    for path in glob.glob('*.html'):
        if path in ('index.html','Homepage.html'):  # homepage uses its native .nav/.dd system
            continue
        if process(path, '', 'pages/services/'): count += 1
    for path in glob.glob('pages/services/*.html'):
        if process(path, '../../', ''): count += 1
    for sub in ('areas', 'blog', 'help'):
        for path in glob.glob(f'pages/{sub}/*.html'):
            if process(path, '../../', '../services/'): count += 1
    print('nav injected into', count, 'pages')

if __name__ == '__main__':
    run()
