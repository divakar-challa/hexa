import re

with open("valid-1page.pdf", "rb") as f:
    data = f.read()

problems = []
if not data.startswith(b"%PDF-"):
    problems.append("no %PDF- header")
tail = data[-1024:]
if b"%%EOF" not in tail:
    problems.append("no %%EOF marker: the file is truncated")
m = re.search(rb"startxref\s+(\d+)\s+%%EOF", tail)
if m:
    offset = int(m.group(1))
    at = data[offset:offset + 20]
    if offset >= len(data) or not (at.startswith(b"xref") or re.match(rb"\d+ \d+ obj", at)):
        problems.append(f"startxref points at byte {offset}, where there is no cross-reference table")

print("; ".join(problems) or "structure looks intact")
