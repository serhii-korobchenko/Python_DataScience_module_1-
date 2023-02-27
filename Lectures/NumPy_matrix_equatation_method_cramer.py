import numpy as np

a = np.matrix("1,2,5;1,-1,3;3,-6,-1")
b = np.matrix("-9;2;25")
a_det = round(np.linalg.det(a))
a_1 = np.matrix(a)
a_1[:, 0] = b
a_2 = np.matrix(a)
a_2[:, 1] = b
a_3 = np.matrix(a)
a_3[:, 2] = b
x = [
    round(np.linalg.det(a_1)) / a_det,
    round(np.linalg.det(a_2)) / a_det,
    round(np.linalg.det(a_3)) / a_det,
]
print(x)