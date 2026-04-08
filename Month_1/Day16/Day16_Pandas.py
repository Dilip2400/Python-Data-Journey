import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Salary": [30000, 50000, 25000, 60000, 45000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
}

df = pd.DataFrame(data)

#GroupBy and finding average salary per department
print(df.groupby("Department")["Salary"].mean())

#Grouping and count per department
print(df.groupby("Department")["Name"].count())

#Grouping and Highest salary per department
print(df.groupby("Department")["Salary"].max())