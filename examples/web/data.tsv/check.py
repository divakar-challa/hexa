import csv

with open("data.tsv", newline="", encoding="utf-8-sig") as f:
    try:
        dialect = csv.Sniffer().sniff(f.read(64 * 1024), delimiters=",;\t|")
    except csv.Error:
        dialect = csv.excel  # the sniffer gives up on irregular files: assume commas
    f.seek(0)
    rows = csv.reader(f, dialect)
    header = next(rows)
    count, bad = 0, []
    for count, row in enumerate(rows, 1):
        if len(row) != len(header):
            bad.append((rows.line_num, len(row)))
print(f"delimiter {dialect.delimiter!r}, {len(header)} columns, {count:,} data rows")
for line, n in bad[:5]:
    print(f"  line {line}: {n} field{'s' * (n != 1)}, expected {len(header)}")
if not bad:
    print("  every row matches the header")
