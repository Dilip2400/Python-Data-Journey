#NumPy & Pandas Mini Project
import numpy as np
import pandas as pd  

np.random.seed(0)

names = ["Dilip", "Manish", "Sai", "Priya", "Sarath", "Vikas", "Uday", "Damu"]
marks = np.random.randint(25, 100, len(names))

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print(df)

#Feature Engineering using NumPy
df["Status"] = np.where(df["Marks"]>=35, "Pass", "Fail")

#Grade System (Pandas)
def grade(m):
    if m >=90:
        return "A+"
    elif m >= 80:
        return "A"
    elif m>= 70:
        return "B+"
    elif m>=60:
        return "B"
    elif m >=35:
        return "C"
    else:
        return "Fail"
    
df["Grades"] = df["Marks"].apply(grade)

print(df.head())

#Analysis using Pandas
print("\n Average Marks: ", df["Marks"].mean())

#Topper
print("\n Topper: \n", df.loc[df["Marks"].idxmax()])

#Passed Students
print("\n Passed Students: \n", df[df["Status"]=="Pass"])

#Grade Distribution -- Count of grades given.
print("\n Grade Count: \n", df["Grades"].value_counts())