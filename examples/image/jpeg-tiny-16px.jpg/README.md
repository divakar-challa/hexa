# jpeg-tiny-16px.jpg

16x16 baseline JPEG - exactly one minimum coded unit.

Page: https://hexaqa.com/file/images/jpeg-tiny-16px-jpg

```bash
curl -fsSL -o "jpeg-tiny-16px.jpg" "https://files.hexaqa.com/image/jpeg-tiny-16px.jpg"
```

SHA-256: `5f0f9348ecd249a0e54cad079f44e4bc3f55a1aa74a8a5ce106e04450090a165`

## Python

Read the width and height from the header and refuse oversized images before any decoder allocates memory. A 265 KB PNG can declare 8000x8000 pixels, which decodes to 256 MB of RGBA. Pillow's default guard (Image.MAX_IMAGE_PIXELS, about 89 million pixels) lets a 64-million-pixel image through without a warning, so set your own limit.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: jpg 16x16
```

## Node.js

The same header check in Node, before the upload reaches sharp, jimp or a canvas.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: jpg 16x16
```
