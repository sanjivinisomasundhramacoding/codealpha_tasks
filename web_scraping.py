import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Get website content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all books
books = soup.find_all("article", class_="product_pod")

# Empty list
data = []

# Extract details
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()

    data.append([title, price, availability])

# Create DataFrame
df = pd.DataFrame(data, columns=["Book Title", "Price", "Availability"])

# Save to CSV
df.to_csv("books.csv", index=False)

print("✅ Dataset created successfully!")
print(df)
df.to_csv("books.csv", index=False, encoding="utf-8-sig")