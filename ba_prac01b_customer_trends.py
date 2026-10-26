import pandas as pd

data = {
    'Customer': ['A', 'B', 'C', 'D', 'E'],
    'Age': [22, 35, 28, 45, 30],
    'Purchase': [5000, 12000, 8000, 15000, 10000]
}

df = pd.DataFrame(data)

print("Customer Data:")
print(df)

print("\nAverage Age =", df['Age'].mean())
print("Average Purchase =", df['Purchase'].mean())

print("\nHighest Purchase Customer:")
print(df.loc[df['Purchase'].idxmax()])
