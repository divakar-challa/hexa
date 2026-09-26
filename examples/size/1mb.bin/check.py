import hashlib

with open("1mb.bin", "rb") as f:
    print(hashlib.file_digest(f, "sha256").hexdigest())
