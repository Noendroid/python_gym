from math import pow
from math import sqrt


class Point:
    attributes = []

    def __init__(self, details):
        a = []
        for d in details:
            d = d.replace(',', '')
            d = d.replace('\n', '')
            d = d.replace('"', '')
            a.append(float(d))

        self.attributes = a

    def __str__(self):
        line = ""
        for a in self.attributes:
            line += str(a) + "\t"
        return line

    def dist(self, point):
        dist = 0
        for i, a in enumerate(self.attributes):
            dist += pow(a - point.attributes[i], 2)
        dist = sqrt(dist)
        return dist

    def __eq__(self, other):
        if len(other.attributes) != len(self.attributes):
            return False
        for i in range(len(self.attributes)):
            if self.attributes[i] != other.attributes[i]:
                return False
        return True
