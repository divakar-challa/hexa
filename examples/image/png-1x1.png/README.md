# png-1x1.png

Single opaque pixel. The smallest valid PNG this corpus produces.

Page: https://hexaqa.com/file/images/png-1x1-png

```bash
curl -fsSL -o "png-1x1.png" "https://files.hexaqa.com/image/png-1x1.png"
```

SHA-256: `077158f9f77953e9b39eb582b999335adbd9af79e0ef9a76921243187682a937`

## Python

Read the width and height from the header and refuse oversized images before any decoder allocates memory. A 265 KB PNG can declare 8000x8000 pixels, which decodes to 256 MB of RGBA. Pillow's default guard (Image.MAX_IMAGE_PIXELS, about 89 million pixels) lets a 64-million-pixel image through without a warning, so set your own limit.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: png 1x1
```

## Node.js

The same header check in Node, before the upload reaches sharp, jimp or a canvas.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: png 1x1
```
