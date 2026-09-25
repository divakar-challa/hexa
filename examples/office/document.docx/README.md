# document.docx

Word document (OOXML) with a heading and two paragraphs.

Page: https://hexaqa.com/file/office-documents/document-docx

```bash
curl -fsSL -o "document.docx" "https://files.hexaqa.com/office/document.docx"
```

SHA-256: `08deccf7b4eb6de82226463b72076dbefbc7fcc89b1c691ed5a83a5db349954c`

## Python

A DOCX that passes a ZIP check can still be unopenable. Check for the parts Word requires.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
has the parts a DOCX needs
```
