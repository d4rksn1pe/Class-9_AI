import pandas as pd
d = pd.read_csv(r'.csv')
d.insert(5, 'Email', ['1', '2', '2',  '23', '5'])
d.drop('Delete', axis=1, inplace=True)
d.head()