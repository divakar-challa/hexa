import json

def points(c):
    if isinstance(c, list) and c and all(isinstance(v, (int, float)) for v in c):
        yield c
    elif isinstance(c, list):
        for item in c:
            yield from points(item)

def check(geom, n):
    kind, coords = geom.get("type"), geom.get("coordinates") or []
    for p in points(coords):
        if len(p) < 2 or not (-180 <= p[0] <= 180 and -90 <= p[1] <= 90):
            yield f"feature {n}: {p} is not [longitude, latitude] in range"
    if kind == "Polygon":
        for ring in coords:
            if len(ring) < 4 or ring[0] != ring[-1]:
                yield f"feature {n}: polygon ring is not closed (4+ positions, last equal to first)"
    if kind in ("LineString", "Polygon"):
        line = coords if kind == "LineString" else coords[0]
        for a, b in zip(line, line[1:]):
            if abs(a[0] - b[0]) > 180:
                yield f"feature {n}: {a} to {b} crosses the antimeridian; split it"

with open("antimeridian.geojson", encoding="utf-8") as f:
    features = json.load(f)["features"]
found = [p for n, feat in enumerate(features, 1) for p in check(feat.get("geometry") or {}, n)]
print(f"{len(features)} features:", "valid" if not found else f"{len(found)} problem{'s' * (len(found) != 1)}")
for p in found:
    print("  " + p)
