# imports

# constants

class ColorInterpolation:
    #  min <= p <= max
    def rygbInterpolate(min, max, p):
        r = 0
        g = 0
        b = 0
        deg = 240 * ((p - min) / (max - min))
        if deg >= 0 and deg <= 240:
            if deg <= 60:
                r = 255
                g = (255 / 60) * deg
                b = 0
            elif deg <= 120:
                r = (-255 / 60) * (deg - 60) + 255
                g = 255
                b = 0
            elif deg <= 180:
                r = 0
                g = 255
                b = (255 / 60) * (deg - 120)
            elif deg <= 240:
                r = 0
                g = (-255 / 60) * (deg - 180) + 255
                b = 255
        else:
            raise ValueError()

        return (int(r), int(g), int(b))

print(ColorInterpolation.rygbInterpolate(0, 1, 0))
