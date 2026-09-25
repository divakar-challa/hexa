# valid-flat.zip

Three deflated text files at the archive root, no directories.

Page: https://hexaqa.com/file/archives/valid-flat-zip

```bash
curl -fsSL -o "valid-flat.zip" "https://files.hexaqa.com/archive/valid-flat.zip"
```

SHA-256: `a8e3fb09b187d71285f1b908f39f1734e43e8143d182505306af44b442852c32`

## Python

Check every entry before extracting anything. Python's extractall already strips "../" and leading slashes, but silently, so the file lands somewhere the archive did not say. Rejecting makes the attack visible and matches what other languages need.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
extracted
```
