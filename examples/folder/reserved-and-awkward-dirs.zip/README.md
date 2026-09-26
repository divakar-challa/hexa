# reserved-and-awkward-dirs.zip

Directories named after Windows reserved devices, plus one ending in a dot and one ending in a space.

Page: https://hexaqa.com/file/folders-and-paths/reserved-and-awkward-dirs-zip

```bash
curl -fsSL -o "reserved-and-awkward-dirs.zip" "https://files.hexaqa.com/folder/reserved-and-awkward-dirs.zip"
```

SHA-256: `7fab653ffe32d53a5ec3921dcc7c589e6e0a942e8f2de92cf3c7549483effb65`

## Python

Check an archive's paths before extracting it on another system. Windows reserves device names, drops trailing dots and spaces, and treats \ as a separator; Windows and macOS compare names without case, so two folders that differ only in case merge. Use orig_filename: on Windows, zipfile quietly turns backslashes into slashes.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
10 entries: 4 portability problems
  'CON': CON is a reserved device name on Windows
  'NUL': NUL is a reserved device name on Windows
  'trailing-dot.': ends in a dot or space, which Windows drops
  'trailing-space ': ends in a dot or space, which Windows drops
```
