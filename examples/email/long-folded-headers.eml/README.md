# long-folded-headers.eml

Headers folded across many continuation lines, including a To: field with 25 recipients and a 300-character subject.

Page: https://hexaqa.com/file/email/long-folded-headers-eml

```bash
curl -fsSL -o "long-folded-headers.eml" "https://files.hexaqa.com/email/long-folded-headers.eml"
```

SHA-256: `f59190b8aa44837cefff19dd8dc1e2b1eb45ac4f4b9b7e0af44bb571238b9f62`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: ava.stone@example.test | subject: A deliberately long subject line that keeps going well past the classic seventy-eight character limit so that it has to be folded across several continuation lines by any correct implementation and unfolded again on the way back in
body: text/plain 'Check that every one of the 25 recipients survived'
```
