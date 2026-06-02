"""Count arts & music venues per county via the keyless OSM Overpass API.
Writes arts.json {county: count}. Counts the union of tourism=gallery,
amenity=arts_centre and amenity=theatre. Caches each county to osm_raw/ so
reruns are cheap.
Run: python3 pull_arts.py  (needs network; paced for the 4-slot rate limit)
See DATA_PIPELINE.md."""
import json, os, time, urllib.request, urllib.parse

URL = "https://overpass-api.de/api/interpreter"
RAW = os.path.join(os.path.dirname(__file__), "osm_raw")
os.makedirs(RAW, exist_ok=True)
COUNTIES = ["Carlow","Cavan","Clare","Cork","Donegal","Dublin","Galway","Kerry","Kildare","Kilkenny",
            "Laois","Leitrim","Limerick","Longford","Louth","Mayo","Meath","Monaghan","Offaly",
            "Roscommon","Sligo","Tipperary","Waterford","Westmeath","Wexford","Wicklow"]

AREA = 'area["name"="County {c}"]["admin_level"="6"]["boundary"="administrative"]->.c;'
ARTS = (AREA +
        'nwr["tourism"="gallery"](area.c);'
        'nwr["amenity"="arts_centre"](area.c);'
        'nwr["amenity"="theatre"](area.c);'
        'out count;')

def run(q):
    data = urllib.parse.urlencode({"data": "[out:json][timeout:120];" + q}).encode()
    req = urllib.request.Request(URL, data=data, headers={"User-Agent": "misery-map/0.1 (workshop)"})
    d = json.load(urllib.request.urlopen(req, timeout=180))
    for el in d.get("elements", []):
        if el.get("type") == "count":
            return int(el["tags"]["total"])
    return 0

results = {}
for c in COUNTIES:
    cache = os.path.join(RAW, f"arts_{c}.txt")
    if os.path.exists(cache):
        results[c] = int(open(cache).read()); continue
    n = None
    for attempt in range(4):
        try:
            n = run(ARTS.format(c=c)); break
        except Exception as e:
            print(f"  retry {c} ({attempt+1}): {str(e)[:60]}"); time.sleep(5)
    results[c] = n if n is not None else 0
    open(cache, "w").write(str(results[c]))
    print(f"  {c:11} arts {results[c]}")
    time.sleep(1.5)

json.dump(results, open("arts.json", "w"), indent=1)
print(f"\narts: total {sum(results.values())}")
