import numpy as np
import pandas as pd

df = pd.read_csv('titanic_with_labels.csv', sep = ' ', index_col = 0)
df = df[df["sex"].str.contains("м|М|Мужчина|m|ж|Ж")]
df = df.replace({'sex':{'м':1, 'М':1, 'm':1, 'Мужчина':1, 'ж':0, 'Ж':0}})
df = df.fillna(df['row_number'].max())
df['liters_drunk'][df['liters_drunk'] > 10] = np.nan
df['liters_drunk'][df['liters_drunk'] < 0] = np.nan
df = df.fillna(df['liters_drunk'].mean())

df.to_csv("out.csv")
print(df.head(10))