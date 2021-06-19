import numpy as np
from numpy.linalg.linalg import det
a = np.array([22,11,3])
b = np.array([1,42,2])
q = np.array([[12,41,4],[1,42,133]])
print(q.T) #transpose matrix
s = np.array([[12,41],[1,42]])
print(np.linalg.inv(s)) #inverse matrix
print(np.linalg.det(s)) #determiner
print(np.diag(a))
