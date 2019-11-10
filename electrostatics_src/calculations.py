# imports

# constants

E0 = 8.854187817 * (10**-12) # permittivity of free space
K = 1 / (4 * np.pi * E0) # coulomb's constant

# variables

# functions

def dist2(x0, y0, x1, y1):
    dist = (x1 - x0) ** 2 + (y1 - y0) ** 2
    if dist == 0:
        dist = 10 ** -9
    return dist

def eField(x0, y0, x, y, q):
    return K * (q / dist2(x0, y0, x, y))
