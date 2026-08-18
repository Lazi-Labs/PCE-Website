#!/usr/bin/env python3
"""
Collect the per-city facts the Location Page design needs but the site does
not already know: how far each city is from the Largo shop, which
neighborhoods sit inside it, and which of our own service areas are actually
its nearest neighbours.

Everything here comes from a citable public source, written to locdata.json
so page generation stays offline and reproducible:

  Nominatim (OSM)  — city centre coordinates
  OSRM             — real driving distance + time from the shop

Neighborhood names are deliberately NOT sourced here: OSM's place=* data for
Pinellas is subdivision plats and apartment complexes ("Avana Coachman"), not
the names locals use. Those live in neighborhoods.json, hand-maintained.

Re-run only when the city list changes; the APIs are public and rate-limited,
so this is deliberately slow and cached.  `python3 locdata.py --refresh` to
rebuild from scratch.
"""
import json, math, pathlib, re, sys, time, urllib.parse, urllib.request

HERE = pathlib.Path(__file__).parent
OUT = HERE / 'locdata.json'
SHOP = (27.8897, -82.8329)          # 13932 Walsingham Rd, Largo FL 33774
UA = {'User-Agent': 'pce-website-locgen/1.0 (+https://callperfectcatch.com)'}

def get(url, data=None, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())
        except Exception as e:
            if i == tries - 1:
                print(f'    ! {type(e).__name__} {str(e)[:60]}')
                return None
            time.sleep(4 * (i + 1))

def geocode(name, county):
    q = urllib.parse.urlencode({'q': f'{name}, {county} County, Florida, USA',
                                'format': 'json', 'limit': 1})
    r = get(f'https://nominatim.openstreetmap.org/search?{q}')
    time.sleep(1.1)                                  # Nominatim: 1 req/sec
    return (float(r[0]['lat']), float(r[0]['lon'])) if r else None

def drive(lat, lon):
    """Real road distance/time from the shop — not straight-line."""
    r = get(f'https://router.project-osrm.org/route/v1/driving/'
            f'{SHOP[1]},{SHOP[0]};{lon},{lat}?overview=false')
    if not r or r.get('code') != 'Ok':
        return None
    leg = r['routes'][0]
    return {'miles': round(leg['distance'] / 1609.34),
            'minutes': round(leg['duration'] / 60)}

# Subdivision noise: apartment complexes, mobile-home parks and bare plat
# names read as filler on a service page. Recognisable places only.
NOISE = re.compile(r'apartment|apts|condo|mobile|trailer|villas of|townhom|'
                   r'^unit |mhp$|r\.?v\.? park|campground', re.I)

def neighborhoods(name, county, coords=None, radius_m=5000):
    q = (f'[out:json][timeout:60];'
         f'area["name"="{name}"]["boundary"="administrative"]'
         f'["admin_level"~"8|9"]->.a;'
         f'(node(area.a)["place"="suburb"];'
         f' node(area.a)["place"="neighbourhood"];'
         f' node(area.a)["place"="quarter"];);out tags;')
    r = get('https://overpass-api.de/api/interpreter',
            data=urllib.parse.urlencode({'data': q}).encode())
    time.sleep(4)                                    # Overpass is shared
    # Half our service areas are CDPs (Apollo Beach, Citrus Park, Palm Harbor)
    # with no admin boundary to search inside — fall back to a radius around
    # the city centre so unincorporated areas get a list too.
    if not r or not r.get('elements'):
        if coords:
            lat, lon = coords
            q2 = (f'[out:json][timeout:60];'
                  f'(node(around:{radius_m},{lat},{lon})'
                  f'["place"~"^(suburb|neighbourhood|quarter)$"];);out tags;')
            r = get('https://overpass-api.de/api/interpreter',
                    data=urllib.parse.urlencode({'data': q2}).encode())
            time.sleep(4)
    if not r:
        return []
    # suburbs first — they are the names locals actually use
    rank = {'suburb': 0, 'quarter': 1, 'neighbourhood': 2}
    seen, out = set(), []
    for e in sorted(r.get('elements', []),
                    key=lambda e: rank.get(e['tags'].get('place'), 9)):
        n = e.get('tags', {}).get('name', '').strip()
        if not n or NOISE.search(n) or n.lower() in seen or n == name:
            continue
        seen.add(n.lower()); out.append(n)
    return out

def haversine(a, b):
    la1, lo1, la2, lo2 = map(math.radians, [*a, *b])
    return 7917.5 * math.asin(math.sqrt(
        math.sin((la2 - la1) / 2) ** 2
        + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)) / 2

def main():
    sys.path.insert(0, str(HERE))
    from locgen import city_facts
    cities = city_facts()
    data = {} if '--refresh' in sys.argv else (
        json.loads(OUT.read_text()) if OUT.exists() else {})

    for slug, f in cities.items():
        d = data.setdefault(slug, {})
        if d.get('done'):
            continue
        print(f'  {f["name"]}')
        if not d.get('coords'):
            c = geocode(f['name'], f['county'])
            if not c:
                print('    ! no geocode'); continue
            d['coords'] = c
        if not d.get('drive'):
            d['drive'] = drive(*d['coords'])
            print(f'    {d["drive"]}')
        d['done'] = True
        OUT.write_text(json.dumps(data, indent=1, sort_keys=True))

    # Nearest OTHER service areas — geographic, unlike the alphabetical
    # "nearby cities" lists the old city pages shipped with.
    pts = {s: tuple(d['coords']) for s, d in data.items() if d.get('coords')}
    for s, d in data.items():
        if s not in pts:
            continue
        d['near'] = [o for o, _ in sorted(
            ((o, haversine(pts[s], p)) for o, p in pts.items() if o != s),
            key=lambda x: x[1])[:4]]
    OUT.write_text(json.dumps(data, indent=1, sort_keys=True))
    ok = [s for s, d in data.items() if d.get('drive')]
    print(f'\n{len(ok)}/{len(cities)} cities with drive data; '
          f'{sum(len(d.get("hoods", [])) for d in data.values())} neighborhoods total')

main()
