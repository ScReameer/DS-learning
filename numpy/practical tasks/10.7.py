import numpy as np


def shuffle_seed(array):
    
    seed = np.random.randint(0, 2**32, dtype=np.int64)
    np.random.seed(seed)
    new_array = np.random.permutation(array)
    
    return (new_array, seed)

array = [1, 2, 3, 4, 5]
print(shuffle_seed(array))
# (array([1, 3, 2, 4, 5]), 2332342819)
print(shuffle_seed(array))
# (array([4, 5, 2, 3, 1]), 4155165971)