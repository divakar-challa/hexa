const fs = require('node:fs');

try {
  JSON.parse(fs.readFileSync('malformed-trailing-comma.json', 'utf8'));
  console.log('valid');
} catch (e) {
  console.log('invalid JSON:', e.message);
}
