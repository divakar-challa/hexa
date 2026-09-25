# truncated-header.wav

A WAV file cut off after 30 bytes, mid-header.

Page: https://hexaqa.com/file/audio-and-video/truncated-header-wav

```bash
curl -fsSL -o "truncated-header.wav" "https://files.hexaqa.com/audio/truncated-header.wav"
```

SHA-256: `1a34ac609c1addcfc3c4e0980b57659d1bbc93a942afe4b39d671e3b1d9aa054`

## Python

Compare what the header declares with what the file holds, and refuse a header that is itself cut short.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
rejected: the header is cut short
```
