# points.geojson

A valid GeoJSON FeatureCollection with Point, LineString and Polygon features and properties.

Page: https://hexaqa.com/file/geospatial/points-geojson

```bash
curl -fsSL -o "points.geojson" "https://files.hexaqa.com/geo/points.geojson"
```

SHA-256: `99bd7b583968d210f1804002156f079c895c7bab473826aee2128b9c3554ade5`

## Python

GeoJSON is [longitude, latitude], polygon rings must close, and RFC 7946 (section 3.1.9) asks for lines that cross the 180th meridian to be split, or a map draws them the long way round the world.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
3 features: valid
```
