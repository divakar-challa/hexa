# 100kb.bin

Exactly 102,400 bytes of deterministic incompressible pseudo-random data.

Page: https://hexaqa.com/file/size-ladder/100kb-bin

```bash
curl -fsSL -o "100kb.bin" "https://files.hexaqa.com/size/100kb.bin"
```

SHA-256: `ab19e27a5f390f15fab446794cdfd7db9d3dfe0630b098d3284094907048923d`

## Python

Verify the download against the SHA-256 published on this page. file_digest (Python 3.11+) reads in chunks, so a 250 MB file does not need 250 MB of memory.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ab19e27a5f390f15fab446794cdfd7db9d3dfe0630b098d3284094907048923d
```

## Node.js

The same in Node, streaming the file through the hash.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ab19e27a5f390f15fab446794cdfd7db9d3dfe0630b098d3284094907048923d
```
