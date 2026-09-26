# presentation.odp

A two-slide OpenDocument presentation built from source, with a title frame and a bullet list.

Page: https://hexaqa.com/file/office-documents/presentation-odp

```bash
curl -fsSL -o "presentation.odp" "https://files.hexaqa.com/office/presentation.odp"
```

SHA-256: `b43b1246da01efa0e6c7dd86ec3c2a1c6eb1da6c201ebc4f66f68923e293ba8e`

## Python

Check for macros before accepting or opening an Office upload. Modern files are ZIPs: VBA lives in vbaProject.bin (Microsoft) or a Basic folder (OpenDocument). Legacy .xls/.doc files are OLE2 containers that need a dedicated parser, such as oletools, to see inside.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
no macro parts among 3 entries
```
