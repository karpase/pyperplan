import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import glob
from functools import reduce


data = []
files = glob.glob('*rphstar.csv')
for f in files:
    df = pd.read_csv(f)    
    data.append(df)



df_merged = pd.concat(data)
print(df_merged)


X = df_merged.loc[:, df_merged.columns != 'hstar']
Y = df_merged["hstar"]
linear_regressor = LinearRegression() 
linear_regressor.fit(X, Y) 
print(linear_regressor.score(X, Y) )

print(X.columns)
print(linear_regressor.coef_)
