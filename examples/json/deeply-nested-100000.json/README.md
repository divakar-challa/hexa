# deeply-nested-100000.json

A single value wrapped in 100,000 levels of nested arrays. Only ~200 KB on disk.

Page: https://hexaqa.com/file/structured-data/deeply-nested-100000-json

```bash
curl -fsSL -o "deeply-nested-100000.json" "https://files.hexaqa.com/json/deeply-nested-100000.json"
```

SHA-256: `8d7bd09c0573c0c4d854b55795e2c3f1a781c2d4f2901de332a5cb8bab350e42`

## Python

Deep nesting exhausts the parser's recursion limit. Catch it, and reject the input as too deep rather than crashing the worker.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
rejected: nested too deeply to parse
```

## Node.js

Check whether your runtime copes before trusting it with uploads: a crash here takes the whole process down.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
parsed
```
