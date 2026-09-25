# bom-and-semicolons.csv

UTF-8 BOM, semicolon delimiters and comma decimal separators - the format Excel produces in most European locales.

Page: https://hexaqa.com/file/structured-data/bom-and-semicolons-csv

```bash
curl -fsSL -o "bom-and-semicolons.csv" "https://files.hexaqa.com/csv/bom-and-semicolons.csv"
```

SHA-256: `f011c1f7fd1b20aa993782865d5884ca6aa23089fabe5dc560b47c041bdf080a`

## Python

European Excel exports use semicolons and often a BOM. The utf-8-sig codec drops the BOM, and the Sniffer finds the delimiter instead of assuming a comma.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
delimiter: ';'
header: ['id', 'name', 'betrag', 'datum']
```
