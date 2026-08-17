#!/usr/bin/env python3
"""Replace the .ftr stub on every page with the design template's full footer + map.
Idempotent (re-replaces between <!--FOOT--> markers). Skips index.html/Homepage.html (v2 has its own footer).
Run from site-preview root."""
import re, glob

CSS = """/* full footer */
.fmap{line-height:0;background:#052B49;margin-top:56px}
.fmap iframe{width:100%;height:320px;border:0;display:block}
footer.site{background:linear-gradient(180deg,#003D6A,#052B49);color:#fff;padding:54px 24px 30px;text-align:left}
.f-cols{display:grid;grid-template-columns:1.5fr .7fr .7fr 1.15fr;gap:44px;max-width:1120px;margin:0 auto 38px;align-items:start}
.f-brand img{width:225px;max-width:100%;height:auto;display:block;margin:-8px 0 22px -6px}
footer.site h4{font-family:'Burbank Big',Impact,sans-serif;font-weight:700;font-size:18px;text-transform:uppercase;letter-spacing:1px;color:#FEDFAE;margin:0 0 14px}
.lic{font-size:13.5px;color:#EAF4FB;margin:0;display:flex;flex-wrap:wrap;gap:4px 7px;white-space:nowrap}
.lic span+span::before{content:"·";margin-right:7px;color:#7FA6C4}
footer.site ul{list-style:none;margin:0;padding:0}
footer.site li{margin-bottom:12px;font-size:14.5px}
footer.site a{color:#fff;text-decoration:none;font-weight:400}
footer.site a:hover{color:#FEDFAE;text-decoration:underline}
.cl{display:flex;gap:11px;align-items:flex-start;margin-bottom:12px;font-size:14.5px;line-height:1.55}
.cl svg{width:17px;height:17px;flex:0 0 auto;fill:#F24E45;margin-top:2px}
.soc{display:flex;gap:7px;flex-wrap:wrap;margin-top:18px}
.soc a{width:34px;height:34px;border-radius:50%;background:#F24E45;display:inline-flex;align-items:center;justify-content:center;color:#fff;transition:background .2s}
.soc a:hover{background:#A7130C;color:#fff;text-decoration:none}
.soc svg{width:14px;height:14px;fill:#fff}
.f-bar{max-width:1180px;margin:0 auto;font-size:14px;color:#DAE6EF;padding-top:8px}
@media(max-width:920px){.f-cols{grid-template-columns:1fr 1fr;gap:36px}}
@media(max-width:560px){.f-cols{grid-template-columns:1fr}}
"""

I_PHONE='<svg viewBox="0 0 24 24"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1C10.61 21 3 13.39 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.24.2 2.45.57 3.57a1 1 0 0 1-.25 1.02l-2.2 2.2z"/></svg>'
I_PIN='<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"/></svg>'
I_CLOCK='<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 10.6 4.2 2.5-.8 1.3L11 13V7h2v5.6z"/></svg>'
I_FB='<svg viewBox="0 0 24 24"><path d="M13.5 21v-7h2.4l.45-3H13.5V9.1c0-.87.29-1.6 1.62-1.6h1.53V4.85c-.27-.04-1.2-.12-2.28-.12-2.26 0-3.87 1.38-3.87 3.9V11H8.1v3h2.4v7h3z"/></svg>'
I_IG='<svg viewBox="0 0 24 24"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.2" cy="6.8" r="1.3"/></svg>'
I_YT='<svg viewBox="0 0 24 24"><path d="M21.58 7.19a2.5 2.5 0 0 0-1.76-1.77C18.25 5 12 5 12 5s-6.25 0-7.82.42A2.5 2.5 0 0 0 2.42 7.2 26.2 26.2 0 0 0 2 12c0 1.62.14 3.23.42 4.81a2.5 2.5 0 0 0 1.76 1.77C5.75 19 12 19 12 19s6.25 0 7.82-.42a2.5 2.5 0 0 0 1.76-1.77c.28-1.58.42-3.19.42-4.81s-.14-3.23-.42-4.81zM10 15.5v-7l5.75 3.5z"/></svg>'
I_LI='<svg viewBox="0 0 24 24"><path d="M4.98 3.5a2.49 2.49 0 1 1 0 4.98 2.49 2.49 0 0 1 0-4.98zM3 9.75h4V21H3zM9.5 9.75h3.83v1.54h.06a4.2 4.2 0 0 1 3.78-2.08c4.04 0 4.78 2.66 4.78 6.12V21H18v-5.06c0-1.21-.02-2.76-1.68-2.76-1.68 0-1.94 1.31-1.94 2.67V21H10.5z"/></svg>'

