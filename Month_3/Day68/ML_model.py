import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error

# Data
X = np.array([1, 2, 3, 4, 5]).reshape(-1,1)
y = np.array([35, 42, 55, 63, 72])

# Create Model
model = LinearRegression()

# Learn Relationship
model.fit(X,y)

# Learned Parameters
m = model.coef_[0]
b = model.intercept_

print("Slope: ", m)
print("Intercept: ", b)

#Predictions
predictions = model.predict(X)

print("Predictions: ", predictions)

# MSE
mse = mean_squared_error(y, predictions)
print("MSE: ", mse)

# New Prediction
new_prediction = model.predict([[6]])

print("Predicted marks for 6 hours: ", new_prediction[0])

# Visualize
plt.scatter(X, y, label="Actual Dataset")
plt.plot(X, predictions, label="Regression Line")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.legend()
plt.show()