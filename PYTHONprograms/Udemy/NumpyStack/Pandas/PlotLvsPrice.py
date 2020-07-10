import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel('E:\Bharath\LEtzBargain\Refrigirators.xlsx','LG')#To read Excel file
def liters(row):
    return row['Attributes'][9:13]

x=df.apply(liters,axis=1)
y=df['Product_MRP ₹']

plt.scatter(x,y)
plt.show()