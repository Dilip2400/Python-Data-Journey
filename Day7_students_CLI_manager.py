#Print menu
def show_menu():
    print("\n STUDENT MANAGER")
    print("1. View students")
    print("2. Add student")
    print("3. Show topper")
    print("4. Passed students")
    print("5. Exit")
    
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
    marks = input("Enter student marks : ")
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
    
def passed_students(students):
    for name, marks in students.items():
        if marks > 35:
            print("Passed students: ", name, marks)
    
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
        print("Exiting...")
        break
    else:
        print("Invalid choice")