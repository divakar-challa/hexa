# schema.sql

A DDL and DML script with constraints, an index, a view, a transaction and dollar-free string literals.

Page: https://hexaqa.com/file/source-code/schema-sql

```bash
curl -fsSL -o "schema.sql" "https://files.hexaqa.com/code/schema.sql"
```

SHA-256: `412fbe6c0646cda5a0829b7672578ab400a98d1e2a9d166a43a3d1492ac16593`

## Python

Splitting a script on every semicolon breaks on semicolons inside strings, comments and triggers. sqlite3.complete_statement knows the grammar, so feed it lines until it says a statement is complete.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
8 statements, all executed
index idx_users_email, table orders, table users, view order_totals
```
