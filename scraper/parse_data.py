import re

import pandas as pd
from bs4 import BeautifulSoup

# Wikipedia footnote markers inside cells, like [1], [a] or [note 2].
FOOTNOTE = re.compile(r"\[[^\]]*\]")


def clean_cell(text):
    return FOOTNOTE.sub("", text).strip()


def parse_table(html):
    soup = BeautifulSoup(html, "lxml")

    # class_="wikitable" matches any table whose classes include "wikitable"
    # (e.g. "wikitable sortable"), so a small class change doesn't break it.
    table = soup.find("table", class_="wikitable")
    if table is None:
        raise ValueError("Couldn't find the companies table — Wikipedia may have changed the page layout.")

    rows = table.find_all("tr")
    columns = [clean_cell(th.text) for th in rows[0].find_all("th")]  # the first row holds the column titles

    data = []
    for row in rows[1:]:  # every row after the titles
        cells = [clean_cell(td.text) for td in row.find_all("td")]
        # Skip rows that don't line up with the titles (e.g. merged cells)
        if len(cells) == len(columns):
            data.append(cells)

    # Building the DataFrame once from a list is much faster than adding
    # rows one at a time with df.loc[i] = ...
    return pd.DataFrame(data, columns=columns)
