#Students Marks Analyzer(Upgrade)
students = {
    "Dilip": 91,
    "Rahul": 35,
    "Poojitha": 98,
    "Mohan": 65,
    "Bose": 93,
    "Rishi": 42,
    "Vikas": 32,
    "Namit": 48
}
#Failed students
def failed_students(students):
    failed = {}
    for name, mark in students.items():
        if mark < 40:
            failed[name] = mark
    return failed
print("Failed students: ", failed_students(students))

#Merit Students
def merit_students(students):
    merit = {}
    for name, mark in students.items():
        if mark > 80:
            merit[name] = mark
    return merit
print("Merit students: ", merit_students(students))

#Passed students
def passed_students(students):
    passed = {}
    for name, mark in students.items():
        if mark > 40:
            passed[name] = mark
    return passed
print("Passed studets: ", passed_students(students))

#Average of class
def average_marks(students):
    avg = 0
    total = 0
    for name in students:
        total += students[name]
    avg = total / len(students)
    return avg
print("Average of class: ", average_marks(students))

#Grade system
def grade_students(students):
    grades = {}
    for name, mark in students.items():
        if mark > 90:
            grades[name] = "A"
        elif mark > 75:
            grades[name] = "B"
        elif mark > 40: 
            grades[name] = "C"
        else:
            grades[name] = "F"
    return grades
print("Grade of students: ", grade_students(students))
