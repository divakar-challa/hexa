# valid.srt

A valid SubRip file: four cues, 1-based numbering, comma decimal separator, blank line between cues.

Page: https://hexaqa.com/file/subtitles-and-captions/valid-srt

```bash
curl -fsSL -o "valid.srt" "https://files.hexaqa.com/subtitle/valid.srt"
```

SHA-256: `9bd108406fd1c6924494a87a90ff6c9e577aa8bec6f697ec3960a63bf3f8af5b`

## Python

SRT puts a comma before the milliseconds and WebVTT a full stop, and WebVTT files must start with WEBVTT. Players differ on the rest: overlapping cues are legal in WebVTT, but many SRT players show only one of them.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
4 cues: valid
```
