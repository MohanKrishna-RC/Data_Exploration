import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv('glass.csv')

#Top 5 our data
print(df.head())

#Last 5 of the data
print(df.tail())

#Viewing the number of rows (214) and number of columns / features (10)
print(df.shape)

#General information of data
print(df.info())

#Look at Descriptive Statistic of Data.
print(df.describe())

#Data is clean and can continue to the Explorary Data Analysis stage
print(df.isnull().sum())

#Univariate analysis Type (Target features).
sns.countplot(df['Type'], color='red')

#Univariate analysis of RI (Refractive Index).
f = plt.figure(figsize=(20, 4))
f.add_subplot(1, 2, 1)
sns.distplot(df['RI'])
f.add_subplot(1, 2, 2)
sns.boxplot(df['RI'])


#Univariate analysis Na (Sodium).
f = plt.figure(figsize=(20, 4))
f.add_subplot(1, 2, 1)
sns.distplot(df['Na'], color='green')
f.add_subplot(1, 2, 2)
sns.boxplot(df['Na'], color='green')


#Correlation between features
df.corr().style.background_gradient().set_precision(2)

"""
There is a fairly strong positive linear relationship between glass types with Na, Al, and Ba.
As for negative linear relationships, the target has a strong relationship with Mg.
"""

