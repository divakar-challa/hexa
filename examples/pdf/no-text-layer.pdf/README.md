# no-text-layer.pdf

PDF whose only page draws vector rectangles and contains zero text operators.

Page: https://hexaqa.com/file/documents/no-text-layer-pdf

```bash
curl -fsSL -o "no-text-layer.pdf" "https://files.hexaqa.com/pdf/no-text-layer.pdf"
```

SHA-256: `b061ce1d9945d157fe3cd86249309776b9d438fbc55f16f5b56a041971d91224`

## Python

Quick triage without a PDF library: count page objects and look for the text-drawing operators (Tj, TJ) in the content streams, inflating Flate streams with zlib. Use it to route files, for example image-only scans to OCR. PDFs that pack objects into compressed object streams need a real parser such as pypdf.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
page objects: 1, content streams that draw text: 0
no text layer: extraction returns nothing, so this needs OCR
```
