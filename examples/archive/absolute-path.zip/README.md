# absolute-path.zip

Archive whose entry name is an absolute path (/tmp/qa-absolute.txt).

Page: https://hexaqa.com/file/archives/absolute-path-zip

```bash
curl -fsSL -o "absolute-path.zip" "https://files.hexaqa.com/archive/absolute-path.zip"
```

SHA-256: `9ea841f8c6258f058270bae465ccc538dc3d85d445dae479db0df4d2c6e6cba3`

## Python

Check every entry before extracting anything. Python's extractall already strips "../" and leading slashes, but silently, so the file lands somewhere the archive did not say. Rejecting makes the attack visible and matches what other languages need.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
blocked: '/tmp/qa-absolute.txt' escapes the target folder
```
