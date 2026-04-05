import pandas as pd  
data = {
    "Name" : ["Dilip", "Poojitha", "Rahul", "Kiran", "Sai"],
    "Marks" : [88, 98, 78, 55, 31]
}
df = pd.DataFrame(data)
print(df.head())

#Finding topper
print(df["Marks"].max())  #Prints maximum marks

index = df["Marks"].idxmax()

topper = df.loc[index]
print("\n -- Topper --\n", topper)

#Counting Passed students
print("-- Passed Students --")
passed_students = (df["Marks"]>35).sum()
print(passed_students)

#Sorting students
print("\n -- Sorting students (High --> Low) --")
print(df.sort_values(by = "Marks", ascending = False))

#Failed students
#index_f = (df["Marks"]<35).idxmax()
failed_students = df[df["Marks"]<35]
print("\n Failed Students \n", failed_students)

#Sorting using alphabets
print("\n Alphabetical order \n", df.sort_values(by = "Name", ascending = True))

#Print Topper Name only
print(topper["Name"])