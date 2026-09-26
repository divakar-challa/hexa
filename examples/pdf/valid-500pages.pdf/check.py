import re
import zlib

with open("valid-500pages.pdf", "rb") as f:
    data = f.read()
pages = len(re.findall(rb"/Type\s*/Page\b", data))
drawing = 0
for m in re.finditer(rb"(?<!end)stream\r?\n", data):
    raw = data[m.end():data.find(b"endstream", m.end())]
    try:
        raw = zlib.decompressobj().decompress(raw)
    except zlib.error:
        pass  # not Flate-compressed
    if re.search(rb"\bT[Jj]\b", raw):
        drawing += 1
print(f"page objects: {pages}, content streams that draw text: {drawing}")
if pages == 0:
    print("no pages: most readers show an error or a blank document")
elif drawing == 0:
    print("no text layer: extraction returns nothing, so this needs OCR")
