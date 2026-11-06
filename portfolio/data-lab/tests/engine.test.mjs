import test from 'node:test';
import assert from 'node:assert/strict';
import {parseCSV, analyzeCSV, toCSV, MAX_ROWS} from '../engine.mjs';

test('supports UTF-8 BOM, quoted commas, escaped quotes and multiline cells', () => {
  const parsed = parseCSV('\ufeffname,note\r\nAlice,"hello, ""friend""\nsecond line"\r\n');
  assert.deepEqual(parsed, [['name','note'], ['Alice','hello, "friend"\nsecond line']]);
});

test('trims data, removes duplicate and blank records, and measures clean cells', () => {
  const data = analyzeCSV(' name ,city\n Alice , Patna\nAlice,Patna\nBob, \n,\n');
  assert.deepEqual(data.headers, ['name', 'city']);
  assert.deepEqual(data.rows, [['Alice', 'Patna'], ['Bob', '']]);
  assert.equal(data.duplicates, 1);
  assert.equal(data.blank, 1);
  assert.equal(data.inputRows, 4);
  assert.equal(data.missing, 1);
  assert.equal(data.completeness, 75);
  assert.equal(data.columns[1].percentage, 50);
});

test('rejects malformed CSV, invalid headers and non-rectangular rows', () => {
  for (const csv of ['', 'a,A\n1,2', 'a,\n1,2', 'a,b\n1', 'a,b\n"x"oops,2', 'a,b\n"unclosed,2', 'a,b\nabc"oops,2']) {
    assert.throws(() => analyzeCSV(csv));
  }
  assert.throws(() => analyzeCSV(Array.from({length: 101}, (_, i) => `h${i}`).join(',')), /100 columns/);
});

test('rejects more than the row limit including otherwise blank records', () => {
  assert.throws(() => analyzeCSV('a\n' + 'x\n'.repeat(MAX_ROWS + 1)), /10,000 data rows/);
});

test('empty dataset has defined completeness and column health', () => {
  const data = analyzeCSV('name,city\n');
  assert.equal(data.completeness, 0);
  assert.equal(data.columns[0].percentage, 0);
  assert.deepEqual(data.rows, []);
});

test('export escapes CSV and prefixes formula-like values including headers', () => {
  const csv = toCSV(['=header', 'note'], [['+cmd', 'quoted, "yes"'], ['-5', '@name'], ['hello\nworld', 'ok']]);
  assert.deepEqual(parseCSV(csv), [["'=header", 'note'], ["'+cmd", 'quoted, "yes"'], ["'-5", "'@name"], ['hello\nworld', 'ok']]);
});

test('CSV export can opt out of formula prefixing in the engine', () => {
  assert.equal(toCSV(['name'], [['=1+1']], {safe:false}), 'name\r\n=1+1\r\n');
});
