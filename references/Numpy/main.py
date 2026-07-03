import numpy as np

array = np.array([
    [['a', 'g', 'f'], ['r', 't', 'e'], ['b', 'n', 'q']],
    [['a', 'g', 'f'], ['r', 't', 'e'], ['b', 'n', 'q']],
    [['a', 'g', 'f'], ['r', 't', 'e'], ['b', 'n', 'q']]
    ])

word = array[0,1,0] + array[1,0,0] + array[2,1,1]
print("Word:" , word)