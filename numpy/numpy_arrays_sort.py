import numpy as np


arr = np.array([23,12,45,12,23,4,15,3])
arr_new = np.sort(arr) # return new sorted array
print(arr)
# [23 12 45 12 23  4 15  3]
print(arr_new)
# [ 3  4 12 12 15 23 23 45]

arr = np.array([23,12,45,12,23,4,15,3])
print(arr.sort()) # changes existed array
# None
print(arr)
# [ 3  4 12 12 15 23 23 45]

data = np.array([4, 9, -4, 3])
roots = np.sqrt(data)
# RuntimeWarning: invalid value encountered in sqrt
# array([2.        , 3.        ,        nan, 1.73205081])
print(None is None)
# True
print(np.nan is np.nan)
# True
print(np.nan is None)
# False
print(None == None)
# True
print(np.nan == np.nan)
# False
sum(roots)
# nan
np.isnan(roots) # which elements is nan <class 'float'>
# array([False, False,  True, False])
roots[np.isnan(roots)]
# array([nan])
roots[np.isnan(roots)] = 0
roots
# array([2.        , 3.        , 0.        , 1.73205081])