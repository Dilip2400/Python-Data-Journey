students = {
    "Dilip": 85,
    "Rahul": 35,
    "Poojitha": 92,
    "Mohan": 65,
    "Bose": 78
}

#Create a new file with students data.
with open("students.txt", "w") as file:
    for name, marks in students.items():
        file.write(f"{name}:{marks}\n")

#Reading the file.       
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())
        
#Add a new student data
with open("students.txt", "a") as file:
    file.write("Manish : 88\n")
    
#Converting file into dictionary
students = {}
with open("students.txt", "r") as file:
    for line in file:
        name, marks = line.strip().split(":")
        students[name] = int(marks)
print(students)

with open("students.txt", "r") as file:
    for line in file:
        name, marks = line.strip().split(":")
        
        if int(marks) > 70:
            print(name)