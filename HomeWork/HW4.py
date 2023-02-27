#RESULT:
# a = 4
# b = 5
# c = 3

import numpy as np
import matplotlib.pyplot as plt


# Define the three points as NumPy arrays:
A = np.array([1, 12])
B = np.array([3, 54])
C = np.array([-1, 2])

init_matrix = np.matrix([A,B, C])
# print(init_matrix)
transpon_matrix = init_matrix.T

x =  np.squeeze(np.asarray(transpon_matrix[0]))
y =  np.squeeze(np.asarray(transpon_matrix[1]))

# Find the coefficients of the quadratic function that fits the points
coefficients = np.polyfit(x, y, 2)


# Print the coefficients
print(coefficients)