import struct

kinds = []
with open("fake-mp4-wrong-magic.mp4", "rb") as f:
    while len(head := f.read(8)) == 8:
        size, kind = struct.unpack(">I4s", head)
        header = 8
        if size == 1:  # a 64-bit size follows
            size, header = struct.unpack(">Q", f.read(8))[0], 16
        kinds.append(kind.decode("ascii") if all(32 <= b < 127 for b in kind) else "0x" + kind.hex())
        if size == 0:
            break  # the box runs to the end of the file
        if size < header:
            print(f"rejected: box {kinds[-1]!r} declares {size} bytes")
            break
        f.seek(size - header, 1)
if not kinds or kinds[0] != "ftyp":
    print("not an MP4: the first box is", kinds[0] if kinds else "missing")
elif "moov" not in kinds:
    print("boxes:", ", ".join(kinds) + "; no moov box, so there is nothing to play")
else:
    print("boxes:", ", ".join(kinds))
