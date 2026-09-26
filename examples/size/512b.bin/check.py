import hashlib

with open("512b.bin", "rb") as f:
    print(hashlib.file_digest(f, "sha256").hexdigest())
