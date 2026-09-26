# unicode-headers.eml

Subject and display name encoded as RFC 2047 encoded-words (=?UTF-8?B?...?=) carrying CJK, Arabic and emoji.

Page: https://hexaqa.com/file/email/unicode-headers-eml

```bash
curl -fsSL -o "unicode-headers.eml" "https://files.hexaqa.com/email/unicode-headers.eml"
```

SHA-256: `b1fdce2f073aca773af37f6e5cfdac7e9c654199d488ed6ce264f0505a943ef7`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: ava.stone@example.test | subject: 請求書 — مرحبا — 🦊 quarterly
body: text/plain 'Unicode lives in the headers, not the body.'
```
