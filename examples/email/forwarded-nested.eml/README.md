# forwarded-nested.eml

A forwarded message: a complete RFC 5322 message embedded as a message/rfc822 part inside another.

Page: https://hexaqa.com/file/email/forwarded-nested-eml

```bash
curl -fsSL -o "forwarded-nested.eml" "https://files.hexaqa.com/email/forwarded-nested.eml"
```

SHA-256: `5abfbe80bb797acc0730b31f7ae1d820e91760d96d0a340e0347c181095995fc`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: ava.stone@example.test | subject: Fwd: Quarterly report
body: text/plain 'Forwarding for your records.'
attached message: Quarterly report
```
