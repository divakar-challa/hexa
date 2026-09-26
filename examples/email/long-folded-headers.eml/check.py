import email
import re
from email import policy
from email.utils import parseaddr

RUNS = (".exe", ".scr", ".bat", ".cmd", ".com", ".js", ".vbs", ".ps1", ".msi", ".jar", ".lnk")

with open("long-folded-headers.eml", "rb") as f:
    msg = email.message_from_binary_file(f, policy=policy.default)

name, addr = parseaddr(str(msg["From"] or ""))
print("from:", addr or "(missing)", "| subject:", msg["Subject"] or "(missing)")
for header in ("Date", "Message-ID"):
    if msg[header] is None:
        print(f"warning: no {header} header")
if "@" in name and parseaddr(name)[1].lower() != addr.lower():
    print(f"warning: display name {name!r} is not the real sender")

body = msg.get_body(preferencelist=("plain", "html"))
text = body.get_content().strip() if body else ""
print(f"body: {body.get_content_type() if body else '(none)'} {text[:50]!r}")

for part in msg.iter_attachments():
    kind = part.get_content_type()
    if kind == "message/rfc822":
        print("attached message:", part.get_content()["Subject"])
        continue
    raw = part.get_filename() or ""
    base = raw.replace("\\", "/").rsplit("/", 1)[-1]
    safe = re.sub(r"[^\w.\- ]", "_", base).strip(". ") or "attachment"
    verdict = "blocked, it runs as a program" if safe.lower().endswith(RUNS) else "save as " + repr(safe)
    print(f"attachment: {kind} {raw!r}: {verdict}")
    if kind == "application/ms-tnef":
        print("  Outlook's TNEF wrapper: the real attachments are inside it")
