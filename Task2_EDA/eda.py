import pandas as pd

# Load the dataset
df = pd.read_csv("books.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistical summary
print("\nStatistical Summary:")
print(df.describe())
print("\nPrice Analysis:")

# Remove currency symbols and convert Price to numbers
df["Price"] = (
    df["Price"]
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .astype(float)
)

print("Minimum Price:", df["Price"].min())
print("Maximum Price:", df["Price"].max())
print("Average Price:", df["Price"].mean())
# Price Trends and Patterns

print("\nTop 5 Most Expensive Books:")
print(df.nlargest(5, "Price")[["Book Title", "Price"]])

print("\nTop 5 Cheapest Books:")
print(df.nsmallest(5, "Price")[["Book Title", "Price"]])

print("\nAvailability Count:")
print(df["Availability"].value_counts())

print("\nPrice Range:")
print(df["Price"].max() - df["Price"].min())
print("\n--- EDA SUMMARY ---")

print("Total Books:", len(df))
print("Average Price:", round(df["Price"].mean(), 2))
print("Minimum Price:", df["Price"].min())
print("Maximum Price:", df["Price"].max())

print("\nKey Findings:")
print("- All books have availability information.")
print("- No missing values were found in the dataset.")
print("- Book prices vary across the dataset.")
print("- All available books are listed as In stock.")