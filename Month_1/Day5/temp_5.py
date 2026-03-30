students = {
    "Dilip": 85,
    "Rahul": 35,
    "Poojitha": 92,
    "Mohan": 65,
    "Bose": 78
}

#Create a new file with students data.
with open("students_1.txt", "a") as file:
    for name, marks in students.items():
        file.write(f"{name}:{marks}\n")
        
with open("students_1.txt", "a") as file:
    file.write("Rahul : abc\n")
    
def process_file():
    with open("students_1.txt", "r") as file:
        for line in file:
            try:
                name, marks = line.strip().split(":")
                marks = int(marks)
                print(name, marks)
            except ValueError:
                print("Skipping bad line:", line.strip())

process_file()