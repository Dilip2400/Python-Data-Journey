import pandas as pd

data = {
    "Name": ["Dilip", "Rahul", None, "Kiran"],
    "Marks": [85, None, 78, 90]
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

print(df)