#Analysis into clean and structured report

## 1. INTRODUCTION - What is this Analysis about?
#Example -- This analysis explores the Titanic dataset to understand the factore that influenced passenger survival.

## 2. Dataset Overview -- What data are you using?
#Example -- The dataset contains passenger details such as age, gender, class, fare, and survival status.

## 3. Data Cleaning -- What did you fix?
#Example - df["Age"].fillna(df["Age"].mean(), inplace=True)

## 4. Analysis and Graphs + Explanation
# Survival by Gender
# Example -- sns.countplot(x="Sex", hue="Survived", data=df)
  #Explanation -- Females had significantly higher survival rates compared to males, suggestin priority given to females.
 
## 5. Key Insights
print("\n 1. Females had higher survival rates.", "\n 2. First class passengers survived more")

## 6. Final Takeaway
print("\n The analysis show that gender and class were the most significant factors influencing survival")


