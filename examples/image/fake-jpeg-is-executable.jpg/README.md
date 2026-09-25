# fake-jpeg-is-executable.jpg

A file named .jpg whose magic bytes are the DOS/PE "MZ" signature. Contains no executable code - just the header and filler.

Page: https://hexaqa.com/file/images/fake-jpeg-is-executable-jpg

```bash
curl -fsSL -o "fake-jpeg-is-executable.jpg" "https://files.hexaqa.com/image/fake-jpeg-is-executable.jpg"
```

SHA-256: `4ba83fec93b79c99a1d2f2be5e10620d7ca634766d5a783a8d9a7a19c47d610f`

## Python

Identify the file by its first bytes and compare that with the name. Never trust the extension or the Content-Type the browser sent.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
name says jpg, bytes say exe: MISMATCH: reject it
```

## Node.js

The same check in Node, reading only the first 16 bytes.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
name says jpg, bytes say exe: MISMATCH: reject it
```
