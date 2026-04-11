import pandas as pd
data = {
    "Name": ["Dilip", "Rahul", "Kiran", "Sai", "Manish", "Pooji"],
    "Marks": [91, 35, 88, 28, 66, 98],
    "Department": ["IT", "HR", "IT", "HR", "Finance", "IT"]
}

df = pd.DataFrame(data)

#print(df.describe())

#Adding a new feature - Status column ("Pass" or "Fail")
df["Status"] = df["Marks"].apply(lambda x: "Pass" if x >= 35 else "Fail")
#print(df)

#Grade creation
def get_grades(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 35:
        return "C"
    else:
        return "Fail"
    
df["Grades"] = df["Marks"].apply(get_grades)

print("\n Students Report \n", df)

#Average marks of students
print("\n Average Marks: \n", df["Marks"].mean())

#Find the topper of students
print("\n Topper: \n", df.loc[df["Marks"].idxmax()])        

#Students above average marks
print("\n Students with marks higher than average: \n", df[df["Marks"] > df["Marks"].mean()])

#GroupBy - Average of students per department
print("\n Average marks per department: ", df.groupby("Department")["Marks"].mean())

#GroupBy - count pass/fail per department
print("\n Count of Pass/Fail per department: \n", df.groupby("Department")["Status"].value_counts())

#Total
print("Total: ", len(df))

#Count of passed students
print("\n Count of Passed students: \n", (df["Status"] == "Pass").sum())

#Count of Failed students
print("\n Count of Failed students: \n", (df["Status"] == "Fail").sum())