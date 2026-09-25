# png-truncated.png

Valid PNG header and partial IDAT, cut off before IEND.

Page: https://hexaqa.com/file/images/png-truncated-png

```bash
curl -fsSL -o "png-truncated.png" "https://files.hexaqa.com/image/png-truncated.png"
```

SHA-256: `5442ebef90a3212ce5fec1b88eb613bcf13ea075d7974af9bdd09700f3f45514`

## Python

Walk the chunks and verify each CRC. Browsers tolerate damage that strict decoders reject, so check before you store or process the image.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
truncated: the IDAT chunk needs 1252 bytes
```
