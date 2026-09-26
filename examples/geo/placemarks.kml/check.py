import xml.etree.ElementTree as ET

points = []  # (lat, lon)
for el in ET.parse("placemarks.kml").getroot().iter():
    tag = el.tag.rsplit("}", 1)[-1]
    if tag in ("trkpt", "rtept", "wpt"):  # GPX
        points.append((float(el.get("lat")), float(el.get("lon"))))
    elif tag == "coordinates":  # KML: lon,lat[,alt] tuples
        for t in el.text.split():
            lon, lat = map(float, t.split(",")[:2])
            points.append((lat, lon))
bad = [p for p in points if not (-90 <= p[0] <= 90 and -180 <= p[1] <= 180)]
print(f"{len(points)} points, first at lat {points[0][0]}, lon {points[0][1]}")
print(f"{len(bad)} out of range" if bad else "all within range")
