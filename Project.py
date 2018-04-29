# Sarah Scholz, 16/04/2018
# Iris Data Set Exploration Project scripts and code; for explanations refer to README

# Chapter 3
# IMPORT relevant packages, libraries etc.
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb 
import numpy as np 
from scipy import stats

# Chapter 4
# PREPARING THE DATA
# Read file and format columns
iris = pd.read_csv('iris.csv', header = None) # include header=None if you wish to assign column names as in the next line. I initially forgot this and ended up with my data set one line short
iris.columns = ['sepal_length','sepal_width','petal_length','petal_width','species']
iris.dropna() # cleanup: delete rows with missing values

# Chapter 5


# BASIC STATS, data exploration

# Commands to be used in IPython, for interactive exploration (else needs to be printed):
iris # have a look at the data set as a whole (however, python might hide some rows due to length)
# As IPython will shorten the data set you might want to double check how many species are in the data:
iris.head(5) # show top 5 rows of data
iris.tail(5) # show last 5 rows of data
iris.shape # displays rows and columns
set(iris['species']) # set is an in-built function in Python which will show you unique values of a given list
iris['species'].value_counts()
iris.describe() # returns basic stats about the dataframe
iris.mean() # returns mean values for columns

# split per species, adapted from: https://www.kaggle.com/willvegapunk/iris-data-set
setosa = iris[iris['species']=='Iris-setosa']
virginica = iris[iris['species']=='Iris-virginica']
versicolor = iris[iris['species']=='Iris-versicolor']
# return mean values
setosa.mean()
virginica.mean()
versicolor.mean()

# Covariance and correlation
iris.cov() # returns co-variance between columns (not used)
iris.corr() # returns correlation between columns

# Python function to print out a summary of some handy stats for a dataset x (use x = iris for the purpose of this project)
x = iris 


def explore(x):
    print('To begin, lets find out how many rows and columns our dataframe has:')
    print(x.shape)
    print('Below you can see the first 5 rows of the dataframe')
    print(x.head(5))
    print() # empty for formatting
    print('Below you can see the last 5 rows of the dataframe')
    print(x.tail(5))
    print()
    print('Below you can see the unique values for the column -species- and how many instances of these are found:')
    print(set(x['species'])) 
    print(x['species'].value_counts())
    print()
    print('The following provides you with some basic stats about the dataframe:')
    print(x.describe()) # returns basic stats about the dataframe
    print()
    print('Lets look at the means of the different species:')
    print()
    # split per species, adapted from: https://www.kaggle.com/willvegapunk/iris-data-set
    setosa = iris[iris['species']=='Iris-setosa']
    virginica = iris[iris['species']=='Iris-virginica']
    versicolor = iris[iris['species']=='Iris-versicolor']
    print('Setosa means are:')
    print(setosa.mean())
    print('Virginica means are:')
    print(virginica.mean())
    print('Means for Versicolor are:')
    print(versicolor.mean())
    print()
    print('Correlation Matrix:')
    print(iris.corr())

explore(iris)

print()
print('done!')


# Tutorials and useful documentation concerning used packages:
# http://pandas.pydata.org/pandas-docs/stable/10min.html
# https://www.scipy.org/getting-started.html
# https://docs.scipy.org/doc/numpy/user/quickstart.html
# https://seaborn.pydata.org/tutorial/categorical.html
# https://matplotlib.org/
