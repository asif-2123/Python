import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Amit", "Riya", "Sourav"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 88]
}
df = pd.DataFrame(data)

# Write DataFrame to Excel file
df.to_excel("students.xlsx", index=False)

print("DataFrame has been written to students.xlsx")