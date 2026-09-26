# inline-image-cid.eml

multipart/related where the HTML body references an inline image through a cid: URL.

Page: https://hexaqa.com/file/email/inline-image-cid-eml

```bash
curl -fsSL -o "inline-image-cid.eml" "https://files.hexaqa.com/email/inline-image-cid.eml"
```

SHA-256: `3493781785165968715bd68abbd2d8a771ca8b49ee37ed73062bfa5a0bcf1f8a`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: ava.stone@example.test | subject: Inline image
body: text/html '<html><body><p>Chart:</p><img src="cid:chart@examp'
attachment: image/png 'chart.png': save as 'chart.png'
```
