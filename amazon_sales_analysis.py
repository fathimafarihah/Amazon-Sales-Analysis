import pandas as pd

df = pd.read_csv("amazon_sales_dataset.csv")

print("\nTotal Revenue:")
print(df["total_revenue"].sum())

print("\nAverage Rating:")
print(df["rating"].mean())

print("\nTop 10 Product Categories by Revenue:")
print(
    df.groupby("product_category")["total_revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Regions by Revenue:")
print(
    df.groupby("customer_region")["total_revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nPayment Method Usage:")
print(df["payment_method"].value_counts())
import matplotlib.pyplot as plt

category_revenue = (
    df.groupby("product_category")["total_revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
category_revenue.plot(kind="bar")
plt.title("Top 10 Categories by Revenue")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("top_categories_revenue.png")
plt.show()