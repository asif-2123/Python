import numpy as np

arr = np.random.randint(20, 80, 15)
print(arr) # original array
print(np.sort(arr)) # sorted array
print(np.argmin(arr)) # minimum value in the array
print(np.argmax(arr)) # maximum value in the array