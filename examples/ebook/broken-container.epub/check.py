import re, zipfile

with zipfile.ZipFile("broken-container.epub") as z:
    first = z.infolist()[0]
    if first.filename != "mimetype" or first.compress_type != zipfile.ZIP_STORED:
        raise SystemExit("rejected: mimetype must be the first entry, stored uncompressed")
    container = z.read("META-INF/container.xml").decode("utf-8")
    opf = re.search(r'full-path="([^"]+)"', container).group(1)
    print("ok" if opf in z.namelist() else f"rejected: container.xml points at {opf}, which is missing")
