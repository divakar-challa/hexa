const fs = require('node:fs');

const MAX_PIXELS = 25_000_000; // a decoder needs about 4 bytes per pixel

function imageSize(file) {
  const buf = Buffer.alloc(64 * 1024);
  const fd = fs.openSync(file, 'r');
  const h = buf.subarray(0, fs.readSync(fd, buf, 0, buf.length, 0));
  fs.closeSync(fd);
  const ascii = (a, b) => h.toString('latin1', a, b);
  if (h.subarray(0, 8).equals(Buffer.from('89504e470d0a1a0a', 'hex'))) return ['png', h.readUInt32BE(16), h.readUInt32BE(20)];
  if (ascii(0, 6) === 'GIF87a' || ascii(0, 6) === 'GIF89a') return ['gif', h.readUInt16LE(6), h.readUInt16LE(8)];
  if (ascii(0, 2) === 'BM') return ['bmp', h.readInt32LE(18), Math.abs(h.readInt32LE(22))];
  if (ascii(0, 4) === 'RIFF' && ascii(8, 12) === 'WEBP') {
    const chunk = ascii(12, 16);
    if (chunk === 'VP8 ') return ['webp', h.readUInt16LE(26) & 0x3fff, h.readUInt16LE(28) & 0x3fff];
    if (chunk === 'VP8L') {
      const bits = h.readUInt32LE(21);
      return ['webp', (bits & 0x3fff) + 1, ((bits >>> 14) & 0x3fff) + 1];
    }
    if (chunk === 'VP8X') return ['webp', h.readUIntLE(24, 3) + 1, h.readUIntLE(27, 3) + 1];
  }
  if (h[0] === 0xff && h[1] === 0xd8 && h[2] === 0xff) {
    for (let i = 2; i + 9 <= h.length && h[i] === 0xff; i += 2 + h.readUInt16BE(i + 2)) {
      const m = h[i + 1];
      if (m >= 0xc0 && m <= 0xcf && ![0xc4, 0xc8, 0xcc].includes(m)) return ['jpg', h.readUInt16BE(i + 7), h.readUInt16BE(i + 5)];
    }
    throw new Error('no JPEG frame header in the first 64 KB');
  }
  throw new Error('not a PNG, GIF, BMP, WebP or JPEG');
}

try {
  const [kind, w, h] = imageSize('gif-static.gif');
  const n = (x) => x.toLocaleString('en-US');
  console.log(w * h > MAX_PIXELS
    ? 'refused: ' + kind + ' ' + w + 'x' + h + ' is ' + n(w * h) + ' pixels, over the ' + n(MAX_PIXELS) + ' limit'
    : 'ok: ' + kind + ' ' + w + 'x' + h);
} catch (e) {
  console.log('rejected:', e.message);
}
