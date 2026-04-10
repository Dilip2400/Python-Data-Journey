#GroupBy Level 2

import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Salary": [30000, 50000, 25000, 60000, 45000, 70000],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"]
}

df = pd.DataFrame(data)

#Multiple Aggregations
print("\n Mean, Max and Min of Salary per department \n", df.groupby("Department")["Salary"].agg(["mean", "max", "min"]))

#Group Size
print("\n Group Size \n", df.groupby("Department").size())

#Sort Group Results
print("\n Sorting Group in Ascending order \n",df.groupby("Department")["Salary"].mean().sort_values(ascending=True))

avg_salary = df.groupby("Department")["Salary"].mean()
print("\n Departments with AVG Salary > 40K ", avg_salary[avg_salary > 40000])