const fs = require('node:fs');

const data = JSON.parse(fs.readFileSync('precision-loss.json', 'utf8'), (key, value, ctx) =>
  typeof value === 'number' && !Number.isSafeInteger(value) && /^-?\d+$/.test(ctx?.source ?? '')
    ? BigInt(ctx.source)
    : value);

console.log('oneAbove:', data.oneAbove);
console.log('snowflakeId:', data.snowflakeId);
