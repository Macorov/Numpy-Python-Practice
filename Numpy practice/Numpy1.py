import numpy as np
a = np.array([[12,41,4],[1,42,133]])
print(a)
print(a.dtype)
print(a.size)
print(a.itemsize)
b = np.array([[122,71,4],[3,466,3]])
k = a*b
print(k)