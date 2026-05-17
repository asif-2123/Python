import numpy as np
#1-D array
arr = np.array([1,2,3,4,5,6,7,8])
# Reshaping the array to 2 rows and 4 columns
reshaped_arr = arr.reshape(2,4) 
print("Original Array:", arr)
print("Reshaped Array:\n", reshaped_arr)

#2-D array
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# Reshaping the 2-D array to 9 rows and 1 column
reshaped_arr2 = arr2.reshape(9,1)
print("Original 2-D Array:\n", arr2)    
print("Reshaped 2-D Array:\n", reshaped_arr2)