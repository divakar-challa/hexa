# document.odt

OpenDocument Text with the mandatory uncompressed "mimetype" entry stored first.

Page: https://hexaqa.com/file/office-documents/document-odt

```bash
curl -fsSL -o "document.odt" "https://files.hexaqa.com/office/document.odt"
```

SHA-256: `b59417f44b6996fd6c611bd8611b0a3c48f2e07f8b94cfb6fa55ee4a12bcaf18`

## Python

Check for macros before accepting or opening an Office upload. Modern files are ZIPs: VBA lives in vbaProject.bin (Microsoft) or a Basic folder (OpenDocument). Legacy .xls/.doc files are OLE2 containers that need a dedicated parser, such as oletools, to see inside.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
no macro parts among 3 entries
```
