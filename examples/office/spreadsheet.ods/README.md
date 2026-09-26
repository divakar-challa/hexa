# spreadsheet.ods

OpenDocument Spreadsheet with a small table and the stored-first mimetype entry.

Page: https://hexaqa.com/file/office-documents/spreadsheet-ods

```bash
curl -fsSL -o "spreadsheet.ods" "https://files.hexaqa.com/office/spreadsheet.ods"
```

SHA-256: `3ceb50ee098eec9e9d27179e972e375ed504bb9262c24b1ccb3b3c02038a0525`

## Python

Check for macros before accepting or opening an Office upload. Modern files are ZIPs: VBA lives in vbaProject.bin (Microsoft) or a Basic folder (OpenDocument). Legacy .xls/.doc files are OLE2 containers that need a dedicated parser, such as oletools, to see inside.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
no macro parts among 3 entries
```
