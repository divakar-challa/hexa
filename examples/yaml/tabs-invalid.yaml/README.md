# tabs-invalid.yaml

YAML indented with tab characters, which the specification forbids.

Page: https://hexaqa.com/file/structured-data/tabs-invalid-yaml

```bash
curl -fsSL -o "tabs-invalid.yaml" "https://files.hexaqa.com/yaml/tabs-invalid.yaml"
```

SHA-256: `02941a4076012f35422bd673abd9b834d4f5783934fe9379ca669b00af728681`

## Python

Python has no YAML parser in its standard library, so this is a line check, not a parser. It flags tab indentation, which YAML forbids, and the plain values that PyYAML and other YAML 1.1 loaders silently convert: NO becomes false, 0755 becomes 493, 1.10 becomes 1.1. Quote them.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
line 2: tab in the indentation, which YAML forbids
line 3: tab in the indentation, which YAML forbids
```
