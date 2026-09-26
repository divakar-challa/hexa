import re

BOOLS = {"yes", "Yes", "YES", "no", "No", "NO", "on", "On", "ON", "off", "Off", "OFF",
         "true", "True", "TRUE", "false", "False", "FALSE"}

with open("tabs-invalid.yaml", encoding="utf-8") as f:
    for n, line in enumerate(f, 1):
        if re.match(r" *\t", line):
            print(f"line {n}: tab in the indentation, which YAML forbids")
            continue
        m = re.match(r"\s*(?:-\s+|[\w.-]+:\s+)([^\s\"'#][^#]*?)\s*$", line)
        value = m.group(1) if m else ""
        if value in BOOLS:
            print(f"line {n}: {value} is read as a boolean")
        elif re.fullmatch(r"0[0-7]+", value):
            print(f"line {n}: {value} is read as an octal number")
        elif re.fullmatch(r"\d+\.\d*0", value):
            print(f"line {n}: {value} is read as a float and loses its trailing zero")
        elif re.fullmatch(r"\d+(?::[0-5]?\d)+", value):
            print(f"line {n}: {value} is read as a base-60 number")
