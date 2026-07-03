import numpy as np

array = np.array([
    [['a', 'g', 'f'], ['r', 't', 'e'], ['b', 'n', 'q']],
    [['a', 'g', 'f'], ['r', 't', 'e'], ['b', 'n', 'q']],
    [['a', 'g', 'f'], ['r', 't', 'e'], ['b', 'n', 'q']]
    ])

print(array.ndim) # ndim: no. of dimensions
print(array.shape) # shape: shape of the array (here: 3 x 3 x 3)