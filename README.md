# Project 2021 for Programming and Scripting

# An investigation into the Fisher's Iris Data Set

## BY: Trish OGrady

### Introduction:

In 1936, Ronald Fisher, a statistician and biologist developed a linear function to differentiate Iris plant species based on the morphology of their flowers. The Fisher’s Iris data set contains 50 samples of the 3 Iris species. They are Iris Setosa, Iris Virginica and Iris versicolor. The dataset contains 4 features - the widths and lengths of petals and sepals. Its reguraly used to test machine learning alogoritms.[1]

### Dataset

The Iris dataset is downloaded as a csv format.[2]

### Explanation of code

*Import Pandas Library*

* The Pandas python toolkik is an open source library that is used for data analysis. It makes working with CSV files simplier and more effective as it can read and write data from different formats, i.e CSV (Common Seperated Values) which is the format of the iris dataset used for this analysis [3] The dataframe object is also useful for groupimg which will be demonstated in this project.
* print(df) clarifies that df is the object name that contains the csv file

*Data Screening*  

* To confirm the file has been read correctly and identify information about the data:

print(df) To confirm that the csv file has been read correctly. It also identifies all column names and the number of rows and columns

* Code
```
import pandas as pd

df=pd.read_csv("tableconvert_csv_o6an2r.csv")

print(df)
```

* Output

![alt text](https://github.com/Trishmcc/Project-2021/blob/main/df.png)

* Dataframe class:

print(type(df)) identifies the class as a dataframe which is a container for storing and manipulating two dimensional data [4]

* Code

```
print(type(df)) 
```
* OUTPUT

![alt text](https://github.com/Trishmcc/Project-2021/blob/main/dfType1.png)

* Sepal Lenght and Width:

To identify and subset the dataframe into 2 specific columns, i.e sepal lenght and sepal width. The double brackets returns a dataframe object as opposed to a series object[4]

* Code
```
df2=df[['sepal_length','sepal_width']]
print((df2))
```
* Output
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/SepalLW.png)

*Descriptive Statistics*

* describe() function

stats=df.describe()   The dataframe.describe() function summarises the columns of the dataframe. It allows the viewing of the mean, count, max, min, std and so forth[5] 

* Code
```
stats=df.describe()
print((stats))
```
* Output
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/Stats.png)


Pandas call the describe function using the dot operator and the double square brackets allow for multiple columns to be displayed.[6] The following code summarises an individual column.

* Code
```
stats=df[['sepal_length']].describe()
print((stats))
```
* Output
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/StatsSL.png)

*Grouping*

* mean by all species

* The groupby function involves splitting the object, applying a function, and/or combining the results.[7] So it searches through multiple categories and groups by a particular value of each category.[8] In this case, the data is split into groups based on the mean of all attributes for each species in the dataframe.[9] 

* code
```
attributes_Mean=df.groupby(['species']).mean()

print((attributes_Mean))
```

* Output
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/meanSpecies.png)

* Count by all species

* The pandas toolkit automatically runs the .count() calculation for all remaining columns, i.e species[11]

* 4 attributes are identified and each species has 50 data points. 

* Code
```
count_species=df.groupby(['species']).count()

print(count_species)
```
* Output
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/countSpecies.png)

*Summary data to text file*

This gives a simple description of the data. The seperator ',' is applied to seperate the columns in the text file. The 'a' append mode is applied too.

```
stats.to_csv('summary_iris.txt', header=True, index=True, sep=',', mode='a')

attributes_Mean.round(2).to_csv('summary_iris.txt', header=True, index=True, sep=',', mode='a')
```

*Exploratory Data Analysis (Graphs and visualisation)*

*Import matplotlib*

* Matplotlib is a useful plotting tool with a collection of functions used for visualisations[15]

CODE
```
import matplotlib.pyplot as plot_lib
```

* Creating the histogram for each variable
  
* A histogram displays continuous data values on a graph by grouping data into bins of equal width. Each bin is plotted as a bar. The height of each bin corresponds to how many data points are in that bin.[16]

Four histograms are created to display the sepal lenght, sepal width, petal lenght and petal width.

The histogram is defined in the function by its x and y axis and histogrm name. The y label is not hard coded meaning the variable will get its value dynamically when the function is called.[17]

The legend is dislpayed in the upper right[18]

* Code

