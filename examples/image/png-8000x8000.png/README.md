# png-8000x8000.png

8000x8000 PNG of flat colour. Compresses to a few hundred KB but expands to roughly 256 MB in memory.

Page: https://hexaqa.com/file/images/png-8000x8000-png

```bash
curl -fsSL -o "png-8000x8000.png" "https://files.hexaqa.com/image/png-8000x8000.png"
```

SHA-256: `0818a806b978790eab13e286e98c069a739648bda085a1b74fa24cc6963e4d58`

## Python

Read the width and height from the header and refuse oversized images before any decoder allocates memory. A 265 KB PNG can declare 8000x8000 pixels, which decodes to 256 MB of RGBA. Pillow's default guard (Image.MAX_IMAGE_PIXELS, about 89 million pixels) lets a 64-million-pixel image through without a warning, so set your own limit.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
refused: png 8000x8000 is 64,000,000 pixels, over the 25,000,000 limit
```

## Node.js

The same header check in Node, before the upload reaches sharp, jimp or a canvas.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
refused: png 8000x8000 is 64,000,000 pixels, over the 25,000,000 limit
```
