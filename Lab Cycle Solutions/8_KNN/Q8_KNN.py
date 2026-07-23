import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import fashion_mnist
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import math
import time

(X_train,y_train),(X_test,y_test)=fashion_mnist.load_data()

X_train=X_train/255.0
X_test=X_test/255.0

#convert into 1 dimension
X_train=X_train.reshape(len(X_train),-1)
X_test=X_test.reshape(len(X_test),-1)

#take only the first 5000data
X_train=X_train[:5000]
y_train=y_train[:5000]
X_test=X_test[:1000]
y_test=y_test[:1000]

for i in range(3,10):
  start_time=time.time()
  K=KNeighborsClassifier(n_neighbors=i,metric='euclidean')


  P=K.fit(X_train,y_train)
  Y=P.predict(X_test)
  print(f"K value :{i}")
  print(f"Accuracy:{accuracy_score(y_test,Y)}")
  end_time=time.time()
  print(f"Time:{end_time-start_time}\n")