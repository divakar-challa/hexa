# modest-zip-bomb.zip

A ~1 MB archive that expands to roughly 1 GB: ten entries of 100 MB of zeroes each. Deliberately modest - this is not a 42 KB / 4.5 PB bomb.

Page: https://hexaqa.com/file/archives/modest-zip-bomb-zip

```bash
curl -fsSL -o "modest-zip-bomb.zip" "https://files.hexaqa.com/archive/modest-zip-bomb.zip"
```

SHA-256: `bdf118f346d0f790e0a707d49b0c15a3ca048463c69f3621949b821e87a1915a`

## Python

Limit what extraction may produce, not the size of the upload. Headers can lie, so the loop counts the bytes actually decompressed as well as the declared sizes.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
refused: declares 1,048,576,000 bytes of content
```
