import pandas as pd  
import matplotlib.pyplot as plt  
import numpy as np 
import seaborn as sns 

df = pd.read_csv("Titanic.csv")

#Combining multiple graphs
fig, axes = plt.subplots(1,2, figsize=(12,5))

sns.countplot(x="Sex", data=df, ax=axes[0])
axes[0].set_title("Gender Count")

sns.countplot(x="Survived", data=df, ax=axes[1])
axes[1].set_title("Survival count")

plt.tight_layout()
plt.show()

#2X2 Graphs View
fig, axes = plt.subplots(2,2, figsize=(12,10))

sns.countplot(x="Sex", data=df, ax=axes[0,0])
sns.countplot(x="Pclass", data=df, ax=axes[0,1])
sns.histplot(df["Age"], ax=axes[1,0])
sns.boxplot(x="Survived", y="Fare", data=df, ax=axes[1,1])

plt.tight_layout()
plt.show()

#Highlighting important insights
plt.figure()
sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("Higher Class --> Higher Survival Probability")
plt.show()

#Sorting before plotting
df["Pclass"].value_counts().sort_index().plot(kind="bar")
plt.show()