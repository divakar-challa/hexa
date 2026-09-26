# 10kb.bin

Exactly 10,240 bytes of deterministic incompressible pseudo-random data.

Page: https://hexaqa.com/file/size-ladder/10kb-bin

```bash
curl -fsSL -o "10kb.bin" "https://files.hexaqa.com/size/10kb.bin"
```

SHA-256: `74b2360b9060b915eb045b412401001af82aa456dcc9c9552d6a94e2b0cee4b9`

## Python

Verify the download against the SHA-256 published on this page. file_digest (Python 3.11+) reads in chunks, so a 250 MB file does not need 250 MB of memory.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
74b2360b9060b915eb045b412401001af82aa456dcc9c9552d6a94e2b0cee4b9
```

## Node.js

The same in Node, streaming the file through the hash.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
74b2360b9060b915eb045b412401001af82aa456dcc9c9552d6a94e2b0cee4b9
```
