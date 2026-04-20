import numpy as np

arr = np.array([1,2,3])
print("NumPy Array: ", arr)

#Difference between NumPy Array vs List
list = [1,2,3]
print("List; ", list*2, "\nArray: ", arr*2)

#Basic Array operations
arr_y = np.array([10,20,30,40,50])
print(arr_y + 5)
print(arr_y *2)
print(arr_y/10)

#Indexing
print(arr_y[0], arr_y[-1])

#2D Array  -- Rows + Columns
arr2d = np.array([[1,2,3],
                  [4,5,6]])
print("2D Array: ", arr2d)

# 2D Array Indexing
print(arr2d[1,1]) #Row - 1, column - 1
print(arr2d[0,2])

marks = np.array([50, 76, 88, 95, 73, 28])
updated = marks + 5
print(updated)

#Pass if marks > 35, else fail
result = np.where(marks >=35, "Pass", "Fail")
print(result)

level = np.where(marks >75, "High", "Low")
print(level)

print("Passed Marks:", marks[marks>35])
print("Failed: ", marks[marks<35])