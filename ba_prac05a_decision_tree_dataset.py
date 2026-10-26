import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

data = {
    "Decision": [
        "Launch Product A", "Launch Product B", "Upgrade Product",
        "Expand Market", "Digital Marketing", "Open New Branch",
        "Online Sales", "New Technology", "Price Discount",
        "Customer Loyalty Program"
    ],
    "Success_Probability": [0.80, 0.65, 0.90, 0.70, 0.75, 0.60, 0.85, 0.78, 0.68, 0.88],
    "Failure_Probability": [0.20, 0.35, 0.10, 0.30, 0.25, 0.40, 0.15, 0.22, 0.32, 0.12],
    "Profit": [500000, 450000, 250000, 600000, 300000,
               700000, 350000, 400000, 280000, 320000],
    "Loss": [-150000, -180000, -50000, -250000, -100000,
             -300000, -80000, -120000, -90000, -70000]
}

df = pd.DataFrame(data)

df["Expected_Value"] = (
    df["Success_Probability"] * df["Profit"] +
    df["Failure_Probability"] * df["Loss"]
)

best_decision = df.loc[df["Expected_Value"].idxmax()]

print("=" * 90)
print("BUSINESS DECISION TREE ANALYSIS")
print("=" * 90)
print(df)

print("\n" + "=" * 90)
print("BEST DECISION")
print("=" * 90)
print("Decision            :", best_decision["Decision"])
print("Expected Value (EV) :", best_decision["Expected_Value"])
