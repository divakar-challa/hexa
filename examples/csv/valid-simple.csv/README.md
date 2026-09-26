# valid-simple.csv

Header row plus 100 rows of clean, unquoted ASCII data.

Page: https://hexaqa.com/file/structured-data/valid-simple-csv

```bash
curl -fsSL -o "valid-simple.csv" "https://files.hexaqa.com/csv/valid-simple.csv"
```

SHA-256: `dfb9d357c93e725493c48f9c0e8cca6b92bcaf0826bcdb493e4ffe3e7bcc1f91`

## Python

Sniff the dialect from a sample, then stream the rows and compare each with the header. The csv module handles quoted commas and newlines inside fields, which is exactly what a split(',') gets wrong. line_num is the physical line, so it stays right when a field spans lines.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
delimiter ',', 5 columns, 100 data rows
  every row matches the header
```
