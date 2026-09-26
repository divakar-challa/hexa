# html-multipart.eml

multipart/alternative carrying both a text/plain and a text/html version of the same message.

Page: https://hexaqa.com/file/email/html-multipart-eml

```bash
curl -fsSL -o "html-multipart.eml" "https://files.hexaqa.com/email/html-multipart.eml"
```

SHA-256: `f0092b2f4414211ce1f3d5813729cc7ed0646f9f0fd4df5fd1de1e5ffd193a07`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: ava.stone@example.test | subject: Quarterly report
body: text/plain 'Plain text version.'
```
