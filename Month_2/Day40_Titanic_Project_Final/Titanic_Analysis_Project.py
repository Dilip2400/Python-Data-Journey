# 1. INTRODUCTION

"""
Titanic Data Analysis

This project analyzes the Titanic dataset to understand the key factors that
influenced passenger survival, such as gender, class, age, fare, and survival.
"""

# 2. Import Libraries

import pandas as pd  
import matplotlib.pyplot as plt  
import numpy as np
import seaborn as sns 

sns.set_style("whitegrid")

# 3. Load Data

df = pd.read_csv("Titanic.csv")
print(df.head())
print(df.info())

# 4. Data Cleaning
# Fill the missing age values
df["Age"].fillna(df["Age"].mean(), inplace=True)

# 5. Analysis & Visualization
#------------------------------------------------
#Graph 1: Survival count

plt.figure()
sns.countplot(x="Survived", data=df)
plt.title("More Passengers Did Not Survive Than Survived")
plt.xlabel("Survival (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

#-------------------------------------------------
# Graph 2: Survival by Gender

plt.figure()
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Females had Significantly Higher Survival Rate Than Males")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

#--------------------------------------------------
# Graph 3: Survival Rate by class

plt.figure()
sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("First Class Passengers Had Higher Survival Probability")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.show()

#---------------------------------------------------
# Graph 4: Survival by Class and Gender

plt.figure()
sns.barplot(x="Pclass", y="Survived", hue="Sex", data=df)
plt.title("Females Across All Classes Survived More than Males")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.show()

#-----------------------------------------------------
# Graph 5: Age Distribution

plt.figure()
sns.histplot(df["Age"], bins=20)
plt.title("Most Passengers Were Between 20 and 40 Years Old")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#---------------------------------------------------------
# Graph 6: Fare vs Survival

plt.figure()
sns.boxplot(x="Survived", y="Fare", data=df)
plt.title("Passengers Who Paid Higher Fares Had Better Survival Chances")
plt.xlabel("Survival")
plt.ylabel("Fare")
plt.show()

#-------------------------------------------------------------
# Graph 7: Correlation Heatmap

plt.figure()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Between Numerical Features")
plt.show()


#--------------------------------------------------------
# 6. Key Insights

print("\n=== KEY INSIGHTS ===\n")

print("- Females had significantly higher survival rates than males.")
print("- First class passengers had better survival probability.")
print("- Higher fare passengers were more likely to survive.")
print("- Lower class males had the lowest survival rate.")
print("- Age had a smaller impact compared to gender and class.")

#---------------------------------------------------------------------
# 7. Conclusion

print("\n=== CONCLUSION ===\n")

print(
    "The analysis indicates that gender and passenger class were the most "
    "important factors influencing survival. Women and higher-class passengers "
    "were given priority during evacuation, leading to higher survival rates."
)
