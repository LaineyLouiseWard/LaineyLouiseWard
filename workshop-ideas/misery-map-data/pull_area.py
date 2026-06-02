"""Compute county land area (km2) from the site GeoJSON.
Writes area.json {county: areaKm2}. Reprojects each county polygon from
EPSG:4326 (WGS84) to EPSG:2157 (Irish Transverse Mercator) so the planar
area is metres-true, then divides by 1e6 for km2.
Run: python3 pull_area.py  (needs shapely + pyproj; no network).
See DATA_PIPELINE.md."""
import json, os
from pyproj import Transformer
from shapely.geometry import shape
from shapely.ops import transform

HERE = os.path.dirname(__file__)
GEOJSON = os.path.join(HERE, "..", "misery-map-site", "counties.geojson")

tf = Transformer.from_crs("EPSG:4326", "EPSG:2157", always_xy=True)
project = lambda x, y: tf.transform(x, y)

gj = json.load(open(GEOJSON))
results = {}
for feat in gj["features"]:
    county = feat["properties"]["county"]
    geom = transform(project, shape(feat["geometry"]))
    results[county] = round(geom.area / 1e6, 2)
    print(f"  {county:11} {results[county]}")

results = {c: results[c] for c in sorted(results)}
json.dump(results, open("area.json", "w"), indent=1)
print(f"\narea: total {round(sum(results.values()), 2)} km2 over {len(results)} counties")
