import hashlib

with open("10mb.bin", "rb") as f:
    print(hashlib.file_digest(f, "sha256").hexdigest())
