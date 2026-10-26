import pandas as pd

data = {
    'Age': [22, 25, 28, 30, 35, 40, 45, 50],
    'Experience': [1, 3, 5, 7, 10, 12, 15, 18],
    'Salary': [25000, 30000, 35000, 40000, 50000, 60000, 70000, 85000]
}

df = pd.DataFrame(data)

corr_matrix = df.corr()

print("Dataset:")
print(df)
print("\nCorrelation Matrix:")
print(corr_matrix.round(2))
