# sql-injection-payloads.txt

Newline-delimited SQL injection strings for input-validation fuzzing. Includes tautologies, comment terminators, union probes and stacked-query syntax.

Page: https://hexaqa.com/file/security-and-validation/sql-injection-payloads-txt

```bash
curl -fsSL -o "sql-injection-payloads.txt" "https://flagged.hexaqa.com/security/sql-injection-payloads.txt"
```

SHA-256: `520b4965c786607d39fcfa27a840d0e6e99c7074e0703dccbcb0537ae316e0d3`

## Python

Pass user input as a parameter, never by building the SQL string. Every payload is then stored as plain text, and the DROP TABLE line drops nothing.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
10 payloads stored verbatim: True
tables: ['users']
```
