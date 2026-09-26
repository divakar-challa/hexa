# empty-ftyp-only.mp4

A valid ftyp box declaring isom/mp42 branding, with no moov and no mdat - structurally an MP4, but with zero tracks.

Page: https://hexaqa.com/file/audio-and-video/empty-ftyp-only-mp4

```bash
curl -fsSL -o "empty-ftyp-only.mp4" "https://files.hexaqa.com/video/empty-ftyp-only.mp4"
```

SHA-256: `5c15fbf395d7d984bba8eeedf90f7adbc0c166cfd9e633d6d18b5153231bdd85`

## Python

An MP4 is a sequence of boxes: a 4-byte size, a 4-byte type, then the contents. Walking the top level shows a missing moov box (no index, so nothing to play) or a file that is not an MP4 at all, without a media library.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
boxes: ftyp; no moov box, so there is nothing to play
```
