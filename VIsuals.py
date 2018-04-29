# Sarah Scholz, 19/04/2018
# Visualisation of Iris Data Set

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
iris = pd.read_csv('iris.csv', header = None) #include header=None if you wish to assign column names as in the next line. I initially forgot this and ended up with my data set one line short
iris.columns = ['sepal_length','sepal_width','petal_length','petal_width','species']
iris.dropna() #cleanup: delete rows with missing values

# From Chapter 5
# Split per species, so you can run tests on individual species, adapted from: https://www.kaggle.com/willvegapunk/iris-data-set
setosa = iris[iris['species']=='Iris-setosa']
virginica = iris[iris['species']=='Iris-virginica']
versicolor = iris[iris['species']=='Iris-versicolor']

# CHAPTER 6: Visualisation

sb.stripplot(x='species', y='sepal_length', data=iris) # stripplot
sb.swarmplot(x='species', y='sepal_length', data=iris) # to see how the data is distributed across the strip
sb.boxplot(x='species', y='sepal_length', data=iris) # boxplot

# Overview
sb.boxplot(data = iris, orient = 'h') # as per https://seaborn.pydata.org/generated/seaborn.boxplot.html
sb.barplot(data = iris, orient = 'v) # not used in favor of boxplot
           
# Swarmplots
sb.swarmplot(x='species', y='petal_width', data=iris)
sb.swarmplot(x='species', y='petal_length', data=iris)
sb.swarmplot(x='species', y='sepal_length', data=iris)
sb.swarmplot(x='species', y='sepal_width', data=iris)
           
# Layered Swarmplot
sb.swarmplot(color = 'red', data = setosa, orient = 'v')
sb.swarmplot(color = 'blue', data = virginica, orient = 'v')
sb.swarmplot(color = 'green', data = versicolor, orient = 'v')
           
# Combine 2 plots (not used in this form)
sb.violinplot(x='species', y='sepal_length', data=iris)
sb.swarmplot(x='species', y='sepal_length', data=iris)
# Issue is that data points aren't well visible. Solution:
sb.violinplot(x='species', y='sepal_length', data=iris)
sb.swarmplot(x='species', y='sepal_length', data=iris, color='w')
# Other option
sb.pairplot(iris)
           
# Swarmplots for Sepal and Petal separately
sb.swarmplot(x='sepal_width', y='sepal_length', hue = 'species', data=iris)
sb.swarmplot(x='petal_width', y='petal_length', hue = 'species', data=iris)
           
# Vosualising Correlation
sb.jointplot(x='petal_width', y='petal_length', data=iris, kind = 'reg') # strong positive correlation

print('done!')
