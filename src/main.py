# imports
from graphics import *

# constants

# variables

# functions

# initiate

win = GraphWin("window 1", 500, 500)
win.setBackground(color_rgb(255, 255, 255))
pt0 = Point(100, 50)
# pt.draw(win)
c = Circle(pt0, 100)
c.draw(win)

pt1 = Point(120, 40)
l0 = Line(pt0, pt1)
l0.draw(win)
win.getMouse()
