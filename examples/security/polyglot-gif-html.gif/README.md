# polyglot-gif-html.gif

A file that is simultaneously a valid GIF (correct GIF89a header and dimensions) and valid HTML containing an inert script. Renders as an image to an image parser and as a page to a browser.

Page: https://hexaqa.com/file/security-and-validation/polyglot-gif-html-gif

```bash
curl -fsSL -o "polyglot-gif-html.gif" "https://flagged.hexaqa.com/security/polyglot-gif-html.gif"
```

SHA-256: `c965bb91779eaa8bbf8a03cca8ea28223de282237a38b736541b8f14eb724b5f`

## Python

A valid image can also contain HTML. Browsers that sniff content may render it as a page, running its script on your domain. Serve uploads with their stored Content-Type and X-Content-Type-Options: nosniff, ideally from a separate domain; this check flags files worth a closer look.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
starts as GIF, but the first 1 KB also contains <html, <script: a sniffing browser may render it as HTML
```
