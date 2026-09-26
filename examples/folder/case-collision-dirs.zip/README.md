# case-collision-dirs.zip

Two sibling directories whose names differ only in case, each holding a different file.

Page: https://hexaqa.com/file/folders-and-paths/case-collision-dirs-zip

```bash
curl -fsSL -o "case-collision-dirs.zip" "https://files.hexaqa.com/folder/case-collision-dirs.zip"
```

SHA-256: `13822c10204f1f63c8e33ef43df20210725cefbca65754e8fe36c0bab0e9141e`

## Python

Check an archive's paths before extracting it on another system. Windows reserves device names, drops trailing dots and spaces, and treats \ as a separator; Windows and macOS compare names without case, so two folders that differ only in case merge. Use orig_filename: on Windows, zipfile quietly turns backslashes into slashes.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
4 entries: 1 portability problem
  'Docs' and 'docs': the same path on Windows and macOS
```
