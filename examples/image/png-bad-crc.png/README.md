# png-bad-crc.png

Structurally complete PNG with a single corrupted byte inside the IDAT chunk CRC.

Page: https://hexaqa.com/file/images/png-bad-crc-png

```bash
curl -fsSL -o "png-bad-crc.png" "https://files.hexaqa.com/image/png-bad-crc.png"
```

SHA-256: `10bcc5c930180c7276678fada6ab4bb9bb4768f559f2e942190fdb265e869c29`

## Python

Walk the chunks and verify each CRC. Browsers tolerate damage that strict decoders reject, so check before you store or process the image.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
bad CRC in the IDAT chunk
```
