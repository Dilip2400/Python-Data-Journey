#Mini Project (Marks Analyzer) - Total, Average, Highest marks, lowest marks.

marks = [45, 78, 90, 66, 88]
count = len(marks)
def total_marks(marks):
    total = 0 
    for i in marks:
        total += i
    return total
print(total_marks(marks))

def highest_mark(marks):
    max_marks = marks[0]
    for i in marks:
        if i > max_marks:
            max_marks = i
    return max_marks
print(highest_mark(marks))

def average(marks):
    #total=0 
    #for i in marks:
        #total += i
    return total_marks(marks)/len(marks)
print(average(marks))

def lowest_mark(marks):
    min_marks = marks[0]
    for i in marks:
        if i < min_marks:
            min_marks = i
    return min_marks
print(lowest_mark(marks))