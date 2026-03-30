#Loops + Contional statements + Functions.

#Conditional Statements. (if, if-else)
num = int(input("Enter a number: "))
if num >0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")
    
#For loop.
for i in range(5):
    print(i)
    
num = [10,20,30,40,50]
for i in num:
    print(i)
    
#Functions.
def greet(name):
    return "Hello " + name
print(greet("Dilip"))

#Finding even numbers from List
num = [10, 15, 20, 25, 30]
for i in num:
    if i%2==0:
        print(i)
        
#Count of numbers in list        
nums = [10,60,70,20,90]
count = 0

for num in nums:
    if num>50:
        count += 1
print("Count: ", count) 

#Finding total in List
nums = [5, 10, 15]
total = 0
for num in nums:
    total += num
print(total)

#Maximum number in a List
nums = [3, 9, 2, 15, 6]
max_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num
print(max_num)

#Even or odd Function
def check_even(num):
    if num%2 ==0:
        return "Num is Even"
    else:
        return "Num is Odd"
print(check_even(6))

#Count Even numbers (Function)
nums = [2,3,4,5,6]

def count_even(nums):
    count = 0
    for num in nums:
        if num%2 ==0:
            count += 1
    return count
print(count_even(nums))

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