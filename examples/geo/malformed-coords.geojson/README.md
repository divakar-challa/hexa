# malformed-coords.geojson

GeoJSON that parses as JSON but violates the spec: a latitude of std 999 and a Polygon whose ring is not closed.

Page: https://hexaqa.com/file/geospatial/malformed-coords-geojson

```bash
curl -fsSL -o "malformed-coords.geojson" "https://files.hexaqa.com/geo/malformed-coords.geojson"
```

SHA-256: `2690623c7de41f9f981408447b5c589bf067c1635bb4fe7d8e29af7af5c057c8`

## Python

GeoJSON is [longitude, latitude], polygon rings must close, and RFC 7946 (section 3.1.9) asks for lines that cross the 180th meridian to be split, or a map draws them the long way round the world.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
2 features: 2 problems
  feature 1: [0, 999] is not [longitude, latitude] in range
  feature 2: polygon ring is not closed (4+ positions, last equal to first)
```
