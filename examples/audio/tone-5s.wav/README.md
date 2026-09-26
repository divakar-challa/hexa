# tone-5s.wav

5 seconds of a 440 Hz sine tone, 16-bit PCM mono at 44.1 kHz.

Page: https://hexaqa.com/file/audio-and-video/tone-5s-wav

```bash
curl -fsSL -o "tone-5s.wav" "https://files.hexaqa.com/audio/tone-5s.wav"
```

SHA-256: `5ed9e874d6e6cb55d098831ac4e965b03633d8186b6dae7128decda2e3f90c02`

## Python

Compare what the header declares with what the file holds, and refuse a header that is itself cut short.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
header says 220500 frames, file holds 220500: ok
```
