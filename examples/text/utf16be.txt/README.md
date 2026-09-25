# utf16be.txt

UTF-16 big-endian with BOM.

Page: https://hexaqa.com/file/documents/utf16be-txt

```bash
curl -fsSL -o "utf16be.txt" "https://files.hexaqa.com/text/utf16be.txt"
```

SHA-256: `f90d1333c7efc583acff83947170dba1e663066c672dd21ae0445edfcd3216d8`

## Python

Let a byte order mark decide the encoding when there is one, and otherwise insist on UTF-8. Guessing silently is how text turns into mojibake.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
utf-16-be with BOM 'The quick brown fox jumps over the lazy '
```

## Node.js

TextDecoder with fatal: true throws on invalid bytes instead of inserting replacement characters.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
utf-16be with BOM "The quick brown fox jumps over the lazy "
```
