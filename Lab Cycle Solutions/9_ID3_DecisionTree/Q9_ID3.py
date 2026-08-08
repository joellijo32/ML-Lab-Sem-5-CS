import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# Load dataset
wine = load_wine()

X = wine.data
y = wine.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ID3 (Entropy)
model = DecisionTreeClassifier(
    criterion="entropy",
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Feature Importance
print("\nFeature Importance:")
for feature, importance in zip(wine.feature_names, model.feature_importances_):
    print(feature, ":", round(importance, 4))

# Visualize Decision Tree
plt.figure(figsize=(16, 8))
plot_tree(
    model,
    feature_names=wine.feature_names,
    class_names=wine.target_names,
    filled=True,
    rounded=True,
    fontsize=8
)

plt.title("Decision Tree using ID3 (Entropy)")
plt.show()