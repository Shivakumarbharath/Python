import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('E:\Bharath\LEtzBargain\Refrigirators.xlsx', 'LG')  # To read Excel file
print(type(df))  # type of the object
print(df.head(5))  # to display 5rows
print(df.info())  # extra info

df['Product_MRP ₹'].plot()
plt.show()

print(df['Attributes'])
