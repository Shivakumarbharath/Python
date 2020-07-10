import pandas as pd

df=pd.read_excel('E:\Bharath\LEtzBargain\Refrigirators.xlsx','LG')#To read Excel file
print(type(df))#type of the object
print(df.head(5))#to display 5rows
print(df.info())#extra info