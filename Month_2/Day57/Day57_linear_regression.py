# Import Libraries

import pandas as pd  
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression 

# Create a simple dataset
data = {
    "Hours": [1,2,3,4,5,6],
    "Marks": [30,40,50,60,70,80]
    }

df = pd.DataFrame(data)
print(df)

#Defining Feature and Target

X = df[["Hours"]] #Input // Feature
y = df["Marks"]  # Target // Output

#Model Creation
model = LinearRegression()

#Train the model
model.fit(X,y)

#Prediction
prediction = model.predict([[7]])
print(prediction)

#Visualize Regression Line
plt.scatter(df["Hours"], df["Marks"])

plt.plot(
    df["Hours"], model.predict(X)
)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Linear Regression")
plt.show()