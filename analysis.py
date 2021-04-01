# An investigation into the Fisher's Iris date set.
# By Trish O'Grady

# The python package named pandas is imported to help with the manipulation of data.

# df is the object name that contains the csv file. 
# The pd.read_csv is the function for reading the csv file. This function will be used to pass an argument.

import pandas as pd

df=pd.read_csv("tableconvert_csv_o6an2r.csv")

#print(df)

#print(pd)

#Data screening

#Checking for type of object that has been created, i.e the pandas dataframe which 
#has the structure of a table.

#print(type(df)) 

#df1 = ["species"].unique()
#print(df1)
# For sepal Length and Width columns:

df2=df[['sepal_length','sepal_width']]
#print((df2))

#Descriptive Statistics

stats=df.describe()
#print((stats))

stats=df[['sepal_length']].describe()
#print((stats))

#mean by all species
mean_sl=df.groupby(['species']).mean()

#print((mean_sl))

#Count by all species

count_species=df.groupby(['species']).count()

#print(count_species)

#Storing summary data to text file

stats.to_csv('summary_iris.txt', header=True, index=True, sep=',', mode='a')

mean_sl.round(2).to_csv('summary_iris.txt', header=True, index=True, sep=',', mode='a')

#Creating the histogram for each variable

import matplotlib.pyplot as plot_lib


plot_lib.figure(figsize=(16,9))
plot_lib.title("Histogram Plot")
plot_lib.hist(df.sepal_length,bins=10, color="#33DAFF", label="Histogram Series")
plot_lib.xlabel("bins")
plot_lib.ylabel("sepal_length")
plot_lib.legend(loc="best")
plot_lib.show()
plot_lib.savefig("sepal_length.png")











