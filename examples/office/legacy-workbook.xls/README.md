# legacy-workbook.xls

A real legacy Excel 97-2003 workbook: BIFF8 records inside an OLE2 compound file, with two sheets, numbers, and text held in a shared string table.

Page: https://hexaqa.com/file/office-documents/legacy-workbook-xls

```bash
curl -fsSL -o "legacy-workbook.xls" "https://files.hexaqa.com/office/legacy-workbook.xls"
```

SHA-256: `e4ddabb0ba6f10493b909d5f3be09e70c94f622d6b97c9d12664c6527f33294e`

## Python

Check for macros before accepting or opening an Office upload. Modern files are ZIPs: VBA lives in vbaProject.bin (Microsoft) or a Basic folder (OpenDocument). Legacy .xls/.doc files are OLE2 containers that need a dedicated parser, such as oletools, to see inside.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
legacy OLE2 file (.xls, .doc, .ppt, .msg): may carry VBA; inspect it with an OLE parser
```
