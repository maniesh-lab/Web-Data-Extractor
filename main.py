import os
import sys

import pandas as pd

from scraper.fetch_page import fetch_page
from scraper.parse_data import parse_table

URL = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
REVENUE = "Revenue (USD millions)"


def to_number(column):
    """'680,985' -> 680985.0. Anything left that isn't a number becomes NaN
    (empty) instead of crashing the whole run."""
    digits_only = column.str.replace(r"[^\d.\-]", "", regex=True)  # drop commas, $ signs, spaces
    return pd.to_numeric(digits_only, errors="coerce")


def main():
    print("Fetching page...")
    html = fetch_page(URL)
    if html is None:
        print("Stopping - could not fetch the page.")
        sys.exit(1)  # a non-zero exit code tells scripts/schedulers the run failed

    print("Parsing data...")
    try:
        df = parse_table(html)
    except ValueError as e:
        print(f"Stopping - {e}")
        sys.exit(1)

    missing = [col for col in (REVENUE, "Employees") if col not in df.columns]
    if missing:
        print(f"Stopping - expected column(s) not found: {missing}. Columns found: {list(df.columns)}")
        sys.exit(1)

    df[REVENUE] = to_number(df[REVENUE])
    df["Employees"] = to_number(df["Employees"]).astype("Int64")  # Int64 (capital I) allows empty values

    bad_rows = df[REVENUE].isna().sum()
    if bad_rows:
        print(f"Note: {bad_rows} row(s) had a revenue value that couldn't be read.")

    print(df)

    os.makedirs("data", exist_ok=True)
    print("Saving CSVs...")
    df.to_csv("data/Top_USA_Companies.csv", index=False)  # index=False: the table already has a Rank column
    df.head(10).to_csv("data/Top_10_Companies.csv", index=False)
    print("Success.\n")

    print(f"Total Companies: {len(df)}")
    print(f"Highest Revenue: ${df[REVENUE].max():,.0f} million")
    print(f"Average Revenue: ${df[REVENUE].mean():,.0f} million\n")


if __name__ == "__main__":
    main()
