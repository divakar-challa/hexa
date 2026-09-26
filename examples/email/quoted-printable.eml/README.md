# quoted-printable.eml

A quoted-printable body with accented characters, soft line breaks and an = sign at a wrap boundary.

Page: https://hexaqa.com/file/email/quoted-printable-eml

```bash
curl -fsSL -o "quoted-printable.eml" "https://files.hexaqa.com/email/quoted-printable.eml"
```

SHA-256: `74a8ec24d3d75585cd8eb718b6fa01b4cd1e5493b20b53fd9c04b417bd15ce28`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: ava.stone@example.test | subject: Quoted printable
body: text/plain 'Café, naïve, Zürich. Une phrase assez longue pour '
```
