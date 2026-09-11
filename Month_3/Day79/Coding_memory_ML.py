import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.metrics import(mean_absolute_error, mean_squared_error, r2_score)

X = np.array([1, 2, 3, 4, 5, 6, 7, 8])
Y = np.array([3, 6, 6, 10, 11, 14, 15, 18])

#Splitting the Data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, random_state=42)

# Model
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train.reshape(-1, 1), Y_train)

pred = model.predict(X_test.reshape(-1, 1))
print(pred)
#pred = np.array(pred)
mae = mean_absolute_error(Y_test, pred)
mse = mean_squared_error(Y_test, pred)
rmse = np.sqrt(mse)
r2 = r2_score(Y_test, pred)

print("MAE: ", mae)
print("MSE: ", mse)
print("RMSE: ", rmse)
print("R2 Score: ", r2)