# norway-problem.yaml

YAML 1.1 implicit-typing traps: unquoted NO becomes false, unquoted YES becomes true, version strings become floats, and leading-zero values parse as octal.

Page: https://hexaqa.com/file/structured-data/norway-problem-yaml

```bash
curl -fsSL -o "norway-problem.yaml" "https://files.hexaqa.com/yaml/norway-problem.yaml"
```

SHA-256: `17ba9fa29d8d1969a11d0f7ca1bce8c25a8421d2b0397b5ecc68616fe033332b`

## Python

Python has no YAML parser in its standard library, so this is a line check, not a parser. It flags tab indentation, which YAML forbids, and the plain values that PyYAML and other YAML 1.1 loaders silently convert: NO becomes false, 0755 becomes 493, 1.10 becomes 1.1. Quote them.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
line 2: NO is read as a boolean
line 5: ON is read as a boolean
line 6: OFF is read as a boolean
line 7: YES is read as a boolean
line 8: 1.10 is read as a float and loses its trailing zero
line 9: 0755 is read as an octal number
line 10: 12:30:00 is read as a base-60 number
line 11: yes is read as a boolean
line 12: no is read as a boolean
```
