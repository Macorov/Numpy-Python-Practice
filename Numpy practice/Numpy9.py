import numpy as np
a = np.array([22,11,3])
b = np.array([1,42,2])
c = np.vstack((a,b))
print(c)
c = np.hstack((a,b))
print(c)