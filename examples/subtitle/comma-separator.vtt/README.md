# comma-separator.vtt

WebVTT that uses the SRT comma decimal separator in its timestamps instead of a full stop.

Page: https://hexaqa.com/file/subtitles-and-captions/comma-separator-vtt

```bash
curl -fsSL -o "comma-separator.vtt" "https://files.hexaqa.com/subtitle/comma-separator.vtt"
```

SHA-256: `4750082833b28bd77e218973efbe11e0b9a9763ae226c99a24ecb0a20f9c8d6b`

## Python

SRT puts a comma before the milliseconds and WebVTT a full stop, and WebVTT files must start with WEBVTT. Players differ on the rest: overlapping cues are legal in WebVTT, but many SRT players show only one of them.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
2 cues: 2 problems
  line 3: WebVTT needs '.' before the milliseconds
  line 6: WebVTT needs '.' before the milliseconds
```
