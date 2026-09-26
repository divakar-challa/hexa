# png-interlaced.png

PNG with the Adam7 interlace flag set in IHDR. Note: pixel data is stored non-interlaced, so strict decoders will reject it - that is intentional.

Page: https://hexaqa.com/file/images/png-interlaced-png

```bash
curl -fsSL -o "png-interlaced.png" "https://files.hexaqa.com/image/png-interlaced.png"
```

SHA-256: `575ae26f4ac35073b117c5c03101ef1debdc8b1e1b34e58c5d856bc1e90e89a0`

## Python

Read the width and height from the header and refuse oversized images before any decoder allocates memory. A 265 KB PNG can declare 8000x8000 pixels, which decodes to 256 MB of RGBA. Pillow's default guard (Image.MAX_IMAGE_PIXELS, about 89 million pixels) lets a 64-million-pixel image through without a warning, so set your own limit.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: png 128x128
```

## Node.js

The same header check in Node, before the upload reaches sharp, jimp or a canvas.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: png 128x128
```
