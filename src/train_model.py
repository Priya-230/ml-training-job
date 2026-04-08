import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("data/dataset.csv")

X = data[["age", "salary"]]
y = data["bought"]

model = LogisticRegression()
model.fit(X, y)

print("Model trained successfully")