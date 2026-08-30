import matplotlib.pyplot as plt

from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

online_retail = fetch_ucirepo(id=352) # id of online retail dataset= 352
print(online_retail.metadata)

print(online_retail.variables)
