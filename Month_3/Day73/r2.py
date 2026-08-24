import numpy as np
from sklearn.metrics import r2_score

actual = np.array([50, 60, 70, 80, 90])

# A Reasonably good model
predicted = np.array([100, 10, 100, 20, 100])

r2 = r2_score(actual, predicted)

print("R2:", r2)

# Baseline

baseline = np.full(len(actual), actual.mean())
print("Baseline: ", baseline)

baseline_r2 = r2_score(actual, baseline)
print("Baseline R2: ", baseline_r2)