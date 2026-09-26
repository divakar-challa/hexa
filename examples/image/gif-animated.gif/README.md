# gif-animated.gif

A looping animated GIF: four frames, 200 ms each, with a NETSCAPE2.0 loop block.

Page: https://hexaqa.com/file/images/gif-animated-gif

```bash
curl -fsSL -o "gif-animated.gif" "https://files.hexaqa.com/image/gif-animated.gif"
```

SHA-256: `1bbfaedc241b6979a270bc4aaf634406e775afcde1d65ab6ca440f3eab6cb545`

## Python

Read the width and height from the header and refuse oversized images before any decoder allocates memory. A 265 KB PNG can declare 8000x8000 pixels, which decodes to 256 MB of RGBA. Pillow's default guard (Image.MAX_IMAGE_PIXELS, about 89 million pixels) lets a 64-million-pixel image through without a warning, so set your own limit.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: gif 96x96
```

## Node.js

The same header check in Node, before the upload reaches sharp, jimp or a canvas.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
ok: gif 96x96
```
