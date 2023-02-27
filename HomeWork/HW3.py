import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the three points as NumPy arrays:
A = np.array([np.sqrt(3), 0, np.sqrt(3)])
B = np.array([np.sqrt(6), 0.5, 0])
C = np.array([1, 1/np.sqrt(3), 1])

# Calculate the midpoints of the line segments AB, AC, and BC:
MAB = (A + B) / 2
MAC = (A + C) / 2
MBC = (B + C) / 2

#Calculate the direction vectors of the line segments AB, AC, and BC:
u = B - A
v = C - A
w = C - B

#Calculate the normal vector of the plane containing the points A, B, and C:
n = np.cross(u, v)

#Calculate the coefficients of the quadratic equation defining the ellipsoid:
alpha = np.dot(u, u)
beta = np.dot(v, v)
gamma = np.dot(w, w)
delta = 2 * np.dot(u, v * np.dot(w, n))
epsilon = 2 * np.dot(u, w * np.dot(v, n))
zeta = 2 * np.dot(v, w * np.dot(u, n))

#Calculate the center of the ellipsoid:
D = np.linalg.solve(np.array([[alpha, delta/2, epsilon/2], [delta/2, beta, zeta/2], [epsilon/2, zeta/2, gamma]]), np.array([np.dot(A, A) - np.dot(MAB, MAB), np.dot(B, B) - np.dot(MBC, MBC), np.dot(C, C) - np.dot(MAC, MAC)]))

#Calculate the radii of the ellipsoid:
a = np.sqrt((np.dot(D-MAB,u)**2 + np.dot(D-MAB,v)**2 + np.dot(D-MAB,w)**2) / alpha)
b = np.sqrt((np.dot(D-MBC,u)**2 + np.dot(D-MBC,v)**2 + np.dot(D-MBC,w)**2) / beta)
c = np.sqrt((np.dot(D-MAC,u)**2 + np.dot(D-MAC,v)**2 + np.dot(D-MAC,w)**2) / gamma)

#Result
print (f' a**2 = {a**2}, b**2 = {b**2}, c**2 = {c**2}')


#Print the standard equation of the ellipsoid:
print(f"(x - {D[0]})**2/{a**2} + (y - {D[1]})**2/{b**2} + (z - {D[2]})**2/{c**2} = 1")

#DEPICT ELLIPSOID
# Define a grid of points to plot the ellipsoid surface
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = D[0] + a * np.outer(np.cos(u), np.sin(v))
y = D[1] + b * np.outer(np.sin(u), np.sin(v))
z = D[2] + c * np.outer(np.ones_like(u), np.cos(v))

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='b')

# Set the plot limits and labels
ax.set_xlim(D[0] - a, D[0] + a)
ax.set_ylim(D[1] - b, D[1] + b)
ax.set_zlim(D[2] - c, D[2] + c)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
