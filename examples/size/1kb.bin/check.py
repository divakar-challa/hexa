import hashlib

with open("1kb.bin", "rb") as f:
    print(hashlib.file_digest(f, "sha256").hexdigest())
