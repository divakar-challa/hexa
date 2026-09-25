import codecs

BOMS = ((codecs.BOM_UTF8, "utf-8"), (codecs.BOM_UTF16_LE, "utf-16-le"), (codecs.BOM_UTF16_BE, "utf-16-be"))

def decode(raw):
    for bom, enc in BOMS:
        if raw.startswith(bom):
            return enc + " with BOM", raw[len(bom):].decode(enc)
    return "utf-8", raw.decode("utf-8")   # raises on anything else: fail loudly

with open("latin1.txt", "rb") as f:
    raw = f.read()
try:
    enc, text = decode(raw)
    print(enc, repr(text[:40]))
except UnicodeDecodeError as e:
    print(f"not UTF-8: {e.reason} at byte {e.start}")
