# valid-1page.pdf

Minimal well-formed single-page PDF 1.4 with selectable Helvetica text.

Page: https://hexaqa.com/file/documents/valid-1page-pdf

```bash
curl -fsSL -o "valid-1page.pdf" "https://files.hexaqa.com/pdf/valid-1page.pdf"
```

SHA-256: `84e95ec0084af11ba5ddee05e2a6755a46124912b65e1378ff80bc1e119609ec`

## Python

A cheap structural check before handing the file to a PDF library, which will often repair these silently. Use it to reject or flag uploads, not to validate PDFs fully.

```bash
python check-pdfCheck.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
structure looks intact
```

## Python

Quick triage without a PDF library: count page objects and look for the text-drawing operators (Tj, TJ) in the content streams, inflating Flate streams with zlib. Use it to route files, for example image-only scans to OCR. PDFs that pack objects into compressed object streams need a real parser such as pypdf.

```bash
python check-pdfText.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
page objects: 1, content streams that draw text: 1
```
