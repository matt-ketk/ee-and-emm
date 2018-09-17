# imports
from parametricGrid import ParametricGrid
import math

# constants

K = 9 * (10 ** 9)

# variables

# functions

def dist(x0, y0, x1, y1):
    return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

def dist2(x0, y0, x1, y1):
    d = (x1 - x0) ** 2 + (y1 - y0) ** 2
    if d == 0:
        d = 1
    return d

# class

class ElectricField:
    def plotCharge(x, y, c, graph):
        if isinstance(graph, ParametricGrid):
            for x1 in range(graph.getXMax()):
                for y1 in range(graph.getYMax()):
                    eField = K * (c / (dist2(x, y, x1, y1)))
                    print(eField)
                    if graph.get(x1, y1) + eField > graph.getMax():
                        graph.set(x1, y1, graph.getMax())
                    elif graph.get(x1, y1) + eField < graph.getMin():
                        graph.set(x1, y1, graph.getMax())
                    else:
                        graph.set(x1, y1, graph.get(x1, y1) + eField)
        else:
            raise TypeError()
