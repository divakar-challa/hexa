import re
import zipfile
import xml.etree.ElementTree as ET

M = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
TRIGGERS = ("=", "+", "-", "@", "\t", "\r")

def text_of(el):
    return "".join(t.text or "" for t in el.iter(M + "t"))

found = 0
with zipfile.ZipFile("formula-injection.xlsx") as z:
    names = z.namelist()
    shared = []
    if "xl/sharedStrings.xml" in names:
        shared = [text_of(si) for si in ET.fromstring(z.read("xl/sharedStrings.xml")).iter(M + "si")]
    for sheet in sorted(n for n in names if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", n)):
        for c in ET.fromstring(z.read(sheet)).iter(M + "c"):
            ref, kind, formula = c.get("r"), c.get("t"), c.find(M + "f")
            if formula is not None:
                print(f"{ref}: formula ={formula.text} (runs when the file is opened)")
                continue
            if kind == "s":
                text = shared[int(c.find(M + "v").text)]
            elif kind == "inlineStr":
                text = text_of(c)
            else:
                continue
            if text.startswith(TRIGGERS):
                print(f"{ref}: text {text!r} turns into a formula when exported to CSV")
                found += 1
print(f"{found} text cell{'s' * (found != 1)} to neutralise before a CSV export" if found else "no formula-like text")
