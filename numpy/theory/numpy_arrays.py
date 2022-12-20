import numpy as np


arr = np.array([1, 5, 2, 9, 10], dtype=np.int8)
nd_arr = np.array([
    [12, 45, 78],
    [34, 56, 13],
    [12, 98, 76]
    ], dtype=np.int16)
 
print(nd_arr.ndim) # how much dimensions in array
# 2
print(nd_arr.shape) # shape of array (rows, columns)
# (3, 3)
print(nd_arr.size) # number of all elements in array
# 9
print(nd_arr.itemsize) # bytes in RAM for each element in array
# 2

zeros_1d = np.zeros(5) # 1-dimensional array with 5 zeros
# array([0., 0., 0., 0., 0.])
zeros_3d = np.zeros((5, 4, 3), dtype=np.float32) # 3-dimensional array with zeros
# zeros_3d.shape == (5, 4, 3)

np.arange(5)
# array([0, 1, 2, 3, 4])
np.arange(2.5, 5)
# array([2.5, 3.5, 4.5])
np.arange(2.5, 5, 0.5)
# array([2.5, 3. , 3.5, 4. , 4.5])
np.arange(2.5, 5, 0.5, dtype=np.float16)
# array([2.5, 3. , 3.5, 4. , 4.5], dtype=float16)

arr = np.linspace(1, 2, 10)
# array([1.        , 1.11111111, 1.22222222, 1.33333333, 1.44444444,
#        1.55555556, 1.66666667, 1.77777778, 1.88888889, 2.        ])
arr = np.linspace(1, 2, 10, endpoint=False)
# array([1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])
arr, step = np.linspace(1, 2, 10, endpoint=True, retstep=True)
# step == 0.1111111111111111
arr, step = np.linspace(1, 2, 10, endpoint=False, retstep=True)
# step == 0.1

arr = np.arange(8)
# array([0, 1, 2, 3, 4, 5, 6, 7])
arr.shape = (2, 4) # change shape of an array (rows, columns)
# array([[0, 1, 2, 3],
#        [4, 5, 6, 7]])

arr = np.arange(8)
arr_new = arr.reshape((2, 4)) # returns a copy of reshaped array

arr = np.arange(8)
# by default is 'C' order, fills by rows.
arr_new = arr.reshape((2, 4), order='F') # 'F' fills array by colums.
# array([[0, 2, 4, 6],
#       [1, 3, 5, 7]])

arr = np.arange(8)
arr.shape = (2, 4)
# array([[0, 1, 2, 3],
#        [4, 5, 6, 7]])
arr_trans = arr.transpose() # columns becomes rows, rows becomes columns (only if ndim > 1)
# array([[0, 4],
#        [1, 5],
#        [2, 6],
#        [3, 7]])

nd_array =  np.linspace(0, 6, 12, endpoint=False).reshape(3,4)
# array([[0. , 0.5, 1. , 1.5],
#        [2. , 2.5, 3. , 3.5],
#        [4. , 4.5, 5. , 5.5]])
nd_array[1, 2] # same as nd_array[1][2]
# 3.0
nd_array[:2, 2]
# array([1., 3.])
nd_array[1:, 2:4]
# array([[3. , 3.5],
#       [5. , 5.5]])
nd_array[:, 2:4]
# array([[1. , 1.5],
#       [3. , 3.5],
#       [5. , 5.5]])
nd_array[:2]
# array([[0. , 0.5, 1. , 1.5],
#       [2. , 2.5, 3. , 3.5]])