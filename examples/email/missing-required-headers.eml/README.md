# missing-required-headers.eml

A message with no Date and no Message-ID, and a body separated by a bare LF instead of CRLF.

Page: https://hexaqa.com/file/email/missing-required-headers-eml

```bash
curl -fsSL -o "missing-required-headers.eml" "https://files.hexaqa.com/email/missing-required-headers.eml"
```

SHA-256: `3a617a25fbe83b53870bbd113f6ca0adc16e8b9e30d8be066b0354be1df25576`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: ava.stone@example.test | subject: No date here
warning: no Date header
warning: no Message-ID header
body: text/plain 'Body after a bare LF.'
```
