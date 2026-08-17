import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 42, 51, 60, 68, 76, 85, 93],
    "Sleep_Hours": [5, 5.5, 6, 6.5, 7, 7.5, 8, 8],
    "Social_Media_Hours": [5, 5, 4.5, 4, 3.5, 3, 2.5, 2]
}

df = pd.DataFrame(data)

print(df)

correlation = df.corr(numeric_only=True)

print("\nCorrelation Matrix:")
print(correlation)

plt.scatter(df["Study_Hours"], df["Marks"])

plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.title("Study Hours vs Marks")

plt.show()

plt.scatter(
    df["Social_Media_Hours"],
    df["Marks"]
)

plt.xlabel("Social Media Hours")
plt.ylabel("Marks")

plt.title("Social Media Hours vs Marks")

plt.show()

df["Study_Minutes"] = df["Study_Hours"] * 60

print(
    df[
        [
            "Study_Hours",
            "Study_Minutes"
        ]
    ].corr()
)