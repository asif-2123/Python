import pandas as pd

student = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 19, 21, 18, 23],
    'Grade': ['A', 'B', 'C', 'A', 'B']
}
df=pd.DataFrame(student)
print(df[df['Age']>20])
print(df[df['Grade']=='A'])
print(df.sort_values('Age'))
