import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

for item in soup.find_all("div", class_="quote"):
    text = item.find("span", class_="text").text
    author = item.find("small", class_="author").text
    
    quotes.append(text)
    authors.append(author)

df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

df.to_csv("quotes.csv", index=False)

print("quotes.csv created successfully!")