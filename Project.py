import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb 
import numpy as np 
from scipy import stats

iris = pd.read_csv('iris.csv')
iris.columns = ['sepal_length','sepal_width','petal_length','petal width','species']

# http://pandas.pydata.org/pandas-docs/stable/10min.html
# https://www.scipy.org/getting-started.html
# https://docs.scipy.org/doc/numpy/user/quickstart.html
# https://seaborn.pydata.org/tutorial/categorical.html
# https://matplotlib.org/
