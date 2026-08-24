import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#------------------------
# Dataset
#------------------------

data = {
    "Study_Hours": [
        1, 2, 2, 3, 3, 4, 4, 5,
        5, 6, 6, 7, 7, 8, 8, 9
    ],

    "Attendance": [
        55, 60, 68, 65, 72, 70, 78, 75,
        82, 80, 88, 85, 92, 90, 95, 96
    ],

    "Sleep_Hours": [
        5, 6, 5, 7, 6, 6, 7, 8,
        6, 7, 8, 6, 7, 8, 7, 8
    ],

    "Previous_Score": [
        42, 48, 52, 55, 58, 60, 64, 66,
        70, 72, 74, 78, 80, 84, 88, 92
    ],

    "Final_Marks": [
        40, 48, 50, 55, 59, 61, 66, 70,
        69, 75, 79, 80, 84, 89, 92, 96
    ]
}

df= pd.DataFrame(data)
print(df.head())

X =df[[
    "Study_Hours",
    "Attendance",
    "Sleep_Hours",
    "Previous_Score"
]]

y = df["Final_Marks"]

# Test - Train Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("\nIntercept:")
print(model.intercept_)
print("\nCoefficients:")
print(model.coef_)

coefficients = pd.DataFrame({
    "Feature": X.columns, "Coefficient": model.coef_
})

print("\nLearned Coefficients:")
print(coefficients)

#Predictions

predictions = model.predict(X_test)

results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})
print("\nPredictions:")
print(results)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nMAE:", mae)
print("MSE:", mse)
print("R2:", r2)

# Predict a New Student
new_student = pd.DataFrame({
    "Study_Hours": [6],
    "Attendance": [68],
    "Sleep_Hours": [7],
    "Previous_Score": [95]
})

prediction = model.predict(new_student)
print("\nPredicted marks for new student: ", prediction[0])