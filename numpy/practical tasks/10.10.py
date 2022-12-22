import numpy as np


def get_loto(num, rows=5, columns=5):
    
    loto = np.random.randint(1, 101, size=(num, rows, columns))
    return loto
    
print(get_loto(3))