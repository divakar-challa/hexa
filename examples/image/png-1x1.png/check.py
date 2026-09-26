import struct

MAX_PIXELS = 25_000_000  # a decoder needs about 4 bytes per pixel

def image_size(path):
    with open(path, "rb") as f:
        head = f.read(64 * 1024)
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        return "png", *struct.unpack(">II", head[16:24])
    if head[:6] in (b"GIF87a", b"GIF89a"):
        return "gif", *struct.unpack("<HH", head[6:10])
    if head[:2] == b"BM":
        w, h = struct.unpack("<ii", head[18:26])
        return "bmp", w, abs(h)  # a negative height means rows are stored top-down
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        chunk = head[12:16]
        if chunk == b"VP8 ":
            w, h = struct.unpack("<HH", head[26:30])
            return "webp", w & 0x3FFF, h & 0x3FFF
        if chunk == b"VP8L":
            bits = int.from_bytes(head[21:25], "little")
            return "webp", (bits & 0x3FFF) + 1, (bits >> 14 & 0x3FFF) + 1
        if chunk == b"VP8X":
            return "webp", int.from_bytes(head[24:27], "little") + 1, int.from_bytes(head[27:30], "little") + 1
    if head[:3] == b"\xff\xd8\xff":
        i = 2
        while i + 9 <= len(head) and head[i] == 0xFF:
            marker, length = head[i + 1], int.from_bytes(head[i + 2:i + 4], "big")
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):  # start of frame
                h, w = struct.unpack(">HH", head[i + 5:i + 9])
                return "jpg", w, h
            i += 2 + length
        raise ValueError("no JPEG frame header in the first 64 KB")
    raise ValueError("not a PNG, GIF, BMP, WebP or JPEG")

try:
    kind, w, h = image_size("png-1x1.png")
except ValueError as e:
    print("rejected:", e)
else:
    if w * h > MAX_PIXELS:
        print(f"refused: {kind} {w}x{h} is {w * h:,} pixels, over the {MAX_PIXELS:,} limit")
    else:
        print(f"ok: {kind} {w}x{h}")
