# mailbox.mbox

An mbox archive of three messages, the format Gmail Takeout, Thunderbird and Apple Mail all export. Includes a body line beginning with "From " that has been escaped to ">From ".

Page: https://hexaqa.com/file/email/mailbox-mbox

```bash
curl -fsSL -o "mailbox.mbox" "https://files.hexaqa.com/email/mailbox.mbox"
```

SHA-256: `85ff4064c9efec3a74d56ef8d3abc2d064f32dd9402bde713e1ff70a216f54da`

## Python

The standard mailbox module reads mbox files message by message, handling the "From " separator lines for you.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
1. Ava Stone <ava.stone@example.test> | Quarterly report
2. Liam Vargas <liam.vargas@example.test> | Re: Quarterly report
3. Ava Stone <ava.stone@example.test> | Tricky body
3 messages
```
