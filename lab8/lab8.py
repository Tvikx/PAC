import numpy as np 
import pandas as pd
import matplotlib as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv('wells_info_with_prod.csv')
df = df.drop(['API'], axis=1)

x = df.drop(['Prod1Year'], axis= 1)
y = df['Prod1Year']

labels = ['PermitDate', 'SpudDate', 'CompletionDate', 'FirstProductionDate', 'operatorNameIHS', 'formation', 'BasinName', 'StateName', 'CountyName']
labelencoder_x = LabelEncoder()

for each in labels:
    x[each] = labelencoder_x.fit_transform(x[each])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

scaler = StandardScaler()
x_train, x_test = scaler.fit_transform(x_train), scaler.transform(x_test)

print(f'{x_train}\n{x_test}')