const neutralise = (cell) => (/^[=+\-@\t\r]/.test(cell) ? "'" + cell : cell);

for (const cell of ['=1+1', '+1+1', '-1+1', '@SUM(1:10)', 'plain text']) {
  console.log(JSON.stringify(cell), '->', JSON.stringify(neutralise(cell)));
}
