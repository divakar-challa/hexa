# presentation.pptx

PowerPoint presentation with a slide master, layout and one titled slide.

Page: https://hexaqa.com/file/office-documents/presentation-pptx

```bash
curl -fsSL -o "presentation.pptx" "https://files.hexaqa.com/office/presentation.pptx"
```

SHA-256: `918c7c135ed89f8b0f662d1ead1bfeb7c5b75a94f2e5e6ca4d4a4aa347a6c35f`

## Python

Check for macros before accepting or opening an Office upload. Modern files are ZIPs: VBA lives in vbaProject.bin (Microsoft) or a Basic folder (OpenDocument). Legacy .xls/.doc files are OLE2 containers that need a dedicated parser, such as oletools, to see inside.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
no macro parts among 10 entries
```
