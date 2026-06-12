import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

data = {
    "Hours":[1,2,3,4,5,6,7,8],
    "Marks":[30,40,50,60,70,80,90,100]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print("MAE: ", mae)
print("R2: ", r2)