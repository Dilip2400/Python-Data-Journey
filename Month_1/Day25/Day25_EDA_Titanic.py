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

#Survival by class -- 
print("\n Survival by class: \n", df.groupby("Pclass")["Survived"].mean())

#Age factor
print("Average age: ", df["Age"].mean())
print("Missing age values: ", df["Age"].isnull().sum())

#Filling missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)

print("Missing Age values: ", df["Age"].isnull().sum())

# Age Group analysis
def age_group(age):
    if age <18:
        return "Child"
    elif age <60:
        return "Adult"
    else:
        return "Senior"
#Feature Engineering - Adding Age Group to Data Frame
df["AgeGroup"] = df["Age"].apply(age_group)

#Survival by Age Group
print("\n Survival by Age Group: \n", df.groupby("AgeGroup")["Survived"].mean())

#Survival of both class and gender
print("\n Survival rate by Gender, Class and Age Group: \n", df.groupby(["Sex", "Pclass", "AgeGroup"])["Survived"].mean())

print("\n --- Insights ---\n")
print("1. Females had higher survival rate than males, \n 2. First class passengers survived more than lower classes, \n 3. Children had better survival rates, \n 4. Poor adult males had the lowest survival")