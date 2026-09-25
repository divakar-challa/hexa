# declared-length-mismatch.wav

Valid WAV whose data chunk header declares ten times more bytes than the file actually contains.

Page: https://hexaqa.com/file/audio-and-video/declared-length-mismatch-wav

```bash
curl -fsSL -o "declared-length-mismatch.wav" "https://files.hexaqa.com/audio/declared-length-mismatch.wav"
```

SHA-256: `fa849fa10674fce6a798353aad7913789f3dd054fa4b677ad368ee8e1e21d790`

## Python

Compare what the header declares with what the file holds, and refuse a header that is itself cut short.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
header says 882000 frames, file holds 88200: truncated or lying header
```
