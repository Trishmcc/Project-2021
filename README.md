# Project 2021 for Programming and Scripting

# An investigation into the Fisher's Iris Data Set

## BY: Trish OGrady

### Introduction:

In 1936, Ronald Fisher, a statistician and biologist developed a linear function to differentiate Iris species based on the morphology of their flowers. The Fisher’s Iris data set contains 50 samples of the 3 Iris species. They are Iris Setosa, Iris Virginica and Iris versicolor. The dataset contains 4 features - the widths and lengths of petals and sepals. Its reguraly used to test machine learning alogoritms.[1]

### Dataset

The Iris dataset is downloaded as a csv format.[2]

### Explanation of code

*Import Pandas Library*

* The Pandas python toolkit which is an open source, is used for data analysis. It makes working with CSV files simplier and more effective as it can read and write data from different formats, i.e CSV (Common Seperated Values)[3] The dataframe object is also useful for groupimg which will be demonstated in this project.
* print(df) clarifies that df is the object name that contains the csv file

*Data Screening*   SHOW CODE

* Confirm file has been read correctly and identify information about the data:

print(df) To confirm that the csv file has been read correctly. It also identifies all column names and the number of rows and columns

* Code

* Output


* Dataframe class:

print(type(df)) identifies the class as a dataframe which is a container for storing and manipulatin two dimensional data [4]

* Sepal Lenght and Width:

df2=df[['sepal_length','sepal_width']] To identify 2 specific columns, i.e sepal lenght and sepal width. The double brackets returns a dataframe object as opposed to a series object[4]

*Descriptive Statistics*

* describe() function

stats=df.describe()   The dataframe.describe() function summarises the columns of the dataframe. It allows the viewing of the mean, count, max, min, std and so forth[5] 


Pandas call the describe function using the dot operator and the double square brackets allow for multiple columns to be displayed.[6]

 stats=df[['sepal_length']].describe() This summarises an individual column

*Grouping*

* mean by all species

* The groupby function involves splitting the object, applying a function, and/or combining the results.[7] So it searches through multiple categories and groups by a particular value of each category.[8] In this case, the data is Split into groups based on the mean of all attributes for each species.[9] This forms a series as one set of brackets are applied i.e [12]

mean_sl=df.groupby(['species']).mean()

* Count by all species

* The pandas toolkit automatically runs the .count() calculation for all remaining columns, i.e species[11]

* 4 attributes are identified and each species has 50 data points. 

count_species=df.groupby(['species']).count()

*Summary data to text file*

stats.to_csv('summary_iris.txt', header=True, index=True, sep=',', mode='a')

mean_sl.round(2).to_csv('summary_iris.txt', header=True, index=True, sep=',', mode='a')

*Exploratory Data Analysis*

*Import matplotlib*

* Matplotlib is a useful plotting tool with a collection of functions used for visualisations[14]

* Creating the histogram for each variable

CODE

import matplotlib.pyplot as plot_lib

OUTPUT






They excluded the NaN values. However, the Iris data set has

### Conclusion:







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
14. https://matplotlib.org/2.0.2/users/pyplot_tutorial.html

