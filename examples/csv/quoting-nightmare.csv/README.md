# quoting-nightmare.csv

Every RFC 4180 quoting edge case in one file: embedded commas, embedded newlines inside quoted fields, escaped double quotes, leading and trailing whitespace, and empty fields.

Page: https://hexaqa.com/file/structured-data/quoting-nightmare-csv

```bash
curl -fsSL -o "quoting-nightmare.csv" "https://files.hexaqa.com/csv/quoting-nightmare.csv"
```

SHA-256: `557f8d813aa8cec4212f6bcb3e6a11cfdeadc48fab3d825f2e9a7fb26bd36d5e`

## Python

Sniff the dialect from a sample, then stream the rows and compare each with the header. The csv module handles quoted commas and newlines inside fields, which is exactly what a split(',') gets wrong. line_num is the physical line, so it stays right when a field spans lines.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
delimiter ',', 4 columns, 7 data rows
  every row matches the header
```
