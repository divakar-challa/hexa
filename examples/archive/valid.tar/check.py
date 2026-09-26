import tarfile

with tarfile.open("valid.tar") as tar:  # detects gzip, bzip2 and xz by itself
    try:
        tar.extractall("out", filter="data")
        print("extracted:", ", ".join(m.name for m in tar.getmembers()))
    except tarfile.FilterError as e:
        print("blocked:", e)
