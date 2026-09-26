# winmail-tnef.eml

A message carrying an application/ms-tnef part named winmail.dat, which is how Outlook wraps rich formatting and attachments when it uses TNEF.

Page: https://hexaqa.com/file/email/winmail-tnef-eml

```bash
curl -fsSL -o "winmail-tnef.eml" "https://files.hexaqa.com/email/winmail-tnef.eml"
```

SHA-256: `a788036cd4a5f4d46f0a658e914bc67e824c578b8527e8913df4f37a4caf4edb`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: ava.stone@example.test | subject: Outlook rich-text message
body: text/plain 'This message used Outlook rich text.'
attachment: application/ms-tnef 'winmail.dat': save as 'winmail.dat'
  Outlook's TNEF wrapper: the real attachments are inside it
```
