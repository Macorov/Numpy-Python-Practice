import numpy as np
s = np.array([[12,41,3,13,312,77],[1,42,913,865,5,21]])
print(s)
print(s[0,1:3])
print(s[:,1])
print(s[0,:])
print(s[s<12])
b = np.where(s>12,s,-1)
print(b)