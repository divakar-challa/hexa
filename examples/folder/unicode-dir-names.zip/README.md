# unicode-dir-names.zip

Directory names in Japanese, Cyrillic and Greek, one made of emoji, and the same accented name in both Unicode normalization forms.

Page: https://hexaqa.com/file/folders-and-paths/unicode-dir-names-zip

```bash
curl -fsSL -o "unicode-dir-names.zip" "https://files.hexaqa.com/folder/unicode-dir-names.zip"
```

SHA-256: `451a050f856e348efa890ef540dcc4a493bb6b6a1af3a8f304ce39e46a012de1`

## Python

Check an archive's paths before extracting it on another system. Windows reserves device names, drops trailing dots and spaces, and treats \ as a separator; Windows and macOS compare names without case, so two folders that differ only in case merge. Use orig_filename: on Windows, zipfile quietly turns backslashes into slashes.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
12 entries: 1 portability problem
  'cafe\u0301-nfd': not NFC-normalised, so it may not match the same name typed elsewhere
```
