import pandas as pd
data = {
    "Name" : ["Dilip", "Poojitha", "Manish", "Sai"],
    "Marks" : [85, 98, 66, 33]
}

df= pd.DataFrame(data)
#print(df.head())

#print(df["Marks"])
print(df.iloc[0])
print(df[df["Marks"]>70])
df["Status"] = ["Pass", "Pass", "Pass", "Fail"]
