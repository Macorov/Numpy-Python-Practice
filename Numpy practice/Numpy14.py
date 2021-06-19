import numpy as np
from numpy.core.fromnumeric import size
a = np.random.random((3,4))
#print(a)
a = np.random.randint(3,10,size=(2,3))
print(a)
p = np.random.choice([2,4,23,13],size=10)
print(p)