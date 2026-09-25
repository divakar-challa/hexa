import json

try:
    with open("malformed-trailing-comma.json", encoding="utf-8") as f:
        json.load(f)
    print("valid")
except json.JSONDecodeError as e:
    print(f"invalid JSON at line {e.lineno}, column {e.colno}: {e.msg}")
