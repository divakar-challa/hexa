# latin1.txt

ISO-8859-1 / Latin-1 encoded text with accented characters.

Page: https://hexaqa.com/file/documents/latin1-txt

```bash
curl -fsSL -o "latin1.txt" "https://files.hexaqa.com/text/latin1.txt"
```

SHA-256: `f55e2be006165fb601823726e6bd0764b442a5dfbc348b7d3a797f4a97fc5d41`

## Python

Let a byte order mark decide the encoding when there is one, and otherwise insist on UTF-8. Guessing silently is how text turns into mojibake.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
not UTF-8: invalid continuation byte at byte 38
```

## Node.js

TextDecoder with fatal: true throws on invalid bytes instead of inserting replacement characters.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
not valid utf-8: The encoded data was not valid for encoding utf-8
```
