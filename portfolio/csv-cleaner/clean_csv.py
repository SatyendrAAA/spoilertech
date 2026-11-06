#!/usr/bin/env python3
"""Clean a CSV without changing the original file (Python standard library only)."""

import argparse
import csv
import os
from pathlib import Path
import sys


def clean_csv(source: Path, destination: Path) -> tuple[int, int, int]:
    """Strip cell whitespace, skip blank rows and remove exact duplicate rows."""
    if source.resolve() == destination.resolve():
        raise ValueError("Input and output must be different files.")

    created = False
    try:
        with source.open("r", encoding="utf-8-sig", newline="") as input_file:
            reader = csv.reader(input_file, strict=True)
            try:
                header = [cell.strip() for cell in next(reader)]
            except StopIteration:
                raise ValueError("Input CSV is empty; a header row is required.") from None
            if not header or any(not cell for cell in header):
                raise ValueError("Every column must have a non-empty header.")
            if len({cell.casefold() for cell in header}) != len(header):
                raise ValueError("Column headers must be unique (ignoring case).")

            # Exclusive creation prevents accidental overwrites, including symlinks.
            with destination.open("x", encoding="utf-8", newline="") as output_file:
                created = True
                writer = csv.writer(output_file)
                writer.writerow(header)
                seen: set[tuple[str, ...]] = set()
                written = duplicates = blank = 0
                for row in reader:
                    if not row or all(not cell.strip() for cell in row):
                        blank += 1
                        continue
                    if len(row) != len(header):
                        raise ValueError(
                            f"Row ending on line {reader.line_num} has {len(row)} columns; "
                            f"expected {len(header)}."
                        )
                    cleaned = tuple(cell.strip() for cell in row)
                    if cleaned in seen:
                        duplicates += 1
                        continue
                    seen.add(cleaned)
                    writer.writerow(cleaned)
                    written += 1
        return written, duplicates, blank
    except (OSError, UnicodeError, csv.Error, ValueError):
        if created:
            try:
                os.unlink(destination)
            except OSError:
                pass
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description="Clean a CSV into a new file.")
    parser.add_argument("input", type=Path, help="Path to the original CSV")
    parser.add_argument("output", type=Path, help="Path for the new CSV (must not exist)")
    args = parser.parse_args()
    try:
        written, duplicates, blank = clean_csv(args.input, args.output)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    print(f"Saved {written} rows to {args.output}; removed {duplicates} duplicates and {blank} blank rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
