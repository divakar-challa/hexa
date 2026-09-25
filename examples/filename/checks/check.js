const BIDI = /[\u202A-\u202E\u2066-\u2069]/;
const RUNS = new Set(['exe', 'scr', 'bat', 'cmd', 'com', 'js', 'vbs', 'ps1', 'msi', 'jar', 'lnk']);

function checkName(name) {
  const problems = [];
  if (BIDI.test(name)) problems.push('contains an invisible direction control');
  const parts = name.toLowerCase().split('.');
  if (parts.length > 2 && RUNS.has(parts.at(-1))) problems.push('double extension .' + parts.at(-2) + '.' + parts.at(-1));
  return problems.length ? problems : ['ok'];
}

// Print control characters as escapes, so the output cannot reorder itself.
const show = (s) => s.replace(/[\u202A-\u202E\u2066-\u2069]/g, (c) => '\\u' + c.charCodeAt(0).toString(16));

for (const name of ['invoice\u202Egnp.txt', 'report.pdf.exe', 'notes.txt']) {
  console.log(show(name), checkName(name));
}
