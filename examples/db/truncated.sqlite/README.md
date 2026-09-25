# truncated.sqlite

The same database cut off in the middle of the second page, so the header still looks correct but the data pages are incomplete.

Page: https://hexaqa.com/file/databases/truncated-sqlite

```bash
curl -fsSL -o "truncated.sqlite" "https://files.hexaqa.com/db/truncated.sqlite"
```

SHA-256: `1b6fd338a1fc3e8d9b112f64a908fe6d83b2c951696efc5ab353e1c0e8215fd4`

## Python

A truncated database usually opens and queries without any error: SQLite reads the missing bytes as zeros, so this file returns ten rows of (0, None, None, None). Run the integrity check before importing anything from an uploaded database.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
rejected: *** in database main *** / Tree 2 page 2 cell 8: Rowid 0 out of order
```
