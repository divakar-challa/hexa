# corrupt-missing-content-types.docx

A DOCX-shaped ZIP that is missing its [Content_Types].xml part.

Page: https://hexaqa.com/file/office-documents/corrupt-missing-content-types-docx

```bash
curl -fsSL -o "corrupt-missing-content-types.docx" "https://files.hexaqa.com/office/corrupt-missing-content-types.docx"
```

SHA-256: `6de45712c47ec56fa5f14b701827e2ee7a6adf7296ec3e8a5657af63babe5b2a`

## Python

A DOCX that passes a ZIP check can still be unopenable. Check for the parts Word requires.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
rejected: a valid ZIP but not an Office file (no [Content_Types].xml)
```
