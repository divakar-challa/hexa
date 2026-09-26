# utf8-no-bom.txt

UTF-8 without a byte-order mark. The correct modern default.

Page: https://hexaqa.com/file/documents/utf8-no-bom-txt

```bash
curl -fsSL -o "utf8-no-bom.txt" "https://files.hexaqa.com/text/utf8-no-bom.txt"
```

SHA-256: `54838db0165f05296350688ed04e2304c616001ff8e1446a54ab24a10e8af99e`

## Python

Read the bytes, not text mode, so the line endings survive to be counted. Invisible format characters (category Cf: zero-width spaces, direction overrides, the BOM) are the ones that make two identical-looking strings compare unequal.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
line endings: 0 CRLF, 2 LF, 0 bare CR
ends with a newline
longest line: 44 characters
invisible characters: none
```
