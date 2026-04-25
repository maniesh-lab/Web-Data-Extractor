from bs4 import BeautifulSoup
import pandas as pd

def parse_table(html):
    soup = BeautifulSoup(html, "lxml")
    
    table = soup.find("table", class_="wikitable sortable")
    
    titles = table.find_all("th")
    clean_titles = [title.text.strip() for title in titles]
    
    df = pd.DataFrame(columns=clean_titles) #the elements of clean_titles gonna be column names now
    
    rows = table.find_all("tr") # the rows with data after titles in the table
    
    for i, row in enumerate(rows[1:], start=1):  # skipping the first empty bracket using [1:]

        row_data = row.find_all("td")   # each row_data inside on tr tags
        individual_row_data = [data.text.strip() for data in row_data]
        
        if len(individual_row_data) == len(clean_titles):
            df.loc[i] = individual_row_data
    
    return df   