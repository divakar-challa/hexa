# flat-96x96.webp

A 96x96 lossless WEBP (VP8L) in a single flat colour, 32 bytes in total.

Page: https://hexaqa.com/file/images/flat-96x96-webp

```bash
curl -fsSL -o "flat-96x96.webp" "https://files.hexaqa.com/image/flat-96x96.webp"
```

SHA-256: `b106293152970ea05fe1349ba69fc45509e1e9bd4a5b2fa0d8b2e109ee79bcf1`

## Python

Read the width and height from the header and refuse oversized images before any decoder allocates memory. A 265 KB PNG can declare 8000x8000 pixels, which decodes to 256 MB of RGBA. Pillow's default guard (Image.MAX_IMAGE_PIXELS, about 89 million pixels) lets a 64-million-pixel image through without a warning, so set your own limit.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: webp 96x96
```

## Node.js

The same header check in Node, before the upload reaches sharp, jimp or a canvas.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: webp 96x96
```
