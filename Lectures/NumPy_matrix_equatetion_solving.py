import numpy as np

a = np.matrix("1,2,5;1,-1,3;3,-6,-1")
b = np.matrix("-9;2;25")
a_inv = np.linalg.inv(a)
x = a_inv.dot(b)
print(x)