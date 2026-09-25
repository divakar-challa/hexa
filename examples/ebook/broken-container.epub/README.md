# broken-container.epub

EPUB whose META-INF/container.xml points at an OPF file that does not exist in the archive.

Page: https://hexaqa.com/file/ebooks/broken-container-epub

```bash
curl -fsSL -o "broken-container.epub" "https://files.hexaqa.com/ebook/broken-container.epub"
```

SHA-256: `afd0525368dec495c11f8cff4db86c5d0e85b131f6888f1ba328502d12e3a59e`

## Python

Follow container.xml to the package document and confirm it exists, which is exactly what a reader does first.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
rejected: container.xml points at OEBPS/missing.opf, which is missing
```
