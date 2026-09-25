const fs = require('node:fs');

const raw = fs.readFileSync('utf16le.txt');
let enc = 'utf-8', start = 0;
if (raw[0] === 0xef && raw[1] === 0xbb && raw[2] === 0xbf) start = 3;
else if (raw[0] === 0xff && raw[1] === 0xfe) { enc = 'utf-16le'; start = 2; }
else if (raw[0] === 0xfe && raw[1] === 0xff) { enc = 'utf-16be'; start = 2; }

try {
  const text = new TextDecoder(enc, { fatal: true, ignoreBOM: true }).decode(raw.subarray(start));
  console.log(enc + (start ? ' with BOM' : ''), JSON.stringify(text.slice(0, 40)));
} catch (e) {
  console.log('not valid ' + enc + ':', e.message);
}
