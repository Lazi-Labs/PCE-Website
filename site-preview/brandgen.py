#!/usr/bin/env python3
"""
Keep the "Brands We Service" marquee in sync across every page that runs one.

The strip is a CSS marquee: one real .mgroup plus identical aria-hidden copies
that make the loop seamless. Editing it by hand means editing the same list
5x on 3 pages, so BRANDS below is the single source of truth and this
rewrites every group from it.

Logo files live in assets/brand-<slug>.webp. Drop new source art (png/svg/jpg)
into ../incoming-logos/ named for the slug and run with --import to convert
and register it before the strip is rebuilt.
"""
import pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).parent
INCOMING = HERE.parent / 'incoming-logos'

# Display order, left to right. alt text is what a screen reader announces.
BRANDS = [
    ('gulfstream', 'Gulf Stream'),
    ('amp',        'AMP Lighting'),
    ('pentair',    'Pentair'),
    ('jandy',      'Jandy'),
    ('hayward',    'Hayward'),
    ('aquastar',   'AquaStar Pool Products'),
    ('moov',       'MOOV Pool Products'),
    ('madimack',   'Madimack'),
    ('pal',        'PAL Lighting'),
]

def import_art():
    """Convert whatever art was dropped in ../incoming-logos into assets/."""
    if not INCOMING.exists():
        print(f'no {INCOMING} — nothing to import'); return
    slugs = {s for s, _ in BRANDS}
    for f in sorted(INCOMING.iterdir()):
        if f.name.startswith('.') or f.is_dir():
            continue
        slug = re.sub(r'[^a-z0-9]+', '', f.stem.lower())
        match = next((s for s in slugs if s in slug or slug in s), None)
        if not match:
            print(f'  ? {f.name} — no BRANDS slug matches, skipped'); continue
        out = HERE / 'assets' / f'brand-{match}.webp'
        # -background none keeps transparency; the strip sits on white and on
        # the navy silo band, so a baked-in white box would show as a card.
        r = subprocess.run(['magick', str(f), '-background', 'none',
                            '-trim', '+repage', '-resize', 'x120',
                            '-quality', '88', str(out)], capture_output=True)
        if r.returncode:
            print(f'  ! {f.name}: {r.stderr.decode()[:90]}')
        else:
            print(f'  ✓ {f.name} → assets/{out.name} ({out.stat().st_size//1024}kb)')

def live():
    """Only brands whose art is actually on disk — a listed-but-missing logo
    would render as a broken image on the live site, which is worse than the
    brand simply not being in the strip yet."""
    return [(s, a) for s, a in BRANDS
            if (HERE / 'assets' / f'brand-{s}.webp').exists()]

def group(hidden):
    return ('<div class="mgroup"' + (' aria-hidden="true"' if hidden else '') + '>'
            + ''.join(f'<img src="{{p}}assets/brand-{s}.webp" alt="{"" if hidden else a}"'
                      f' loading="lazy" width="150" height="60">'
                      for s, a in live()) + '</div>')

def rebuild():
    pages = [p for p in HERE.rglob('*.html') if 'brand-hayward' in p.read_text()]
    for p in pages:
        s = p.read_text()
        prefix = '../' * len(p.relative_to(HERE).parts[:-1])
        m = re.search(r'(<div class="(?:mtrack|silo-brandtrack)">)(.*?)'
                      r'(</div>\s*</(?:section|div)>)', s, re.S)
        if not m:
            print(f'  ! {p.name}: no .mtrack'); continue
        n = len(re.findall(r'<div class="mgroup"', m.group(2)))
        track = (group(False) + ''.join(group(True) for _ in range(n - 1))
                 ).replace('{p}', prefix)
        s = s[:m.start(2)] + track + s[m.end(2):]
        p.write_text(s)
        print(f'  {p.relative_to(HERE)}: {len(live())} logos × {n} groups')
    have = {s for s, _ in live()}
    missing = [s for s, _ in BRANDS if s not in have]
    print(f'\n{len(pages)} pages rebuilt with {len(have)} logos.'
          + (f'\nAWAITING ART (left out of the strip, not broken): '
             f'{", ".join(missing)}\nDrop the files in {INCOMING} and re-run '
             f'with --import' if missing else '\nall logo files present'))

if '--import' in sys.argv:
    import_art()
rebuild()
