# antimeridian.geojson

A LineString and Polygon that cross the 180° antimeridian (longitudes near +180 and -180).

Page: https://hexaqa.com/file/geospatial/antimeridian-geojson

```bash
curl -fsSL -o "antimeridian.geojson" "https://files.hexaqa.com/geo/antimeridian.geojson"
```

SHA-256: `b99aef5a88f6357dd081b6b9abce13070772029887c24cb474889fc637cd246d`

## Python

GeoJSON is [longitude, latitude], polygon rings must close, and RFC 7946 (section 3.1.9) asks for lines that cross the 180th meridian to be split, or a map draws them the long way round the world.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
2 features: 1 problem
  feature 1: [170, 0] to [-170, 0] crosses the antimeridian; split it
```
