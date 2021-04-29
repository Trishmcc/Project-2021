# An investigation into the Fisher's Iris date set.
# By Trish O'Grady

# The python package named pandas is imported to help with the manipulation of data.

# df is the object name that contains the csv file. 
# The pd.read_csv is the function for reading the csv file. This function will be used to pass an argument.
import pandas as pd

import matplotlib.pyplot as plot_lib

iris_df=pd.read_csv("tableconvert_csv_o6an2r.csv")

import seaborn as sns

#print(iris_df)


#print(pd)

#Data screening

#Checking for type of object that has been created, i.e the pandas dataframe which 
#has the structure of a table.

#print(type(iris_df))

#iris_df1 = ["species"].unique()
#print(df1)

# For sepal Length and Width columns:
''' Checking Pandas dataframe functionalty
iris_df2=iris_df[['sepal_length','sepal_width']]
#print((df2))
'''

#Descriptive Statistics

#stats=iris_df.describe()
#print((stats))
'''
stats=iris_df[['sepal_length']].describe()
#print((stats))

#mean by all species

attributes_Mean=iris_df.groupby(['species']).mean()

#print((attributes_Mean))

#Count by all species

count_species=iris_df.groupby(['species']).count()

#print(count_species)

'''
'''
#Storing summary data to text file

stats.to_csv('summary_iris.txt', header=True, index=True, sep=',', mode='a')

attributes_Mean.round(2).to_csv('summary_iris.txt', header=True, index=True, sep=',', mode='a')
'''
'''
```
##Function definition
def Summary(Column):
    Summary=iris_df[[Column]].describe()
    #print(Summary)
    Summary_new=Summary.reset_index()
    Summary_new.columns.values[0]='Statistics'
    #print(Summary_new)
    File_heading=open('summary_iris.txt','a')
    File_heading.write('The summary statistics for '+Column+ ' are mentioned below'+'\n'*2)
    File_heading.close()
    Summary_new.to_csv('summary_iris.txt', header=True, index=False, sep=',', mode='a')
    File_heading=open('summary_iris.txt','a')
    File_heading.write('\n'*2)
    File_heading.close()
    
    ##function calling
    
Summary('sepal_length')
Summary('petal_length')
Summary('sepal_width')
Summary('petal_width')

'''

 
#Creating the histogram for each variable

# plot_lib.figure(figsize=(10,6))
# plot_lib.title("Histogram Plot")
# #plot_lib.hist(iris_df.sepal_length,bins=10, color="blue", label="Histogram Series")
# plot_lib.xlabel("bins")
# plot_lib.ylabel("sepal_length")
# plot_lib.legend(loc="best")
# #plot_lib.show()
# plot_lib.savefig("sepal_length.png")


# def histogram_creation(y_value,y_label,image_name):

#     plot_lib.figure(figsize=(10,6))
#     plot_lib.title("Histogram Plot")
#     plot_lib.hist(y_value,bins=10, color="blue", label="Histogram Series")
#     plot_lib.xlabel("bins")
#     plot_lib.ylabel(y_label)
#     plot_lib.legend(loc="best")
#     plot_lib.show()
#     plot_lib.savefig(image_name)
    

# histogram_creation(iris_df.sepal_length,"sepal_length","hist_sl.png")
# histogram_creation(iris_df.sepal_width,"sepal_width","hist_sw.png")
# histogram_creation(iris_df.petal_length,"petal_length","hist_pl.png")
# histogram_creation(iris_df.petal_width,"petal_width","hist_pw.png")



#Create a scatter plot

# sns.pairplot(iris_df,hue="species", height=3)


plot_lib.figure(figsize=(10,6))
plot_lib.title("Scatter Plot")
plot_lib.scatter(iris_df.sepal_width,iris_df.sepal_length, color="green", label="scatter plot series")
plot_lib.xlabel("sepal_width")
plot_lib.ylabel("sepal_length")
plot_lib.legend(loc="best")
#plot_lib.show()
plot_lib.savefig("sepal_length_SP_SW.png")


def scatter_plot(x_value, y_value, x_label,y_label,image_name):

    plot_lib.figure(figsize=(10,6))
    plot_lib.title("Scatter Plot")
    plot_lib.scatter(x_value,y_value, color="green", label="scatter plot series")
    plot_lib.xlabel(x_label)
    plot_lib.ylabel(y_label)
    plot_lib.legend(loc="best")
    #plot_lib.show()
    plot_lib.savefig(image_name)


scatter_plot(iris_df.sepal_length,iris_df.sepal_width,"sepal_length","sepal_width","SL_SW.png")

scatter_plot(iris_df.sepal_length,iris_df.petal_length,"sepal_length","petal_length","SL_PL.png")

scatter_plot(iris_df.sepal_length,iris_df.petal_width,"sepal_length","petal_width", "SL_PW.png") 

scatter_plot(iris_df.sepal_width,iris_df.petal_length,"sepal_width","petal_length","SW_PL.png")

scatter_plot(iris_df.sepal_width,iris_df.petal_width,"sepal_width","petal_width","SW_PW.png")

scatter_plot(iris_df.petal_length,iris_df.petal_width,"petal_length","petal_width","PL_PW.png")




scatter_plot(iris_df.sepal_width,iris_df.sepal_length,"sepal_width","sepal_length","SW_SL.png")

scatter_plot(iris_df.petal_length,iris_df.sepal_length,"petal_length","sepal_length","PL_SL.png")

scatter_plot(iris_df.petal_width,iris_df.sepal_length,"petal_width","sepal_length", "PW_SL.png") 

scatter_plot(iris_df.petal_length,iris_df.sepal_width,"petal_length","sepal_width","PL_SW.png")

scatter_plot(iris_df.petal_width,iris_df.sepal_width,"petal_width","sepal_width","PW_SW.png")

scatter_plot(iris_df.petal_width,iris_df.petal_length,"petal_width","petal_length","PW_PL.png")
