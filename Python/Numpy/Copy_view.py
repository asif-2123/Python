import numpy as np

arr=np.array([1,2,3,4,5])
b=arr.copy()
b[0]=10
print("arr:", arr)
print("b:", b)
c=arr.view()
c[2]=11
print("arr:", arr)
print("c:", c)
