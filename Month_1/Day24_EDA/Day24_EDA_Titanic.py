import pandas as pd  

df = pd.read_csv("Titanic.csv")
print(df.head())

#Data Frame information - to find data types and missing values in data
print("\n Info: \n", df.info()) ####################################################3
#Columns - to get column names (Names of data)
print("\n Columns: \n", df.columns)  ################################################33
#Shape - To get no. of rows and columns of data
print("\n Shape \n", df.shape) ######################################################

#Finding missing values --- .sum() gives total no. of missing values present in the data
print("\n Missing Values: \n", df.isnull().sum()) #########################################################

#To find basic stats of data (Max, Min, Mean, STD) - Helps in understanding Data Range
print(df.describe())      #######################################

#Questions --- 
#Survival count.
print("\n Survival count: \n", df["Survived"].value_counts())

#Count of Male and Female Passengers
print("\n Gender count: \n", df["Sex"].value_counts())

#GroupBY -- 
#Survival by gender -- 
print("\n Survival by Gender: \n", df.groupby("Sex")["Survived"].mean()) 
