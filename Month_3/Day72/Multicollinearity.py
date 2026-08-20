import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Previous_Score": [45, 50, 55, 60, 65, 70, 75, 80],
    "Final_Marks": [40, 48, 53, 61, 66, 72, 78, 85]
}

df = pd.DataFrame(data)

print(df)

df["Study_Minutes"] = (df["Study_Hours"] * 60 + [2, -3, 4, -2, 3, -4, 2, -3])

X = df[
    [
        "Study_Hours",
        "Study_Minutes",
        "Previous_Score"
    ]
]
y = df["Final_Marks"]

print("\nFeature Correlation:")
print(X.corr())

# Train the Model
model = LinearRegression()
model.fit(X,y)
print("\nCoefficients:")

for feature, coefficient in zip(
    X.columns,
    model.coef_
):
    print(feature, ":", coefficient)

print(df[["Study_Hours", "Study_Minutes"]].corr())