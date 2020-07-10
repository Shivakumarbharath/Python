import pandas as pd

df=pd.read_excel('E:\Bharath\LEtzBargain\Refrigirators.xlsx','LG')#To read Excel file
print(type(df))#type of the object
print(df.head(5))#to display 5rows
print(df.info())#extra info


#the apply function is like a for loop for a complete row or for a complete column

def func(row):
    return row['Product_Brand'][0]


#the function is applied to all the elent in that colunmn
print(df.apply(func,axis=1))