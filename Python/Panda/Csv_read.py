import pandas as pd

df=pd.read_csv('data.csv')


print(df.head(1)) # first 1 rows of the dataframe
print(df.tail(1)) # last 1 rows of the dataframe
print(df.info()) # information about the dataframe
print(df.describe()) # statistical summary of the dataframe
print(df[df['Age']<30]) # filter rows where Age is less than 30