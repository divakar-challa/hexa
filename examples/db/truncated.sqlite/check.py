import sqlite3

con = sqlite3.connect("file:truncated.sqlite?mode=ro", uri=True)
try:
    result = con.execute("PRAGMA integrity_check").fetchone()[0]
    print("integrity: ok" if result == "ok" else "rejected: " + " / ".join(result.splitlines()[:2]))
except sqlite3.DatabaseError as e:
    print("rejected:", e)
finally:
    con.close()
