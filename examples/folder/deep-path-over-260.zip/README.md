# deep-path-over-260.zip

An archive whose innermost file sits at a path over 300 characters long, built from 30 nested directories.

Page: https://hexaqa.com/file/folders-and-paths/deep-path-over-260-zip

```bash
curl -fsSL -o "deep-path-over-260.zip" "https://files.hexaqa.com/folder/deep-path-over-260.zip"
```

SHA-256: `8b3de365e61d959c7deb2000aacc3868c845d21592ef5dfbf722eeb50ff4858e`

## Python

Check an archive's paths before extracting it on another system. Windows reserves device names, drops trailing dots and spaces, and treats \ as a separator; Windows and macOS compare names without case, so two folders that differ only in case merge. Use orig_filename: on Windows, zipfile quietly turns backslashes into slashes.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
31 entries: 1 portability problem
  longest entry is 278 characters: extracted into any folder, it passes the 260-character limit
```
