import posixpath
from urllib.parse import unquote

def safe_relative(user_path):
    p = user_path
    try:
        for _ in range(3):
            p = unquote(p, errors="strict")
    except UnicodeDecodeError:
        raise ValueError("invalid UTF-8 once decoded") from None
    p = p.replace("\\", "/")
    if "\0" in p:
        raise ValueError("contains a NUL byte")
    if p.startswith("/") or ":" in p:
        raise ValueError("absolute, drive or URL path")
    p = posixpath.normpath(p)
    if p == ".." or p.startswith("../"):
        raise ValueError("climbs out of the folder")
    if any(seg.endswith((".", " ")) for seg in p.split("/")):
        raise ValueError("has a segment Windows would rewrite")
    return p

with open("path-traversal-payloads.txt", encoding="utf-8") as f:
    payloads = [line.strip() for line in f if line.strip()]
for p in payloads:
    try:
        print("allowed:", safe_relative(p))
    except ValueError as e:
        print(f"blocked {p!r}: {e}")
