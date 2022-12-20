import numpy as np


mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)

nans_index = np.isnan(mystery)
n_nan = len(mystery[nans_index])
mystery_new = mystery.copy()
mystery_new[nans_index] = 0
mystery_int = mystery_new.copy()
np.int32(mystery_int)
array = mystery_int.copy()
array.sort()
table = array.reshape(5, 3, order='F')
col = table[:, 1]
