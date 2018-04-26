# Sarah Scholz, 19/04/2018
# Visualisation of Iris Data Set

# IMPORT relevant packages, libraries etc.
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb 
import numpy as np 
from scipy import stats

# PREPARING THE DATA
# Read file and format columns
iris = pd.read_csv('iris.csv', header = None) #include header=None if you wish to assign column names as in the next line. I initially forgot this and ended up with my data set one line short
iris.columns = ['sepal_length','sepal_width','petal_length','petal_width','species']
iris.dropna() #cleanup: delete rows with missing values

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
sb.barplot(data = iris, orient = 'v)

# Combine 2 plots
sb.violinplot(x='species', y='sepal_length', data=iris)
sb.swarmplot(x='species', y='sepal_length', data=iris)
# Issue is that data points aren't well visible. Solution:
sb.violinplot(x='species', y='sepal_length', data=iris)
sb.swarmplot(x='species', y='sepal_length', data=iris, color='w')

sb.pairplot(iris)
           
# Combination Swarmplot
sb.swarmplot(color = 'red', data = setosa, orient = 'v')
sb.swarmplot(color = 'blue', data = virginica, orient = 'v')
sb.swarmplot(color = 'green', data = versicolor, orient = 'v')
           
# Correlation
sb.jointplot(x='petal_width', y='petal_length', data=iris, kind = 'reg') # strong positive correlation
sb.jointplot(x='petal_length', y='sepal_width', data=iris, kind = 'reg') # not a positive correlation

print('done!')
