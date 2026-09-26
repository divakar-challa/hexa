# 1kb.bin

Exactly 1,024 bytes of deterministic incompressible pseudo-random data.

Page: https://hexaqa.com/file/size-ladder/1kb-bin

```bash
curl -fsSL -o "1kb.bin" "https://files.hexaqa.com/size/1kb.bin"
```

SHA-256: `36e805711b4ffe56b60eb0d2b3a426ad09ed11e06afaaa7b663a11887232d892`

## Python

Verify the download against the SHA-256 published on this page. file_digest (Python 3.11+) reads in chunks, so a 250 MB file does not need 250 MB of memory.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
36e805711b4ffe56b60eb0d2b3a426ad09ed11e06afaaa7b663a11887232d892
```

## Node.js

The same in Node, streaming the file through the hash.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
36e805711b4ffe56b60eb0d2b3a426ad09ed11e06afaaa7b663a11887232d892
```
