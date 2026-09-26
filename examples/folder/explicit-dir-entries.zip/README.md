# explicit-dir-entries.zip

An archive that declares its directories explicitly, as zero-length entries whose names end in a slash, alongside the files inside them.

Page: https://hexaqa.com/file/folders-and-paths/explicit-dir-entries-zip

```bash
curl -fsSL -o "explicit-dir-entries.zip" "https://files.hexaqa.com/folder/explicit-dir-entries.zip"
```

SHA-256: `6a760c7019a8c82678b7ce9c0f162968c0bcecf21023047ff336e452e6b5e3a0`

## Python

Check an archive's paths before extracting it on another system. Windows reserves device names, drops trailing dots and spaces, and treats \ as a separator; Windows and macOS compare names without case, so two folders that differ only in case merge. Use orig_filename: on Windows, zipfile quietly turns backslashes into slashes.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
7 entries: portable
```
