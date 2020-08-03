import pandas as pd

df = pd.read_excel('E:\Bharath\LEtzBargain\Refrigirators.xlsx', 'LG')  # To read Excel file
print(type(df))  # type of the object
print(df.head(5))  # to display 5rows
k = df.columns  # this provides the headings of the columns

df.columns = ['Title', 'Attributes', 'Flipkart Link', 'Product_MRP ₹',
              'Product__Model', 'Product_Brand', 'Product_Category',
              'product_sub__categories']  # IN this way you can change the data only in output not in the file

print(df.columns)

print(df.head())

# to print a particular column

print(df['Attributes'])

# more than one column

print(df[['Attributes', 'Product_MRP ₹']])

# accesing the rpws

print(df.loc[1])

# accessing more rows

# To print refrigirators more than 100000

print(df[df['Product_MRP ₹'] > 100000])
