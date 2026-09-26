# svg-plain.svg

Clean SVG with shapes and text, no scripts or external references.

Page: https://hexaqa.com/file/images/svg-plain-svg

```bash
curl -fsSL -o "svg-plain.svg" "https://files.hexaqa.com/image/svg-plain.svg"
```

SHA-256: `083bfde9c3ad9327b6d94c7337d66455717c543f2d765b3ad0a968188abcfcb0`

## Python

An SVG is a document that can run script, so an uploaded one is an XSS risk when served inline. This screen is triage, not a sanitiser: serve user SVGs from a separate domain with a strict Content-Security-Policy, or rasterise them.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
no active content found
```
