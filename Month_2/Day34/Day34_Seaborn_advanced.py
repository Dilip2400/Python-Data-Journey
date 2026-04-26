import seaborn as sns 
import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt  

df = pd.read_csv("Titanic.csv")

#Bar Plot
sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("Survival by Class")
plt.show()

#Gender + Class
sns.barplot(x="Pclass", y="Survived", hue="Sex", data=df)
plt.title("Survival by Class and Gender")
sns.set_style("whitegrid")
plt.show()

#Violin Plot
sns.violinplot(x="Pclass", y="Age", data=df)
plt.title("Age Distribution by Class")
plt.show()

#Box Plot
sns.boxplot(x="Survived", y="Age", data = df)
plt.title("Survival by Age")
plt.show()
