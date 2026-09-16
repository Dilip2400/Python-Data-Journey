import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X = np.array([1, 2, 3, 4, 5, 6, 7, 8])
Y = np.array([0, 0, 0, 1, 1, 1, 1, 1 ])

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, random_state=42)

model =LogisticRegression()
model.fit(X_train.reshape(-1, 1), Y_train)

pred = model.predict(X_test.reshape(-1, 1))
prob = model.predict_proba(X_test.reshape(-1, 1))
print(pred)
print(prob)
