MARKERS = (b"<html", b"<script", b"<body", b"<iframe", b"<svg", b"<!doctype html")

with open("polyglot-gif-html.gif", "rb") as f:
    head = f.read(1024)
kind = {b"GIF8": "GIF", b"\x89PNG": "PNG", b"\xff\xd8\xff\xe0": "JPEG"}.get(head[:4], "unknown")
found = [m.decode() for m in MARKERS if m in head.lower()]
if found:
    print(f"starts as {kind}, but the first 1 KB also contains {', '.join(found)}: a sniffing browser may render it as HTML")
else:
    print(f"{kind}: no HTML markers in the first 1 KB")
