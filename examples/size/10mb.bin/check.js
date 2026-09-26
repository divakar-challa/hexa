const crypto = require('node:crypto');
const fs = require('node:fs');

const hash = crypto.createHash('sha256');
fs.createReadStream('10mb.bin')
  .on('data', (chunk) => hash.update(chunk))
  .on('end', () => console.log(hash.digest('hex')));
