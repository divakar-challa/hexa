# spoofed-display-name.eml

A display name that reads as a trusted address while the real envelope address is something else entirely.

Page: https://hexaqa.com/file/email/spoofed-display-name-eml

```bash
curl -fsSL -o "spoofed-display-name.eml" "https://files.hexaqa.com/email/spoofed-display-name.eml"
```

SHA-256: `6146a3fbb9e0c1c2effc36c6bc8396a1faddc2a87b36aaa536d350049c706762`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: attacker@evil.example.test | subject: Action required: verify your account
warning: display name 'support@yourbank.example' is not the real sender
body: text/plain 'This is a harmless test fixture, not a real phishi'
```
