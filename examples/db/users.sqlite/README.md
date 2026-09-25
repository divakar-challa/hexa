# users.sqlite

A genuinely valid SQLite 3 database with one table (users) and 10 rows, written byte-by-byte from source so the file is reproducible.

Page: https://hexaqa.com/file/databases/users-sqlite

```bash
curl -fsSL -o "users.sqlite" "https://files.hexaqa.com/db/users.sqlite"
```

SHA-256: `876aa8e4bd7df3ec7f2f9b27d5738b618ed4bda5436cd88f34721edeaa203cf6`

## Python

A truncated database usually opens and queries without any error: SQLite reads the missing bytes as zeros, so this file returns ten rows of (0, None, None, None). Run the integrity check before importing anything from an uploaded database.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
integrity: ok
```
