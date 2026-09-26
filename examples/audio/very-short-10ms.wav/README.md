# very-short-10ms.wav

10 milliseconds of audio - 441 samples.

Page: https://hexaqa.com/file/audio-and-video/very-short-10ms-wav

```bash
curl -fsSL -o "very-short-10ms.wav" "https://files.hexaqa.com/audio/very-short-10ms.wav"
```

SHA-256: `d23833d93b968455dd817ba1849dd1a6e7d534dbde2cf28cca98130a115ab95b`

## Python

Compare what the header declares with what the file holds, and refuse a header that is itself cut short.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
header says 441 frames, file holds 441: ok
```
