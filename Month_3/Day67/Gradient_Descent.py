import numpy as np
import matplotlib.pyplot as plt 

# Dataset
X = np.array([1, 2, 3, 4, 5], dtype = float)

y = np.array([3, 5, 7, 9, 11], dtype = float)

# Initial Model

m = 0
b = 0

learning_rate = 0.1

epochs = 10

# Prediction Function
def predict(x, m, b):
    return m*x+b

# MSE Function
def calculate_mse(actual, predicted):
    return np.mean((actual-predicted)**2)

for epoch in range(epochs):
    predictions = predict(X, m, b)
    
    mse = calculate_mse(y, predictions)
    
    print(f"Epoch {epoch+1}")
    print(f"Slope (m): {m:.2f}")
    print(f"Intercept (b): {b:.2f}")
    print(f"MSE: {mse:.2f}")
    
    print("-"*30)
    
    # Temporary manual updates
    m += 0.2
    b += 0.1

# Visualization

plt.scatter(X, y, color = "blue", label = "Actual Data")

plt.plot(X, predict(X, m, b),
         color = "red",
         label = "Current Model")

plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.legend()
plt.grid(True)
plt.show()