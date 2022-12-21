import numpy as np


vec1 = np.array([2, 4, 7, 2.5])
vec2 = np.array([12, 6, 3.6, 13])
vec1 + vec2 # in <class type='list'> '+' equals *.extend() func
# array([14. , 10. , 10.6, 15.5])

vec = np.array([3, 4])
length = np.sqrt(np.sum(vec ** 2)) # distance between start and end point of vector
# 5.0
length = np.linalg.norm(vec) # norm (length) of vector
# 5.0

vec1 = np.array([0, 3, 5])
vec2 = np.array([12, 4, 7])
distance = np.sqrt(np.sum((vec1 - vec2) ** 2)) # distance between endpoints of vec1 and vec2
# 12.206555615733702
vec1 = np.array([0, 3, 5])
vec2 = np.array([12, 4, 7])
distance = np.linalg.norm(vec1 - vec2)
# 12.206555615733702

vec1 = np.arange(1, 6)
vec2 = np.linspace(10, 20, 5)
scalar_product = np.sum(vec1 * vec2) # scalar (dot) product of vectors
# 250.0
scalar_product = np.dot(vec1, vec2)
# 250.0

x = np.array([25, 0])
y = np.array([0, 10])
np.dot(x, y)
# 0 means angle between vectors is 90 degrees

vec = np.array([2,7,18,28,18,1,8,4])
vec.min()
# 1
np.max(vec)
# 28
vec.mean()
# 10.75