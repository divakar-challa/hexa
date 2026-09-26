# 1b.bin

Exactly 1 bytes of deterministic incompressible pseudo-random data.

Page: https://hexaqa.com/file/size-ladder/1b-bin

```bash
curl -fsSL -o "1b.bin" "https://files.hexaqa.com/size/1b.bin"
```

SHA-256: `dabd3aff769f07eb2965401eb029974ebba3407afd02b26ddb564ea5f8efae72`

## Python

Verify the download against the SHA-256 published on this page. file_digest (Python 3.11+) reads in chunks, so a 250 MB file does not need 250 MB of memory.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
dabd3aff769f07eb2965401eb029974ebba3407afd02b26ddb564ea5f8efae72
```

## Node.js

The same in Node, streaming the file through the hash.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
dabd3aff769f07eb2965401eb029974ebba3407afd02b26ddb564ea5f8efae72
```
