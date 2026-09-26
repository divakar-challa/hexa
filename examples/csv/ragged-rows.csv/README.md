# ragged-rows.csv

Rows with too few and too many columns relative to the header.

Page: https://hexaqa.com/file/structured-data/ragged-rows-csv

```bash
curl -fsSL -o "ragged-rows.csv" "https://files.hexaqa.com/csv/ragged-rows.csv"
```

SHA-256: `2292b423c8910544ee2df0a720e17cfaebb15f10270c0dd64e39bfc411635cb4`

## Python

Sniff the dialect from a sample, then stream the rows and compare each with the header. The csv module handles quoted commas and newlines inside fields, which is exactly what a split(',') gets wrong. line_num is the physical line, so it stays right when a field spans lines.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
delimiter ',', 3 columns, 5 data rows
  line 3: 2 fields, expected 3
  line 4: 5 fields, expected 3
  line 6: 1 field, expected 3
```
