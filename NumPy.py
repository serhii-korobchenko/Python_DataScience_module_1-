import numpy as np

# массив NumPy
a = np.array([1, 2, 3, 4, 5], dtype=float)

print(a)  # [1. 2. 3. 4. 5.]

#матрица NumPy
m = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)

print(m)


a = np.array([1, 2, 3, 4, 5], dtype=float)
print(a.shape)  # (5,)

m = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
print(m.shape)  # (2, 3)