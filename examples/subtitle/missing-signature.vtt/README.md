# missing-signature.vtt

A WebVTT file with correct cues but no "WEBVTT" first line, which makes the whole file invalid.

Page: https://hexaqa.com/file/subtitles-and-captions/missing-signature-vtt

```bash
curl -fsSL -o "missing-signature.vtt" "https://files.hexaqa.com/subtitle/missing-signature.vtt"
```

SHA-256: `50cf66ef41bf05706e150236a4c48c25a65fc23b54c06cfba0c9143abe57b3f2`

## Python

SRT puts a comma before the milliseconds and WebVTT a full stop, and WebVTT files must start with WEBVTT. Players differ on the rest: overlapping cues are legal in WebVTT, but many SRT players show only one of them.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
2 cues: 1 problem
  line 1: no WEBVTT signature
```
