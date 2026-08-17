#!/usr/bin/env python3
"""Replace every inner page's old white-pill header with Homepage v2's dark header
(topbar + sticky nav row + mega menus + rating badge + CTAs + mobile burger menu).
Source of truth: extracts live from index.html each run, so homepage edits propagate.
Idempotent via <!--HDR--> markers. Skips index.html/Homepage.html.
Run from site-preview root: python3 headergen.py
"""
import re, glob

HOME = open('index.html').read()

def extract():
    s = HOME
    i = s.find('<div class="topbar"')
    k = s.find('<div class="mmenu"', i)
    header = s[i:k]
    j = s.find('<main', k)
    mmenu = s[k:j]
    css_all = re.search(r'<style>(.*?)</style>', s, re.S).group(1)
    toks = ['.topbar','.tb-','.hdr','.hwrap','.hright','.hrow','.grat','.logo','.skip',
            '.nav','.mega','.has-mega','.dd','.car','.burger','.mm-','.mmenu','.btn-sp','.hdr-ctas']
    def parse(block):
        # yield (selector, body, is_at) with balanced braces
        out=[]; i=0; n=len(block)
        while i<n:
            b=block.find('{', i)
            if b<0: break
            sel=block[i:b].strip()
            depth=1; j=b+1
            while j<n and depth:
                if block[j]=='{': depth+=1
                elif block[j]=='}': depth-=1
                j+=1
            out.append((sel, block[b+1:j-1]))
            i=j
        return out
    keep=[]
    for sel, body in parse(css_all):
        if sel.startswith('@media'):
            inner=[(s2,b2) for s2,b2 in parse(body) if any(t in s2 for t in toks)]
            if inner:
                keep.append(sel+'{'+''.join(f'{s2}{{{b2}}}' for s2,b2 in inner)+'}')
        elif any(t in sel for t in toks):
            keep.append(f'{sel}{{{body}}}')
    css = '\n'.join(keep)
    defs_all = re.search(r'<svg width="0" height="0".*?</svg>', s, re.S).group(0)
    need = ['i-pin','i-phone','i-chev','i-menu','i-x','i-star','i-fish']
    syms = [m for m in re.findall(r'<symbol id="[^"]+".*?</symbol>', defs_all, re.S)
            if any(f'id="{n}"' in m for n in need)]
    defs = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
            + ''.join(syms) + '</defs></svg>')
    js = [m for m in re.findall(r'<script>(?:(?!</script>).)*?</script>', s, re.S)
          if 'burger' in m][0]
    return header, mmenu, css, defs, js

HEADER, MMENU, CSS, DEFS, JS = extract()

# header CSS references v2 :root vars that inner pages don't define — scope them
VARS = (".topbar,.hdr,.mmenu{--coral:#F24E45;--coral-d:#DD4A43;--red:#A7130C;--navy:#003D6A;"
        "--navy-d:#052B49;--teal:#42BE9F;--teal-lt:#8FE3CC;--cream:#FEDFAE;--sky:#E6F4FF;"
        "--sand:#FFF5E6;--ink:#001E33;--body:#3F444B;--muted:#706F6F;"
        "--disp:'Burbank Big',Impact,sans-serif;--txt:'Sofia Sans',Arial,sans-serif}\n")

MA, MB = "<!--HDR-->", "<!--/HDR-->"

def adapt(html, R):
    h = html
    h = h.replace('src="assets/', f'src="{R}assets/')
    h = h.replace('src="uploads/', f'src="{R}uploads/')
    h = h.replace('href="pages/', f'href="{R}pages/')
    for root_page in ('about-us.html','reviews.html','specials.html','referral-program.html',
                      'giving-back.html','contact-us.html','privacy-policy.html',
                      'terms-of-service.html','cookie-policy.html','index.html'):
        h = h.replace(f'href="{root_page}"', f'href="{R}{root_page}"')
    h = h.replace('href="/"', f'href="{R}index.html"')
    # homepage section anchors -> real pages when off-homepage
    h = h.replace('href="#services"', f'href="{R}pages/services/index.html"')
    h = h.replace('href="#reviews"', f'href="{R}reviews.html"')
    h = h.replace('href="#offers"', f'href="{R}specials.html"')
    h = h.replace('href="#contact"', f'href="{R}contact-us.html"')
    h = h.replace('href="#areas"', f'href="{R}pages/areas/index.html"')
    h = h.replace('href="#why"', f'href="{R}about-us.html"')
    return h

def block(R):
    return (MA + DEFS + adapt(HEADER, R) + adapt(MMENU, R) + MB)

def process(path, R):
    s = open(path).read()
    s2 = re.sub(re.escape(MA)+r'.*?'+re.escape(MB), '@@H@@', s, flags=re.S)
    if '@@H@@' not in s2:
        s2 = re.sub(r'<div class="hdr-zone">.*?</header></div>', '@@H@@', s, count=1, flags=re.S)
    if '@@H@@' not in s2:
        return False
    s2 = s2.replace('@@H@@', block(R), 1)
    # refresh header css block
    s2 = re.sub(r'/\* v2 header \*/.*?/\* /v2 header \*/', '', s2, flags=re.S)
    s2 = s2.replace('</style>', '/* v2 header */\n' + VARS + CSS + '\n/* /v2 header */</style>', 1)
    # header JS once, before </body>
    s2 = re.sub(r'<script>(?:(?!</script>).)*?burger(?:(?!</script>).)*?</script>', '', s2, flags=re.S)
    s2 = s2.replace('</body>', JS + '</body>', 1)
    open(path, 'w').write(s2)
    return True

def run():
    n = 0
    for p in glob.glob('*.html'):
        if p in ('index.html', 'Homepage.html'):
            continue
        if process(p, ''): n += 1
    for sub in ('services', 'areas', 'blog', 'help'):
        for p in glob.glob(f'pages/{sub}/*.html'):
            if process(p, '../../'): n += 1
    print('v2 header on', n, 'pages')

if __name__ == '__main__':
    run()
