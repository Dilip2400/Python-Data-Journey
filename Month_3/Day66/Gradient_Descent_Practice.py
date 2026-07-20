# ----------------------------------
# Import Libraries
# ----------------------------------

import numpy as np
import matplotlib.pyplot as plt  


# ----------------------------------
# Dataset
# ----------------------------------

X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

print("Study Hours: ", X)
print("Actual Marks: ", y)

# Model - 1
m = 0
b = 0

predictions = m * X + b
print("M1 Predicted output: ", predictions)

# Measure Error

mse_m1 = np.mean((y - predictions)**2)
print("Model 1 MSE: ", mse_m1)

# Model - 2
m1 = 1
b1 = 0

predictions_1 = m1 * X + b1
print("Predicted output: ", predictions_1)

# Measure Error

mse_m2 = np.mean((y - predictions_1)**2)
print("Model 2 MSE: ", mse_m2)

# Model 3
m2 = 2
b2 = 0

predictions_2 = m2 * X + b2
print("Predicted output: ", predictions_2)

# Measure Error

mse_m3 = np.mean((y - predictions_2)**2)
print("Model 3 MSE: ", mse_m3)

# Model 4
m3 = 2
b3 = 1

predictions_3 = m3 * X + b3
print("Predicted output: ", predictions_3)

# Measure Error

mse_m4 = np.mean((y - predictions_3)**2)
print("Model 4 MSE: ", mse_m4)


plt.figure(figsize=(8,5))

plt.scatter(X, y, label="Actual Data")

plt.plot(X, 0*X+0, label="Model 1")

plt.plot(X, 1*X+0, label="Model 2")

plt.plot(X, 2*X+0, label="Model 3")

plt.plot(X, 2*X+1, label="Final Model")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.title("Watching the Model Improve")

plt.legend()

plt.grid(True)

plt.show()