# mixed-indentation.py

Python that mixes tab and space indentation inside one block, which the interpreter rejects.

Page: https://hexaqa.com/file/source-code/mixed-indentation-py

```bash
curl -fsSL -o "mixed-indentation.py" "https://files.hexaqa.com/code/mixed-indentation.py"
```

SHA-256: `ebf668cedebc40c144d82aad5bc1b02c05697e8428db91faa23f44924b416c54`

## Python

The standard tabnanny module finds indentation that mixes tabs and spaces ambiguously, the kind that looks right in one editor and raises TabError in Python 3.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
mixed-indentation.py 4 '\t\ttotal += row      # this line is indented with TABS, the rest with spaces'
```
