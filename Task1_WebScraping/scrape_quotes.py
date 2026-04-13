import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

data = []

for i in range(len(quotes)):
    data.append({
        "Quote": quotes[i].text,
        "Author": authors[i].text
    })

df = pd.DataFrame(data)
df.to_csv("quotes.csv", index=False)
print(f"Total quotes scraped: {len(df)}")

print("Scraping completed successfully!")