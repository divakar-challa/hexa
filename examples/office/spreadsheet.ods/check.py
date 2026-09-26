import zipfile

OLE2 = bytes.fromhex("d0cf11e0a1b11ae1")

with open("spreadsheet.ods", "rb") as f:
    magic = f.read(8)
if magic == OLE2:
    print("legacy OLE2 file (.xls, .doc, .ppt, .msg): may carry VBA; inspect it with an OLE parser")
elif not zipfile.is_zipfile("spreadsheet.ods"):
    print("not an Office file")
else:
    with zipfile.ZipFile("spreadsheet.ods") as z:
        names = z.namelist()
        types = z.read("[Content_Types].xml").decode() if "[Content_Types].xml" in names else ""
    macros = [n for n in names if n.lower().endswith("vbaproject.bin") or n.startswith(("Basic/", "Scripts/"))]
    if macros or "macroEnabled" in types:
        print("contains macros:", ", ".join(macros) or "declared in [Content_Types].xml")
    else:
        print(f"no macro parts among {len(names)} entries")
