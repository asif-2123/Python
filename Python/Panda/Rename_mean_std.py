import pandas as pd

students = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Grade': ['A', 'B', 'C', 'A', 'B']
}
df=pd.DataFrame(students)
print(df) # print the dataframe
df2=df.rename(columns={'Age':'Years'})
print(df2) # print the modified dataframe
print(df2['Years'])
print(df2['Years'].mean()) # mean of the 'Years' column 
print(df2['Years'].std()) # maximum of the 'Years' column