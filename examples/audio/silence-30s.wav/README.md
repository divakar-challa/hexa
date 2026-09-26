# silence-30s.wav

30 seconds of digital silence, 16-bit PCM mono.

Page: https://hexaqa.com/file/audio-and-video/silence-30s-wav

```bash
curl -fsSL -o "silence-30s.wav" "https://files.hexaqa.com/audio/silence-30s.wav"
```

SHA-256: `34e20072bd56124004287878b329f8869869aba39273214720521bf7a0a3425f`

## Python

Compare what the header declares with what the file holds, and refuse a header that is itself cut short.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
header says 1323000 frames, file holds 1323000: ok
```
