import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "http://quotes.toscrape.com/"

# Send GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract quotes and authors
for quote in soup.find_all("span", class_="text"):
    author = quote.find_next("small", class_="author").text
    print(f"Quote: {quote.text}\nAuthor: {author}\n")
