# with-attachment.eml

multipart/mixed with a base64-encoded PNG attachment and a Content-Disposition filename.

Page: https://hexaqa.com/file/email/with-attachment-eml

```bash
curl -fsSL -o "with-attachment.eml" "https://files.hexaqa.com/email/with-attachment.eml"
```

SHA-256: `ca97de3ad84e6e15180a50d27b2a9195d4a77ea10f6fce7e3ae5ff6f47c3e3bf`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: ava.stone@example.test | subject: Report with attachment
body: text/plain 'See attached.'
attachment: image/png 'chart.png': save as 'chart.png'
```
