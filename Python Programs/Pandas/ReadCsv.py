import pandas as pd

# to show maximum columns needed
# this is just for the view but all will be saved in the dataframe variable
# pd.set_option('display.max_columns',61)


# Read a csv file and store it in a variable
# syntax
# variable = pd.read_<file_type>(path)
df = pd.read_csv('Data/survey_results_public.csv')

# Dataframes
# here df is a dataframe
# dataframe is rows and colunms

# to view the data
# in pycharm to view as tables debug and right click on the variable ->view as dataframe
print(df)

# if you want to see a certain number of rows use the head method
print(df.head(15))

# if you want to view the last few rows then use the tail method same as above

# shape attribute gives the rows and colums in tuple form(rows ,coloumns)
# here shape is attribute and not method therefore no paranthesis
print(df.shape, 18)

# the info method gives the rows and coloumns and datatypes of allthe columns
print(df.info(), 21)
# here the object datatype usually mean strings


pd.set_option('display.max_rows', 60)
schema_df = pd.read_csv('Data/survey_results_schema.csv')
print(schema_df)
