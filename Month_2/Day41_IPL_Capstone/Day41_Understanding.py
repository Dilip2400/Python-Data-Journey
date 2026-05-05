#Import libraries
import pandas as pd  

#Load Dataset
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

#Understanding dataset
print(matches.head())
print(matches.info())

print(deliveries.head())
print(deliveries.info())

#Finding Missing Values
print(matches.isnull().sum())
print(deliveries.isnull().sum())