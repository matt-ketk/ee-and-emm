# imports
from graphics import *
from graph import Graph
from colorInterpolation import ColorInterpolation

import threading

# constants
TICK_MARK_LENGTH = 5

PARAMETRIC_LEGEND_OFFSET = 35
PARAMETRIC_LEGEND_WIDTH = 20
PARAMETRIC_LEGEND_LENGTH = 200
# variables

# functions

# class

class ParametricGrid(Graph):

    _min = 0
    _max = 1
    _parametricUnit = "a"
    _gridValues = []
    def __init__(self, origin, xMax, xSteps, xLabel, yMax, ySteps, yLabel, min, max, unit):
        super().__init__(origin, xMax, xSteps, xLabel, yMax, ySteps, yLabel)
        self._min = min
        self._max = max
        self._parametricUnit = unit
        self._gridValues = [[0 for y in range(self._yScale.stop)] for x in range(self._xScale.stop)]


    def get(self, x, y):
        return self._gridValues[x][y]

    def set(self, x, y, v):
        if v >= self._min and v <= self._max:
            self._gridValues[x][y] = v
        else:
            raise ValueError

    def getMin(self):
        return self._min

    def getMax(self):
        return self._max

    def draw(self, window):
        super().draw(window)

        rectOrigin = (self._origin.getX(), self._origin.getY() + PARAMETRIC_LEGEND_OFFSET)
        rectOpposite = (rectOrigin[0] + PARAMETRIC_LEGEND_LENGTH, rectOrigin[1] + PARAMETRIC_LEGEND_WIDTH)
        Rectangle(Point(rectOrigin[0], rectOrigin[1]), Point(rectOpposite[0], rectOpposite[1])).draw(window)
        label = Text(Point(rectOpposite[0] + 3 * TICK_MARK_LENGTH, rectOrigin[1] + 2 * TICK_MARK_LENGTH), self._parametricUnit)
        label.setSize(2 * self._yIntervals)
        label.draw(window)
        interval = 0
        for x in range(0, int(rectOpposite[0] - rectOrigin[0]), int(int(rectOpposite[0] - rectOrigin[0]) / 4)):
            Line(Point(rectOrigin[0] + x, rectOpposite[1] + TICK_MARK_LENGTH), Point(rectOrigin[0] + x, rectOpposite[1])).draw(window)
            label = Text(Point(rectOrigin[0] + x, rectOpposite[1] + 3 * TICK_MARK_LENGTH), self._min + (interval / 4) * (self._max - self._min))
            label.setSize(2 * self._yIntervals)
            label.draw(window)
            interval += 1
        fillOrigin = (rectOrigin[0] + 1, rectOrigin[1] + 1)
        fillOpposite = (rectOpposite[0] - 1, rectOpposite[1] - 1)
        print(int(fillOpposite[0] - fillOrigin[0]))
        grad = range(int(fillOpposite[0] - fillOrigin[0]), -1, -1)
        for x in grad:
            for y in range(int(fillOpposite[1] - fillOrigin[1] + 1)):
                color = ColorInterpolation.rygbInterpolate(grad.start, grad.stop, x)
                window.plot(fillOrigin[0] + x, fillOrigin[1] + y, color_rgb(color[0], color[1], color[2]))

        for x in range(len(self._gridValues)):
            for y in range(len(self._gridValues[x])):
                color = ColorInterpolation.rygbInterpolate(self._min, self._max, self._max - self._gridValues[x][y])
                window.plot(self._origin.getX() + x, self._origin.getY() - y, color_rgb(color[0], color[1], color[2]))
