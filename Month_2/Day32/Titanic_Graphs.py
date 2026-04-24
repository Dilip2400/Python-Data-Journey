import matplotlib.pyplot as plt  
import numpy as np
import pandas as pd  

#Figure Size
x = [1,2,3]
y = [10,20,30]
#plt.figure(figsize=(8,5))
#plt.plot(x,y)
#plt.show()

#Color
#plt.plot(x,y, color='red', marker='o')
#plt.grid(True)
#plt.show()

# Bar Chart Styling
categories = ["A", "B", "C", "D", "E"]
values = [50, 70, 85, 90, 35]
plt.figure(figsize=(10,6))
#plt.bar(categories, values, color ='green')
plt.title("Category Performance")
plt.xlabel("Categories")
plt.ylabel("Values")
#plt.grid(True)
#plt.show()

#Titanic Dataset Plotting
df = pd.read_csv("Titanic.csv")
#Graph of Gender count
#df["Sex"].value_counts().plot(kind="bar", color=["blue", "pink"])
#plt.title("Gender Distribution")
#plt.xlabel("Gender")
#plt.ylabel("Count")
#plt.show()

#Survival count
plt.figure(figsize=(6,4))
df["Survived"].value_counts().plot(kind="bar")
plt.title("1. Survival count")
plt.show()

#Survival by gender
plt.figure(figsize=(6,4))
df.groupby("Sex")["Survived"].sum().plot(kind="bar")
plt.title("2. Survival by Gender")
plt.show()

#Survival rate by class
plt.figure(figsize=(6,4))
df.groupby("Pclass")["Survived"].sum().plot(kind="bar")
plt.title("3. Survival by class")
plt.show()

#Age Distribution -- Age spread
plt.figure(figsize=(6,4))
df["Age"].hist()
plt.title("4. Age Distribution")
plt.show()

#Survival by Age Group
def age_group(age):
    if age < 18:
        return "Child"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

df["AgeGroup"] = df["Age"].apply(age_group)
plt.figure(figsize=(6,4))
df.groupby("AgeGroup")["Survived"].mean().plot(kind="bar", color="green")
plt.title("5. Survival by Age Group")
plt.show()

#Fare Distribution
plt.figure(figsize=(6,4))
df["Fare"].hist()
plt.title("6. Fare Distribution")
plt.show()

#Fare Category Survival
def fare_category(fare):
    if fare<10:
        return "Low"
    elif fare<50:
        return "Medium"
    else:
        return "High"
df["FareCategory"] = df["Fare"].apply(fare_category)
plt.figure(figsize=(6,4))
df.groupby("FareCategory")["Survived"].mean().plot(kind="bar", color="pink")
plt.title("7. Survival by Fare Category")
plt.show()

#Family vs Alone
plt.figure(figsize=(8,5))
df["FamilySize"] = df["SibSp"] + df["Parch"]
df["IsAlone"] = df["FamilySize"].apply(lambda x: "Alone" if x == 0 else "With Family")
df.groupby("IsAlone")["Survived"].mean().plot(kind = "bar")
plt.title("8. Survival: Family vs Alone")
plt.show()

#Survival by both Gender and Class
plt.figure(figsize=(10,6))
df.groupby(["Sex", "Pclass"])["Survived"].mean().plot(kind="bar", color="red")
plt.title("9. Survival by Gender & Class")
plt.xlabel("Gender and Class")
plt.ylabel("Survival Rate")
plt.show()