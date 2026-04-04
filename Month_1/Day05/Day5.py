students = {
    "Dilip": 85,
    "Rahul": 35,
    "Poojitha": 92,
    "Mohan": 65,
    "Bose": 78
}

#Create a new file with students data.
with open("students_1.txt", "w") as file:
    for name, marks in students.items():
        file.write(f"{name}:{marks}\n")
        
# Load students from file
def load_students():
    students = {}
    
    with open("students_1.txt", "r") as file:
        for line in file:
            name, marks = line.strip().split(":")
            students[name] = int(marks)
    
    return students

# Find topper
def find_topper(students):
    topper = ""
    max_marks = 0
    
    for name, marks in students.items():
        if marks > max_marks:
            max_marks = marks
            topper = name
    
    return topper, max_marks


# Count passed students
def count_passed(students):
    count = 0
    
    for marks in students.values():
        if marks > 40:
            count += 1
    
    return count

# Get merit students (>70)
def get_merit(students):
    result = []
    
    for name, marks in students.items():
        if marks > 70:
            result.append(name)
    
    return result


# MAIN
students = load_students()

print("Students:", students)
print("Topper:", find_topper(students))
print("Passed count:", count_passed(students))
print("Merit students:", get_merit(students))

with open("students_1.txt", "r") as file:
    for line in file:
        try:
            name, marks = line.strip().split(":")
            marks = int(marks)
            print(name, marks)
        except:
            print("Skipping bad line:", line.strip())