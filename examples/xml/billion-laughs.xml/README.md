# billion-laughs.xml

Classic entity-expansion bomb: nine levels of entities each referencing the previous ten times. Under 1 KB on disk, expands to ~1 GB of text if entity expansion is unbounded.

Page: https://hexaqa.com/file/structured-data/billion-laughs-xml

```bash
curl -fsSL -o "billion-laughs.xml" "https://files.hexaqa.com/xml/billion-laughs.xml"
```

SHA-256: `9ca01fc0e877f248ff50f66de22330cbfb71785e34f26656cf68a0aac21f642c`

## Python

Python's standard parser (expat 2.4.1 or later) refuses entity-expansion bombs and does not fetch external entities, so this file fails to parse instead of attacking you. Parsers in other languages differ: make sure DTDs and external entities are disabled in yours. For untrusted XML in Python, the defusedxml package forbids entity declarations outright.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
refused: limit on input amplification factor (from DTD and entities) breached: line 14, column 6
```
