import sqlite3

statements, current = [], ""
with open("schema.sql", encoding="utf-8") as f:
    for line in f:
        current += line
        if sqlite3.complete_statement(current):
            statements.append(current.strip())
            current = ""
db = sqlite3.connect(":memory:", isolation_level=None)  # the script manages its own transaction
for s in statements:
    db.execute(s)
made = db.execute("SELECT type, name FROM sqlite_master WHERE name NOT LIKE 'sqlite_%' ORDER BY type, name").fetchall()
print(len(statements), "statements, all executed")
print(", ".join(f"{kind} {name}" for kind, name in made))
