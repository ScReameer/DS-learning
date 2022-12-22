import numpy as np


def get_unique_loto(num, rows=5, columns=5):
    
    subsequence = np.arange(1, 101)
    result_array = np.zeros((num, rows, columns))
    
    for value in range(num):
        
        loto = np.random.choice(subsequence, size=(rows, columns), replace=False)
        result_array[value] = loto
        
    return result_array
        
    
print(get_unique_loto(3))