import pandas as pd  
import numpy as np

data = {
    "Name": ["A","B","C","D","E"],
    "Marks": [50,75,93,76,88]
}

df= pd.DataFrame(data)

marks_array = df["Marks"].values
print(marks_array)

#NumPy on Data
updated_marks = marks_array + 5
print(updated_marks)

#Update in Data Frame
df["UpdatedMarks"] = updated_marks
print(df)

## Real Mini Use Case

#Simulate Marks
marks = np.random.randint(30,100, 10)  #Generates marks 

#Create Data Frame
df = pd.DataFrame({"Marks": marks})

#Add Bonus using NumPy
df["UpdatedMarks"] = df["Marks"]+5

#Add Status 
df["Status"] = np.where(df["UpdatedMarks"]>=50, "Pass", "Fail")

print(df)