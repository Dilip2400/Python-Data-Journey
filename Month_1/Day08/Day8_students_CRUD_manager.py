#Print menu
def show_menu():
    print("\n STUDENT MANAGER")
    print("1. View students")
    print("2. Add student")
    print("3. Show topper")
    print("4. Passed students")
    print("5. Update student")
    print("6. Delete student")
    print("7. Exit")
    
#Load students    
def load_students():
    students = {}
    try:
        with open("students.txt", "r") as file:
            for line in file:
                try:
                    name, marks = line.strip().split(":")
                    students[name] = int(marks)
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
 
    return students

#Add and save a new student
def add_student():
    name = input("Enter a name : ")
    if name in students:
        print("Student already exists ❌")
        return
    marks = input("Enter marks: ")
    try:
        marks = int(marks)
        
        with open("students.txt", "a") as file:
            file.write(f"{name}:{marks}\n")
        print("Student added succesfully")
    except ValueError:
        print("Invalid Marks")
        
# View students
def view_students(students):
    for name, marks in students.items():
        print(name, marks)
        
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
    with open("students.txt", "w") as file:
        for name, marks in students.items():
            file.write(f"{name}:{marks}\n")

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
    
#Main loop to show menu
while True:
    show_menu()
    choice = input("Enter choice: ")
    students = load_students()
    
    if choice == "1":
        view_students(students)
    elif choice == "2":
        add_student()
    elif choice == "3":
        show_topper(students)
    elif choice == "4":
        passed_students(students)
    elif choice == "5":
        update_student(students)
    elif choice == "6":
        delete_student(students)
    elif choice == "7":    
        print("Exiting...")
        break
    else:
        print("Invalid choice")