# CSV Cleaner

A small, dependency-free Python tool that cleans a CSV file into a **new** file. It's a portfolio example of a practical data-cleanup task—not a hosted service.

## What it does

- Removes leading and trailing whitespace from headers and cells.
- Removes fully blank rows and exact duplicate rows **after trimming**; keeps the first occurrence.
- Checks for missing or duplicate column names and rows with the wrong number of columns.
- Reads UTF-8 CSV files (including an optional BOM) and writes UTF-8 CSV. Quoted commas and multiline values are supported by Python's CSV parser.
- Refuses to overwrite an existing output file. If a parsing error occurs, it removes the incomplete output.

It does not validate email addresses, merge similar records, change letter case, or protect against spreadsheet formula injection. Review the result before using it, and take care opening untrusted CSVs in spreadsheet software. All rows used for deduplication are kept in memory, so this example is not intended for very large files.

## Try it

Requires Python 3.9 or newer. From this directory:

```sh
python3 clean_csv.py examples/sample.csv cleaned.csv
```

Expected message:

```text
Saved 2 rows to cleaned.csv; removed 1 duplicates and 1 blank rows.
```

The original sample remains unchanged. To rerun, choose a different output filename or remove your previous output manually. Don't commit real customer data.

Run the tests:

```sh
python3 -m unittest discover -s tests -v
```
