from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
import Input
import Accuracy_Test
def MLR(x_train,x_test,y_train):
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    return y_pred

#############Implement Accuracy Models##########
def KNN(x_train,x_test,y_train,y_test):
    knn_model = KNeighborsRegressor(n_neighbors=7)
    knn_model.fit(x_train,y_train)
    y_pred=knn_model.predict(x_train)
    return y_pred

x_test_norm,x_train_norm,y_train,y_test= Input.main()
y_pred = MLR(x_train_norm,x_test_norm,y_train)
t_pred = KNN(x_train_norm,x_test_norm,y_train,y_test)
print(t_pred[0])
print(y_pred[0])
print(y_train[0])