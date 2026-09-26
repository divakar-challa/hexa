# valid.tar.gz

The gzip-compressed form of a tar archive - the ubiquitous .tar.gz.

Page: https://hexaqa.com/file/archives/valid-tar-gz

```bash
curl -fsSL -o "valid.tar.gz" "https://files.hexaqa.com/archive/valid.tar.gz"
```

SHA-256: `0da101bf8694244200910ca6601eb14a9b7cd9cc543af255392559d3521d2548`

## Python

Extract with the 'data' filter (Python 3.12+, and backported to security releases of 3.8 to 3.11). It refuses absolute paths, '..', links that point outside the folder and device files. Python 3.14 makes it the default, but passing it keeps older versions safe.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
extracted: readme.txt, logs/app.log
```
