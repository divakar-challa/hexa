# threaded-reply.eml

A reply carrying In-Reply-To and a References chain four messages deep.

Page: https://hexaqa.com/file/email/threaded-reply-eml

```bash
curl -fsSL -o "threaded-reply.eml" "https://files.hexaqa.com/email/threaded-reply.eml"
```

SHA-256: `93622a38599065bf45895c90078bdd1bb739898428d6c04737a0b06dd2b73863`

## Python

Parse with the modern email API (policy=default): it decodes encoded headers and bodies, and get_body picks the readable part. Treat attachment names as hostile: keep only the base name, replace unusual characters, and refuse names that run as programs. Compare the display name with the real address too, the oldest spoofing trick there is.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
from: liam.vargas@example.test | subject: Re: Quarterly report
body: text/plain 'Looks good, shipping it.\n\n> Figures are attached.'
```
