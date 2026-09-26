# empty-directory.zip

An archive containing a directory with nothing in it, which can only be represented by an explicit directory entry.

Page: https://hexaqa.com/file/folders-and-paths/empty-directory-zip

```bash
curl -fsSL -o "empty-directory.zip" "https://files.hexaqa.com/folder/empty-directory.zip"
```

SHA-256: `0258bda2b3665effb82bee3ab210169fa0cec1a8399bc61980bf4600b3e7baef`

## Python

Check an archive's paths before extracting it on another system. Windows reserves device names, drops trailing dots and spaces, and treats \ as a separator; Windows and macOS compare names without case, so two folders that differ only in case merge. Use orig_filename: on Windows, zipfile quietly turns backslashes into slashes.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
3 entries: portable
```
