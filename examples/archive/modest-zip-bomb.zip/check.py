import zipfile

MAX_TOTAL = 100 * 1024 * 1024   # refuse to produce more than 100 MB
MAX_RATIO = 100                 # or any entry that expands more than 100x

with zipfile.ZipFile("modest-zip-bomb.zip") as z:
    declared = sum(i.file_size for i in z.infolist())
    if declared > MAX_TOTAL:
        raise SystemExit(f"refused: declares {declared:,} bytes of content")
    written = 0
    for info in z.infolist():
        if info.compress_size and info.file_size / info.compress_size > MAX_RATIO:
            raise SystemExit(f"refused: {info.filename} expands {info.file_size // info.compress_size}x")
        with z.open(info) as src:
            while chunk := src.read(65536):
                written += len(chunk)
                if written > MAX_TOTAL:
                    raise SystemExit("refused: output passed the limit")
    print("ok to extract")
