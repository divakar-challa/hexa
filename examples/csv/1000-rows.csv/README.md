# 1000-rows.csv

A clean 1,000-row CSV with a header and five typed columns: id, name, email, amount and active.

Page: https://hexaqa.com/file/structured-data/1000-rows-csv

```bash
curl -fsSL -o "1000-rows.csv" "https://files.hexaqa.com/csv/1000-rows.csv"
```

SHA-256: `4204cc7b7f08b2e072c1af0de342f55cce111c521174bdad1ff4f918c869a69a`

## Python

Sniff the dialect from a sample, then stream the rows and compare each with the header. The csv module handles quoted commas and newlines inside fields, which is exactly what a split(',') gets wrong. line_num is the physical line, so it stays right when a field spans lines.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
delimiter ',', 5 columns, 1,000 data rows
  every row matches the header
```
