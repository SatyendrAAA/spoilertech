# Data Lab

A local-first CSV exploration and cleaning dashboard. Import a CSV and see record counts, missing cells, column completeness, exact duplicates, and a searchable preview. Download a cleaned CSV without sending the file to a server.

**[Try the live demo →](https://satyendraaa.github.io/spoilertech/portfolio/data-lab/)**

**This is a deterministic data tool, not an AI model, and it does not make predictions.** Once its static files have loaded, processing happens in your browser. The sample is fictional. Don't enter private information into public GitHub issues.

## Try it locally

Python 3 is enough to serve the static files (no install or API key):

```sh
cd portfolio/data-lab
python3 -m http.server 8000
```

Open `http://localhost:8000` on your own computer. The included sample loads automatically; import a `.csv` or drag one onto the upload area. The table shows up to eight matching rows; export always includes **all** clean rows, not only search matches. Use the sample button to reset.

## How it works

- Reads UTF-8 CSV files, including quoted commas, escaped quotes and multiline values.
- Trims outer whitespace from headers and cells, removes completely blank rows and exact duplicate rows, and checks row lengths and unique headers.
- Computes completeness on the resulting clean rows; it does not validate the accuracy of values. Empty data has 0% completeness.
- Export prefixes values beginning with `=`, `+`, `-`, `@`, tab, or carriage return with an apostrophe (including headers) to reduce spreadsheet formula risks. This **changes those exported values**, including negative numbers, and is not a guarantee of safety in every spreadsheet application. Always treat untrusted files cautiously.
- Original files are never modified. Data is processed in memory, with limits of 5 MB, 10,000 input data records, and 100 columns. It is not intended for large or sensitive production workflows.
- It supports comma-separated UTF-8 CSV only. It does not infer delimiters, clean fuzzy duplicates, or offer automatic recovery for malformed CSV.

The app doesn't send file contents to a server and doesn't store datasets between sessions. Serving the app still requires downloading its static files, and the source link leads to GitHub; network logs or browser extensions may have their own behavior.

## Run tests

Requires Node.js 20 or newer:

```sh
node --test portfolio/data-lab/tests/*.test.mjs
```

Run from the repository root. Tests cover parsing, quality metrics, input validation and safer export. The GitHub Actions workflow also runs the tests.

## Deployment

This static app is published with GitHub Pages from the repository's `main` branch and root folder. The nested `portfolio/data-lab/` directory is available under the corresponding path on the Pages site. Branch-based publishing serves the repository root or `/docs` and their included subdirectories; publishing the repository without enabling a static host does not make the app a website.
