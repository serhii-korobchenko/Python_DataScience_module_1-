import numpy as np

a = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)



print('___________________________________________')


a = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diag = np.diag(a)
print(diag)
b = np.diag(diag)
print(b)

print('___________________________________________')


a = np.eye(4, k=-1, dtype=float)
print(a)