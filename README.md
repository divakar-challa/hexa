# HEXAQA test files

Free, deterministic test files for QA engineers and developers, mirrored from [hexaqa.com](https://hexaqa.com).
Every file is generated from source code, so none of it carries third-party copyright, and every file
has a published SHA-256 so you can prove what you downloaded.

This repository holds the curated **test packs**, the full **manifest** of all 211 files, and **code
examples** that handle specific broken files in Python and Node.js. Each example was run against the real
file, and its README shows the output it printed.

## Test packs

Each pack is a ZIP answering one question, with a README naming every file and the result a correct
implementation should produce, a machine-readable `manifest.json`, and its own `SHA256SUMS`.

| Pack | Files | Size | What it covers |
|---|---:|---:|---|
| [Upload Torture Test Pack](https://hexaqa.com/test-packs/upload-torture) | 22 | 1.0 MB | Every check on the upload validation checklist, in one archive. |
| [Filename Compatibility Pack](https://hexaqa.com/test-packs/filename-compatibility) | 26 | 13 KB | Every filename that breaks on some operating system. |
| [Encoding & Unicode Pack](https://hexaqa.com/test-packs/encoding-unicode) | 17 | 11 KB | BOMs, UTF-16, mojibake, normalization and invisible characters. |
| [Archive & ZIP Security Pack](https://hexaqa.com/test-packs/archive-security) | 13 | 12 KB | Path traversal, absolute paths, deep nesting and a decompression bomb. |
| [Document Parser Pack](https://hexaqa.com/test-packs/document-parser) | 15 | 33 KB | PDF, Word, Excel, PowerPoint, OpenDocument and EPUB, valid and broken. |
| [Image Pipeline Pack](https://hexaqa.com/test-packs/image-pipeline) | 17 | 52 KB | Every common format, both TIFF byte orders, and the ones built to break decoders. |
| [Structured Data Pack](https://hexaqa.com/test-packs/structured-data) | 14 | 41 KB | CSV, JSON, XML, YAML and NDJSON, valid and hostile. |
| [Email Parser Pack](https://hexaqa.com/test-packs/email-parser) | 19 | 19 KB | Every mail format and every header trap, in one archive. |
| [RAG Test Corpus](https://hexaqa.com/test-packs/rag-test-corpus) | 11 | 17 KB | Documents that hide facts behind real extraction traps, with an answer key. |

The same packs are served from `https://files.hexaqa.com/pack/<name>.zip`. Digests: [packs/SHA256SUMS](packs/SHA256SUMS).

## Use a pack in CI

```bash
curl -fsSLO https://files.hexaqa.com/pack/upload-torture-pack.zip
echo "ccdfb70856e375153309efea81762f6c4d680aae8237d6d2b51aba9a963d08fe  upload-torture-pack.zip" | sha256sum -c -
unzip -q upload-torture-pack.zip -d fixtures
(cd fixtures && sha256sum -c SHA256SUMS)
```

A complete GitHub Actions example is in [examples/ci/github-actions.yml](examples/ci/github-actions.yml).

The pack contains file names that some systems cannot store, which is part of the test. On Windows the
last check reports up to three files missing. The ZIP marks its non-ASCII names as UTF-8, as the format
requires, but the Windows build of Info-ZIP `unzip` (the one in Git Bash) still mangles two of them; Python's
`zipfile` keeps them intact (`python -m zipfile -e upload-torture-pack.zip fixtures`). The third,
`trailing-dot.txt.`, loses its final dot on Windows whatever extracts it, because Windows removes it.

## Code examples

Standard library only, so they run with no install. Download the file next to the script, then run it.

| File | Examples |
|---|---|
| [archive/zip-slip-traversal.zip](examples/archive/zip-slip-traversal.zip) | Python |
| [archive/absolute-path.zip](examples/archive/absolute-path.zip) | Python |
| [archive/valid-flat.zip](examples/archive/valid-flat.zip) | Python |
| [archive/modest-zip-bomb.zip](examples/archive/modest-zip-bomb.zip) | Python |
| [archive/nested-10-deep.zip](examples/archive/nested-10-deep.zip) | Python |
| [archive/corrupt-central-directory.zip](examples/archive/corrupt-central-directory.zip) | Python |
| [json/precision-loss.json](examples/json/precision-loss.json) | Node.js, Python |
| [json/deeply-nested-100000.json](examples/json/deeply-nested-100000.json) | Python, Node.js |
| [json/malformed-trailing-comma.json](examples/json/malformed-trailing-comma.json) | Python, Node.js |
| [csv/formula-injection.csv](examples/csv/formula-injection.csv) | Python, Node.js |
| [csv/bom-and-semicolons.csv](examples/csv/bom-and-semicolons.csv) | Python |
| [pdf/truncated.pdf](examples/pdf/truncated.pdf) | Python |
| [pdf/corrupt-xref.pdf](examples/pdf/corrupt-xref.pdf) | Python |
| [pdf/valid-1page.pdf](examples/pdf/valid-1page.pdf) | Python, Python |
| [image/png-truncated.png](examples/image/png-truncated.png) | Python |
| [image/png-bad-crc.png](examples/image/png-bad-crc.png) | Python |
| [image/png-valid-256.png](examples/image/png-valid-256.png) | Python, Python, Node.js |
| [image/fake-jpeg-is-executable.jpg](examples/image/fake-jpeg-is-executable.jpg) | Python, Node.js |
| [image/no-extension](examples/image/no-extension) | Python |
| [db/truncated.sqlite](examples/db/truncated.sqlite) | Python |
| [db/users.sqlite](examples/db/users.sqlite) | Python |
| [xml/xxe-file-disclosure.xml](examples/xml/xxe-file-disclosure.xml) | Python |
| [xml/billion-laughs.xml](examples/xml/billion-laughs.xml) | Python |
| [text/utf8-with-bom.txt](examples/text/utf8-with-bom.txt) | Python, Node.js |
| [text/utf16le.txt](examples/text/utf16le.txt) | Python, Node.js |
| [text/utf16be.txt](examples/text/utf16be.txt) | Python, Node.js |
| [text/latin1.txt](examples/text/latin1.txt) | Python, Node.js |
| [audio/declared-length-mismatch.wav](examples/audio/declared-length-mismatch.wav) | Python |
| [audio/truncated-header.wav](examples/audio/truncated-header.wav) | Python |
| [office/corrupt-missing-content-types.docx](examples/office/corrupt-missing-content-types.docx) | Python |
| [office/document.docx](examples/office/document.docx) | Python |
| [ebook/broken-container.epub](examples/ebook/broken-container.epub) | Python |
| [ebook/valid.epub](examples/ebook/valid.epub) | Python |
| [file names](examples/filename/checks) | Python, Node.js |
| [image/png-1x1.png](examples/image/png-1x1.png) | Python, Node.js |
| [image/png-8000x8000.png](examples/image/png-8000x8000.png) | Python, Node.js |
| [image/png-alpha-gradient.png](examples/image/png-alpha-gradient.png) | Python, Node.js |
| [image/png-interlaced.png](examples/image/png-interlaced.png) | Python, Node.js |
| [image/gif-animated.gif](examples/image/gif-animated.gif) | Python, Node.js |
| [image/gif-static.gif](examples/image/gif-static.gif) | Python, Node.js |
| [image/bmp-24bit.bmp](examples/image/bmp-24bit.bmp) | Python, Node.js |
| [image/jpeg-baseline.jpg](examples/image/jpeg-baseline.jpg) | Python, Node.js |
| [image/jpeg-tiny-16px.jpg](examples/image/jpeg-tiny-16px.jpg) | Python, Node.js |
| [image/flat-96x96.webp](examples/image/flat-96x96.webp) | Python, Node.js |
| [image/transparent-1x1.webp](examples/image/transparent-1x1.webp) | Python, Node.js |
| [email/plain-text.eml](examples/email/plain-text.eml) | Python |
| [email/html-multipart.eml](examples/email/html-multipart.eml) | Python |
| [email/with-attachment.eml](examples/email/with-attachment.eml) | Python |
| [email/attachment-tricky-filename.eml](examples/email/attachment-tricky-filename.eml) | Python |
| [email/spoofed-display-name.eml](examples/email/spoofed-display-name.eml) | Python |
| [email/missing-required-headers.eml](examples/email/missing-required-headers.eml) | Python |
| [email/unicode-headers.eml](examples/email/unicode-headers.eml) | Python |
| [email/quoted-printable.eml](examples/email/quoted-printable.eml) | Python |
| [email/inline-image-cid.eml](examples/email/inline-image-cid.eml) | Python |
| [email/forwarded-nested.eml](examples/email/forwarded-nested.eml) | Python |
| [email/winmail-tnef.eml](examples/email/winmail-tnef.eml) | Python |
| [email/long-folded-headers.eml](examples/email/long-folded-headers.eml) | Python |
| [email/empty-body.eml](examples/email/empty-body.eml) | Python |
| [email/threaded-reply.eml](examples/email/threaded-reply.eml) | Python |
| [email/dkim-spf-headers.eml](examples/email/dkim-spf-headers.eml) | Python |
| [email/mailbox.mbox](examples/email/mailbox.mbox) | Python |
| [folder/case-collision-dirs.zip](examples/folder/case-collision-dirs.zip) | Python |
| [folder/deep-path-over-260.zip](examples/folder/deep-path-over-260.zip) | Python |
| [folder/empty-directory.zip](examples/folder/empty-directory.zip) | Python |
| [folder/explicit-dir-entries.zip](examples/folder/explicit-dir-entries.zip) | Python |
| [folder/reserved-and-awkward-dirs.zip](examples/folder/reserved-and-awkward-dirs.zip) | Python |
| [folder/separator-confusion.zip](examples/folder/separator-confusion.zip) | Python |
| [folder/unicode-dir-names.zip](examples/folder/unicode-dir-names.zip) | Python |
| [archive/unicode-entry-names.zip](examples/archive/unicode-entry-names.zip) | Python |
| [archive/valid-nested-dirs.zip](examples/archive/valid-nested-dirs.zip) | Python |
| [archive/empty.zip](examples/archive/empty.zip) | Python |
| [archive/valid.tar](examples/archive/valid.tar) | Python |
| [archive/valid.tar.gz](examples/archive/valid.tar.gz) | Python |
| [office/macro-enabled.xlsm](examples/office/macro-enabled.xlsm) | Python |
| [office/spreadsheet.xlsx](examples/office/spreadsheet.xlsx) | Python, Python |
| [office/formula-injection.xlsx](examples/office/formula-injection.xlsx) | Python |
| [office/presentation.pptx](examples/office/presentation.pptx) | Python |
| [office/document.odt](examples/office/document.odt) | Python |
| [office/spreadsheet.ods](examples/office/spreadsheet.ods) | Python |
| [office/presentation.odp](examples/office/presentation.odp) | Python |
| [office/legacy-workbook.xls](examples/office/legacy-workbook.xls) | Python |
| [text/line-endings-crlf.txt](examples/text/line-endings-crlf.txt) | Python |
| [text/line-endings-lf.txt](examples/text/line-endings-lf.txt) | Python |
| [text/no-trailing-newline.txt](examples/text/no-trailing-newline.txt) | Python |
| [text/zero-width-and-rtl.txt](examples/text/zero-width-and-rtl.txt) | Python |
| [text/utf8-no-bom.txt](examples/text/utf8-no-bom.txt) | Python |
| [text/very-long-single-line.txt](examples/text/very-long-single-line.txt) | Python |
| [subtitle/valid.srt](examples/subtitle/valid.srt) | Python |
| [subtitle/overlapping-cues.srt](examples/subtitle/overlapping-cues.srt) | Python |
| [subtitle/valid.vtt](examples/subtitle/valid.vtt) | Python |
| [subtitle/missing-signature.vtt](examples/subtitle/missing-signature.vtt) | Python |
| [subtitle/comma-separator.vtt](examples/subtitle/comma-separator.vtt) | Python |
| [csv/ragged-rows.csv](examples/csv/ragged-rows.csv) | Python |
| [csv/valid-simple.csv](examples/csv/valid-simple.csv) | Python |
| [csv/quoting-nightmare.csv](examples/csv/quoting-nightmare.csv) | Python |
| [csv/1000-rows.csv](examples/csv/1000-rows.csv) | Python |
| [web/data.tsv](examples/web/data.tsv) | Python |
| [pdf/no-text-layer.pdf](examples/pdf/no-text-layer.pdf) | Python |
| [pdf/valid-500pages.pdf](examples/pdf/valid-500pages.pdf) | Python |
| [pdf/empty-zero-pages.pdf](examples/pdf/empty-zero-pages.pdf) | Python |
| [geo/points.geojson](examples/geo/points.geojson) | Python |
| [geo/malformed-coords.geojson](examples/geo/malformed-coords.geojson) | Python |
| [geo/antimeridian.geojson](examples/geo/antimeridian.geojson) | Python |
| [geo/track.gpx](examples/geo/track.gpx) | Python |
| [geo/placemarks.kml](examples/geo/placemarks.kml) | Python |
| [image/svg-plain.svg](examples/image/svg-plain.svg) | Python |
| [image/svg-with-script.svg](examples/image/svg-with-script.svg) | Python |
| [image/svg-external-entity.svg](examples/image/svg-external-entity.svg) | Python |
| [security/polyglot-gif-html.gif](examples/security/polyglot-gif-html.gif) | Python |
| [video/empty-ftyp-only.mp4](examples/video/empty-ftyp-only.mp4) | Python |
| [video/fake-mp4-wrong-magic.mp4](examples/video/fake-mp4-wrong-magic.mp4) | Python |
| [audio/silence-30s.wav](examples/audio/silence-30s.wav) | Python |
| [audio/tone-5s.wav](examples/audio/tone-5s.wav) | Python |
| [audio/very-short-10ms.wav](examples/audio/very-short-10ms.wav) | Python |
| [code/mixed-indentation.py](examples/code/mixed-indentation.py) | Python |
| [code/sample.py](examples/code/sample.py) | Python |
| [code/schema.sql](examples/code/schema.sql) | Python |
| [security/sql-injection-payloads.txt](examples/security/sql-injection-payloads.txt) | Python |
| [security/path-traversal-payloads.txt](examples/security/path-traversal-payloads.txt) | Python |
| [yaml/norway-problem.yaml](examples/yaml/norway-problem.yaml) | Python |
| [yaml/tabs-invalid.yaml](examples/yaml/tabs-invalid.yaml) | Python |
| [font/qa-sans.ttf](examples/font/qa-sans.ttf) | Python |
| [font/qa-sans.woff](examples/font/qa-sans.woff) | Python |
| [font/qa-sans.woff2](examples/font/qa-sans.woff2) | Python |
| [xml/unclosed-tag.xml](examples/xml/unclosed-tag.xml) | Python |
| [xml/valid.xml](examples/xml/valid.xml) | Python |
| [size/0b.bin](examples/size/0b.bin) | Python, Node.js |
| [size/1b.bin](examples/size/1b.bin) | Python, Node.js |
| [size/512b.bin](examples/size/512b.bin) | Python, Node.js |
| [size/1kb.bin](examples/size/1kb.bin) | Python, Node.js |
| [size/10kb.bin](examples/size/10kb.bin) | Python, Node.js |
| [size/100kb.bin](examples/size/100kb.bin) | Python, Node.js |
| [size/1mb.bin](examples/size/1mb.bin) | Python, Node.js |
| [size/5mb.bin](examples/size/5mb.bin) | Python, Node.js |
| [size/10mb.bin](examples/size/10mb.bin) | Python, Node.js |

## Every file

[manifest.json](manifest.json) lists all 211 files with format, size, MIME type, SHA-256 and a
description of the bug each one catches. Individual files are served from `https://files.hexaqa.com/<key>`, with
HTTP Range support. Browse them by category at [hexaqa.com](https://hexaqa.com).

Also on the site:

- [Generator](https://hexaqa.com/generator): CSV, JSON, NDJSON, XML, SQL, logs and binary files of any size, streamed on demand.
- [Mock API](https://hexaqa.com/mock-api-for-agent-evals): deterministic records, pagination, and failures on demand, for testing clients and AI agents.
- [RAG test corpus](https://hexaqa.com/rag-test-corpus): documents that hide facts behind real extraction traps, with an answer key.
- [File signature inspector](https://hexaqa.com/tools/file-signature-inspector): what a file really is, from its magic bytes, in your browser.

## Safety

Nothing here is malware. Some files are deliberately malformed, and a few (a zip bomb, a Zip Slip
archive, XML entity attacks) are built to be mishandled by careless software. Open them in a disposable
environment. The EICAR and GTUBE test strings are not in this repository; they are served from
`https://flagged.hexaqa.com` so that antivirus on your machine does not quarantine the rest.

## Licence

[CC0 1.0](LICENSE): public domain. Use, modify and redistribute anything here, with or without attribution.
