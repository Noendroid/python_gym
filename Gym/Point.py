from math import pow
from math import sqrt
from math import fabs


class Point:
    x = None
    y = None

    def __init__(self, details):
        a = []
        for d in details:
            d = d.replace(',', '')
            d = d.replace('\n', '')
            d = d.replace('"', '')
            a.append(float(d))

        self.x = a[0]
        self.y = a[1]

    def __str__(self):
        line = "x: " + str(self.x) + ", y: " + str(self.y)
        return line

    def dist(self, point):
        dist = pow(self.x - point.x, 2) + pow(self.y - point.y, 2)
        dist = fabs(dist)
        dist = sqrt(dist)
        return dist
