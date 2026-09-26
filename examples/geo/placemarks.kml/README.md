# placemarks.kml

A KML document with a Placemark point, a LineString path and a styled polygon.

Page: https://hexaqa.com/file/geospatial/placemarks-kml

```bash
curl -fsSL -o "placemarks.kml" "https://files.hexaqa.com/geo/placemarks.kml"
```

SHA-256: `ec08fd9db64a893d4c7a2274d48d0cfe08272f35534465791221683f676221ff`

## Python

GPX stores lat and lon as attributes; KML writes "lon,lat,alt" text, the opposite order. Read each in its own order and validate the ranges, or points end up swapped across the globe.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
4 points, first at lat 51.5072, lon -0.1276
all within range
```
