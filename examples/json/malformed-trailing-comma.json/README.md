# malformed-trailing-comma.json

JSON with a trailing comma before the closing brace - invalid per RFC 8259.

Page: https://hexaqa.com/file/structured-data/malformed-trailing-comma-json

```bash
curl -fsSL -o "malformed-trailing-comma.json" "https://files.hexaqa.com/json/malformed-trailing-comma.json"
```

SHA-256: `d66c56297d3e2d3c7854ff366bccce90d007c64d890f21388bf0fc266a4219b9`

## Python

Report where the error is. A line and column turn "invalid file" into something a user can fix.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
invalid JSON at line 3, column 9: Illegal trailing comma before end of object
```

## Node.js

The error message includes the position in recent Node versions.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
invalid JSON: Expected double-quoted property name in JSON at position 22 (line 4 column 1)
```
