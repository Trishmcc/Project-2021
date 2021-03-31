# Project 2021 for Programming and Scripting

# An investigation into the Fisher's Iris Data Set

## BY: Trish OGrady

### Introduction:

In 1936, Ronald Fisher, a statistician and biologist developed a linear function to differentiate Iris species based on the morphology of their flowers. The Fisher’s Iris data set contains 50 samples of the 3 Iris species. They are Iris Setosa, Iris Virginica and Iris versicolor. The dataset contains 4 features - the widths and lengths of petals and sepals. Its reguraly used to test machine learning alogoritms.[1]

### Dataset

The Iris dataset is downloaded as a csv format.[2]

### Explanation of code

*Import Pandas Library*

* The Pandas python toolkit which is an open source, is used for data analysis. It makes working with CSV files simplier and more effective as it can read and write data from different formats, i.e CSV (Common Seperated Values)[3] The dataframe object is also useful for subsetting which will be demonstated in this project.
* print(df) clarifies that df is the object name that contains the csv file

*Data Screening*   SHOW CODE

* Confirm file has been read correctly and identify information about the data:

print(df) To confirm that the csv file has been read correctly. It also identifies all column names and the number of rows and columns


* Dataframe class:

print(type(df)) identifies the class as a dataframe which is a container for storing and manipulatin two dimensional data [4]

* Sepal Lenght and Width:

df2=df[['sepal_length','sepal_width']] To identify 2 specific columns, i.e sepal lenght and sepal width

*Descriptive Statistics*

* describe() function

stats=df.describe()   The describe() function summarises the columns of the dataframe. It allows the viewing of the mean, count, max, min, percentile, std and so forth[5] Pandas call the describe function using the dot operator and the double brackets allow for multiple columns to be displayed.[6]

* Subsetting

 stats=df[['sepal_length']].describe() This summarises an individual column



They excluded the NaN values. However, the Iris data set has




### References:
1. https://en.wikipedia.org/wiki/Iris_flower_data_set
2. https://archive.ics.uci.edu/ml/datasets/Iris
3. https://pandas.pydata.org/about/index.html
4. https://pythontic.com/pandas/dataframe-attributes/introduction
4. https://statkclee.github.io/R-ecology-lesson/03-data-frames.html
5. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
6. https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/


