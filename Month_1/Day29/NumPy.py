import numpy as np

#Random data
arr = np.random.randint(1,100, size=10)
print(arr)

#Array of a particular range
arr = np.arange(1,13)
#1D Array --> 2D Array
reshaped = arr.reshape(3,4)
print(reshaped)

#2D Array --> 1D Array
flat = reshaped.flatten()
print(flat)

#Axis wise operations
arr2d = np.array([[1,2,3],
                  [4,5,6]])

print(arr2d.sum(axis=0)) #Column wise sum
print(arr2d.sum(axis=1)) #Row wise sum

#Boolean Masking

arr = np.array([10,50,30,80,60,90])
print(arr[arr > 40])  # Similar to df[df["Marks"]>40] in Pandas

#Combining conditions
print(arr[(arr>30) & (arr<90)])  #Multiple conditions


#Example
marks = np.random.randint(30,100, 10)

#Add bonus marks
updated = marks + 5

#Pass/Fail
status = np.where(updated >50, "Pass", "Fail")

print(marks)
print(updated)
print(status)

print(updated.shape)