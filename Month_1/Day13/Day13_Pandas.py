#Working with CSV Files

#Read a CSV file
import pandas as pd  
df = pd.read_csv("students.csv")
print(df.head())

#Find topper
index = df["Marks"].idxmax()
topper = df.loc[index]

print("\n -- Topper -- \n", topper)

#Passed Students
print("\n -- Passed Students -- \n", df["Marks"]>35)

#Sorting
print(df.sort_values(by = "Marks", ascending = False))

#Failed students
print("\n -- Failed Students -- \n", df[df["Marks"] < 35])
