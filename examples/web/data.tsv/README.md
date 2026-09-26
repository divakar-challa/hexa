# data.tsv

Tab-separated values with a header row and a field that itself contains spaces.

Page: https://hexaqa.com/file/web-and-text-formats/data-tsv

```bash
curl -fsSL -o "data.tsv" "https://files.hexaqa.com/web/data.tsv"
```

SHA-256: `4f207e63c97aca7063ba37237cf4c32ced1d0fc46a2a06120e70d001eee7ed11`

## Python

Sniff the dialect from a sample, then stream the rows and compare each with the header. The csv module handles quoted commas and newlines inside fields, which is exactly what a split(',') gets wrong. line_num is the physical line, so it stays right when a field spans lines.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
delimiter '\t', 3 columns, 3 data rows
  every row matches the header
```
