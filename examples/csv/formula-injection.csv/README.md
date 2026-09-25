# formula-injection.csv

Cells beginning with =, +, -, @ and tab, which spreadsheet applications interpret as formulas. The payloads are non-destructive: they reference HYPERLINK and a harmless calculation.

Page: https://hexaqa.com/file/structured-data/formula-injection-csv

```bash
curl -fsSL -o "formula-injection.csv" "https://files.hexaqa.com/csv/formula-injection.csv"
```

SHA-256: `c591c3c65f09f7ce69b6b47558650baf9ad511d14df5c95e0fdd9977bcbf0d0f`

## Python

Neutralise cells that a spreadsheet would run as a formula when you export user data to CSV. This is the OWASP recommendation: prefix a single quote.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
'=1+1,Formula in name column,evaluates to 2 if unescaped
```

## Node.js

The same rule in JavaScript, applied to each cell before you quote and join it.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
"=1+1" -> "'=1+1"
"+1+1" -> "'+1+1"
"-1+1" -> "'-1+1"
"@SUM(1:10)" -> "'@SUM(1:10)"
"plain text" -> "plain text"
```
