# overlapping-cues.srt

SRT whose cues overlap in time and are not in chronological order, with one zero-length cue.

Page: https://hexaqa.com/file/subtitles-and-captions/overlapping-cues-srt

```bash
curl -fsSL -o "overlapping-cues.srt" "https://files.hexaqa.com/subtitle/overlapping-cues.srt"
```

SHA-256: `cf5259514f8ff313a3c625dab6d1932e5c8a7f7a3df74c58d89667ba68b41a86`

## Python

SRT puts a comma before the milliseconds and WebVTT a full stop, and WebVTT files must start with WEBVTT. Players differ on the rest: overlapping cues are legal in WebVTT, but many SRT players show only one of them.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
3 cues: 3 problems
  line 6: starts before the previous cue (out of order)
  line 6: overlaps the previous cue by 2000 ms
  line 10: zero length, so it never shows
```