```
def histogram_creation(y_value,y_label,image_name):

    plot_lib.figure(figsize=(16,9))
    plot_lib.title("Histogram Plot")
    plot_lib.hist(y_value,bins=10, color="blue", label="Histogram Series")
    plot_lib.xlabel("bins")
    plot_lib.ylabel(y_label)
    plot_lib.legend(loc="best")
    #plot_lib.show()
    plot_lib.savefig(image_name)
    

histogram_creation(df.sepal_length,"sepal_length","hist_sl.png")
histogram_creation(df.sepal_width,"sepal_width","hist_sw.png")
histogram_creation(df.petal_length,"petal_length","hist_pl.png")
histogram_creation(df.petal_width,"petal_width","hist_pw.png")
```
* Output

![alt text](https://github.com/Trishmcc/Project-2021/blob/main/hist_pl.png)
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/hist_pw.png)
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/hist_sl.png)
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/hist_sw.png)

* Create a Scatter Plot

A scatter plot is a graph that displays plotted points which identify a relationship between two variables[24]

The x and y labels are dynamic as are the x and y arguements. 

12 scatter plots are created.

Each dot represents either sepal lenght, sepal width, petal lenght and petal width.

Variations in Scatter plots: sepal_length=1, sepal_width=2, petal_length=3, petal_width=4
1,2 1,3 1,4 2,3 2,4 3,4
2,1 3,1 4,1 3,2 4,2 4,3

* Code
```
#def scatter_plot(x_value, y_value, x_label,y_label,image_name):

    #plot_lib.figure(figsize=(16,9))
    #plot_lib.title("Scatter Plot")
    #plot_lib.scatter(x_value,y_value, color="green", label="scatter plot series")
    #plot_lib.xlabel(x_label)
    #plot_lib.ylabel(y_label)
    #plot_lib.legend(loc="best")
    #plot_lib.show()
    #plot_lib.savefig(image_name)
```
    

* Output
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/SL_SW.png)
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/SL_PL.png)
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/SL_PW.png)
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/SW_PL.png)
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/SW_PW.png)
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/PL_PW.png)

![alt text](https://github.com/Trishmcc/Project-2021/blob/main/SW_SL.png)
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/PL_SL.png)
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/PW_SL.png)
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/PL_SW.png)
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/PW_SW.png)
![alt text](https://github.com/Trishmcc/Project-2021/blob/main/PW_PL.png)



They excluded the NaN values. However, the Iris data set has

### Conclusion:

The Python open source library Pandas is used to manipulate the Iris dataset. The functions of Panda’s DataFrame objects which include the describe function and grouping are important parts of exploratory data analysis and data visualization.

The describe() function summarises the data by displaying statistics such as the mean, median, standard deviation etc, for any variable or group applied.

Groupby is a powerful function as it allows you to chose particualr variables by splitting the data into various groups as seen above when I grouped the data by species.[27]

So, Pandas make the capability of grouping large data frames by different variables and the calculation of different statistics very simple. 




### References:
1. https://en.wikipedia.org/wiki/Iris_flower_data_set
2. https://archive.ics.uci.edu/ml/datasets/Iris
3. https://pandas.pydata.org/about/index.html
4. https://pythontic.com/pandas/dataframe-attributes/introduction
4. https://statkclee.github.io/R-ecology-lesson/03-data-frames.html
5. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
6. https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/
7. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#:~:text=A%20groupby%20operation%20involves%20some,compute%20operations%20on%20these%20groups.
8. https://pandas.pydata.org/pandas-docs/version/0.25.3/user_guide/groupby.html
9. https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.GroupBy.mean.html
10. https://stackoverflow.com/questions/29836477/pandas-create-new-column-with-count-from-groupby
11. https://data36.com/pandas-tutorial-2-aggregation-and-grouping/
12. https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
13. https://realpython.com/python-csv/
14. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
15. https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
16. https://statistics.laerd.com/statistical-guides/understanding-histograms.php
17. https://www.quora.com/What-is-hard-coding-in-Python
18. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
19. https://realpython.com/python-histograms/
20. https://www.geeksforgeeks.org/matplotlib-pyplot-hist-in-python/
21. https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
22. https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html
23. https://matplotlib.org/3.1.1/gallery/color/named_colors.html
24. https://en.wikipedia.org/wiki/Scatter_plot
27. https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
