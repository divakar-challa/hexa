# empty-body.eml

Valid headers followed by a completely empty body.

Page: https://hexaqa.com/file/email/empty-body-eml

```bash
curl -fsSL -o "empty-body.eml" "https://files.hexaqa.com/email/empty-body.eml"
```

SHA-256: `08a9c0d43008deae3ba10bd3bcf1eccfd8ad0bb0fd6c7df9696cc11b24f77ef3`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: ava.stone@example.test | subject: Subject only, no body
body: text/plain ''
```
