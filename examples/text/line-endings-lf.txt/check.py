import unicodedata

with open("line-endings-lf.txt", "rb") as f:
    data = f.read()
crlf = data.count(b"\r\n")
lf, cr = data.count(b"\n") - crlf, data.count(b"\r") - crlf
print(f"line endings: {crlf} CRLF, {lf} LF, {cr} bare CR")
print("ends with a newline" if data.endswith(b"\n") else "no newline at the end of the file")
text = data.decode("utf-8")
print(f"longest line: {max(map(len, text.splitlines()), default=0):,} characters")
hidden = sorted({f"U+{ord(c):04X} {unicodedata.name(c, '?')}" for c in text if unicodedata.category(c) == "Cf"})
print("invisible characters:", ", ".join(hidden) if hidden else "none")
