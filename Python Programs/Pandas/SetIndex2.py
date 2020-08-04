import pandas as pd

df = pd.read_csv('Data/survey_results_public.csv', index_col='Respondent')
# To make the default index respondant

scema_df = pd.read_csv('Data/survey_results_schema.csv', index_col='Column')

print(scema_df.head())

# Now .loc[label] can be used
k = scema_df.loc['Age1stCode', 'QuestionText']
# questiontext  is the column name
# It is used here to view the full question
print(k)

# To sort the index
print(scema_df.sort_index())
# This is in accesnding

# If needed in deceinding
print(scema_df.sort_index(ascending=False))
