#Dictionaries
student = {
    "name": "Dilip",
    "marks": "85"
}
print(student["name"])

students = {
    "Dilip": 92,
    "Manish": 86,
    "Poojitha": 98,
    "Mohan": 65
}
#for name in students:
#    print(name, students[name])
    
#Functions with Dictionaries
#Mini Project
#Find the topper
def find_topper(students):
    max_marks=0
    topper = ""
    
    for name in students:
        if students[name]>max_marks:
            max_marks=students[name]
            topper = name
    return topper, max_marks

print(find_topper(students))

#Average Marks
def average_marks(students):
    average = sum(students.values()) / len(students)
    return average
print("Average: ", average_marks(students))

#Print students with marks >80
def merit_students(students):
    result = {}
    for name, marks in students.items():
        if marks > 80:
            result[name] = marks
    return result
print(merit_students(students))

#Count students with marks >40
def passed_students(students):
    count = 0
    for name, marks in students.items():
        if marks>40:
            count += 1
    return count
print(passed_students(students))