# imports
from graphics import *
from graph import Graph
from colorInterpolation import ColorInterpolation
from parametricGrid import ParametricGrid
from electricField import ElectricField

# constants

# variables

# functions

# initiate

win = GraphWin("window 1", 800, 600)
win.setBackground(color_rgb(255, 255, 255))
# pt0 = Point(100, 50)
# pt.draw(win)
# c = Circle(pt0, 100)
# c.draw(win)

# pt1 = Point(120, 40)
# l0 = Line(pt0, pt1)
# l0.draw(win)

"""
g = Graph(Point(200, 500), 400, 5, "m", 400, 5, "m")
g.draw(win)
for i in range(0, 100):
    win.plotPixel(200 + i, 550, color_rgb(255, 0, 0))
"""

pg = ParametricGrid(Point(200, 500), 200, 5, "m", 200, 5, "m", -100, 100, "N/C")
ElectricField.plotCharge(20, 20, (0.000000001), pg)
ElectricField.plotCharge(30, 40, (0.000001), pg)
pg.draw(win)


win.getMouse()
