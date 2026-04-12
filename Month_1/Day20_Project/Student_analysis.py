def show_menu():
    print("\n --- STUDENT ANALYZER --- \n")
    print("1. Full Report")
    print("2. Show Topper")
    print("3. Department Analysis")
    print("4. Passed Students")
    print("5. Failed Students")
    print("6. Students grades")
    print("7. Exit")

import pandas as pd

data = {
    "Name" : ["Dilip", "Harish", "Pooji", "Kiran", "Sai", "Rahul", "Manish"],
    "Marks" :[92, 88, 98, 67, 28, 36, 78],
    "Department": ["IT", "HR", "IT", "Finance", "Finance", "HR", "IT"]
}

df=pd.DataFrame(data)

def get_grades(marks):
    if marks >=95:
        return "A+"
    elif marks >= 85:
        return "A"
    elif marks >= 75:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 35:
        return "C"
    else:
        return"Fail"
df["Grades"] = df["Marks"].apply(get_grades)
    
#print(df.head())
#print(df.info())
#print(df.describe())

def show_topper(df):
    topper = df.loc[df["Marks"].idxmax()]
    print("\n Topper: \n", topper)
    
def passed_students(df):
    passed_students = df[df["Marks"]>35]
    print("\n Passed Students: \n", passed_students)
    
def failed_students(df):
    failed = df[df["Marks"]<35]
    print("\n Failed Students: \n", failed)
    
while True:
    show_menu()
    choice = input("Enter choice: ")
    if choice == "1":
        print(df)
    elif choice == "2":
        show_topper(df)
    elif choice == "3":
        print("\n Average Marks per department: \n", df.groupby("Department")["Marks"].mean())
    elif choice == "4":
        passed_students(df)
    elif choice == "5":
        failed_students(df)
    elif choice == "6":
        print("\n Student Grades by Department \n")
        for dept, group in df.groupby("Department"):
            print(f"\n Department:{dept}")
            print(group[["Name", "Grades"]])
    elif choice == "7":
        break
    