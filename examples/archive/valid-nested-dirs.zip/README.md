# valid-nested-dirs.zip

Archive with entries five directory levels deep.

Page: https://hexaqa.com/file/archives/valid-nested-dirs-zip

```bash
curl -fsSL -o "valid-nested-dirs.zip" "https://files.hexaqa.com/archive/valid-nested-dirs.zip"
```

SHA-256: `45eb1c114ac57aae4c176790023d361faf483bf8dc266e0f4c31480f696dacd4`

## Python

Check an archive's paths before extracting it on another system. Windows reserves device names, drops trailing dots and spaces, and treats \ as a separator; Windows and macOS compare names without case, so two folders that differ only in case merge. Use orig_filename: on Windows, zipfile quietly turns backslashes into slashes.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
3 entries: portable
```
