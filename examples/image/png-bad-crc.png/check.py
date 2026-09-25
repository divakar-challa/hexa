import struct, zlib

with open("png-bad-crc.png", "rb") as f:
    data = f.read()
if data[:8] != b"\x89PNG\r\n\x1a\n":
    raise SystemExit("not a PNG")

pos = 8
while True:
    if pos + 8 > len(data):
        raise SystemExit("truncated: the file ends before an IEND chunk")
    length, ctype = struct.unpack(">I4s", data[pos:pos + 8])
    end = pos + 12 + length
    if end > len(data):
        raise SystemExit(f"truncated: the {ctype.decode()} chunk needs {length} bytes")
    if zlib.crc32(data[pos + 4:end - 4]) != struct.unpack(">I", data[end - 4:end])[0]:
        raise SystemExit(f"bad CRC in the {ctype.decode()} chunk")
    if ctype == b"IEND":
        break
    pos = end
print("chunk structure is valid")
