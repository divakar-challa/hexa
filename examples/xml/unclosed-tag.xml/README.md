# unclosed-tag.xml

XML with a tag that is never closed.

Page: https://hexaqa.com/file/structured-data/unclosed-tag-xml

```bash
curl -fsSL -o "unclosed-tag.xml" "https://files.hexaqa.com/xml/unclosed-tag.xml"
```

SHA-256: `7de03c5a454c2e81def4c6bf72d0e35f80e24d7f8e2a40d60e9cabd51598477a`

## Python

Python's standard parser (expat 2.4.1 or later) refuses entity-expansion bombs and does not fetch external entities, so this file fails to parse instead of attacking you. Parsers in other languages differ: make sure DTDs and external entities are disabled in yours. For untrusted XML in Python, the defusedxml package forbids entity declarations outright.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
refused: mismatched tag: line 4, column 2
```
