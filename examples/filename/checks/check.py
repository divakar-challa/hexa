import unicodedata

BIDI = {"LRE", "RLE", "PDF", "LRO", "RLO", "LRI", "RLI", "FSI", "PDI"}
RUNS = {"exe", "scr", "bat", "cmd", "com", "js", "vbs", "ps1", "msi", "jar", "lnk"}

def check_name(name):
    problems = []
    if any(unicodedata.bidirectional(c) in BIDI for c in name):
        problems.append("contains an invisible direction control")
    parts = name.lower().split(".")
    if len(parts) > 2 and parts[-1] in RUNS:
        problems.append(f"double extension .{parts[-2]}.{parts[-1]}")
    return problems or ["ok"]

for name in ["invoice\u202Egnp.txt", "report.pdf.exe", "notes.txt"]:
    print(ascii(name), check_name(name))
