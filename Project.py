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

# Tutorials and useful documentation concerning used packages:
# http://pandas.pydata.org/pandas-docs/stable/10min.html
# https://www.scipy.org/getting-started.html
# https://docs.scipy.org/doc/numpy/user/quickstart.html
# https://seaborn.pydata.org/tutorial/categorical.html
# https://matplotlib.org/
