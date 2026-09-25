# png-valid-256.png

256x256 RGBA checkerboard, non-interlaced, 8-bit.

Page: https://hexaqa.com/file/images/png-valid-256-png

```bash
curl -fsSL -o "png-valid-256.png" "https://files.hexaqa.com/image/png-valid-256.png"
```

SHA-256: `febec136e1589e5b7a53bfedddf957a01222b5722edb3735560e5d3ffebe134a`

## Python

Walk the chunks and verify each CRC. Browsers tolerate damage that strict decoders reject, so check before you store or process the image.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
chunk structure is valid
```
