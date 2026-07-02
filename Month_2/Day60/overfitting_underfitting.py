import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# -------------------------------
# Dataset
# -------------------------------

X = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)

y = np.array([3,5,7,8,11,13,14,16,18,21])

# Smooth X values for plotting
X_plot = np.linspace(1,10,100).reshape(-1,1)

# -------------------------------
# Linear Regression (Underfitting)
# -------------------------------

linear = LinearRegression()
linear.fit(X,y)

y_linear = linear.predict(X_plot)

# -------------------------------
# Polynomial Degree 2 (Good Fit)
# -------------------------------

poly2 = PolynomialFeatures(degree=2)

X_poly2 = poly2.fit_transform(X)
X_plot2 = poly2.transform(X_plot)

model2 = LinearRegression()
model2.fit(X_poly2,y)

y_poly2 = model2.predict(X_plot2)

# -------------------------------
# Polynomial Degree 9 (Overfitting)
# -------------------------------

poly9 = PolynomialFeatures(degree=9)

X_poly9 = poly9.fit_transform(X)
X_plot9 = poly9.transform(X_plot)

model9 = LinearRegression()
model9.fit(X_poly9,y)

y_poly9 = model9.predict(X_plot9)

# -------------------------------
# Plot
# -------------------------------

plt.figure(figsize=(12,7))

plt.scatter(X,y,color="black",label="Actual Data")

plt.plot(
    X_plot,
    y_linear,
    label="Underfitting (Linear)"
)

plt.plot(
    X_plot,
    y_poly2,
    label="Good Fit (Degree 2)"
)

plt.plot(
    X_plot,
    y_poly9,
    label="Overfitting (Degree 9)"
)

plt.title("Underfitting vs Good Fit vs Overfitting")

plt.xlabel("X")

plt.ylabel("Y")

plt.legend()

plt.show()