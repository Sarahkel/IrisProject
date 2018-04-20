# Sarah Scholz, 16/04/2018
# Iris Data Set Exploration Project scripts and code; for explanations refer to README

# IMPORT relevant packages, libraries etc.
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb 
import numpy as np 
from scipy import stats

# PREPARING THE DATA
# Read file and format columns
iris = pd.read_csv('iris.csv', header = None) # include header=None if you wish to assign column names as in the next line. I initially forgot this and ended up with my data set one line short
iris.columns = ['sepal_length','sepal_width','petal_length','petal width','species']
iris.dropna() # cleanup: delete rows with missing values

# split per species, adapted from: https://www.kaggle.com/willvegapunk/iris-data-set
setosa = iris[iris['species']=='Iris-setosa']
virginica = iris[iris['species']=='Iris-virginica']
versicolor = iris[iris['species']=='Iris-versicolor']

# Chapter3: BASIC STATS, data exploration

# Commands to be used in IPython, for interactive exploration (else needs to be printed):
iris # have a look at the data set as a whole (however, python might hide some rows due to length)
iris.shape # displays rows and columns
iris.head(5) # show top 5 rows of data
iris.tail(5) # show last 5 rows of data
# As IPython will shorten the data set you might want to double check how many species are in the data:
set(iris['species']) # set is an in-built function in Python which will show you unique values of a given list
iris['species'].value_counts()
iris.describe() # returns basic stats about the dataframe
iris.mean() # returns mean values for columns
setosa.mean()
virginica.mean()
versicolor.mean()
iris.cov() # returns co-variance between columns
iris.corr() # returns correlation between columns

# Python function to print out a summary of some handy stats for a dataset x (use x = iris for the purpose of this project)
def explore(x):
    print('To begin, lets find out how many rows and columns our dataframe x has:')
    print(x.shape)
    print('Below you can see the first 5 rows of the dataframe x')
    print(x.head(5))
    print()
    print('Below you can see the last 5 rows of the dataframe x')
    print(x.tail(5))
    print()
    print('Below you can see the unique values for the column -species- and how many instances of these are found:')
    print(set(x['species'])) # change this for any column you are interested in
    print(x['species'].value_counts()) # change this for any column you are interested in
    print()
    print('The following provides you with some basic stats about the dataframe:')
    print(x.describe()) # returns basic stats about the dataframe
# Not really universally usable. Maybe find more elegant solution for species column



# Tutorials and useful documentation concerning used packages:
# http://pandas.pydata.org/pandas-docs/stable/10min.html
# https://www.scipy.org/getting-started.html
# https://docs.scipy.org/doc/numpy/user/quickstart.html
# https://seaborn.pydata.org/tutorial/categorical.html
# https://matplotlib.org/
