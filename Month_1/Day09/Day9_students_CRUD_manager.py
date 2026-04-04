#File Path
import os
file_path = os.path.join(os.path.dirname(__file__), "students.txt")
print("FILE PATH BEING USED:", file_path)

#Print menu
def show_menu():
    print("\n STUDENT MANAGER")
    print("1. View students")
    print("2. Add student")
    print("3. Show topper")
    print("4. Passed students")
    print("5. Update student")
    print("6. Delete student")
    print("7. Search student")
    print("8. Sort students")
    print("9. Generate Report")
    print("10. Exit")
    
#Load students    
def load_students():
    students = {}
    try:
        with open(file_path, "r") as file:
        #with open("students.txt", "r") as file:
            for line in file:
                try:
                    name, marks = line.strip().split(":")
                    students[name] = int(marks)
                except ValueError:
                    continue
    except FileNotFoundError:
        print("File not found")
 
    return students

#Add and save a new student
def add_student(students):
    name = input("Enter a name : ")
    
    if name in students:
        print("Student already exists ❌")
        return
    
    marks = input("Enter marks: ")
    
    try:
        marks = int(marks)
        
        students[name] = marks   # update dictionary
        save_student(students)   # save everything
        
        print("Student added successfully ✅")    
    except ValueError:
        print("Invalid Marks")
        
# View students
def view_students(students):
    print("\n --- Students List ---")
    for name, marks in students.items():
        print(f"{name}-{marks}")
        
# Show Topper
def show_topper(students):
    topper = ""
    max_marks = 0
    for name, marks in students.items():
        if marks > max_marks:
            topper = name
            max_marks = marks
    print("Topper: ", topper, max_marks)

#Passed Students    
def passed_students(students):
    for name, marks in students.items():
        if marks > 35:
            print("Passed students: ", name, marks)
            
#Save student
def save_student(students):
    with open(file_path, "w") as file:  ##########################################################################################
        for name, marks in students.items():
            file.write(f"{name}:{marks}\n")
    print("Saving data:", students)

#Update students info.
def update_student(students):
    name = input("Enter a student name: ")
    if name in students:
        new_marks = input("Enter marks of student: ")
        try:
            students[name] = int(new_marks)
            save_student(students)
            print("Updated student successfully...")
        except ValueError:
            print("Invalid marks")
    else:
        print("Student not found")        
            
#Delete student
def delete_student(students):
    name = input("Enter a name to delete: ")
    if name in students:
        del students[name]
        save_student(students)
        print("Deleted successfully")
    else:
        print("Student not found")   
        
#Search function
def search_student(students):
    name = input("Enter a name: ")
    if name in students:
        print(f"{name}:{students[name]}")
    else:
        print("Student not found")
        
#Sort students
def sort_students(students):
    sorted_list = sorted(students.items(), key = lambda x:x[1], reverse = True)
    print("--- Sorted Students (High --> Low) ---")
    for name, marks in sorted_list:
        print(f"{name} - {marks}")
        
#Generate Report
def generate_report(students):
    total = len(students)
    passed = sum(1 for m in students.values() if m > 35)
    failed = total - passed
    
    topper = max(students, key = students.get) if students else None
    print("\n --- Report ---")
    print(f"Total Students: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    if topper:
        print(f"Topper: {topper} ({students[topper]})")
    
#Main loop to show menu
while True:
    show_menu()
    choice = input("Enter choice: ")
    students = load_students()
    
    if choice == "1":
        view_students(students)
    elif choice == "2":
        add_student(students)
    elif choice == "3":
        show_topper(students)
    elif choice == "4":
        passed_students(students)
    elif choice == "5":
        update_student(students)
    elif choice == "6":
        delete_student(students)
    elif choice == "7":
        search_student(students)
    elif choice == "8":
        sort_students(students)
    elif choice == "9":
        generate_report(students)
    elif choice == "10":    
        print("Exiting...")
        break
    else:
        print("Invalid choice")