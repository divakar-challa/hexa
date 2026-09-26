# 1mb.bin

Exactly 1,048,576 bytes of deterministic incompressible pseudo-random data.

Page: https://hexaqa.com/file/size-ladder/1mb-bin

```bash
curl -fsSL -o "1mb.bin" "https://files.hexaqa.com/size/1mb.bin"
```

SHA-256: `30b93b424b6eaae04620a6bafe1f7eb6b2aa62fb1455210bd5be45730fa777ff`

## Python

Verify the download against the SHA-256 published on this page. file_digest (Python 3.11+) reads in chunks, so a 250 MB file does not need 250 MB of memory.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
30b93b424b6eaae04620a6bafe1f7eb6b2aa62fb1455210bd5be45730fa777ff
```

## Node.js

The same in Node, streaming the file through the hash.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
30b93b424b6eaae04620a6bafe1f7eb6b2aa62fb1455210bd5be45730fa777ff
```
