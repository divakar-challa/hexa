# corrupt-xref.pdf

Valid PDF body with a deliberately wrong startxref offset, so the cross-reference table cannot be located.

Page: https://hexaqa.com/file/documents/corrupt-xref-pdf

```bash
curl -fsSL -o "corrupt-xref.pdf" "https://files.hexaqa.com/pdf/corrupt-xref.pdf"
```

SHA-256: `bd5efc3d6ec6afa54aec7d16a763577239ce2e1fda8636bea12497b4d9046f32`

## Python

A cheap structural check before handing the file to a PDF library, which will often repair these silently. Use it to reject or flag uploads, not to validate PDFs fully.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
startxref points at byte 999999, where there is no cross-reference table
```
