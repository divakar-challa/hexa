# plain-text.eml

A minimal, fully valid RFC 5322 message: text/plain, UTF-8, CRLF line endings and all required headers.

Page: https://hexaqa.com/file/email/plain-text-eml

```bash
curl -fsSL -o "plain-text.eml" "https://files.hexaqa.com/email/plain-text.eml"
```

SHA-256: `761804bd96c81708c2e692bcaac173aac84182ffbc078b9dd6e891f3b63fe30a`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: ava.stone@example.test | subject: Quarterly report
body: text/plain 'Hi Liam,\n\nFigures are attached. Let me know before'
```
