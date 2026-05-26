import pandas as pd

students = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Grade': ['A', 'B', 'C', 'A', 'B']
}
df=pd.DataFrame(students)
print(df) # print the dataframe