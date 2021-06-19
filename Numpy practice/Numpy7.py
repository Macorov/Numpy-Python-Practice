import numpy as np
k = np.arange(1,7)
print(k)
k = k.reshape((2,3))
print(k)
b = k[np.newaxis,:]
k = k[:,np.newaxis]
print(k)
print(b)