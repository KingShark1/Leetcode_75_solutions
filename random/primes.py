import numpy as np

import sys

arr_1= np.array([[1,4,9,16,25,36,49], [1,3,5,7,9,11,13]])

arr_2 = np.array([[12,36,54,98,78,45,25], [123,56,498,75,58,256,2511]])
arr_3 = np.array([[3.25,2.25], [1.0,2.0, 3.0]], dtype='int64') 
arr_2[:,2]=[1.3]

arr_1 = arr_2+2

temp = np.full((1, 2), 2)

c = np.identity(4)

temp_1 = np.linalg.det(c)

print(arr_1)

print(temp)

print(temp_1)

print(arr_3)