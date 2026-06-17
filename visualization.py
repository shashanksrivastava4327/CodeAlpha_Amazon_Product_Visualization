import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("amazon.csv")

print(df.head())
print(df.info())

df = df.dropna()

plt.figure(figsize=(10,6))

df['category'].value_counts().head(10).plot(
    kind='bar'
)

plt.title("Top 10 Product Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=90)

plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.savefig("category_chart.png")
plt.show()

plt.figure(figsize=(12,6))

sns.histplot(
    df['rating'],
    bins=20,
    kde=True
)

plt.title("Product Rating Distribution")
plt.subplots_adjust(bottom=0.3)
plt.savefig("rating_distribution.png")
plt.show()

if 'discount_percentage' in df.columns:

    plt.figure(figsize=(8,5))

    sns.histplot(
        df['discount_percentage'],
        bins=20
    )

    plt.title("Discount Percentage Distribution")
    plt.subplots_adjust(bottom=0.3)

    plt.savefig("discount_distribution.png")
    plt.show()

top_products = df.sort_values(
    by='rating',
    ascending=False
).head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x='rating',
    y='product_name',
    data=top_products
)

plt.title("Top Rated Products")

plt.tight_layout()
plt.subplots_adjust(bottom=0.3)

plt.savefig("top_products.png")
plt.show()