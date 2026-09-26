# unicode-entry-names.zip

Entries named in Japanese, Arabic, Russian and emoji, with the UTF-8 flag (bit 11) set correctly.

Page: https://hexaqa.com/file/archives/unicode-entry-names-zip

```bash
curl -fsSL -o "unicode-entry-names.zip" "https://files.hexaqa.com/archive/unicode-entry-names.zip"
```

SHA-256: `905894694aafd53e946ca6328a8765cbf53f36ffc2c473f394ded37c9f0fad4f`

## Python

Check an archive's paths before extracting it on another system. Windows reserves device names, drops trailing dots and spaces, and treats \ as a separator; Windows and macOS compare names without case, so two folders that differ only in case merge. Use orig_filename: on Windows, zipfile quietly turns backslashes into slashes.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
4 entries: portable
```
