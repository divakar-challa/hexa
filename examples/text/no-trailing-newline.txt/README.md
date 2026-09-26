# no-trailing-newline.txt

Three lines where the final line has no terminating newline.

Page: https://hexaqa.com/file/documents/no-trailing-newline-txt

```bash
curl -fsSL -o "no-trailing-newline.txt" "https://files.hexaqa.com/text/no-trailing-newline.txt"
```

SHA-256: `3ed32da374e230c6228e132c8c334191759286fee4813e1ed4eba4d9b9366ea7`

## Python

Read the bytes, not text mode, so the line endings survive to be counted. Invisible format characters (category Cf: zero-width spaces, direction overrides, the BOM) are the ones that make two identical-looking strings compare unequal.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
line endings: 0 CRLF, 2 LF, 0 bare CR
no newline at the end of the file
longest line: 7 characters
invisible characters: none
```
