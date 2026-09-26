# path-traversal-payloads.txt

A newline-delimited list of path-traversal encodings: plain, URL-encoded, double-encoded, UTF-8 overlong, backslash and mixed variants. Intended as fuzzer input, not as a file to extract.

Page: https://hexaqa.com/file/security-and-validation/path-traversal-payloads-txt

```bash
curl -fsSL -o "path-traversal-payloads.txt" "https://flagged.hexaqa.com/security/path-traversal-payloads.txt"
```

SHA-256: `d28d1320f9769e30d043f970fd9ca87134427d4e03ea395e03377e8d811bbf3e`

## Python

Decide on the string before touching the file system: undo percent-encoding (repeatedly, since payloads are often double-encoded), treat backslashes as separators, refuse absolute, drive and URL paths, normalise, then refuse anything that climbs out. It gives the same answer on Windows and Linux. Better still, store uploads under a name you generate.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
blocked '../../../etc/passwd': climbs out of the folder
blocked '..\\..\\..\\windows\\win.ini': climbs out of the folder
blocked '%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd': climbs out of the folder
blocked '%252e%252e%252fetc%252fpasswd': climbs out of the folder
blocked '..%c0%af..%c0%afetc/passwd': invalid UTF-8 once decoded
blocked '....//....//etc/passwd': has a segment Windows would rewrite
blocked '..%2F..%2F..%2Fetc%2Fpasswd': climbs out of the folder
blocked '/var/www/../../etc/passwd': absolute, drive or URL path
blocked 'file:///etc/passwd': absolute, drive or URL path
blocked '\\\\?\\C:\\windows\\win.ini': absolute, drive or URL path
blocked 'C:../../../windows/win.ini': absolute, drive or URL path
blocked '..%00/etc/passwd': contains a NUL byte
```
