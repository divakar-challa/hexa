# no-extension

A genuinely valid PNG with no file extension at all.

Page: https://hexaqa.com/file/images/no-extension

```bash
curl -fsSL -o "no-extension" "https://files.hexaqa.com/image/no-extension"
```

SHA-256: `c84d8425542305e68c674701ed5a8db2f4e6fe0045d8543be22ca3ddc0a88f40`

## Python

Identify the file by its first bytes and compare that with the name. Never trust the extension or the Content-Type the browser sent.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
name says nothing, bytes say png: MISMATCH: reject it
```
