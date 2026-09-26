# 5mb.bin

Exactly 5,242,880 bytes of deterministic incompressible pseudo-random data.

Page: https://hexaqa.com/file/size-ladder/5mb-bin

```bash
curl -fsSL -o "5mb.bin" "https://files.hexaqa.com/size/5mb.bin"
```

SHA-256: `e9a81188e0425fa657c93cec88b47707f5c2c415cd2168f8cdf764df9477dc51`

## Python

Verify the download against the SHA-256 published on this page. file_digest (Python 3.11+) reads in chunks, so a 250 MB file does not need 250 MB of memory.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
e9a81188e0425fa657c93cec88b47707f5c2c415cd2168f8cdf764df9477dc51
```

## Node.js

The same in Node, streaming the file through the hash.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
e9a81188e0425fa657c93cec88b47707f5c2c415cd2168f8cdf764df9477dc51
```
