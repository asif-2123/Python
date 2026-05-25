import pandas as pd

list=[['Asif', 25, 'A'], ['Bob', 30, 'B'], ['Charlie', 35, 'C'], ['David', 40, 'A'], ['Eve', 45, 'B']]
df=pd.DataFrame(list, columns=['Name', 'Age', 'Grade'])
print(df) # print the dataframe