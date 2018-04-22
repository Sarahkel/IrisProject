# Iris Course Project - Programming and Scripting
GMIT Course Project on exploration of Fisher's Iris Data Set

### Task 
> *Imagine that you are to give a brief presentation to your co-workers on the data set, where you explain to them what investigating a data set entails and how Python can be used to do it.
The project entails researching the data set, and then writing documentation and code in the Python programming language based on that research*

**Use:** Python (www.python.org) - Note: Installed with Anaconda (free and open source distribution, comes with over 250 data science packages - find it on: www.anaconda.com)

**Project Plan:** Can be found in GitHub Issues


# Table of Contents
- 1: About Fisher's Iris Data Set
  - References
- 2: Packages used in this project
- 3: Importing Packages
- 4: Importing the Data
- 5: Using Python to gather basic stats about a dataset

## 1: About Fisher's Iris Data Set

The data of the Iris Data Set was collected in 1935 by botanist Edgar Anderson. He measured the sepal and petal length and width of 3 different Iris species: *Iris setosa*, *Iris versicolor* and *Iris virginica*. The data set received attention when it was used by British statistician and geneticist Sir Ronald Aylmer Fisher as an example in multivariant discriminate analysis a year later. (1,2)

 ![Petal and sepal demonstrated on species versicolor](http://suruchifialoke.com/img/icon_iris.png)
 
 *[Picture 1](http://suruchifialoke.com/img/icon_iris.png) Petal and sepal demonstrated on species Iris versicolor*

Nowadays the Iris Data Set has become a staple for testing in machine learning and statistics. The data set contains multivariate and real data. For each investigated species 50 instances were measured, totalling 150 instances. Each instance includes measurement of 4 attributes (petal width, petal length, sepal width, sepal length) as well as the corresponding species. The data set is freely available online, the data set used for this project was taken from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris) 

Its appeal for analysis is fittingly described by an online user (3): 
> “small but not trivial” 

> “simple but challenging”

### 1. References
(1)
(2)
(3)

## 2. Packages used in this project

Python has become very popular in Data Science. Packages and built-ins make data analysis with Python accessible and efficient, even if you aren’t an expert programmer.

The easiest way to avail of a variety of useful packages for Python is to download a Python distribution. Personally, I have installed Python through the [Anaconda distribution](https://www.anaconda.com/distribution/). Anaconda claims to be the most popular Python Data Science Distribution and installs 1000+ packages and helps manage these. Some of the popular packages included, and used in this project, are:

**IPython** – “a rich interactive interface, letting you quickly process data and test ideas.” (4) http://ipython.org/

**NumPy** – “the fundamental package for numerical computation. It defines the numerical array and matrix types and basic operations on them.” (4)  http://www.numpy.org/

**Matplotlib** – “a mature and popular plotting package, that provides publication-quality 2D plotting as well as rudimentary 3D plotting” (4) https://matplotlib.org/ 

**Seaborn** – “a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.”(5)  https://seaborn.pydata.org/

**Pandas** – “providing high-performance, easy to use data structures.” (4) http://pandas.pydata.org/ 

**SciPy Library** – “a collection of numerical algorithms and domain-specific toolboxes, including signal processing, optimization, statistics and much more.” (4) https://www.scipy.org/scipylib/index.html

I found SciPy to provide a great starting point and resource, more information can be found on: https://www.scipy.org/index.html.

### 2. References
(4) https://www.scipy.org/about.html
(5) https://seaborn.pydata.org/

## 3: Importing Packages

As seen above there is a host of useful packages. To be able to use these, they have to be imported into Python, use `import` to do so:

```
import pandas as pd 

import matplotlib.pyplot as plt 

import seaborn as sb 

import numpy as np 

from scipy import stats
```

An `as`can be added after the import command to give the package a different name to call upon, which saves time as you are writing your commands. Going forward Python will recognise the names and call upon the packages if asked to do so.


## 4: Importing the data

``` 
iris = pd.read_csv('iris.csv', header = None)
```

Reading the file through pandas by using `pandas.read_csv`reads a comma-separated csv into a DataFrame (I have called mine iris). It provides a tabular structure with labelled axes. 

Note: Make sure to check whether the file has headers. If not, include `header = None`  as seen above. Otherwise pandas will assume that the first row of data is a header.

As the csv file that I am using does not include a header, I have chosen to set a header with column names myself, to make analysis easier going forward:
``` 
iris.columns = ['sepal_length','sepal_width','petal_length','petal width','species']
```

There are several powerful options to clean up your data. I have chosen an easy command to exclude rows with missing data from my dataset: 
``` 
iris.dropna() #cleanup: delete rows with missing values
```


## 5: Using Python to gather basic stats about a dataset (v1)
Python is a handy tool to explore data. If you use IPython it enables an interactive session to explore data and figure out the key characteristics of the data you are working with on the fly.  I have used some handy commands to have Python give me more information about the data:

Print the whole DataFrame:
``` 
iris # have a look at the data set as a whole 
```

As the set seems to be very large, it might be enough to only have a sneak-peak at it and print only the first or last rows of the Dataframe. These commands came in very handy in double-checking whether I had assigned the column names properly:
```
iris.head(5) # show top 5 rows of data

iris.tail(5) # show last 5 rows of data 
```

Find out how many rows and columns the Dataframe consists of:
```
iris.shape # displays rows and columns
```

Find out which unique values a certain column contains by using the built-in `set()` command. In this case it makes sense to find out how many different species of Iris were measured:
```
set(iris['species'])
```

Are the measurements evenly distributed across the different species?
```
iris['species'].value_counts()
```

Gather some basic statistical information about the dataframe, like the mean of the columns:
```
iris.describe() # returns basic stats about the dataframe
iris.mean() # shows mean of columns
```

Python let’s you easily check the correlation between columns:
```
iris.corr() # returns correlation between columns
```

Note: All of these commands can also be used outside of IPython, however, you have to set them into a `print()` command to see the results displayed in the terminal.

In order to try out a different approach and get a lot of the basic stats in one go without using an interactive IPython session, I have bundled up some useful commands in a regular Python function called `explore(x)`. This prints out a nicely formatted overview of all the key points:

[insert code once finalized]

