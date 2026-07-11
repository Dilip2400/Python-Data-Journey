import pandas as pd

#Actual and Predicted values
data = {
    "Actual": [500,1000,1500,2000],
    "Predicted": [470, 960, 1540, 1990]
}

df = pd.DataFrame(data)

#Caluculate Error
df["Error"] = df["Actual"] - df["Predicted"]

#Absolute Error
df["Absolute Error"] = abs(df["Error"])

print(df)

#Average Error
average_error = df["Absolute Error"].mean()

print("\n Average Error: ", average_error)