import pandas as pd  

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Salary": [30000, 50000, 25000, 60000, 45000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
}

df = pd.DataFrame(data)

print(df.head())
print(df.describe())

#Average Salary
print("Average salary of employees: ", df["Salary"].mean())

#Highest Salary
print("Highest salary:", df["Salary"].max())

#Employees of Salary > 40K
print("Employees of Salary above 40,000/- : ", df[df["Salary"]>40000])

#Count per department
print("Count of employees per department: ", df["Department"].value_counts())

#Highest paid employee
print("\n Highest paid employee : \n", df.loc[df["Salary"].idxmax()])

#Minimum salary
print("\n Minimum employee salary: \n", df["Salary"].min())

#Average Salary per department
print("\n Average salary per department: \n", df.groupby("Department")["Salary"].mean())