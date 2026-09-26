# line-endings-crlf.txt

20 lines terminated with Windows CRLF (\r\n).

Page: https://hexaqa.com/file/documents/line-endings-crlf-txt

```bash
curl -fsSL -o "line-endings-crlf.txt" "https://files.hexaqa.com/text/line-endings-crlf.txt"
```

SHA-256: `f1d13bf3e400ae9865148d88e8cbecbc553c5c78e76e833cf3b8e81d65280115`

## Python

Read the bytes, not text mode, so the line endings survive to be counted. Invisible format characters (category Cf: zero-width spaces, direction overrides, the BOM) are the ones that make two identical-looking strings compare unequal.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
line endings: 20 CRLF, 0 LF, 0 bare CR
ends with a newline
longest line: 52 characters
invisible characters: none
```
