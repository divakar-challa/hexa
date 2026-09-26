# zero-width-and-rtl.txt

Text containing zero-width spaces, zero-width joiners, and bidirectional override characters (U+202E).

Page: https://hexaqa.com/file/documents/zero-width-and-rtl-txt

```bash
curl -fsSL -o "zero-width-and-rtl.txt" "https://files.hexaqa.com/text/zero-width-and-rtl.txt"
```

SHA-256: `655072c13266ced43394f7f4f66a7e59d5047ae53e2f17447b2a9bafe8a83e30`

## Python

Read the bytes, not text mode, so the line endings survive to be counted. Invisible format characters (category Cf: zero-width spaces, direction overrides, the BOM) are the ones that make two identical-looking strings compare unequal.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
line endings: 0 CRLF, 4 LF, 0 bare CR
ends with a newline
longest line: 35 characters
invisible characters: U+200B ZERO WIDTH SPACE, U+200D ZERO WIDTH JOINER, U+202C POP DIRECTIONAL FORMATTING, U+202E RIGHT-TO-LEFT OVERRIDE
```
