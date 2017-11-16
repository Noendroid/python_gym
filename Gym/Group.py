from Point_array import Point


class Group:
    points = []
    center = None

    def __init__(self, points):
        self.points = points
        self.init_center()

    def init_center(self):
        sums = [0] * len(self.points[0].attributes)
        count = 0
        for p in self.points:
            for i, attribute in enumerate(self.points[0].attributes):
                sums[i] += attribute
            count += 1
        avg = []
        for s in sums:
            avg.append(s / count)
        self.center = Point([])
        self.center.attributes = avg

    def center_dist(self):
        dist = 0
        for p in self.points:
            dist += self.center.dist(p)
        return dist
