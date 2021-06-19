import numpy as np
a = np.array([12,145,1])
b = a
b[0] = 111
print(a)
b = a.copy()
b[0] = 44
print(a)