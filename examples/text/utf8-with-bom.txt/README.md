# utf8-with-bom.txt

UTF-8 with a leading BOM (EF BB BF).

Page: https://hexaqa.com/file/documents/utf8-with-bom-txt

```bash
curl -fsSL -o "utf8-with-bom.txt" "https://files.hexaqa.com/text/utf8-with-bom.txt"
```

SHA-256: `ac0d490b3c84d5f8e830a7860f3f9c96846a92021d9b124a97bef0cfd021391d`

## Python

Let a byte order mark decide the encoding when there is one, and otherwise insist on UTF-8. Guessing silently is how text turns into mojibake.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
utf-8 with BOM 'The quick brown fox jumps over the lazy '
```

## Node.js

TextDecoder with fatal: true throws on invalid bytes instead of inserting replacement characters.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
utf-8 with BOM "The quick brown fox jumps over the lazy "
```
