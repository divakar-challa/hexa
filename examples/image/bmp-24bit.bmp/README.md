# bmp-24bit.bmp

128x128 uncompressed 24-bit BMP with bottom-up row order.

Page: https://hexaqa.com/file/images/bmp-24bit-bmp

```bash
curl -fsSL -o "bmp-24bit.bmp" "https://files.hexaqa.com/image/bmp-24bit.bmp"
```

SHA-256: `01e674d234756a13da06a462f27a7d2f39a2179dfe304695c7fb8387f2a3acae`

## Python

Read the width and height from the header and refuse oversized images before any decoder allocates memory. A 265 KB PNG can declare 8000x8000 pixels, which decodes to 256 MB of RGBA. Pillow's default guard (Image.MAX_IMAGE_PIXELS, about 89 million pixels) lets a 64-million-pixel image through without a warning, so set your own limit.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: bmp 128x128
```

## Node.js

The same header check in Node, before the upload reaches sharp, jimp or a canvas.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: bmp 128x128
```
