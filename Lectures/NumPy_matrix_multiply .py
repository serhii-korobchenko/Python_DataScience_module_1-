import numpy as np

a = np.matrix("1,2,3;0,1,2")
b = np.matrix("1,2;0,4;-1,0")
c = a.dot(b)
print(c)