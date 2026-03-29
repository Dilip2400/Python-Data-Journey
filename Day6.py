#List Comprehension
marks = [10, 30, 50, 70, 80, 90]

#get marks > 50 using List comprehension

result = [mark for mark in marks if mark > 50]
print(result)

students = {
    "Dilip": 85,
    "Rahul": 35,
    "Kiran": 92
}

# get list of names with marks > 70
def merit_students(students):
    return[name for name, mark in students.items() if mark > 70]

print(merit_students(students))