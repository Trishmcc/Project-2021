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

attributes_Mean=df.groupby(['species']).mean()

#print((attributes_Mean))

#Count by all species

count_species=df.groupby(['species']).count()

#print(count_species)

#Storing summary data to text file

stats.to_csv('summary_iris.txt', header=True, index=True, sep=',', mode='a')

attributes_Mean.round(2).to_csv('summary_iris.txt', header=True, index=True, sep=',', mode='a')

#Creating the histogram for each variable
import matplotlib.pyplot as plot_lib

#plot_lib.figure(figsize=(16,9))
#plot_lib.title("Histogram Plot")
#plot_lib.hist(df.sepal_length,bins=10, color="blue", label="Histogram Series")
#plot_lib.xlabel("bins")
#plot_lib.ylabel("sepal_length")
#plot_lib.legend(loc="best")
#plot_lib.show()
#plot_lib.savefig("sepal_length.png")


#def histogram_creation(y_value,y_label,image_name):

    #plot_lib.figure(figsize=(16,9))
    #plot_lib.title("Histogram Plot")
    #plot_lib.hist(y_value,bins=10, color="blue", label="Histogram Series")
    #plot_lib.xlabel("bins")
    #plot_lib.ylabel(y_label)
    #plot_lib.legend(loc="best")
    #plot_lib.show()
    #plot_lib.savefig(image_name)
    

#histogram_creation(df.sepal_length,"sepal_length","hist_sl.png")
#histogram_creation(df.sepal_width,"sepal_width","hist_sw.png")
#histogram_creation(df.petal_length,"petal_length","hist_pl.png")
#histogram_creation(df.petal_width,"petal_width","hist_pw.png")



#Create a scatter plot


#plot_lib.figure(figsize=(16,9))
#plot_lib.title("Scatter Plot")
#plot_lib.scatter(df.sepal_width,df.sepal_length, color="green", label="scatter plot series")
#plot_lib.xlabel("sepal_width")
#plot_lib.ylabel("sepal_length")
#plot_lib.legend(loc="best")
#plot_lib.show()
#plot_lib.savefig("sepal_length_SP_SW.png")


def scatter_plot(x_value, y_value, x_label,y_label,image_name):

    plot_lib.figure(figsize=(16,9))
    plot_lib.title("Scatter Plot")
    plot_lib.scatter(x_value,y_value, color="green", label="scatter plot series")
    plot_lib.xlabel(x_label)
    plot_lib.ylabel(y_label)
    plot_lib.legend(loc="best")
   # plot_lib.show()
    plot_lib.savefig(image_name)


scatter_plot(df.sepal_length,df.sepal_width,"sepal_length","sepal_width","SL_SW.png")

scatter_plot(df.sepal_length,df.petal_length,"sepal_length","petal_length","SL_PL.png")

scatter_plot(df.sepal_length,df.petal_width,"sepal_length","petal_width", "SL_PW.png") 

scatter_plot(df.sepal_width,df.petal_length,"sepal_width","petal_length","SW_PL.png")

scatter_plot(df.sepal_width,df.petal_width,"sepal_width","petal_width","SW_PW.png")

scatter_plot(df.petal_length,df.petal_width,"petal_length","petal_width","PL_PW.png")




scatter_plot(df.sepal_width,df.sepal_length,"sepal_width","sepal_length","SW_SL.png")

scatter_plot(df.petal_length,df.sepal_length,"petal_length","sepal_length","PL_SL.png")

scatter_plot(df.petal_width,df.sepal_length,"petal_width","sepal_length", "PW_SL.png") 

scatter_plot(df.petal_length,df.sepal_width,"petal_length","sepal_width","PL_SW.png")

scatter_plot(df.petal_width,df.sepal_width,"petal_width","sepal_width","PW_SW.png")

scatter_plot(df.petal_width,df.petal_length,"petal_width","petal_length","PW_PL.png")
