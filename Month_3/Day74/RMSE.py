import numpy as np
from sklearn.metrics import(mean_absolute_error, mean_squared_error)

actual = np.array([19, 22, 36, 86, 88])

predicted = np.array([20, 23, 39, 83, 93])

mae = mean_absolute_error(actual, predicted)

mse = mean_squared_error(actual, predicted)

rmse = np.sqrt(mse)

print("MAE: ", mae)
print("MSE: ", mse)
print("RMSE: ", rmse)