MA, MB = "<!--FOOT-->", "<!--/FOOT-->"

def footer(R):
    return f'''{MA}<div class="fmap"><iframe title="Perfect Catch location — 13932 Walsingham Rd STE A, Largo, FL" src="https://www.google.com/maps?q=13932%20Walsingham%20Rd%20STE%20A%20Largo%20FL%2033774&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<footer class="site">
<div class="f-cols">
<div class="f-brand">
<img src="{R}assets/logo-full.webp" alt="Perfect Catch — Swimming Pool Repair, Gas &amp; Electric" loading="lazy" decoding="async">
<h4>License Numbers:</h4>
<p class="lic"><span>CPC1459998</span><span>CGC1531306</span><span>EC13011994</span><span>LI4527</span></p>
</div>
<div><h4>Navigation</h4><ul><li><a href="{R}index.html">Home</a></li><li><a href="{R}about-us.html">About Us</a></li><li><a href="{R}pages/blog/index.html">Blog</a></li><li><a href="{R}pages/help/index.html">Troubleshooting</a></li><li><a href="{R}pages/areas/index.html">Service Areas</a></li><li><a href="{R}contact-us.html">Contact Us</a></li></ul></div>
<div><h4>Useful Links</h4><ul><li><a href="{R}pages/services/index.html">All Services</a></li><li><a href="{R}reviews.html">Reviews</a></li><li><a href="{R}specials.html">Specials</a></li><li><a href="{R}privacy-policy.html">Privacy Policy</a></li><li><a href="{R}terms-of-service.html">Terms of Service</a></li><li><a href="{R}cookie-policy.html">Cookie Policy</a></li></ul></div>
<div><h4>Contact</h4>
<div class="cl">{I_PHONE}<a href="tel:7273165206">727-316-5206</a></div>
<div class="cl">{I_PIN}<span>13932 Walsingham Rd, STE A, Largo, FL, 33774</span></div>
<div class="cl">{I_CLOCK}<span>Monday — Friday: 8:00 AM — 5:00 PM</span></div>
<div class="soc">
<a href="https://www.facebook.com/people/Perfect-Catch/61570828732967/" target="_blank" rel="noopener" aria-label="Facebook">{I_FB}</a>
<a href="https://www.instagram.com/callperfectcatch" target="_blank" rel="noopener" aria-label="Instagram">{I_IG}</a>
<a href="https://www.youtube.com/@Perfectcatchelectric" target="_blank" rel="noopener" aria-label="YouTube">{I_YT}</a>
<a href="https://www.linkedin.com/company/call-perfect-catch-electric" target="_blank" rel="noopener" aria-label="LinkedIn">{I_LI}</a>
</div>
</div>
</div>
<div class="f-bar">©2026 Perfect Catch Swimming Pool Repair, Gas, &amp; Electric. All rights reserved.</div>
</footer>{MB}'''

def process(path, R):
    s = open(path).read()
    s2 = re.sub(re.escape(MA)+r'.*?'+re.escape(MB), '@@F@@', s, flags=re.S)
    if '@@F@@' not in s2:
        s2 = re.sub(r'<div class="ftr">.*?</div>', '@@F@@', s, count=1, flags=re.S)
    if '@@F@@' not in s2:
        return False
    s2 = s2.replace('@@F@@', footer(R), 1)
    if '/* full footer */' not in s2:
        s2 = s2.replace('</style>', CSS + '</style>', 1)
    open(path, 'w').write(s2)
    return True

def run():
    n = 0
    for p in glob.glob('*.html'):
        if p in ('index.html', 'Homepage.html', 'DESIGN-HUB-REF.html'):
            continue
        if process(p, ''): n += 1
    for sub in ('services', 'areas', 'blog', 'help'):
        for p in glob.glob(f'pages/{sub}/*.html'):
            if process(p, '../../'): n += 1
    print('full footer on', n, 'pages')

if __name__ == '__main__':
    run()
