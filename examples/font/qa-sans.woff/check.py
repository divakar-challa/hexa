import struct

REQUIRED = {"cmap", "head", "hhea", "hmtx", "maxp", "name", "post"}

with open("qa-sans.woff", "rb") as f:
    data = f.read()
sig = data[:4]
if sig == b"wOF2":
    n = struct.unpack(">H", data[12:14])[0]
    print(f"WOFF2 with {n} tables, Brotli-compressed: read further with fontTools")
elif sig in (b"wOFF", b"\x00\x01\x00\x00", b"true", b"OTTO"):
    if sig == b"wOFF":
        kind, n, start, step = "WOFF", struct.unpack(">H", data[12:14])[0], 44, 20
    else:
        kind = "OpenType (CFF)" if sig == b"OTTO" else "TrueType"
        n, start, step = struct.unpack(">H", data[4:6])[0], 12, 16
    tags = {data[start + i * step:start + i * step + 4].decode("latin-1") for i in range(n)}
    missing = sorted(REQUIRED - tags)
    print(f"{kind} with {n} tables: {', '.join(sorted(tags))}")
    print("missing required tables: " + ", ".join(missing) if missing else "all required tables present")
else:
    print("not a font: starts with", sig.hex())
