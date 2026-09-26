# formula-injection.xlsx

Workbook whose cells contain =, +, - and @ prefixed strings and a HYPERLINK formula.

Page: https://hexaqa.com/file/office-documents/formula-injection-xlsx

```bash
curl -fsSL -o "formula-injection.xlsx" "https://files.hexaqa.com/office/formula-injection.xlsx"
```

SHA-256: `f3a7e7c4d1b67e339a5e918da7a81a3ac6bdb52f9581f63586774e1dcf8ed10b`

## Python

Text cells starting with =, +, - or @ are harmless inside Excel, but become live formulas when your app exports them to CSV. Scan the sheet XML directly: an .xlsx is a ZIP, and cell text is either inline or in the shared-strings table.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
B2: text '=1+1' turns into a formula when exported to CSV
B3: text '+1+1' turns into a formula when exported to CSV
B4: text '@SUM(1+1)' turns into a formula when exported to CSV
B5: formula =HYPERLINK("https://example.test","click") (runs when the file is opened)
3 text cells to neutralise before a CSV export
```
