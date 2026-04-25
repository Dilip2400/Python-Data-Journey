import seaborn as sns  
import matplotlib.pyplot as plt  
import numpy as np
import pandas as pd  

df = pd.read_csv("Titanic.csv")

#Countplot
sns.countplot(x="Sex", data=df)
plt.title("Gender count")
plt.show()

#Survival by Gender 
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Survival by gender")
plt.show()

#Survival by Class
sns.countplot(x="Pclass", hue="Survived", data = df)
plt.title("Survival by Class")
plt.show()

#Histogram
sns.histplot(df["Age"], bins=20)
plt.title("Age Distribution")
plt.show()

#Class vs Age -- Box Plot
sns.boxplot(x="Pclass", y="Age", data=df)
plt.title("Age Distribution by Class")
plt.show()

#Survival vs Fare 
sns.boxplot(x="Survived", y="Fare", data=df)
plt.title("Survival vs Fare")
plt.show()


#Heat Map
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()