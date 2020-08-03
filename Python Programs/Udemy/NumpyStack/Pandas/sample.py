import pandas as pd

name = "april2012.xls"
df = pd.read_excel('E:\shiva\\' + name, 'Sheet2', header=5)
print(df.head())
print(df.columns)
