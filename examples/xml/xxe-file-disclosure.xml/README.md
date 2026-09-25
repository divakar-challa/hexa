# xxe-file-disclosure.xml

XML declaring an external entity that reads a local file. Targets /etc/hostname - deliberately innocuous rather than /etc/passwd.

Page: https://hexaqa.com/file/structured-data/xxe-file-disclosure-xml

```bash
curl -fsSL -o "xxe-file-disclosure.xml" "https://files.hexaqa.com/xml/xxe-file-disclosure.xml"
```

SHA-256: `3b24847c3f0f1c1e34b3d8b2bee9d2229da9613a35b7163bb4842ffcaf4aae83`

## Python

Python's standard parser (expat 2.4.1 or later) refuses entity-expansion bombs and does not fetch external entities, so this file fails to parse instead of attacking you. Parsers in other languages differ: make sure DTDs and external entities are disabled in yours. For untrusted XML in Python, the defusedxml package forbids entity declarations outright.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
refused: undefined entity &xxe;: line 6, column 8
```
