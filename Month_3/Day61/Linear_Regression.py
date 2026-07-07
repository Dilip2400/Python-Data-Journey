import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Experience": [1,2,3,4,5],
    "Salary": [3,4,5,6,15]
}

df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()

model.fit(X,y)

predictions = model.predict(X)

print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_)

plt.scatter(df["Experience"], df["Salary"], label="Actual Data")
plt.plot(df["Experience"], predictions, label="Regression Line")

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Linear Regression")

plt.legend()

plt.show()