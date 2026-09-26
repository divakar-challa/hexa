# spreadsheet.xlsx

Excel workbook with a header row, data rows, and a live SUM formula.

Page: https://hexaqa.com/file/office-documents/spreadsheet-xlsx

```bash
curl -fsSL -o "spreadsheet.xlsx" "https://files.hexaqa.com/office/spreadsheet.xlsx"
```

SHA-256: `ad3641fda07651acf26ca9bbaea3d2ad56358ae560768524b2d4d3b5b3310dae`

## Python

Check for macros before accepting or opening an Office upload. Modern files are ZIPs: VBA lives in vbaProject.bin (Microsoft) or a Basic folder (OpenDocument). Legacy .xls/.doc files are OLE2 containers that need a dedicated parser, such as oletools, to see inside.

```bash
python check-officeMacros.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
no macro parts among 5 entries
```

## Python

Text cells starting with =, +, - or @ are harmless inside Excel, but become live formulas when your app exports them to CSV. Scan the sheet XML directly: an .xlsx is a ZIP, and cell text is either inline or in the shared-strings table.

```bash
python check-xlsxFormula.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
B4: formula =SUM(B2:B3) (runs when the file is opened)
C4: formula =SUMPRODUCT(B2:B3,C2:C3) (runs when the file is opened)
no formula-like text
```
