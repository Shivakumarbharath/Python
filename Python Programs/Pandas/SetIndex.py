import pandas as pd

people = {

    'Name': ['Bharath', "Amulya", 'Bheema'],
    'Salary': ['1.5M', '2M', '1M'],
    'Net Worth': ['75B', '80B', '30B']

}

df = pd.DataFrame(people)

# Index for the above data
# Pandas by default give integer index
# to set custom column as index we use
# the set_index method


# This method returns another dataframe making the Net worth as the index
print(df.set_index('Net Worth'))
print(df)

# To replace the original dataframe itself
# we use the below syntax

df.set_index('Net Worth', inplace=True)

print(df)

# To view the changed  index
# use .index attribute
print(df.index)

# After the index is changed the arguments in the loc will also be changed as it will be a unique
print(df.loc['80B'])

# Name      Amulya
# Salary        2M
# Name: 80B, dtype: object
# Here the Name is the index

# If used in loc type error is raised
# Still if integers is to be used then used iloc in such situation
try:
    print(df.loc[0], '47')
except:
    print(df.iloc[0], '49')

# To remove the index that has been set use reset method
df.reset_index(inplace=True)
print(df, '53')

# To make the index while creating the dataframe
# df = pd.read_csv('Data/survey_results_public.csv',index_cloumn='Name')
