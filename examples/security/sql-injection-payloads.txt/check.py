import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE users (name TEXT)")
with open("sql-injection-payloads.txt", encoding="utf-8") as f:
    payloads = [line.rstrip("\n") for line in f if line.strip()]
for p in payloads:
    db.execute("INSERT INTO users (name) VALUES (?)", (p,))  # a parameter, not string formatting
stored = [row[0] for row in db.execute("SELECT name FROM users")]
print(f"{len(payloads)} payloads stored verbatim: {stored == payloads}")
print("tables:", [row[0] for row in db.execute("SELECT name FROM sqlite_master WHERE type = 'table'")])
