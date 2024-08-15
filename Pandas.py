import pandas as pd
import numpy as np
ser = pd.Series(np.random.rand(10))
print(ser)
print(type(ser))
print(ser.dtype)

data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)

data = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}
series = pd.Series(data)
# print(series)


print(series[0])  # Access the first element
print(series['B'])  # Access the element with label 'B'
print(series[2:4])  # Access elements at index 2 and 3

To Create a DF using Dictionary 
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)

print(df)


# Creating a DataFrame from a List of Lists:

data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco'],
    ['Charlie', 35, 'Los Angeles']
]

columns = ['Name', 'Age', 'City']

df = pd.DataFrame(data, columns=columns)

# Creating a DataFrame from a NumPy Array:

data = np.array([
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco'],
    ['Charlie', 35, 'Los Angeles']
])

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])


#TO Read From CSV file 
df = pd.read_csv('data.csv')


#Creating an Empty DataFrame:

data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'San Francisco'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Los Angeles'}
]

df = pd.DataFrame()
df['Name'] = ['Alice', 'Bob', 'Charlie']
df['Age'] = [25, 30, 35]
df['City'] = ['New York', 'San Francisco', 'Los Angeles']


Creating a DataFrame from a List of Dictionaries:

data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'San Francisco'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Los Angeles'}
]

df = pd.DataFrame(data)

print(df)

# To select specific columns in 

selected_columns = df[['Column1', 'Column2']]


# How to filter the rows 


condition = df['Column'] > 50

filtered_df = df[condition]

#OR

filtered_df = df[df['score']>80]

#Using more than one column

condition = (df['Column1'] > 50) & (df['Column2'] == 'Value')
filtered_df = df[condition]


#Using Sql type syntax

filtered_df = df.query('Column1 > 50 and Column2 == "Value"')


#Find max value in a column

maxi = df['score'].max()


# FInd the data types for a particular column
# Find some regular expressions

print(df.dtypes)print(df['Age'].mean())
print(df['Age'].sum())
print(df['Age'].min())
print(df["Age"].max())
print(df['Age'].std())
print(df['Age'].value_counts())
print(df['Age'].nunique)
new_df = df.sort_values(by = ['Age'],ascending = [False])
print(new_df)
print(df['Age'].count())

#Using is in operator in Python 
df2 = df[df['department'].isin(['marketing','engineering'])]

#How to join or merge two columns in 
db_employee_dept = db_employee.merge(db_dept, how = 'left', left_on = 'department_id', right_on = 'id')


#To change the index

new_df = df.index['first','second']

#To create DF using np
new_df = pd.DataFrame(np.random.rand(10,5),index = np.arange(10))

#To transpose 
n_df = df.T

#axis =0 implies rows

#To sort based on index

n_df = df.sort_index(axis=0,ascending = False)

#To get the number of rows and columns 

df.shape

#To drop the columns

df.drop(['column1','column2'],inplace=True)
new_df = df.drop(['column1','column2'])

#To know the null values in a particular column
pd.isnull(df)
pd.isnull(df).sum()

#To drop all the rows where there are null values 

df.dropna(inplace=True)


# To change the data type 
df['Amount']= df['Amount'].astype('int')

#To rename the columns 
df.rename(columns={'NaME':'Name'})

#To sort Based on index
df.sort_index()

#To find n largest elements

df['column'].nlargest(5)

#Find how many times each value occured in a column

df['Column'].value_counts()

#Find how many times each value occured in a column by percentage
df['Column'].value_counts(normalize = True)

#How to group the data and use aggregate functions

data = {'Category': ['A', 'B', 'A', 'B', 'A'],
        'Value': [10, 15, 20, 25, 30]}

df = pd.DataFrame(data)
grouped   =  df.groupby('Category')['Value'].min().reset_index()
grouped_1 =  df.groupby('Category')['Value'].max().reset_index()
grouped_2 =  df.groupby('Category')['Value'].agg(['sum','min','max']).reset_index()
print(grouped)
print(grouped_1)
print(grouped_2)
















