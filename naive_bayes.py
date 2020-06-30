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
print(df())

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

# Create a Naive Bayes object
nb = GaussianNB()
#Create variable x and y.
x = df.drop(columns=['Type'])
y = df['Type']
#Split data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=4)
#Training the model
nb.fit(x_train, y_train)
#Predict testing set
y_pred = nb.predict(x_test)
#Check performance of model
print(accuracy_score(y_test, y_pred))


"""
From the accuracy score, it can be seen that the value is 48% which in my opinion still needs to be improved again.
From my analysis, why the accuracy value of the Naive Bayes model is so low is due to imbalanced data.
"""
