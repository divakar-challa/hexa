import re

TIME = r"(?:(\d+):)?(\d{2}):(\d{2})([.,])(\d{3})"
CUE = re.compile(TIME + r"\s+-->\s+" + TIME)

def ms(h, m, s, sep, frac):
    return ((int(h or 0) * 60 + int(m)) * 60 + int(s)) * 1000 + int(frac)

name = "missing-signature.vtt"
vtt = name.lower().endswith(".vtt")
with open(name, encoding="utf-8-sig") as f:
    text = f.read()
problems, cues = [], []
if vtt and not text.startswith("WEBVTT"):
    problems.append("line 1: no WEBVTT signature")
for n, line in enumerate(text.splitlines(), 1):
    m = CUE.search(line)
    if not m:
        continue
    g = m.groups()
    right = "." if vtt else ","
    if g[3] != right or g[8] != right:
        problems.append(f"line {n}: {'WebVTT' if vtt else 'SRT'} needs {right!r} before the milliseconds")
    start, end = ms(*g[:5]), ms(*g[5:])
    if end < start:
        problems.append(f"line {n}: the cue ends before it starts")
    elif end == start:
        problems.append(f"line {n}: zero length, so it never shows")
    if cues:
        prev_start, prev_end = cues[-1]
        if start < prev_start:
            problems.append(f"line {n}: starts before the previous cue (out of order)")
        overlap = min(end, prev_end) - max(start, prev_start)
        if overlap > 0:
            problems.append(f"line {n}: overlaps the previous cue by {overlap} ms")
    cues.append((start, end))
print(f"{len(cues)} cues:", "valid" if not problems else f"{len(problems)} problem{'s' * (len(problems) != 1)}")
for p in problems:
    print("  " + p)
