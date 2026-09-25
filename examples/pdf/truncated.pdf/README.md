# truncated.pdf

A valid PDF cut off at 60% of its length, simulating an interrupted upload.

Page: https://hexaqa.com/file/documents/truncated-pdf

```bash
curl -fsSL -o "truncated.pdf" "https://files.hexaqa.com/pdf/truncated.pdf"
```

SHA-256: `a0975aad80c61f7b47103d04c4143122aa1a48da51d0c7fe74772f3af3479d7b`

## Python

A cheap structural check before handing the file to a PDF library, which will often repair these silently. Use it to reject or flag uploads, not to validate PDFs fully.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
no %%EOF marker: the file is truncated
```
