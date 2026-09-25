# Checking uploaded file names

Two names from the filename edge cases: one hides its extension with an invisible right-to-left override, one uses a double extension. No download needed; the names are in the code.

All 26 filename edge cases: https://hexaqa.com/filename-edge-cases

## Python

Check uploaded file names for invisible direction controls and executable double extensions before you store or display them.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
'invoice\u202egnp.txt' ['contains an invisible direction control']
'report.pdf.exe' ['double extension .pdf.exe']
'notes.txt' ['ok']
```

## Node.js

The same checks in JavaScript.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
invoice\u202egnp.txt [ 'contains an invisible direction control' ]
report.pdf.exe [ 'double extension .pdf.exe' ]
notes.txt [ 'ok' ]
```
