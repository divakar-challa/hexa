# track.gpx

A GPX 1.1 track with timestamped, elevation-tagged track points, plus a waypoint.

Page: https://hexaqa.com/file/geospatial/track-gpx

```bash
curl -fsSL -o "track.gpx" "https://files.hexaqa.com/geo/track.gpx"
```

SHA-256: `a33e9e431f34ab79b1c7eb4ae6d1bc4cd59412cfa5eca6dddd6673a5f629dc68`

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
