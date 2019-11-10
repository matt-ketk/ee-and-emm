# imports
import numpy as np

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

# class

class ElectricField:


    def plotCharge(fieldGrid, x0, y0, q):
        for x in range(0, len(fieldGrid)):
            for y in range(0, len(fieldGrid[x])):
                fieldGrid[x, y] += K * (q / dist2(x0, y0, x, y))

"""
test = np.zeros((200, 200))

for x in range(0, len(test)):
    for y in range(0, len(test[x])):
        test[x, y] = 1

print(test)
"""
"""
test = np.zeros((10, 10))
ElectricField.plotCharge(test, 4, 4, 10 ** -8)
print(test)
"""
