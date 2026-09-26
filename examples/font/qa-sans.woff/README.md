# qa-sans.woff

The same "QA Sans" font packaged as WOFF 1.0 - every sfnt table individually zlib-compressed behind a WOFF header and table directory.

Page: https://hexaqa.com/file/fonts/qa-sans-woff

```bash
curl -fsSL -o "qa-sans.woff" "https://files.hexaqa.com/font/qa-sans.woff"
```

SHA-256: `25bc662e7cc23e7c28d0f518f2442191dd98faafb6259e4da24546deea7d5bd5`

## Python

Check the signature and the table directory before handing a font to a renderer. TrueType and OpenType list their tables in a plain directory; WOFF wraps the same tables with zlib; WOFF2 compresses them with Brotli, which the standard library cannot read.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
WOFF with 10 tables: OS/2, cmap, glyf, head, hhea, hmtx, loca, maxp, name, post
all required tables present
```
