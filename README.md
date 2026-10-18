# Web Data Extractor – Top USA Companies

## 📌 Project Overview

A Python automation tool that scrapes real-world company data from Wikipedia 
and delivers a clean, structured CSV ready for analysis or reporting.

Extracts company name, rank, revenue, and industry — automatically cleaned 
and formatted using pandas. No manual copy-paste. Just run and get data.
---

## ⚙️ Features

* Scrapes real-world data from a website
* Extracts table data (company, revenue, rank, etc.)
* Cleans and structures the data using pandas
* Exports data to CSV format
* Clear error messages if the page can't be fetched or the table layout changes
* Strips Wikipedia footnote markers (like `[a]`) before converting numbers

---

## 🛠️ Tech Stack

* Python
* requests
* BeautifulSoup (bs4)
* pandas

---

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the script:

```
python main.py
```

---

## 📂 Output

The extracted data will be saved in:

```
data/Top_USA_Companies.csv
```

Example outputs:

1.
![CSV Preview](screenshots/csv_preview.png)

2.
![Terminal output](screenshots/terminal_output.png)

---

## ⚠️ Note

Always verify a website's robots.txt and terms of service before scraping in production.
