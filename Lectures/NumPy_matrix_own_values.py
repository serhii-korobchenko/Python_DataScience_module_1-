import numpy as np

a = np.matrix("1,0,3;-1,-1,2;4,7,2")
w, v = np.linalg.eig(a)

print(w)
print(v)