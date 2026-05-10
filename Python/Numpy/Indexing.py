import numpy as np
#creating a 1-D array
# [start,end,step]   [::step slicing]
arr = np.array([1, 2, 3, 4, 5])
print(arr[2])       #accessing the 3rd element of the array
print(arr[0:3])     #accessing elements from index 0 to 2
print(arr[1:4:2])   #accessing elements from index 1 to 3 with a step of 2
print(arr[-1])      #accessing the last element of the array
print(arr[-4:-2])   #accessing elements from the 4th last to the 2nd last
print(arr[::2])     #accessing every 2nd element of the array
print(arr[::-1])    #accessing the array in reverse order