from scraper import fetch_page
from scraper import parse_table

URL = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

def main():
    print("Fetching page...")
    html = fetch_page(URL)

    if html is None:
        print("Stopping- could not fetch the page.")
        exit()
    

    print("Parsing data...")
    df = parse_table(html)

    # df.rename(columns={"Revenue (USD millions)": "Revenue (USD millions)"},inplace=True) #inplace modifies directly, no new copy

    df["Revenue (USD millions)"] = df["Revenue (USD millions)"].str.replace(",","",regex=False)
    df["Revenue (USD millions)"] = df["Revenue (USD millions)"].astype(float)


    df["Employees"] = df["Employees"].str.replace(",","",regex=False)
    df["Employees"] = df["Employees"].astype(int)


    print(df)

    top_10 = df.head(10)

    
    print("Saving CSVs'...")
    df.to_csv("data/Top_USA_Companies.csv", index=False)
    top_10.to_csv("data/Top_10_Companies.csv",index=False)
    print("Success.")


    print()

    print(f"Total Companies:{len(df)}")
    print(f"Highest Revenue:${df['Revenue (USD millions)'].max()} millions")
    print(f"Average Revenue:${df['Revenue (USD millions)'].mean()} millions")


    print()

if __name__ == "__main__":
    main()