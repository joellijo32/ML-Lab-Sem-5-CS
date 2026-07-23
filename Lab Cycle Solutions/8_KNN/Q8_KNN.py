import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import fashion_mnist
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import math
import time

(x_train,y_train),(x_test,y_test)=fashion_mnist.load_data()

x_train=x_train/255.0
x_test=x_test/255.0

#convert into 1 dimension
x_train=x_train.reshape(len(x_train),-1)
x_test=x_test.reshape(len(x_test),-1)

#take only the first 5000data
x_train=x_train[:5000]
y_train=y_train[:5000]
x_test=x_test[:1000]
y_test=y_test[:1000]

for i in range(3,10):
  start_time=time.time()
  K=KNeighborsClassifier(n_neighbors=i,metric='euclidean')


  P=K.fit(x_train,y_train)
  Y=P.predict(x_test)
  print(f"K value :{i}")
  print(f"Accuracy:{accuracy_score(y_test,Y)}")
  end_time=time.time()
  print(f"Time:{end_time-start_time}\n")