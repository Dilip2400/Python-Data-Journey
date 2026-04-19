import pandas as pd  

df = pd.read_csv("Titanic.csv")
print(df.head())

#Data Frame information - to find data types and missing values in data
#print("\n Info: \n", df.info()) ####################################################3
#Columns - to get column names (Names of data)
#print("\n Columns: \n", df.columns)  ################################################33
#Shape - To get no. of rows and columns of data
#print("\n Shape \n", df.shape) ######################################################

#Finding missing values --- .sum() gives total no. of missing values present in the data
#print("\n Missing Values: \n", df.isnull().sum()) #########################################################

#To find basic stats of data (Max, Min, Mean, STD) - Helps in understanding Data Range
#print(df.describe())      #######################################

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

#Filtering specific groups
#Females only
female_df = df[df["Sex"] == "female"]
print("\n Survival rate of Females only: \n", female_df["Survived"].mean())

#Rich Females (Combining conditions)
rich_females = df[(df["Sex"] == "female") & (df["Pclass"] == 1)]
print("\n Survival rate of Rich Females: ", rich_females["Survived"].mean())

#Worst case -- Poor Male
poor_males = df[(df["Sex"] == "male") & (df["Pclass"] == 3)]
print("\n Survival rate of Poor Men: ", poor_males["Survived"].mean())

#Children vs Adults
#Age Influence check.
children = df[df["AgeGroup"] == "Child"]
adults = df[df["AgeGroup"] == "Adult"]
print("\n Survival rate of Children: ", children["Survived"].mean())
print("\n Survival rate of Adults: ", adults["Survived"].mean())

#Feature Engineering - Family Size
df["FamilySize"] = df["SibSp"] + df["Parch"]
print("\n Survivale rate by family size: \n", df.groupby("FamilySize")["Survived"].mean())

#Categorization - Family size
def family_type(size):
    if size == 0:
        return "Alone"
    elif size <=3:
        return "Small"
    else:
        return "Large"
    
df["FamilyType"] = df["FamilySize"].apply(family_type)

print("\n Survival rate by Family Type: \n", df.groupby("FamilyType")["Survived"].mean())

#Male - Survival analysis
male = df[df["Sex"] == "male"]
print("\n Survival rate by Male: ", male.groupby("Pclass")["Survived"].mean())

#Survival - Passengers travelling alone vs with Family
print("\n Survival rate of Alone Passengers: ", df[df["FamilySize"] == 0]["Survived"].mean())
print("\n Survival rate of Passengers with Family: ", df[df["FamilySize"] > 0]["Survived"].mean())

#Fare Understanding - Economic status
print("\n Average Fare Price: \n", df["Fare"].mean())
#print("\n Fare Summary: \n", df["Fare"].describe())

#Fare division
def fare_category(fare):
    if fare<10:
        return "Low"
    elif fare < 50:
        return "Medium"
    else:
        return "High"
    
df["FareCategory"] = df["Fare"].apply(fare_category)

#Survival rate by Fare Category
print("\n Survival rate by Fare Category: \n", df.groupby("FareCategory")["Survived"].mean())

#Correlation
print("\n Correlation: \n", df.corr(numeric_only=True))

#Outliers
print("\n Maximum Fare: \n", df["Fare"].max())
print("\n Minimum Fare: \n", df["Fare"].min())

#Multi Factor Analysis - Survival rate by Fare and Class

print("\n Survival rate by Fare and Class: \n", df.groupby(["Fare", "Pclass"])["Survived"].mean())

print("\n --- Insights ---\n")
print(" 1. High Fare passengers had better survival rate. \n 2. Fare is positively related to survival. \n 3. First Class passengers paid higher fare and survived, \n 4. Lower fare passengers had low survival rate")
