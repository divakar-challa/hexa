# valid.tar

A USTAR tar archive with three files, including one in a subdirectory.

Page: https://hexaqa.com/file/archives/valid-tar

```bash
curl -fsSL -o "valid.tar" "https://files.hexaqa.com/archive/valid.tar"
```

SHA-256: `10423077ca0e6bd4595013c517de17a831309c3c0fa9c79bb3c2f01d46e2ee7c`

## Python

Extract with the 'data' filter (Python 3.12+, and backported to security releases of 3.8 to 3.11). It refuses absolute paths, '..', links that point outside the folder and device files. Python 3.14 makes it the default, but passing it keeps older versions safe.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
extracted: readme.txt, data/numbers.csv, data/notes.txt
```
