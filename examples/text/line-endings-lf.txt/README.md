# line-endings-lf.txt

20 lines terminated with Unix LF (\n). Byte-for-byte content twin of the CRLF file.

Page: https://hexaqa.com/file/documents/line-endings-lf-txt

```bash
curl -fsSL -o "line-endings-lf.txt" "https://files.hexaqa.com/text/line-endings-lf.txt"
```

SHA-256: `a6ef6400340b1a434b5d8eb8527e5ee71cf2eefff19135dab9f2b726c390df07`

## Python

Read the bytes, not text mode, so the line endings survive to be counted. Invisible format characters (category Cf: zero-width spaces, direction overrides, the BOM) are the ones that make two identical-looking strings compare unequal.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
line endings: 0 CRLF, 20 LF, 0 bare CR
ends with a newline
longest line: 52 characters
invisible characters: none
```
