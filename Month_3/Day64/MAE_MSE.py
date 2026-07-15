import numpy as np 

#Errors from two models
model_A = np.array([2,2,2,2,20])
model_B = np.array([5,5,5,5,6])

#MAE - Mean Absolute Error
mae_A = np.mean(np.abs(model_A))
mae_B = np.mean(np.abs(model_B))

#MSE - Mean Square Error
mse_A = np.mean(model_A ** 2)
mse_B = np.mean(model_B ** 2)

print("Model A: ")
print("MAE: ", mae_A)
print("MSE: ", mse_A)

print()

print("Model B: ")
print("MAE: ", mae_B)
print("MSE: ", mse_B)