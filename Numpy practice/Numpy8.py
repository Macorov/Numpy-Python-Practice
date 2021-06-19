import numpy as np
a = np.array([[1,32],[7,4]])
b = np.array([[13,54]])
k = np.concatenate((a,b),axis = None)
print(k)
k = np.concatenate((a,b),axis = 0)
print(k)
k = np.concatenate((a,b.T),axis = 1)
print(k)