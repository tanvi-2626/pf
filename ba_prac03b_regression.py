import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'Advertising_Expenditure': [10, 20, 30, 40, 50, 60, 70, 80],
    'Sales_Revenue': [25, 35, 45, 55, 65, 75, 85, 95]
}

df = pd.DataFrame(data)

X = df[['Advertising_Expenditure']]
Y = df['Sales_Revenue']

model = LinearRegression()
model.fit(X, Y)

predictions = model.predict(X)

print("Dataset:")
print(df)

print("\nRegression Equation:")
print(f"Sales Revenue = {model.coef_[0]:.2f} * Advertising Expenditure + {model.intercept_:.2f}")

print("\nPredicted Sales Revenue:")
for ad, pred in zip(df['Advertising_Expenditure'], predictions):
    print(f"Advertising = {ad}, Predicted Sales = {pred:.2f}")
