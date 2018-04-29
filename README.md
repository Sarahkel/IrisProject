# Iris Course Project - Programming and Scripting
GMIT Course Project on exploration of Fisher's Iris Data Set

### Task 
> *Imagine that you are to give a brief presentation to your co-workers on the data set, where you explain to them what investigating a data set entails and how Python can be used to do it.
The project entails researching the data set, and then writing documentation and code in the Python programming language based on that research*

**Use:** Python (www.python.org) - Note: Installed with Anaconda (free and open source distribution, comes with data science packages - find it on: www.anaconda.com)

**Project Plan:** Can be found in GitHub Issues

**How to use this code**:
The code for this project was written in Python and can be found in the files [Project.py]( https://github.com/Sarahkel/IrisProject/blob/master/Project.py) and [Visuals.py]( https://github.com/Sarahkel/IrisProject/blob/master/VIsuals.py). I suggest running the commands as needed in an interactive session in IPython to explore the data interactively. When using Python please note that you may have to add `print()` statements around the code in order for the result to be printed to the terminal. Also `plt.show()` may need to be added after plot commands in order for the plot to be shown in a separate window.


# Table of Contents
- 1: [About Fisher's Iris Data Set](https://github.com/Sarahkel/IrisProject/blob/master/README.md#1-about-fishers-iris-data-set)
  - 1.1: [References](https://github.com/Sarahkel/IrisProject/blob/master/README.md#11-references)
- 2: [Packages used in this project](https://github.com/Sarahkel/IrisProject/blob/master/README.md#2-packages-used-in-this-project)
  - 2.1: [References](https://github.com/Sarahkel/IrisProject/blob/master/README.md#21-references)
- 3: [Importing Packages](https://github.com/Sarahkel/IrisProject/blob/master/README.md#3-importing-packages)
- 4: [Importing the Data](https://github.com/Sarahkel/IrisProject/blob/master/README.md#4-importing-the-data)
- 5: [Using Python to gather basic stats about a dataset](https://github.com/Sarahkel/IrisProject/blob/master/README.md#5-using-python-to-gather-basic-stats-about-a-dataset-v1)
  - 5.1: [Summary of basic stats](https://github.com/Sarahkel/IrisProject/blob/master/README.md#51-summary-of-basic-stats)
- 6: [Using Visualisation](https://github.com/Sarahkel/IrisProject/blob/master/README.md#6-using-visualisation-v1)
  - 6.1: [Swarmplots](https://github.com/Sarahkel/IrisProject#61-swarmplots)
  - 6.2: [Layered Swarmplot](https://github.com/Sarahkel/IrisProject#62-layered-swarmplot)
  - 6.3: [Visualising Correlation](https://github.com/Sarahkel/IrisProject#63-visualising-correlation)
  - 6.4: [Summary of Visualisation findings](https://github.com/Sarahkel/IrisProject#64-summary-of-visualisation-findings)
- 7: [Conclusion](https://github.com/Sarahkel/IrisProject/blob/master/README.md#7-conclusion)

## 1: About Fisher's Iris Data Set

The data of the Iris Data Set was collected in 1935 by botanist Edgar Anderson. He measured the sepal and petal length and width of 3 different Iris species: *Iris setosa*, *Iris versicolor* and *Iris virginica*. The data set received attention when it was used by British statistician and geneticist Sir Ronald Aylmer Fisher as an example in multivariant discriminate analysis a year later. (1,2)

 <img src="http://suruchifialoke.com/img/icon_iris.png" alt="Petal and sepal demonstrated on species versicolor" height="200" />
 
 *[Picture 1](http://suruchifialoke.com/img/icon_iris.png) Petal and sepal demonstrated on species Iris versicolor*

Nowadays the Iris Data Set has become a staple for testing in machine learning and statistics. The data set contains multivariate and real data. For each investigated species 50 instances were measured, totalling 150 instances. Each instance includes measurement of 4 attributes (petal width, petal length, sepal width, sepal length) as well as the corresponding species. The data set is freely available online, the data set used for this project was taken from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris) 

Its appeal for analysis is fittingly described by an online user (3): 
> “small but not trivial” 

> “simple but challenging”

### 1.1: References
(1) Python Data Analytics: Data Analysis and Science using pandas, matplotlib and the Python Programming Language; Fabio Nelli, 2015; p. 238

(2) Data Analytics: Models and Algorithms for Intelligent Data Analysis; Thomas A. Runkler; 2016; p. 5

(3) https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching

## 2: Packages used in this project

Python has become very popular in Data Science. Packages and built-ins make data analysis with Python accessible and efficient, even if you aren’t an expert programmer.

The easiest way to avail of a variety of useful packages for Python is to download a Python distribution. Personally, I have installed Python through the [Anaconda distribution](https://www.anaconda.com/distribution/). Anaconda claims to be the most popular Python Data Science Distribution and installs 1000+ packages and helps manage these. Some of the popular packages included, and used in this project, are:

**IPython** – “a rich interactive interface, letting you quickly process data and test ideas.” (4) http://ipython.org/

**NumPy** – “the fundamental package for numerical computation. It defines the numerical array and matrix types and basic operations on them.” (4)  http://www.numpy.org/

**Matplotlib** – “a mature and popular plotting package, that provides publication-quality 2D plotting as well as rudimentary 3D plotting” (4) https://matplotlib.org/ 

**Seaborn** – “a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.”(5)  https://seaborn.pydata.org/

**Pandas** – “providing high-performance, easy to use data structures.” (4) http://pandas.pydata.org/ 

**SciPy Library** – “a collection of numerical algorithms and domain-specific toolboxes, including signal processing, optimization, statistics and much more.” (4) https://www.scipy.org/scipylib/index.html

I found SciPy to provide a great starting point and resource, more information can be found on: https://www.scipy.org/index.html.

### 2.1: References
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

Reading the file through pandas by using `pandas.read_csv`reads a comma-separated .csv into a DataFrame (I have called mine *iris*). It provides a tabular structure with labelled axes. 

Note: Make sure to check whether the file has headers. If not, include `header = None`  as seen above. Otherwise pandas will assume that the first row of data is a header.

As the .csv file that I am using does not include a header, I have chosen to set a header with column names myself, to make analysis easier going forward:

``` 
iris.columns = ['sepal_length','sepal_width','petal_length','petal width','species']
```

There are several powerful options to clean up your data. I have chosen an easy command to exclude rows with missing data from my dataset: 
``` 
iris.dropna() #cleanup: delete rows with missing values
```


## 5: Using Python to gather basic stats about a dataset

*Find the code used in this chapter in [Project.py]( https://github.com/Sarahkel/IrisProject/blob/master/Project.py)* 

Python is a useful tool to explore data. If you use IPython it enables an interactive session to explore data and figure out the key characteristics of the data you are working with on the fly. I have used some useful commands to have IPython give me more information about the data and provide a good starting point to find features worth investigating further. 

Firstly, tell IPython to run Project.py:

``` 
In [1]: run Project.py
``` 

Print the whole DataFrame:
``` 
iris # have a look at the data set as a whole 
```

As the set seems to be very large, it might be enough to only have a sneak-peak at it and print only the first or last rows of the Dataframe. These commands came in very useful in double-checking whether I had assigned the column names properly:
```
iris.head(5) # show top 5 rows of data

iris.tail(5) # show last 5 rows of data 
```

Find out how many rows and columns the Dataframe consists of:
```
In [2]: iris.shape # displays rows and columns
Out[2]: (150, 5)
```
 :arrow_right: IPython tells me that my iris DataFrame has 150 rows and 5 columns
 
Find out which unique values a certain column contains by using the built-in `set()` command. In this case it makes sense to find out how many different species of Iris were measured:
```
In [3]: set(iris['species'])
Out[3]: {'Iris-setosa', 'Iris-versicolor', 'Iris-virginica'}
```
:arrow_right: When looking at the data preview above, I could only see two species. However, after running above command it appears that there are 3 different species in the DataFrame.

Are the measurements evenly distributed across the different species?
```
In [4]: iris['species'].value_counts()
Out[4]:
Iris-versicolor    50
Iris-setosa        50
Iris-virginica     50
Name: species, dtype: int64
```
:arrow_right:  In the next chapter I will explore whethere there are significant differences between the different species. It will be useful to compare the stats of the species against each other.

Gather some basic statistical information about the dataframe, like the mean, min and max of the columns:
```
In [6]: iris.describe() # returns basic stats about the dataframe
Out[6]:
       sepal_length  sepal_width  petal_length  petal width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
```
```
In [7]: iris.mean() # shows mean of columns
Out[7]:
sepal_length    5.843333
sepal_width     3.054000
petal_length    3.758667
petal width     1.198667
dtype: float64
```
:arrow_right:  There appears to be a lot of variation in the size of petals and sepals. In the next chapter I will therefore attempt to have a closer look at the possible differences between the 3 species and if these are more clear-cut.

With a data set like this it makes sense to compare the different species against each other. For this, I have sliced the dataset into the different species:

```
setosa = iris[iris['species']=='Iris-setosa']
virginica = iris[iris['species']=='Iris-virginica']
versicolor = iris[iris['species']=='Iris-versicolor']
# see https://www.kaggle.com/willvegapunk/iris-data-set
```
Now I can use the very same commands to get insights into a particular subset of the data. I have chosen to print out the `.mean()` values: 

![screenshots mean](https://user-images.githubusercontent.com/35706251/39363592-b9a2bb78-4a22-11e8-9d9c-234016cd0cb1.png)

:arrow_right: There appear to be significant differences in the sizes of the species, with the petal being the most distinguished. We can also see that *Iris setosa* is by far the smallest. In the next chapter I will use plots to have a look at how to measurements present themselves.

**Correlation**

Python let’s you easily check the correlation between columns. Correlations gives an indication of the relationship between values. It ranges between -1 and 1. A correlation of 0 indicates that there is no relationship between values, -1 indicates a perfect negative correlation (as one goes up, the other goes down), 1 a perfect positive correlation (as one goes up, the other goes up as well). 
```
In [8]: iris.corr() # returns correlation between columns
Out[8]:
              sepal_length  sepal_width  petal_length  petal width
sepal_length      1.000000    -0.109369      0.871754     0.817954
sepal_width      -0.109369     1.000000     -0.420516    -0.356544
petal_length      0.871754    -0.420516      1.000000     0.962757
petal width       0.817954    -0.356544      0.962757     1.000000
```
:arrow_right: There appears to a strong positive correlation between petal size and sepal length, whereas it does not seem to correlate as much to the sepal width. It also appears that the longer the petal, the wider it is as well. Interestingly, there seems to be very little correlation between sepal length and sepal width. 

In order to try out a different approach and get a lot of the basic stats in one go without using an interactive IPython session, I have bundled up some useful commands in a regular Python function called `explore(x)`. This prints out a nicely formatted overview of all the key points:

[insert code once finalized]

### 5.1 Summary of basic stats
 :bar_chart: With just a quick script, I was able to gather a lot of information about my dataset. I learned that the DataFrame has **150 rows, 5 columns** and contains **50 measurements each** of **Petal Length, Petal Width, Sepal Length, Sepal Width** of the **3 Iris species Iris setosa, Iris versicolor and Iris virginica**. By looking at the **mean** it is evident that the sepal is significantly longer and wider than the petal on average. However, the size of both seem to be **correlated**, as there appears to be a strong positive correlation between petal size and sepal length even though this correlation does not seem to extend to the sepal width. As the **min and max** of the different values stretches across quite a large range it will be interesting to slice the data by the different species and see how they differ as well as use visualizations on the data in the next chapter.

## 6. Using visualisation

*Find the code used in this chapter in [Visuals.py]( https://github.com/Sarahkel/IrisProject/blob/master/VIsuals.py)*

Using the above introduced packages, especially matplotlib and seaborn (which is built matplotlib), I have created graphs. These are useful to present data to an audience. The graphs are customizable which also allows to adapt them to company branding.

First off, let's have a look at the data across all features in a boxplot. A boxplot provides a lot of information in one plot. We can see the median (black line in the box), with the box itself presenting the middle 50% of data. The black lines going outwards of the box show how far the range spans. The little black dots represent outliers. Where the median line liest within the box also gives an indication of how the data is skewed.

```
sb.boxplot(data = iris, orient = 'h')
```

![boxplot_complete](https://user-images.githubusercontent.com/35706251/39364156-e5b9e7a2-4a24-11e8-977c-a03e31ac4ce6.png)

:arrow_right: This boxplot gives an overview of how wide the measurements span and where their median and the bulk of the measurements fall. Sepal Width shows the smallest variation with petal length showing the most variation of measurements.

I would now like to understand if any differences between the species can be seen. 

### 6.1 Swarmplots

A swarmplot is a great option to get a good look at the data. Each point represents one measurement:


```
sb.swarmplot(x='species', y='petal_width', data=iris)
```
![swarm_petal width](https://user-images.githubusercontent.com/35706251/39330533-dda6b29c-4999-11e8-8ec5-282a44760e1f.png)

```
sb.swarmplot(x='species', y='petal_length', data=iris)
```

![swarm_petal length](https://user-images.githubusercontent.com/35706251/39330537-de2e2e70-4999-11e8-9e28-e1b1767856ff.png)

```
sb.swarmplot(x='species', y='sepal_length', data=iris)
```

![swarm_sepal length](https://user-images.githubusercontent.com/35706251/39330535-ddd7312e-4999-11e8-88f6-6089c5a36ebb.png)

```
sb.swarmplot(x='species', y='sepal_width', data=iris)
```
![swarm_sepal width](https://user-images.githubusercontent.com/35706251/39330536-de02d4aa-4999-11e8-8040-7a0fada01e6a.png)



:arrow_right: It is evident that there are indeed differences between the species to be observed. *Iris virginica* tends to be the largest of the species, with *Iris setosa* having a significantly smaller petal and shorter sepal, even though the sepal appears to be the widest of all three species. It can also be seen that there appears to be a good bit of overlap and similiarity between *Iris versicolo*r and *Iris Virginica* size-wise in all four characterists, whereas petal width and length of *Iris setosa* is considerably smaller to the point that there are no overlapping measurements.

### 6.2 Layered Swarmplot

Seaborn allows you to layer plots by bundling differet plots and running them in the same `plt.show()` command.
With this, it is possible for me to layer the swarmplots for the individual species and assign each its own color. (red = *Iris setosa*, green = *Iris versicolor*, blue = *Iris virginica*)

```
sb.swarmplot(color = 'red', data = setosa, orient = 'v')
sb.swarmplot(color = 'blue', data = virginica, orient = 'v')
sb.swarmplot(color = 'green', data = versicolor, orient = 'v')
```
![swarm_complete](https://user-images.githubusercontent.com/35706251/39333245-109f7a64-49a2-11e8-9160-d4b6087d9373.png)

*(red = Iris setosa, green = Iris versicolor, blue = Iris virginica)*

:arrow_right: Seeing all the species and characteristics in one chart makes it very evident that the main differenciating feature between the three is the length and width of their petals. The sepals, whereas not identical are a lot closer in size and indeed it reconfirms that the only feature in which *Iris setosa*  boasts the biggest size is the sepal width.

This can also be observed in the following graphs, which show the measurements per species for sepal and petal using `hue`: 

```
sb.swarmplot(x='sepal_width', y='sepal_length', hue = 'species', data=iris)
```

![swarm_sepal](https://user-images.githubusercontent.com/35706251/39359692-f2dfc10c-4a12-11e8-8500-1649f61b1089.png)

```
sb.swarmplot(x='petal_width', y='petal_length', hue = 'species', data=iris)
```

![swarm petal](https://user-images.githubusercontent.com/35706251/39359693-f302bf68-4a12-11e8-8029-f921b915ef20.png)



### 6.3 Visualising Correlation

In chapter 5 the `.corr` command suggested a strong positive correlation between petal length and petal width. The following jointplot illustrates this very well: 

```
sb.jointplot(x='petal_width', y='petal_length', data=iris, kind = 'reg') 
```

![correlation_all](https://user-images.githubusercontent.com/35706251/39334964-ecd953dc-49a8-11e8-95b4-6e710b0ffe3f.png)


:arrow_right: The joinplot not only underlines the correlation, it also adds extra information. It shows the [Pearson Correlation Coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) to be very close to 1 (positive correlation). It also provides a [p-value](http://www.dummies.com/education/math/statistics/what-a-p-value-tells-you-about-statistical-data/),  which is used in statistics to determine the significance of results.

### 6.4: Summary of Visualisation findings

In this chapter I set out to illustrate the differences between the species. The analysis shows that there are significant differences between the three flower species. A boxplot demonstrates that the widest variation in size occurs in the length of sepal and petal, with the petal length having the most variation. Swarmplots showed that the most distinguishing feature appears to be the petal. Species *Iris setosa* came out as the smallest of the three, however as the one with the widest sepal, *Iris virginica* is the largest. These findings were illustrated in one layered swarmplot as well, showing again how different the petal is from the other variables. The finding from the basic statistics chapter, indicates a strong positive correlation between petal length and petal width. A swarmplot of the leaf indicated a strong positive correlation which I was able to illustrate more clearly in a jointplot which also indicates the Pearson coefficient and statistical significance of the correlation.

## 7. Conclusion

In this project I attempted to analyse the Iris Data Set using Python and available packages to showcase not only a data analysis but more importantly how Python can support analysis.

Programming can be intimidating, and many users would expect to need a vast pre-existing knowledge of both mathematics and programming to use Python efficiently. I have introduced popular packages, which I have played around with over the duration of this projects and which can be used freely with Python such as pandas and matplotlib and how to avail of them and where to find tutorials on how to use them. 

I showcased how commands built into those packages allow a user to explore the given data set and effortlessly return not only the shape of the dataset in question but also statistical values, such as mean, min and max. I have written a function to print out a nicely formatted basic summary of the dataset as well. Find a summary of the analysis [here](https://github.com/Sarahkel/IrisProject/blob/master/README.md#51-summary-of-basic-stats).

Taking these insights, I have set out to showcase how visualisation can be used to dig deeper and to explore how the different Iris species differ from one another. I was able to show that the three species differ in appearance and was also able to visualize the apparent correlation between certain features. Find a summary of the analysis [here]().

Knowing that the three species differ in their features gives the user an interesting option to dive deeper and maybe even use Python to explore machine learning with the data set. An interesting notebook on machine learning with the Iris data set can be found on [Kaggle]( https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset). 



