import os, zipfile

def safe_extract(archive, dest):
    dest = os.path.realpath(dest)
    with zipfile.ZipFile(archive) as z:
        for info in z.infolist():
            target = os.path.realpath(os.path.join(dest, info.filename))
            if os.path.commonpath([dest, target]) != dest:
                raise ValueError(f"blocked: {info.filename!r} escapes the target folder")
        z.extractall(dest)

try:
    safe_extract("zip-slip-traversal.zip", "out")
    print("extracted")
except ValueError as e:
    print(e)
