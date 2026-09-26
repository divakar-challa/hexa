# valid.vtt

A valid WebVTT file with the required signature, a NOTE comment, a named cue and cue settings.

Page: https://hexaqa.com/file/subtitles-and-captions/valid-vtt

```bash
curl -fsSL -o "valid.vtt" "https://files.hexaqa.com/subtitle/valid.vtt"
```

SHA-256: `301323cac0aa86219c7f17917e84c18b5e0c8792d431d855798e50c5326be685`

## Python

SRT puts a comma before the milliseconds and WebVTT a full stop, and WebVTT files must start with WEBVTT. Players differ on the rest: overlapping cues are legal in WebVTT, but many SRT players show only one of them.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
4 cues: valid
```
