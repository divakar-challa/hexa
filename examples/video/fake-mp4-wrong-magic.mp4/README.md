# fake-mp4-wrong-magic.mp4

Named .mp4 but the first bytes are random noise rather than an ftyp box. Contains no video data.

Page: https://hexaqa.com/file/audio-and-video/fake-mp4-wrong-magic-mp4

```bash
curl -fsSL -o "fake-mp4-wrong-magic.mp4" "https://files.hexaqa.com/video/fake-mp4-wrong-magic.mp4"
```

SHA-256: `678b109814ee687b8672b6fe9f559cfae722aa79285ac23bf1ca792de9e97ded`

## Python

An MP4 is a sequence of boxes: a 4-byte size, a 4-byte type, then the contents. Walking the top level shows a missing moov box (no index, so nothing to play) or a file that is not an MP4 at all, without a media library.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
not an MP4: the first box is 0x62dda363
```
