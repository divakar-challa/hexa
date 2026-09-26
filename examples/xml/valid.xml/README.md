# valid.xml

Well-formed XML with namespaces, attributes, CDATA and a comment.

Page: https://hexaqa.com/file/structured-data/valid-xml

```bash
curl -fsSL -o "valid.xml" "https://files.hexaqa.com/xml/valid.xml"
```

SHA-256: `83894bdebdcc14d2a95a4144e89839b39b66b775dc53fde2a886a3f78549f490`

## Python

Python's standard parser (expat 2.4.1 or later) refuses entity-expansion bombs and does not fetch external entities, so this file fails to parse instead of attacking you. Parsers in other languages differ: make sure DTDs and external entities are disabled in yours. For untrusted XML in Python, the defusedxml package forbids entity declarations outright.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
parsed
```
