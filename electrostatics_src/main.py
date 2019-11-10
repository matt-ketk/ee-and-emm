import matplotlib.pyplot as plt
import numpy as np
# from electricField import ElectricField

"""
t = numpy.arange(-5., 5., 0.001)

# red dashes, blue squares and green triangles
plt.plot(numpy.cos(t), numpy.sin(t), linewidth=2.0)
plt.ylabel('some numbers')
plt.xlabel('x')
plt.show()
"""

# constants

E0 = 8.854187817 * (10**-12) # permittivity of free space
K = 1 / (4 * np.pi * E0) # coulomb's constant

# variables

# functions

def dist2(x0, y0, x, y):
    if np.any(np.power(y - y0, 2) + np.power(x - x0, 2) == 0.0):
        return 10**-9
    return np.power(y - y0, 2) + np.power(x - x0, 2)

def eField(x, y, x0, y0, q):
    return K * (q / dist2(x0, y0, x, y))

x = np.linspace(-0.1, 0.1, 1000)
y = np.linspace(-0.1, 0.1, 1000)

X, Y = np.meshgrid(x, y)
Z = eField(X, Y, X[10], Y[10], 10**-1)


fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title("Electric Field Intensity")
plt.show()

# print(numpy.zeros((20, 30)))
