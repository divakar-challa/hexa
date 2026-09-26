import hashlib

with open("5mb.bin", "rb") as f:
    print(hashlib.file_digest(f, "sha256").hexdigest())
