# svg-with-script.svg

SVG containing an inline <script> block and an onload attribute. The payload only calls console.log and sets document.title - it is inert and does not exfiltrate anything.

Page: https://hexaqa.com/file/images/svg-with-script-svg

```bash
curl -fsSL -o "svg-with-script.svg" "https://files.hexaqa.com/image/svg-with-script.svg"
```

SHA-256: `cda5b1d93e5c72c74f1f3444232e2b52a927757aa6e240bcf724a0748408d623`

## Python

An SVG is a document that can run script, so an uploaded one is an XSS risk when served inline. This screen is triage, not a sanitiser: serve user SVGs from a separate domain with a strict Content-Security-Policy, or rasterise them.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
unsafe to serve inline: contains <script>, has an on* event handler
```
