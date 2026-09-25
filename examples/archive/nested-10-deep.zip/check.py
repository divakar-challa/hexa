import io, zipfile

MAX_DEPTH = 3

def walk(data, depth=0):
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        for info in z.infolist():
            if info.filename.lower().endswith(".zip"):
                if depth + 1 > MAX_DEPTH:
                    raise ValueError(f"refused: archives nested deeper than {MAX_DEPTH} ({info.filename})")
                walk(z.read(info), depth + 1)

try:
    with open("nested-10-deep.zip", "rb") as f:
        walk(f.read())
    print("ok")
except ValueError as e:
    print(e)
