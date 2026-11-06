import {analyzeCSV, toCSV} from './engine.mjs';

const SAMPLE = `Name,Role,City,Status,Last contact
Aarav Mehta,Designer,Delhi,Active,2026-10-18
Meera Shah,Developer,Mumbai,Active,2026-10-22
Kabir Singh,Founder,Bengaluru,Follow up,2026-10-14
Ananya Rao,Researcher,Patna,Active,2026-10-20
Ishaan Verma,Designer,Pune,Pending,
Meera Shah,Developer,Mumbai,Active,2026-10-22
Zara Khan,Consultant,Jaipur,Follow up,2026-10-12
Rohan Das,,Kolkata,Active,2026-10-21
,,,,
`;
const $ = id => document.getElementById(id);
const maxBytes = 5 * 1024 * 1024;
let result = null;
let readVersion = 0;

function notify(text, isError = false) {
  $('message').textContent = text;
  $('message').classList.toggle('error', isError);
}
function textElement(tag, value, className) {
  const element = document.createElement(tag);
  element.textContent = value;
  if (className) element.className = className;
  return element;
}
function renderTable() {
  if (!result) return;
  const query = $('search').value.toLocaleLowerCase().trim();
  const matches = result.rows.filter(row => row.some(value => value.toLocaleLowerCase().includes(query)));
  const headerRow = document.createElement('tr');
  for (const heading of result.headers) headerRow.append(textElement('th', heading));
  $('table-head').replaceChildren(headerRow);
  const fragment = document.createDocumentFragment();
  for (const row of matches.slice(0, 8)) {
    const tr = document.createElement('tr');
    for (const value of row) tr.append(textElement('td', value || '—', value ? '' : 'empty'));
    fragment.append(tr);
  }
  if (!matches.length) {
    const tr = document.createElement('tr');
    const td = textElement('td', result.rows.length ? 'No matching records.' : 'No data rows to preview.', 'empty');
    td.colSpan = result.headers.length;
    tr.append(td); fragment.append(tr);
  }
  $('table-body').replaceChildren(fragment);
  $('table-count').textContent = `Showing ${Math.min(matches.length, 8)} of ${matches.length.toLocaleString()} ${query ? 'matching ' : ''}records`;
}
function renderColumns() {
  const fragment = document.createDocumentFragment();
  for (const col of result.columns) {
    const group = document.createElement('div');
    const top = document.createElement('div'); top.className = 'column-top';
    top.append(textElement('span', col.name), textElement('strong', `${col.percentage}%`));
    const bar = document.createElement('div'); bar.className = 'bar';
    const fill = document.createElement('span'); fill.style.width = `${col.percentage}%`; bar.append(fill);
    group.append(top, bar, textElement('div', `${col.filled.toLocaleString()} of ${result.rows.length.toLocaleString()} filled`, 'column-sub'));
    fragment.append(group);
  }
  $('columns').replaceChildren(fragment);
}
function loadText(text, name, isSample = false) {
  try {
    const next = analyzeCSV(text);
    result = next;
    $('search').value = '';
    $('dataset-name').textContent = name;
    $('dataset-description').textContent = isSample ? 'A quick look at the sample dataset.' : 'A quick look at your locally processed dataset.';
    $('preview-caption').textContent = `${next.headers.length} columns · duplicates and blank rows removed`;
    $('record-count').textContent = next.rows.length.toLocaleString();
    $('completeness').textContent = `${next.completeness}%`;
    $('duplicates').textContent = next.duplicates.toLocaleString();
    $('missing').textContent = next.missing.toLocaleString();
    $('quality-insight').textContent = next.rows.length === 0 ? 'No data rows to assess yet.' : next.missing ? `${next.missing.toLocaleString()} empty ${next.missing === 1 ? 'cell' : 'cells'} across your clean data. Review before using it.` : 'All cells in your clean data have a value. Review content accuracy separately.';
    renderTable(); renderColumns();
    notify(isSample ? 'Sample loaded. Try importing a CSV of your own.' : `Processed locally: ${next.inputRows.toLocaleString()} input rows, ${next.duplicates} duplicates and ${next.blank} blank rows removed.`);
  } catch (error) {
    notify(`${error.message} The previous dataset is still displayed.`, true);
  }
}
async function loadFile(file) {
  const version = ++readVersion;
  if (!file) return;
  if (!file.name.toLowerCase().endsWith('.csv')) { notify('Please choose a .csv file.', true); return; }
  if (file.size > maxBytes) { notify('File is larger than 5 MB. Choose a smaller CSV.', true); return; }
  try {
    const text = new TextDecoder('utf-8', {fatal: true}).decode(await file.arrayBuffer());
    if (version === readVersion) loadText(text, file.name);
  } catch {
    if (version === readVersion) notify('Could not read the file as UTF-8. Please check its encoding and try again.', true);
  }
}
function downloadCSV() {
  if (!result) return;
  const blob = new Blob([toCSV(result.headers, result.rows)], {type: 'text/csv;charset=utf-8'});
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a'); link.href = url; link.download = 'data-lab-cleaned.csv';
  document.body.append(link); link.click(); link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
  notify('Clean CSV downloaded. Formula-like values are prefixed with an apostrophe for safer spreadsheet use.');
}
$('choose-file').addEventListener('click', () => $('file-input').click());
$('choose-file-bottom').addEventListener('click', () => $('file-input').click());
$('file-input').addEventListener('change', event => { loadFile(event.target.files[0]); event.target.value = ''; });
$('load-demo').addEventListener('click', () => { readVersion++; loadText(SAMPLE, 'Sample dataset', true); });
$('search').addEventListener('input', renderTable);
$('download').addEventListener('click', downloadCSV);
const zone = $('drop-zone');
for (const event of ['dragenter', 'dragover']) zone.addEventListener(event, e => { e.preventDefault(); zone.classList.add('dragging'); });
for (const event of ['dragleave', 'drop']) zone.addEventListener(event, e => { e.preventDefault(); zone.classList.remove('dragging'); });
zone.addEventListener('drop', e => loadFile(e.dataTransfer.files[0]));
loadText(SAMPLE, 'Sample dataset', true);
