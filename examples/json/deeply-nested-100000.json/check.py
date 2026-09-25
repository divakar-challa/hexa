import json

try:
    with open("deeply-nested-100000.json", encoding="utf-8") as f:
        json.load(f)
    print("parsed")
except RecursionError:
    print("rejected: nested too deeply to parse")
