# qa-sans.woff2

The same "QA Sans" font as WOFF2: every table concatenated into a single Brotli stream behind a WOFF2 header and a variable-length table directory.

Page: https://hexaqa.com/file/fonts/qa-sans-woff2

```bash
curl -fsSL -o "qa-sans.woff2" "https://files.hexaqa.com/font/qa-sans.woff2"
```

SHA-256: `b317987f196d3143a3fc42d506b9700f49d4ccec2335910e4c220fa9013395ef`

## Python

Check the signature and the table directory before handing a font to a renderer. TrueType and OpenType list their tables in a plain directory; WOFF wraps the same tables with zlib; WOFF2 compresses them with Brotli, which the standard library cannot read.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
WOFF2 with 10 tables, Brotli-compressed: read further with fontTools
```
