import pandas as pd

df = pd.read_csv('Data/survey_results_public.csv')

# This contains a hobbiyst soloumn which says yes or no
# to get the count of unique values in the column

k = df['Hobbyist'].value_counts()
print(k)

# Slicing can be used for loc method for both rows and columns

print(df.loc[0:3, 'Hobbyist'])
