SIGNATURES = {
    b"\x89PNG\r\n\x1a\n": "png", b"\xff\xd8\xff": "jpg", b"GIF8": "gif",
    b"%PDF-": "pdf", b"PK\x03\x04": "zip", b"MZ": "exe", b"\x7fELF": "elf",
}

def sniff(path):
    with open(path, "rb") as f:
        head = f.read(16)
    return next((ext for sig, ext in SIGNATURES.items() if head.startswith(sig)), None)

name = "fake-jpeg-is-executable.jpg"
actual = sniff(name)
claimed = name.rsplit(".", 1)[1].lower() if "." in name else None
claimed = {"jpeg": "jpg", "jpe": "jpg"}.get(claimed, claimed)
verdict = "ok" if actual == claimed else "MISMATCH: reject it"
print(f"name says {claimed or 'nothing'}, bytes say {actual or 'unknown'}: {verdict}")
