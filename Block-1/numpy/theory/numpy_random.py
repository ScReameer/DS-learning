import numpy as np


np.random.rand() # float 0 < x < 1

np.random.rand(5) # form of massive (rows, columns)
# array([0.83745099, 0.58426808, 0.89206204, 0.41149807, 0.42445145])
np.random.rand(2, 3)
# array([[0.94931212, 0.06680018, 0.26707599],
#      [0.67908873, 0.18001743, 0.97732239]])

shape = (2, 3)
np.random.sample(shape)
# array([[0.39756103, 0.01995168, 0.2768951 ],
#       [0.82195372, 0.26435273, 0.00957881]])

np.random.uniform(-1000, 500, size=(2, 3)) # (low, high, size=*form of array in tuple*)
# array([[ 129.22164163,   77.69090611, -132.9656972 ],
#        [  18.65802226, -317.14793906,   85.3613547 ]])

np.random.randint(6, 12, size=(3,3))
# array([[ 9,  6, 10],
#        [10, 11, 10],
#        [ 7, 10, 11]])

arr = np.arange(6)
print(arr)
# [0 1 2 3 4 5]
print(np.random.shuffle(arr))
# None
arr
# array([0, 5, 1, 3, 2, 4])
np.random.permutation(arr) # returns shuffled array

np.random.permutation(10) # arange(10) -> shuffle
# array([7, 8, 2, 9, 4, 3, 1, 0, 5, 6])

workers = ['Ivan', 'Nikita', 'Maria', 'John', 'Kate']
choice = np.random.choice(workers, size=2, replace=False) # replace - can elements have duplicates or not
print(choice) # random 2 names

np.random.seed(23) # fixes random seed 