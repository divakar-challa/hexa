# 512b.bin

Exactly 512 bytes of deterministic incompressible pseudo-random data.

Page: https://hexaqa.com/file/size-ladder/512b-bin

```bash
curl -fsSL -o "512b.bin" "https://files.hexaqa.com/size/512b.bin"
```

SHA-256: `e6fa777e57935c99990559e1afcc155fd9a1cf6669cbf1ec3ddd9b8ef40ee7a1`

## Python

Verify the download against the SHA-256 published on this page. file_digest (Python 3.11+) reads in chunks, so a 250 MB file does not need 250 MB of memory.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
e6fa777e57935c99990559e1afcc155fd9a1cf6669cbf1ec3ddd9b8ef40ee7a1
```

## Node.js

The same in Node, streaming the file through the hash.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
e6fa777e57935c99990559e1afcc155fd9a1cf6669cbf1ec3ddd9b8ef40ee7a1
```
