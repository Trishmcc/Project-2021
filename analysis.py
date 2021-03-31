# An investigation into the Fisher's Iris date set.
# By Trish O'Grady

# The python package named pandas is imported to help with the manipulation of data.

# df is the object name that contains the csv file. 
# The pd.read_csv is the function for reading the csv file. This function will be used to pass an argument.

import pandas as pd

df=pd.read_csv("tableconvert_csv_o6an2r.csv")

#print(df)

#print(pd)

#Checking for type of object that has been created, i.e the pandas dataframe which 
#has the structure of a table.

#print(type(df)) 

#df1 = ["species"].unique()
#print(df1)
# For sepal Length and Width columns:
    
df2=df[['sepal_length','sepal_width']]
print((df2))





