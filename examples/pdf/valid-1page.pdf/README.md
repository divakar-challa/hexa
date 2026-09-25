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
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
structure looks intact
```
