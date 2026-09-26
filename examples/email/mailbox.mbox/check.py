import mailbox

box = mailbox.mbox("mailbox.mbox", create=False)
for i, msg in enumerate(box, 1):
    print(f"{i}. {msg['From']} | {msg['Subject']}")
print(len(box), "messages")
box.close()
