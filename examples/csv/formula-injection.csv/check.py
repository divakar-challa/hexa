import csv

def neutralise(cell):
    # Excel and Sheets treat a cell starting with any of these as a formula.
    return "'" + cell if cell[:1] in ("=", "+", "-", "@", "\t", "\r") else cell

with open("formula-injection.csv", newline="", encoding="utf-8") as src, \
        open("safe.csv", "w", newline="", encoding="utf-8") as out:
    writer = csv.writer(out)
    for row in csv.reader(src):
        writer.writerow([neutralise(c) for c in row])

with open("safe.csv", encoding="utf-8") as f:
    print(f.read().splitlines()[1])
