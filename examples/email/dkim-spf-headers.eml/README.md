# dkim-spf-headers.eml

A message with a realistic Received chain plus Authentication-Results, DKIM-Signature and ARC headers.

Page: https://hexaqa.com/file/email/dkim-spf-headers-eml

```bash
curl -fsSL -o "dkim-spf-headers.eml" "https://files.hexaqa.com/email/dkim-spf-headers.eml"
```

SHA-256: `ddc10028aad8088ea9d05c20e5edb33b9abf85da602a5d0c47371de0c277492c`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: ava.stone@example.test | subject: Signed message
body: text/plain 'This message carries a full authentication header '
```
