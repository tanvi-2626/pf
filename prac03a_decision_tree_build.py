import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv("play_tennis.csv")
data.columns = data.columns.str.replace(" ", "")
data = pd.get_dummies(data)

X = data.drop("PlayTennis_Yes", axis=1)
y = data["PlayTennis_Yes"]

model = DecisionTreeClassifier()
model.fit(X, y)

prediction = model.predict(X.iloc[[0]])
print("Prediction:", "Yes" if prediction[0] == 1 else "No")
