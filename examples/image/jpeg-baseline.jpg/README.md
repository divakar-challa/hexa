# jpeg-baseline.jpg

256x256 baseline JPEG, 4:2:0 chroma subsampling, quality ~85, encoded from source.

Page: https://hexaqa.com/file/images/jpeg-baseline-jpg

```bash
curl -fsSL -o "jpeg-baseline.jpg" "https://files.hexaqa.com/image/jpeg-baseline.jpg"
```

SHA-256: `cd87b4048afdb864fad74f0ff409c81c844d0043a00870bafeb5685dd061722d`

## Python

Read the width and height from the header and refuse oversized images before any decoder allocates memory. A 265 KB PNG can declare 8000x8000 pixels, which decodes to 256 MB of RGBA. Pillow's default guard (Image.MAX_IMAGE_PIXELS, about 89 million pixels) lets a 64-million-pixel image through without a warning, so set your own limit.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: jpg 256x256
```

## Node.js

The same header check in Node, before the upload reaches sharp, jimp or a canvas.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: jpg 256x256
```
