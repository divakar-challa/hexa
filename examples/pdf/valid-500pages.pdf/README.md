# valid-500pages.pdf

Well-formed PDF with 500 numbered pages.

Page: https://hexaqa.com/file/documents/valid-500pages-pdf

```bash
curl -fsSL -o "valid-500pages.pdf" "https://files.hexaqa.com/pdf/valid-500pages.pdf"
```

SHA-256: `a950f538dcb5480d277dd180a38ee00dfd827a6f1e2b1d34c72fd3ce0a618a25`

## Python

Quick triage without a PDF library: count page objects and look for the text-drawing operators (Tj, TJ) in the content streams, inflating Flate streams with zlib. Use it to route files, for example image-only scans to OCR. PDFs that pack objects into compressed object streams need a real parser such as pypdf.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
page objects: 500, content streams that draw text: 500
```
