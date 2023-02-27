import numpy as np

a = np.matrix("1,2,3;4,5,6")
b = a.reshape((3, 2))
print(b)