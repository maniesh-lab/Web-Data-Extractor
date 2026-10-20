# Web Data Extractor – Top USA Companies

A Python script that scrapes Wikipedia's table of the largest US companies by
revenue and saves it as a clean CSV: footnote marks removed and revenue and
employee counts turned into real numbers, ready for analysis. It also saves a
top-10 file.

It keeps all 7 columns of the table: rank, name, industry, revenue (USD
millions), revenue growth, employees and headquarters.

---

## Features

* Downloads the Wikipedia page with `requests` and finds the companies table with BeautifulSoup
* Strips Wikipedia footnote markers (like `[a]` or `[1]`) from every cell
* Turns revenue and employee counts into real numbers, and says how many revenue values couldn't be read
* Saves the full table and a top-10 table as CSV
* Prints the total, highest and average revenue at the end
* Clear error messages, and a non-zero exit code, if the page can't be fetched or the table layout changes

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Language |
| `requests` | Downloads the page |
| `beautifulsoup4` | Finds the table and reads its cells |
| `lxml` | The HTML parser BeautifulSoup uses |
| `pandas` | Cleans the numbers and saves the CSVs |

---

## Project Structure

```
Web-Data-Extractor/
│
├── scraper/
│   ├── fetch_page.py          # downloads the Wikipedia page (requests)
│   └── parse_data.py          # finds the table, strips footnotes, builds the DataFrame
│
├── data/
│   ├── Top_USA_Companies.csv  # full cleaned table (100 companies)
│   └── Top_10_Companies.csv   # first 10 rows
│
├── screenshots/
│   ├── csv_preview.png
│   └── terminal_output.png
│
├── main.py                    # entry point: fetch, parse, clean numbers, save CSVs
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

---

## How to Run

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python main.py
```

---

## Output

The extracted data is saved in two files:

```
data/Top_USA_Companies.csv   # full cleaned table
data/Top_10_Companies.csv    # first 10 rows
```

Example outputs:

1.
![CSV Preview](screenshots/csv_preview.png)

2.
![Terminal output](screenshots/terminal_output.png)

---

## Known Limitations

- It reads only the first table on the page with the `wikitable` class. If Wikipedia moves another table above it, the script stops with an error instead of saving the wrong data
- Rows that don't have one cell per column (for example, merged cells) are skipped without a message
- Revenue growth is kept as text (like `5.1%`), not turned into a number

---

## Note

Always verify a website's robots.txt and terms of service before scraping in production.

---

## Author

**Manish Pandeya** · [github.com/maniesh-lab](https://github.com/maniesh-lab)
