import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

data = {
    "Advertising": [10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 38],
    "Customers": [200, 220, 250, 280, 300, 320, 350, 380, 400, 420, 450, 480],
    "Sales": [52, 58, 65, 73, 80, 86, 95, 104, 110, 116, 125, 134]
}

df = pd.DataFrame(data)

X = df[["Advertising", "Customers"]]
y = df["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("REGRESSION ANALYSIS")
print("-------------------")
print("Advertising Coefficient:", round(model.coef_[0], 2))
print("Customers Coefficient:", round(model.coef_[1], 2))
print("MAE:", round(mae, 2))
print("R2:", round(r2, 2))

future = pd.DataFrame({
    "Advertising": [40],
    "Customers": [500]
})

prediction = model.predict(future)

print("\nFUTURE SALES PREDICTION")
print("-----------------------")
print("Advertising = 40")
print("Customers = 500")
print("Predicted Sales =", round(prediction[0], 2))
