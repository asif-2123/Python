import numpy as np

r, c = 2, 3
arr = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    arr.append(row)
print(np.array(arr))