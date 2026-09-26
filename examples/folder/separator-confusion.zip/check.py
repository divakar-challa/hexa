import unicodedata
import zipfile

RESERVED = {"CON", "PRN", "AUX", "NUL"} | {f"{d}{i}" for d in ("COM", "LPT") for i in range(1, 10)}
LONG = 200  # leaves room for the folder it is extracted into, under Windows' classic 260

def problems(names):
    paths = {}  # every entry and every parent folder, in order
    for name in names:
        parts = name.rstrip("/").split("/")
        for i in range(len(parts)):
            paths.setdefault("/".join(parts[:i + 1]), parts[i])
    for path, part in paths.items():
        if "\\" in part:
            yield f"{path!r}: a backslash is a folder separator on Windows"
        if part in ("", "."):
            yield f"{path!r}: empty or '.' segment"
        elif part.split(".")[0].upper() in RESERVED:
            yield f"{path!r}: {part} is a reserved device name on Windows"
        elif part != part.rstrip(". "):
            yield f"{path!r}: ends in a dot or space, which Windows drops"
        if unicodedata.normalize("NFC", part) != part:
            yield f"{ascii(path)}: not NFC-normalised, so it may not match the same name typed elsewhere"
    groups = {}
    for path in paths:
        groups.setdefault(unicodedata.normalize("NFC", path).casefold(), []).append(path)
    for same in groups.values():
        if len(same) > 1:
            yield " and ".join(map(repr, same)) + ": the same path on Windows and macOS"
    longest = max(names, key=len, default="")
    if len(longest) > LONG:
        yield f"longest entry is {len(longest)} characters: extracted into any folder, it passes the 260-character limit"

with zipfile.ZipFile("separator-confusion.zip") as z:
    names = [info.orig_filename for info in z.infolist()]
found = list(problems(names))
print(f"{len(names)} entries: " + (f"{len(found)} portability problem{'s' * (len(found) != 1)}" if found else "portable"))
for p in found:
    print("  " + p)
