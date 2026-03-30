students = {
    "Dilip": 85,
    "Rahul": 78,
    "Kiran": 92,
    "Anil": 66
}

# Total marks
def total_marks(students):
    total = 0
    for marks in students.values():
        total += marks
    return total

# Average marks
def average_marks(students):
    return total_marks(students) / len(students)

# Topper
def find_topper(students):
    topper = ""
    max_marks = 0
    
    for name, marks in students.items():
        if marks > max_marks:
            max_marks = marks
            topper = name
    
    return topper, max_marks

# Passed students (>40)
def count_passed(students):
    count = 0
    
    for marks in students.values():
        if marks > 40:
            count += 1
    
    return count

# Students above 80
def high_scorers(students):
    result = []
    
    for name, marks in students.items():
        if marks > 80:
            result.append(name)
    
    return result


# OUTPUT
print("Total:", total_marks(students))
print("Average:", average_marks(students))
print("Topper:", find_topper(students))
print("Passed count:", count_passed(students))
print("High scorers:", high_scorers(students))