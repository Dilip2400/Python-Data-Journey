import numpy as np 

X = np.array([1, 2, 3, 4, 5])
Y = np.array([1, 4, 9, 16, 25])

# Model A
from sklearn.linear_model import LinearRegression

model_a = LinearRegression()
model_a.fit(X.reshape(-1, 1), Y)

pred_a = model_a.predict(X.reshape(-1, 1))
print(pred_a)
print(model_a.predict([[6]]))

# Model B
X_squared = X**2
X_poly = np.column_stack((X, X_squared))

model_b = LinearRegression()
model_b.fit(X_poly, Y)
pred_b = model_b.predict(X_poly)

print(pred_b)
print(model_b.predict([[6, 36]]))