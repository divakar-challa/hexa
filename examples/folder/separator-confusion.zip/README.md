# separator-confusion.zip

Entry names containing a literal backslash, a doubled slash, a "." segment and a trailing-slash file, all of which are legal bytes that extractors interpret differently.

Page: https://hexaqa.com/file/folders-and-paths/separator-confusion-zip

```bash
curl -fsSL -o "separator-confusion.zip" "https://files.hexaqa.com/folder/separator-confusion.zip"
```

SHA-256: `478fc2728e7182256dee9406fc5deb8a4f940b6ad1d5846799cd6a24f2a8f8bc`

## Python

Check an archive's paths before extracting it on another system. Windows reserves device names, drops trailing dots and spaces, and treats \ as a separator; Windows and macOS compare names without case, so two folders that differ only in case merge. Use orig_filename: on Windows, zipfile quietly turns backslashes into slashes.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
4 entries: 3 portability problems
  'literal\\backslash.txt': a backslash is a folder separator on Windows
  'double/': empty or '.' segment
  'dot/.': empty or '.' segment
```
