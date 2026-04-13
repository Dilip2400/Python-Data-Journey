def show_menu():
    print("\n --- STUDENT ANALYZER --- \n")
    print("1. Full Report")
    print("2. Show Topper")
    print("3. Department Analysis")
    print("4. Passed Students")
    print("5. Failed Students")
    print("6. Students grades")
    print("7. Search a student")
    print("8. Save report")
    print("9. Add a student")
    print("10. Exit")

import pandas as pd
df = pd.read_csv("students.csv")
#print(df.head())
#print(df.info())
#print(df.describe())

#Grades for students marks
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

#Finding Topper of students
def show_topper(df):
    topper = df.loc[df["Marks"].idxmax()]
    print("\n Topper: \n", topper)

#Passed students    
def passed_students(df):
    passed_students = df[df["Marks"]>35]
    print("\n Passed Students: \n", passed_students)
    
#Failed Students
def failed_students(df):
    failed = df[df["Marks"]<35]
    print("\n Failed Students: \n", failed)

#Add Search feature
def search_student(df):
    name = input("Enter student name: ")
    result = df[df["Name"]== name]
    if not result.empty:
        print("\n Student found: \n", result)
    else:
        print("Student not found")
        
#Save a report
def save_report(df):
    df.to_csv("report.csv", index = False)
    print("Report saved successfully")
    
def add_student(df):
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")
    department = input("Enter student department: ")
    new_student = {
        "Name":name,
        "Marks":marks,
        "Department":department
    }
    df = pd.concat([df,pd.DataFrame([new_student])], ignore_index=True)
    df.to_csv("students.csv", index=False)
    print("Student added successfully")
    return df
        
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
        search_student(df)
    elif choice == "8":
        save_report(df)
    elif choice == "9":
        add_student(df)    
    elif choice == "10":
        break