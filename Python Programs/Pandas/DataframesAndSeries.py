import pandas as pd

# Dataframe is made up of rows and columns
# conveting data into dataframe using the dataframe method

# dictionary to dataframe

people = {

    'Name': ['Bharath', "Amulya", 'Bheema'],
    'Salary': ['1.5M', '2M', '1M'],
    'Net Worth': ['75B', '80B', '30B']

}

df = pd.DataFrame(people)

print(df)

# Accesing a single column

print(df['Net Worth'])

# The columns of the dataframe is a series object
print(type(df['Net Worth']))

# Series is basically a list of data
# just like dataframe it has lot more functionality than the list
# it is rows of single column


# We can use . notation

print(df.Salary)

# accecing more than one column
# Note to use an extra []

print(df[['Net Worth', 'Salary']])
# as it is more than one column it is no longer a series Object

# This returns another dataframe


# To get the indexes of the column
print(df.columns)

# To access row
# To get the integer location of the row we use
# iloc[index]

print(df.iloc[0])

# To access multiple rows
# we send lisst of indexes
# Note the inner square paraenthesis
print(df.iloc[[0, 1]])

# iloc can be used to access only specific columns
# but it should be in integer format of columns

print(df.iloc[[0,1],1])#to get salary column

# Same using loc names can be used

print(df.loc[[0,1],['Salary','Net Worth']])