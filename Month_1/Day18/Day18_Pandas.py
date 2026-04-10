import pandas as pd

data = {
    "Name": ["Dilip", "Rahul", "Kiran", "Sai"],
    "Marks": [85, 35, 92, 28]
}

df = pd.DataFrame(data)

#Create new column
df["Status"] = df["Marks"]>35
print(df)
#Pass or Fail
df["Status"] = df["Marks"].apply(lambda x: "Pass" if x>35 else "Fail")
print(df["Status"])

#Apply grade

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
    
df["Status"] = df["Marks"].apply(get_grade)
print(df)