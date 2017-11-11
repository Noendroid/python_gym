import random
from math import inf

import matplotlib.pyplot as plt

from Point import Point


def get_data_from_file(file_name):
    details = []
    with open(file_name, "r") as customers_file:
        for line in customers_file:
            details.append(line.split("\t"))
    arr = []
    for d in details:
        c = Point(d)
        arr.append(c)
    return arr


def get_groups(points, centers):
    groups = []
    for c in centers:
        groups.append([])
    for p in points:
        centers_distances = []
        for c in centers:
            centers_distances.append(c.dist(p))
        # append to groups in the index of the center with the minimum distance
        groups[centers_distances.index(min(centers_distances))].append(p)
    return groups


def get_new_centers(centers, groups):
    for i, c in enumerate(centers):
        c.sum = [0] * len(c.attributes)
        if len(groups[i]) > 0:
            for point in groups[i]:
                for x, a in enumerate(point.attributes):
                    c.sum[x] += a
            for x, a in enumerate(c.attributes):
                a = c.sum[x] / len(groups[i])
    return centers


def get_distances_sum(centers, groups):
    distances = []
    for i in range(len(centers)):
        distances.append([])
    # continue from here



def main():
    print("start")
    k = 2
    centers = [None] * k
    points = get_data_from_file("data.TXT")
    old_dist_sum = [0] * k
    new_dist_sum = [None] * k

    while True:
        for i in range(k):
            centers[i] = points[random.randint(0, len(points) - 1)]
            for a in centers[i].attributes:
                a += random.randint(-100, 100)
        if len(centers) == len(set(centers)):
            break

    count = 0
    while True:
        groups = get_groups(points, centers)
        centers = get_new_centers(centers, groups)
        new_dist_sum = get_distances_sum(centers, groups)
        if new_dist_sum == old_dist_sum:
            break
        else:
            old_dist_sum = new_dist_sum


    for c in centers:
        print(c.attributes)

    figure = plt.figure()
    figure.canvas.set_window_title("Kmeans")
    axes = figure.add_subplot(1, 1, 1)
    colorRange = list(range(0x000000, 0xEFFFFF)) + list(range(0xFEFFFF, 0xEFFFFF))
    for g in groups:
        randonColor = "#{:06x}".format(random.choice(colorRange))
        for point in g:
            axes.scatter(point.attributes[0], point.attributes[1], color=randonColor)

    for c in centers:
        axes.scatter(c.attributes[0], c.attributes[1], color="#ff0000")

    plt.show()


if __name__ == '__main__':
    main()
