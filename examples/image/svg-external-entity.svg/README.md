# svg-external-entity.svg

SVG with a DOCTYPE declaring an external entity pointing at a local file path.

Page: https://hexaqa.com/file/images/svg-external-entity-svg

```bash
curl -fsSL -o "svg-external-entity.svg" "https://files.hexaqa.com/image/svg-external-entity.svg"
```

SHA-256: `34cb8313af9e13289866d0db78d8173e91532750a8886345e6e637beefa0b53f`

## Python

An SVG is a document that can run script, so an uploaded one is an XSS risk when served inline. This screen is triage, not a sanitiser: serve user SVGs from a separate domain with a strict Content-Security-Policy, or rasterise them.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
unsafe to serve inline: declares entities (XXE)
```
