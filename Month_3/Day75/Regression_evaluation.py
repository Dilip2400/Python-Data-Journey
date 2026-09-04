actual = [50, 60, 70, 80, 200]

model_a = [51, 61, 69, 81, 160]

model_b = [50, 63, 68, 79, 195]

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

mae_a = mean_absolute_error(actual, model_a)
mse_a = mean_squared_error(actual, model_a)
rmse_a = np.sqrt(mse_a)
r2_a = r2_score(actual, model_a)

mae_b = mean_absolute_error(actual, model_b)
mse_b = mean_squared_error(actual, model_b)
rmse_b = np.sqrt(mse_b)
r2_b = r2_score(actual, model_b)

print("Model A")
print("MAE:", mae_a)
print("MSE:", mse_a)
print("RMSE:", rmse_a)
print("R²:", r2_a)

print("\nModel B")
print("MAE:", mae_b)
print("MSE:", mse_b)
print("RMSE:", rmse_b)
print("R²:", r2_b)