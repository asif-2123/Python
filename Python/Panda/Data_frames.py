import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
}
df = pd.DataFrame(data)
print(df)  # Print the DataFrame
print(df['Name'])  # Access the 'Name' column
print(df['Age'])  # Access the 'Age' column
print(df.loc[0])  # Access the first row using loc