import numpy as np
from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.0001
    y_pred = 0
    for i in range(iterations):
        y_pred = m_curr*x + b_curr
        m_deriv = -(2/n)*sum(x*(y-y_pred))
        b_deriv = -(2/n)*sum(y-y_pred)
        m_curr = m_curr - learning_rate*(m_deriv)
        b_curr = b_curr - learning_rate*(b_deriv)
        print(f"m: {m_curr} b: {b_curr} iteration: {i}")
    plt.scatter(x, y)
    plt.plot(x, y_pred)
    plt.show()
    


data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['MedHouseVal'] = data.target

X = np.array(df['AveRooms'][:10])
y = np.array(df['MedHouseVal'][:10])
# X = X.reshape(-1, 1)

gradient_descent(X, y)
