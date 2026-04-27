import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns  

df = pd.read_csv("Titanic.csv")

print(df.info())
#Fill Missing Age - Before plotting
df["Age"].fillna(df["Age"].mean(), inplace=True)

sns.set_style("whitegrid")

#Graph 1 - Survival count
plt.figure()
sns.countplot(x="Survived", data=df)
plt.title("1. Survival count")
plt.show()

#Graph 2 - Survival by Gender
plt.figure()
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("2. Survival by Gender")
plt.show()

#Graph 3 -- Survival by class
plt.figure()
sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("3. Survival by Class")
plt.show()

#Graph 4 -- Survival by Gender + Class
plt.figure()
sns.barplot(x="Pclass", y="Survived", hue="Sex", data = df)
plt.title("4. Survival by Gender and Class")
plt.show()

#Graph 5 -- Age distribution
plt.figure()
sns.histplot(df["Age"], bins=20)
plt.title("5. Age Distribution")
plt.show()

#Graph 6 -- Fare vs Survival
plt.figure()
sns.boxplot(x="Survived", y="Fare", data=df)
plt.title("6. Fare vs Survival")
plt.show()

#Graph 7 -- Heatmap
plt.figure()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("7. Correlation Heatmap")
plt.show()

#Insights
print("\n -- Insights -- \n")
print("1. Females had significantly higher survival rate", "\n 2. First class passenger survived more than lower class",
      "\n 3. Higher fare passengers had better survival chances", "\n 4. Children had better survival than adults", "\n 5. Third class males had lowest survival rate")