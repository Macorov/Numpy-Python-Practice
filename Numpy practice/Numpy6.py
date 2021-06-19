import numpy as np
a = np.array([22,11,3,122,31,154,31])
k = np.argwhere(a%2==0).flatten() #finding even number
print(a[k])