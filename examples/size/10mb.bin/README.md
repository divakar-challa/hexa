# 10mb.bin

Exactly 10,485,760 bytes of deterministic incompressible pseudo-random data.

Page: https://hexaqa.com/file/size-ladder/10mb-bin

```bash
curl -fsSL -o "10mb.bin" "https://files.hexaqa.com/size/10mb.bin"
```

SHA-256: `7d14befba4830a4cf23b62671cb1b6d8fc4876a72018266dff9f267c4316510c`

## Python

Verify the download against the SHA-256 published on this page. file_digest (Python 3.11+) reads in chunks, so a 250 MB file does not need 250 MB of memory.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
7d14befba4830a4cf23b62671cb1b6d8fc4876a72018266dff9f267c4316510c
```

## Node.js

The same in Node, streaming the file through the hash.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
7d14befba4830a4cf23b62671cb1b6d8fc4876a72018266dff9f267c4316510c
```
