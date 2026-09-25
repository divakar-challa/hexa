const fs = require('node:fs');

try {
  JSON.parse(fs.readFileSync('deeply-nested-100000.json', 'utf8'));
  console.log('parsed');
} catch (e) {
  console.log('rejected:', e.name, e.message);
}
