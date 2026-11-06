// All processing is local and deterministic; no AI or network requests are used.
export const MAX_ROWS = 10000;
export const MAX_COLUMNS = 100;

export function parseCSV(input) {
  const text = input.replace(/^\uFEFF/, '');
  const records = [];
  let row = [], field = '', quoted = false, afterQuote = false;
  function endField() {
    row.push(field);
    if (row.length > MAX_COLUMNS) throw new Error(`Limit: ${MAX_COLUMNS} columns.`);
    field = ''; afterQuote = false;
  }
  function endRow() {
    endField();
    records.push(row);
    if (records.length > MAX_ROWS + 1) throw new Error(`Limit: ${MAX_ROWS.toLocaleString()} data rows.`);
    row = [];
  }
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (quoted) {
      if (ch === '"' && text[i + 1] === '"') { field += '"'; i++; }
      else if (ch === '"') { quoted = false; afterQuote = true; }
      else field += ch;
    } else if (ch === ',') {
      endField();
    } else if (ch === '\r' || ch === '\n') {
      endRow();
      if (ch === '\r' && text[i + 1] === '\n') i++;
    } else if (ch === '"' && field === '' && !afterQuote) {
      quoted = true;
    } else if (afterQuote || ch === '"') {
      throw new Error('Invalid CSV quoting. Check for unmatched quotes or characters after a closing quote.');
    } else {
      field += ch;
    }
  }
  if (quoted) throw new Error('Unclosed quoted value in CSV.');
  if (field !== '' || row.length || afterQuote) endRow();
  return records;
}

export function analyzeCSV(text) {
  const records = parseCSV(text);
  if (!records.length) throw new Error('This file is empty. Add a header row and try again.');
  const headers = records[0].map(cell => cell.trim());
  if (headers.length > MAX_COLUMNS) throw new Error(`Limit: ${MAX_COLUMNS} columns.`);
  if (headers.some(h => !h)) throw new Error('Each column needs a non-empty header.');
  if (new Set(headers.map(h => h.toLowerCase())).size !== headers.length) throw new Error('Column names must be unique, ignoring case.');
  const seen = new Set(), rows = [];
  let duplicates = 0, blank = 0;
  for (let i = 1; i < records.length; i++) {
    const row = records[i].map(value => value.trim());
    if (row.every(value => value === '')) { blank++; continue; }
    if (row.length !== headers.length) throw new Error(`Record ${i + 1} has ${row.length} columns; expected ${headers.length}.`);
    const key = JSON.stringify(row);
    if (seen.has(key)) { duplicates++; continue; }
    seen.add(key);
    rows.push(row);
  }
  const columns = headers.map((name, i) => {
    const filled = rows.reduce((n, row) => n + (row[i] !== '' ? 1 : 0), 0);
    return {name, filled, missing: rows.length - filled, percentage: rows.length ? Math.round(filled / rows.length * 100) : 0};
  });
  const totalCells = rows.length * headers.length;
  const filledCells = columns.reduce((n, col) => n + col.filled, 0);
  return {headers, rows, duplicates, blank, inputRows: records.length - 1, columns, missing: totalCells - filledCells, completeness: totalCells ? Math.round(filledCells / totalCells * 100) : 0};
}

function encodeCell(value, safe) {
  let cell = value;
  // Defense in depth, not a substitute for treating untrusted CSV as untrusted.
  if (safe && /^[=+\-@\t\r]/.test(cell)) cell = "'" + cell;
  return /[",\r\n]/.test(cell) ? `"${cell.replace(/"/g, '""')}"` : cell;
}

export function toCSV(headers, rows, {safe = true} = {}) {
  return [headers, ...rows].map(row => row.map(cell => encodeCell(cell, safe)).join(',')).join('\r\n') + '\r\n';
}
