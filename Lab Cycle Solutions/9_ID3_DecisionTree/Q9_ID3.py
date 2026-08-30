import matplotlib.pyplot as plt

from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import pandas as pd

online_retail = fetch_ucirepo(id=352) # id of online retail dataset= 352
df = online_retail.data.features

df = df.dropna(subset=["CustomerID"])
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

customer = df.groupby("CustomerID").add({
	"Quantity" : "sum",
	"UnitPrice" : "mean",
	"InvoiceNo" : "nunique",
	"TotalAmount" : "sum"
})

median = customer["TotalAmount"].median()

customer["Segment"] = (customer["TotalAmount"] >= median).astype(int)

X = customer[["Quantity", "UnitPrice", "InvoiceNo"]]
y = customer["Segment"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

model = DecisionTreeClassifier(criterion = "entropy", random_state = 42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy = {accuracy}")

print("\nFeature Importance: ")

for feature, importance in zip(X.columns, model.feature_importances_):
	print(f"{feature} : {importance:.4f}")
