const fs = require('node:fs');

const SIGNATURES = [['89504e470d0a1a0a', 'png'], ['ffd8ff', 'jpg'], ['47494638', 'gif'],
  ['255044462d', 'pdf'], ['504b0304', 'zip'], ['4d5a', 'exe'], ['7f454c46', 'elf']];

const name = 'fake-jpeg-is-executable.jpg';
const head = Buffer.alloc(16);
const fd = fs.openSync(name, 'r');
fs.readSync(fd, head, 0, 16, 0);
fs.closeSync(fd);

const hex = head.toString('hex');
const actual = (SIGNATURES.find(([sig]) => hex.startsWith(sig)) || [])[1] || 'unknown';
const dot = name.lastIndexOf('.');
const claimed = dot > 0 ? name.slice(dot + 1).toLowerCase().replace(/^jpe?g$/, 'jpg') : 'nothing';
console.log('name says ' + claimed + ', bytes say ' + actual + ': ' + (actual === claimed ? 'ok' : 'MISMATCH: reject it'));
