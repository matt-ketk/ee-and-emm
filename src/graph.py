# imports
from graphics import *

# constants
TICK_MARK_LENGTH = 5


# variables

# functions

# class

class Graph:

    _origin = Point(0, 0)
    _xScale = range(1)
    _yScale = range(1)

    _xIntervals = 1
    _yIntervals = 1

    _xLabel = "x"
    _yLabel = "y"

    def __init__(self, origin, xMax, xSteps, xLabel, yMax, ySteps, yLabel):

        self._origin = origin
        self._xScale = range(xMax)
        self._yScale = range(yMax)

        self._xIntervals = xSteps
        self._yIntervals = ySteps

        self._xLabel = xLabel
        self._yLabel = yLabel

    def draw(self, window):
        Line(self._origin, Point(self._origin.getX(), self._origin.getY() - self._yScale.stop)).draw(window);
        label = Text(Point(self._origin.getX(), self._origin.getY() - self._yScale.stop - 4 * TICK_MARK_LENGTH), "y (" + self._yLabel + ")")
        label.setSize(2 * self._yIntervals)
        label.draw(window)
        Line(self._origin, Point(self._origin.getX() + self._xScale.stop, self._origin.getY())).draw(window);
        label = Text(Point(self._origin.getX() + self._xScale.stop + 4 * TICK_MARK_LENGTH, self._origin.getY()), "x (" + self._xLabel + ")")
        label.setSize(2 * self._yIntervals)
        label.draw(window)

        for x in range(0, self._xScale.stop, int(self._xScale.stop / self._xIntervals)):
            Line(Point(x + self._origin.getX(), self._origin.getY() + TICK_MARK_LENGTH), Point(x + self._origin.getX(), self._origin.getY())).draw(window);
            label = Text(Point(x + self._origin.getX(), self._origin.getY() + 4 * TICK_MARK_LENGTH), x)
            label.setSize(2 * self._xIntervals)
            label.draw(window)
        for y in range(0, self._yScale.stop, int(self._yScale.stop / self._yIntervals)):
            Line(Point(self._origin.getX() - TICK_MARK_LENGTH, self._origin.getY() - y), Point(self._origin.getX(), self._origin.getY() - y)).draw(window);
            label = Text(Point(self._origin.getX() - 4 * TICK_MARK_LENGTH, self._origin.getY() - y), y)
            label.setSize(2 * self._yIntervals)
            label.draw(window)

    def getOrigin(self):
        return self._origin

    def isIn(self, pt):
        return ((pt.getX() in self._xScale) and (pt.getY() in self._yScale))

    def getXMax(self):
        return self._xScale.stop

    def getYMax(self):
        return self._yScale.stop
