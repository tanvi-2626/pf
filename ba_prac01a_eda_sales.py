import pandas as pd

data = {
    'Product': ['Mobile', 'Laptop', 'Rice', 'Shirt', 'Mobile'],
    'Category': ['Electronics', 'Electronics', 'Groceries', 'Clothing', 'Electronics'],
    'Sales': [15000, 45000, 3000, 2000, 18000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nTotal Sales =", df['Sales'].sum())

category_sales = df.groupby('Category')['Sales'].sum()
print("\nSales by Category:")
print(category_sales)

print("\nStatistics:")
print(df['Sales'].describe())

print("\nInsights from EDA")
print("Total Revenue: Rs.", df['Sales'].sum())
print("Average Sale per Product: Rs.", df['Sales'].mean())
print("Best-Selling Category:", category_sales.idxmax(), "(Rs.", category_sales.max(), ")")
print("Lowest-Selling Category:", category_sales.idxmin(), "(Rs.", category_sales.min(), ")")
