import pandas as pd

data = {
    "Name": ["Dilip", "Poojitha", "Rahul", None, "Kiran", "Manish"],
    "Marks": [92, 98, None, 36, 90, 75]
}

df = pd.DataFrame(data)

#print(df)
#To find null values .isnull() is used
print(df.isnull())       
print(df.isnull().sum())

#Clean df (Remove null values)
#clean_df = df.dropna()
#print(clean_df)

#Fill the missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print(df.describe())
print(df["Name"].unique())

print(df["Name"].value_counts())

#Count Passed students.
print("Count of Passed students: ", (df["Marks"] > 35).sum())

#Average marks
print("Average marks scored: ", df["Marks"].mean())

#Find Highest marks
print("Highest marks scored: ", df["Marks"].max())

#Find minimum marks 
print("Minimum marks scored: ", df["Marks"].min())


#How many students scored above average marks. Hint - compare with mean.
print("\n Students score above average marks: \n", df[df["Marks"]>df["Marks"].mean()])

#Print topper of students
print("\n Topper \n", df.loc[df["Marks"].idxmax()])