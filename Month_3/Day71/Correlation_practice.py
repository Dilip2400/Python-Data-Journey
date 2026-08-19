import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

df["Study_Minutes"] = df["Study_Hours"] * 60

print(df)

correlation = df["Study_Hours"].corr(df["Study_Minutes"])
print("Correlation: ", correlation)