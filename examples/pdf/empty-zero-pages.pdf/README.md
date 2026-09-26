# empty-zero-pages.pdf

Structurally valid PDF whose /Pages node declares /Count 0 and an empty /Kids array.

Page: https://hexaqa.com/file/documents/empty-zero-pages-pdf

```bash
curl -fsSL -o "empty-zero-pages.pdf" "https://files.hexaqa.com/pdf/empty-zero-pages.pdf"
```

SHA-256: `c9ff80b477c10ff11270c788b35152f7d5f7147c288d7c1d051dd19bca1b8253`

## Python

Quick triage without a PDF library: count page objects and look for the text-drawing operators (Tj, TJ) in the content streams, inflating Flate streams with zlib. Use it to route files, for example image-only scans to OCR. PDFs that pack objects into compressed object streams need a real parser such as pypdf.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
page objects: 0, content streams that draw text: 0
no pages: most readers show an error or a blank document
```
