# zip-slip-traversal.zip

Archive containing an entry named ../../../../tmp/qa-zip-slip.txt. The payload is a harmless text marker, but the path escapes the extraction directory.

Page: https://hexaqa.com/file/archives/zip-slip-traversal-zip

```bash
curl -fsSL -o "zip-slip-traversal.zip" "https://files.hexaqa.com/archive/zip-slip-traversal.zip"
```

SHA-256: `bf5ee2334900a786100f6b030fa929e1a6101b1075f501ff8d7be41c0b38107e`

## Python

Check every entry before extracting anything. Python's extractall already strips "../" and leading slashes, but silently, so the file lands somewhere the archive did not say. Rejecting makes the attack visible and matches what other languages need.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
blocked: '../../../../tmp/qa-zip-slip.txt' escapes the target folder
```
