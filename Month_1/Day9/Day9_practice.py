def search_student(students):
    name = input("Enter a name: ")
    if name in students:
        print(f"{name} : {students[name]}")
    else:
        print("Student not found...")
        
def sort_students(students):
    sorted_list = sorted(students.items(), key = lambda x : x[1], reverse = True)
    print("-- Sorted Students (High --> Low) --")
    for name, marks in sorted_list:
        print(f"{name}-{marks}")