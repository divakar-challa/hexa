# valid.epub

A valid EPUB 2 with metadata, an NCX table of contents and three chapters.

Page: https://hexaqa.com/file/ebooks/valid-epub

```bash
curl -fsSL -o "valid.epub" "https://files.hexaqa.com/ebook/valid.epub"
```

SHA-256: `ad719e81f75520420d5d4688da7043e5acb7956cc26e7ca6b6523d48d647253d`

## Python

Follow container.xml to the package document and confirm it exists, which is exactly what a reader does first.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok
```
