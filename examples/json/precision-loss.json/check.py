import json
from decimal import Decimal

with open("precision-loss.json", encoding="utf-8") as f:
    data = json.load(f, parse_float=Decimal)

print("oneAbove:", data["oneAbove"])
print("highPrecisionDecimal:", data["highPrecisionDecimal"])
