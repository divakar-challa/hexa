# utf16le.txt

UTF-16 little-endian with BOM, which is what Windows PowerShell and Notepad historically emit.

Page: https://hexaqa.com/file/documents/utf16le-txt

```bash
curl -fsSL -o "utf16le.txt" "https://files.hexaqa.com/text/utf16le.txt"
```

SHA-256: `4496b6b074dfaf6b170cfce06dae05970fa0787985232918b702d85381fdf793`

## Python

Let a byte order mark decide the encoding when there is one, and otherwise insist on UTF-8. Guessing silently is how text turns into mojibake.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
utf-16-le with BOM 'The quick brown fox jumps over the lazy '
```

## Node.js

TextDecoder with fatal: true throws on invalid bytes instead of inserting replacement characters.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
utf-16le with BOM "The quick brown fox jumps over the lazy "
```
