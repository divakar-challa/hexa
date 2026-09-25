# corrupt-central-directory.zip

Valid local file headers, but the central directory signature is overwritten with garbage.

Page: https://hexaqa.com/file/archives/corrupt-central-directory-zip

```bash
curl -fsSL -o "corrupt-central-directory.zip" "https://files.hexaqa.com/archive/corrupt-central-directory.zip"
```

SHA-256: `d1194edeac6e322b76436927038138a9dc8325a93fc5daed8e399df8b68ed7d5`

## Python

Open it inside a try block and report the failure to the user, instead of letting a background job die on it later.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
rejected: Bad magic number for central directory
```
