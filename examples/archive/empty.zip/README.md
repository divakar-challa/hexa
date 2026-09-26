# empty.zip

A structurally valid ZIP containing zero entries (22-byte end-of-central-directory only).

Page: https://hexaqa.com/file/archives/empty-zip

```bash
curl -fsSL -o "empty.zip" "https://files.hexaqa.com/archive/empty.zip"
```

SHA-256: `8739c76e681f900923b900c9df0ef75cf421d39cabb54650c4b9ad19b6a76d85`

## Python

Check an archive's paths before extracting it on another system. Windows reserves device names, drops trailing dots and spaces, and treats \ as a separator; Windows and macOS compare names without case, so two folders that differ only in case merge. Use orig_filename: on Windows, zipfile quietly turns backslashes into slashes.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
0 entries: portable
```
