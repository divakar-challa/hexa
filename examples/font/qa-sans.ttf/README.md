# qa-sans.ttf

A minimal but genuinely valid TrueType font ("QA Sans") with 6 glyphs (.notdef, space, A, B, C, Q), the full required sfnt table set and correct checksums.

Page: https://hexaqa.com/file/fonts/qa-sans-ttf

```bash
curl -fsSL -o "qa-sans.ttf" "https://files.hexaqa.com/font/qa-sans.ttf"
```

SHA-256: `d1f5a5853af23af5a1b61aa531f77cdc5cda94ccfe00f0473be0438bf7327284`

## Python

Check the signature and the table directory before handing a font to a renderer. TrueType and OpenType list their tables in a plain directory; WOFF wraps the same tables with zlib; WOFF2 compresses them with Brotli, which the standard library cannot read.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
TrueType with 10 tables: OS/2, cmap, glyf, head, hhea, hmtx, loca, maxp, name, post
all required tables present
```
