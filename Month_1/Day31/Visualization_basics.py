import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd  

#Basic Line Plot
x = [1,2,3,4]
y = [10,20,30,40]
#plt.plot(x,y)
#plt.title("Simple Line Plot")
#plt.show()

a = [25,36,45,55]
b = [50,35,85,100]
#plt.plot(a,b)
#plt.show()

#Bar Chart
students = ["Dilip", "Pooja", "Sarath", "Vikas", "Sai"]
marks = [88, 96, 86, 76, 36]
#plt.bar(students,marks)
#plt.show()

# Random data generation
data = np.random.randint(1,100,50)
#Histogram Graph
#plt.hist(data)
plt.title("Distribution")
#plt.show() 

#Labels (X-axis, Y-axis)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
#plt.show()

#Read real data
df = pd.read_csv("Titanic.csv")
#Pandas and Matplot integration
#df["Sex"].value_counts().plot(kind="bar")
plt.title("Gender count")
#plt.show()

df["Age"].value_counts().plot(kind="hist")
plt.show()