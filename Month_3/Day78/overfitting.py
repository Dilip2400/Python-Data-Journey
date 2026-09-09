import numpy as np 

X = np.array([1, 2, 3, 4, 5, 6, 7, 8])
Y= np.array([2, 5, 10, 15, 26, 34, 50, 63])

# Splitting the Data (Train and Test)

X_train = X[:6]
Y_train = Y[:6]

X_test = X[6:]
Y_test = Y[6:]

# Degree 1 Model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

poly1 = PolynomialFeatures(degree=1)

X_train_1 = poly1.fit_transform(X_train.reshape(-1, 1))
X_test_1 = poly1.transform(X_test.reshape(-1, 1))

model1 = LinearRegression()
model1.fit(X_train_1, Y_train)

train_pred_1 = model1.predict(X_train_1)
test_pred_1 = model1.predict(X_test_1)

# Calculate

from sklearn.metrics import mean_squared_error

train_error_1 = mean_squared_error(Y_train, train_pred_1)
test_error_1 = mean_squared_error(Y_test, test_pred_1)

print("Degree 1")
print("Training MSE: ", train_error_1)
print("Testing MSE: ", test_error_1)


# Degree 2 
poly2 = PolynomialFeatures(degree=2)

X_train_2 = poly2.fit_transform(X_train.reshape(-1, 1))
X_test_2 = poly2.transform(X_test.reshape(-1, 1))

model2 = LinearRegression()
model2.fit(X_train_2, Y_train)

train_pred_2 = model2.predict(X_train_2)
test_pred_2 = model2.predict(X_test_2)

train_error_2 = mean_squared_error(Y_train, train_pred_2)
test_error_2 = mean_squared_error(Y_test, test_pred_2)

print("Degree 2")
print("Training MSE:", train_error_2)
print("Testing MSE:", test_error_2)

# Degree 8 (Overfitting Model)
poly8 = PolynomialFeatures(degree=8)

X_train_8 = poly8.fit_transform(X_train.reshape(-1, 1))
X_test_8 = poly8.transform(X_test.reshape(-1, 1))

model8 = LinearRegression()
model8.fit(X_train_8, Y_train)

train_pred_8 = model8.predict(X_train_8)
test_pred_8 = model8.predict(X_test_8)

train_error_8 = mean_squared_error(Y_train, train_pred_8)
test_error_8 = mean_squared_error(Y_test, test_pred_8)

print("Degree 8")
print("Training MSE:", train_error_8)
print("Testing MSE:", test_error_8)