import pandas as pd   
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic.csv")

#Comparing categories
sns.barplot(x="Pclass", y="Survived", hue="Sex",data=df)
plt.title("Survival Rate by class and Gender")
plt.show()
print("\n Females in all classes had higher survival rates than males.",
"\n First class females had the highest survival, while third class males had the lowest.")

#Age vs Survival
sns.boxplot(x="Survived", y="Age", data=df)
plt.title("Age Distribution by Survival")
plt.show()

print("\n Younger passengers had slightly higher survival rates, suggesting children were prioritized")

#Violin plot
sns.violinplot(x="Pclass", y="Age", hue="Survived", data=df)
plt.title("Age Distribution by Class and Survival")
plt.show()