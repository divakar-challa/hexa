# transparent-1x1.webp

A 1x1 semi-transparent lossless WEBP, the smallest useful WEBP fixture.

Page: https://hexaqa.com/file/images/transparent-1x1-webp

```bash
curl -fsSL -o "transparent-1x1.webp" "https://files.hexaqa.com/image/transparent-1x1.webp"
```

SHA-256: `643ed5e4ce28a95a6f079364243b6ce181b544d8b11f5a626d7831af3abb12b4`

## Python

Read the width and height from the header and refuse oversized images before any decoder allocates memory. A 265 KB PNG can declare 8000x8000 pixels, which decodes to 256 MB of RGBA. Pillow's default guard (Image.MAX_IMAGE_PIXELS, about 89 million pixels) lets a 64-million-pixel image through without a warning, so set your own limit.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: webp 1x1
```

## Node.js

The same header check in Node, before the upload reaches sharp, jimp or a canvas.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: webp 1x1
```
