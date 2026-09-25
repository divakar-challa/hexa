import zipfile

with zipfile.ZipFile("document.docx") as z:
    names = set(z.namelist())

if "[Content_Types].xml" not in names:
    print("rejected: a valid ZIP but not an Office file (no [Content_Types].xml)")
elif "word/document.xml" not in names:
    print("rejected: no word/document.xml")
else:
    print("has the parts a DOCX needs")
