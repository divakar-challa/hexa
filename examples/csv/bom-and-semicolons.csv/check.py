import csv

with open("bom-and-semicolons.csv", newline="", encoding="utf-8-sig") as f:
    dialect = csv.Sniffer().sniff(f.read(4096), delimiters=",;\t")
    f.seek(0)
    rows = list(csv.reader(f, dialect))

print("delimiter:", repr(dialect.delimiter))
print("header:", rows[0])
