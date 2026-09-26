# macro-enabled.xlsm

Macro-enabled workbook structure with an inert VBA project placeholder (no executable code).

Page: https://hexaqa.com/file/office-documents/macro-enabled-xlsm

```bash
curl -fsSL -o "macro-enabled.xlsm" "https://files.hexaqa.com/office/macro-enabled.xlsm"
```

SHA-256: `f6ec219c93f337cc21e5cca02e3cd2a6928811c9a61e824b80c972306380c8b0`

## Python

Check for macros before accepting or opening an Office upload. Modern files are ZIPs: VBA lives in vbaProject.bin (Microsoft) or a Basic folder (OpenDocument). Legacy .xls/.doc files are OLE2 containers that need a dedicated parser, such as oletools, to see inside.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
contains macros: xl/vbaProject.bin
```
