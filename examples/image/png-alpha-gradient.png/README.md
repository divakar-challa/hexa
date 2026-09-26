# png-alpha-gradient.png

256x256 PNG with a horizontal alpha ramp from fully transparent to fully opaque.

Page: https://hexaqa.com/file/images/png-alpha-gradient-png

```bash
curl -fsSL -o "png-alpha-gradient.png" "https://files.hexaqa.com/image/png-alpha-gradient.png"
```

SHA-256: `8e81decafe428a492142b1b04d1a63a32133f18f3e6393753f872c7a01a32c1d`

## Python

Read the width and height from the header and refuse oversized images before any decoder allocates memory. A 265 KB PNG can declare 8000x8000 pixels, which decodes to 256 MB of RGBA. Pillow's default guard (Image.MAX_IMAGE_PIXELS, about 89 million pixels) lets a 64-million-pixel image through without a warning, so set your own limit.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: png 256x256
```

## Node.js

The same header check in Node, before the upload reaches sharp, jimp or a canvas.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: png 256x256
```
