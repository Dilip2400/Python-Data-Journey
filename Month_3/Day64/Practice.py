import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

#Actual values
actual = [9, 15, 76, 88, 100]

#Predictions
#Model A
predicted_A = [7, 17, 73, 81, 96]

#Model B
predicted_B = [10, 14, 78, 91, 123]

predicted_C = [6, 12, 75, 89, 200]

predicted_D = [9, 14, 79, 93, 156]

predicted_E = [6, 20, 70, 85, 133]

print("MODEL A")
print("MAE:", mean_absolute_error(actual, predicted_A))
print("MSE:", mean_squared_error(actual, predicted_A))

print()

print("MODEL B")
print("MAE:", mean_absolute_error(actual, predicted_B))
print("MSE:", mean_squared_error(actual, predicted_B))

print()

print("MODEL C")
print("MAE:", mean_absolute_error(actual, predicted_C))
print("MSE:", mean_squared_error(actual, predicted_C))
print()
print("MODEL D")
print("MAE:", mean_absolute_error(actual, predicted_D))
print("MSE:", mean_squared_error(actual, predicted_D))

print()
print("MODEL E")
print("MAE:", mean_absolute_error(actual, predicted_E))
print("MSE:", mean_squared_error(actual, predicted_E))