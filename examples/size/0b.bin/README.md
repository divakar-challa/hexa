# 0b.bin

Empty file, exactly 0 bytes.

Page: https://hexaqa.com/file/size-ladder/0b-bin

```bash
curl -fsSL -o "0b.bin" "https://files.hexaqa.com/size/0b.bin"
```

SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

## Python

Verify the download against the SHA-256 published on this page. file_digest (Python 3.11+) reads in chunks, so a 250 MB file does not need 250 MB of memory.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

## Node.js

The same in Node, streaming the file through the hash.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```
