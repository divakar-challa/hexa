# nested-10-deep.zip

A ZIP containing a ZIP containing a ZIP, ten levels down, with a text file at the centre.

Page: https://hexaqa.com/file/archives/nested-10-deep-zip

```bash
curl -fsSL -o "nested-10-deep.zip" "https://files.hexaqa.com/archive/nested-10-deep.zip"
```

SHA-256: `0a16d5d585e29772e170d57f939b3211f2ad5649ce876afc2a0d0d9d42752ab4`

## Python

Recursive extraction needs a depth limit as well as a size limit, or one small file becomes an unbounded amount of work.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
refused: archives nested deeper than 3 (level-4.zip)
```
