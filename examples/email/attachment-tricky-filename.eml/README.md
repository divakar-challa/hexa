# attachment-tricky-filename.eml

An attachment whose filename uses RFC 2231 continuation encoding, contains a double extension and non-ASCII characters.

Page: https://hexaqa.com/file/email/attachment-tricky-filename-eml

```bash
curl -fsSL -o "attachment-tricky-filename.eml" "https://files.hexaqa.com/email/attachment-tricky-filename.eml"
```

SHA-256: `5dfc33093885d6ea39ab2ca3fcd4abe70acb1c0433515258e44a66618b4c66a0`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: ava.stone@example.test | subject: Invoice
body: text/plain 'Invoice attached.'
attachment: application/octet-stream 'счет-invoice.pdf.exe': blocked, it runs as a program
```
