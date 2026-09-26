# very-long-single-line.txt

A single line of 1,000,000 characters with no newline anywhere in the file.

Page: https://hexaqa.com/file/documents/very-long-single-line-txt

```bash
curl -fsSL -o "very-long-single-line.txt" "https://files.hexaqa.com/text/very-long-single-line.txt"
```

SHA-256: `c51ef575b90527d834c783bc9a303383b421e84e7d885c225e2eaa3e59768754`

## Python

Read the bytes, not text mode, so the line endings survive to be counted. Invisible format characters (category Cf: zero-width spaces, direction overrides, the BOM) are the ones that make two identical-looking strings compare unequal.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
line endings: 0 CRLF, 0 LF, 0 bare CR
no newline at the end of the file
longest line: 1,024,000 characters
invisible characters: none
```
