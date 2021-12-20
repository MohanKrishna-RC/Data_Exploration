import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

print(df.shape)

print(df.head())

# print(df.tail())

# df.rename(columns={'Id': 'id', 'PID': 'pid', 'MSSubClass': 'ms_subclass'}, inplace =True)

df.columns = [i.replace(' ','_').lower() for i in df.columns]

# print(df.head())
# print(df.columns)

#EDA analysis
"""
Next, I want to examine my data to inspect data types, identify null values, 
and inspect the summary statistics for each column available.
"""

def ames_eda(df):
    eda_df = {}
    eda_df['null_sum'] = df.isnull().sum()
    eda_df['null_pct'] = df.isnull().mean()
    eda_df['dtypes' ] = df.dtypes
    eda_df['count'] = df.count()
    eda_df['mean'] = df.mean()
    eda_df['median'] = df.median()
    eda_df['min'] = df.min()
    eda_df['max'] = df.max()

    return pd.DataFrame(eda_df)

# print(ames_eda(df))

# I want to inspect what all my column types and evaluate if there are any implications for EDA
df.dtypes.value_counts()

print(df.select_dtypes(include=['object']).columns)

"""
A key step in EDA investment to explore whether there is a relationship between our potential feature columns and our target.
"""
"""
We can calculate the correlations between potential features and our target, but correlations won't be calcuated 
for non-numeric columns.
"""
"""
Using seaborn, we can visualize these pair-wise correlations.
"""
correlations = df.corrwith(df['saleprice']).iloc[:-1].to_frame()
correlations['abs'] = correlations[0].abs()
sorted_correlations = correlations.sort_values('abs',ascending=False)[0]

fig,ax = plt.subplots(figsize=(10,20))
sns.heatmap(sorted_correlations.to_frame(),cmap='coolwarm',annot=True,vmin=-1,vmax=1, ax = ax)

"""
A great way to achieve this is to generate a box plot that compares the values of an ordinal/categorical and visualize a relationship with the target variable.

"""
sns.boxplot(df['central_air'],df['saleprice']).set_title('Central Air vs. Sale Price')
"""
Based on this visualization, we will need to convert these columns to represent numeric values when we clean our data before modeling.
We can also use the box plots to look at features that have categorical values. For example, kitchen quality is ranked on a scale from poor to excellent and again we can visualize a relationship to target(price).
"""
sns.boxplot(df['kitchen_qual'],df['saleprice']).set_title('Kitchen Quality vs. Sale Price')

"""
One option to clean our categorical data is to define a function and apply it to our data such as in the example below to convert the garage quality from its categorical labels to numeric.
First, we want to identify the range of values that a certain feature may contain. Based on the values identified, we can create a function to overwrite each value with numerical values.
"""
def garage_qual_cleaner(cell):
    if cell == 'Ex':
        return 5
    elif cell == 'Gd':
        return 4
    elif cell == 'TA':
        return 3
    elif cell == 'Fa':
        return 2
    elif cell == 'Po':
        return 1
    else:
        return 0

print(df['kitchen_qual'].value_counts())

df['kitchen_qual'].map({'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1})


def data_cleaner(df):
    # map numeric values onto all the quality columns using a quality dictionary
    qual_dict = {'Po': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4}
    # create a list of ordinal column names
    # last section ignores "overall quality columns which will be addressed below
    ordinal_col_names = [col for col in df.columns if (
        col[-4:] in ['qual', 'cond']) and col[:3] != 'ove']
    # creating a new feature called age
    df['age'] = df.apply(lambda row: row['yr_sold'] -
                         max(row['year_built'], row['year_remod/add']), axis=1)
    # dummify the date sold column
    df['date_sold'] = df.apply(lambda row: str(
        row['mo_sold']) + '-' + str(row['yr_sold']), axis=1)
    df.loc[:, df.dtypes != 'object'] = df.loc[:, df.dtypes !=
                                              'object'].apply(lambda col: col.fillna(col.mean()))

    # transforming columns
    df[ordinal_col_names] = df[ordinal_col_names].applymap(
        lambda cell: 2 if pd.isnull(cell) else qual_dict[cell])

    return df


# applying the function to train data
train = data_cleaner(df)
