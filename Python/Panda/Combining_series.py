import pandas as pd

county=pd.Series(['USA', 'India', 'China', 'Brazil', 'Russia'])
population=pd.Series([331, 1380, 1439, 212, 146])

s=pd.Series(population.values, index=county.values)
print(s) # print the series
print(s['India']) # access element with index 'India'