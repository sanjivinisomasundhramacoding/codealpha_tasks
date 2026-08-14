import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books.csv")

df["Price"] = df["Price"].str.replace("£", "", regex=False)
df["Price"] = df["Price"].str.replace("Â", "", regex=False)
df["Price"] = pd.to_numeric(df["Price"])

top_books = df.head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_books["Book Title"], top_books["Price"])

plt.title("Book Prices - Top 10 Books")
plt.xlabel("Book Title")
plt.ylabel("Price (£)")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig("book_prices.png")
plt.show()
# Price distribution histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=8)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()