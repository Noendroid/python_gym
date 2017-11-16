import random
from builtins import print

import matplotlib.pyplot as plt

from Group import Group
from Point_array import Point
from numpy import array_equal


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
    _groups = []
    for c in range(len(centers)):
        _groups.append([])
    for p in points:
        centers_distances = []
        for c in centers:
            centers_distances.append(c.dist(p))
        # append to groups in the index of the center with the minimum distance
        _groups[centers_distances.index(min(centers_distances))].append(p)
    groups = []
    for g in _groups:
        groups.append(Group(g))
    return groups


# def get_new_centers(centers, groups):
#     for i, c in enumerate(centers):
#         c.sum = [0] * len(c.attributes)
#         if len(groups[i]) > 0:
#             for point in groups[i]:
#                 for x, a in enumerate(point.attributes):
#                     c.sum[x] += a
#             for x, a in enumerate(c.attributes):
#                 a = c.sum[x] / len(groups[i])
#     return centers


# def same_centers(old, new):
#     if len(old) != len(new):
#         return False
#     for i in range(len(old)):
#         if old[i].attributes is not new[i].attributes:
#             return False
#     return True


# def get_distance_to_center(center, points):
#     distance_sum = 0
#     for p in points:
#         distance_sum += center.dist(p)
#     return distance_sum


# def get_distances(centers, groups):
#     distances = []
#     for i, center in enumerate(centers):
#         distances.append(get_distance_to_center(center, groups[i]))
#     return distances


def main():
    # (1)get all the points from the data.TXT
    # (2)set random points from the data to be the centers
    # (3)get groups for those centers
    # (4)start a loop:
    #       (4.1)calculate new centers for the old groups
    #       (4.2)if the distances of those groups equal to the previous:
    #            break loop
    #       else
    #       (4.3)create new groups
    #       (4.4)set old centers to be the new centers
    #       loop again
    # (5)show the results on the graph

    # (1)
    print("start")
    k = 2
    centers = [None] * k
    points = get_data_from_file("data.TXT")
    # (2)
    while True:
        for i in range(k):
            centers[i] = points[random.randint(0, len(points) - 1)]
            # for a in centers[i].attributes:
            #     a += random.randint(-100, 100)
        # if len(centers) == len(set(centers)):
        break

    # (3)
    groups = get_groups(points, centers)
    dist = []
    for g in groups:
        dist.append(g.center_dist())
    # (4)
    while True:
        print("while")
        # (4.1)
        new_centers = []
        for g in groups:
            new_centers.append(g.center)
        # (4.2)
        new_dist = []
        for g in groups:
            new_dist.append(g.center_dist())
        if array_equal(set(dist), set(new_dist)):
            print("equal")
            break
        # (4.3)
        dist = new_dist
        centers = new_centers
        groups = get_groups(points, centers)
        for c in centers:
            print(c)
        print("done")
        exit(0)
    # while True:
    #     old_centers = new_centers
    #     groups = get_groups(points, new_centers)
    #     new_centers = get_new_centers(new_centers, groups)
    #     if same_centers(old_centers, new_centers):
    #         break
    #         # new_dist_sum = get_distances_sum(new_centers, groups)
    #         # if new_dist_sum == old_dist_sum:
    #         #     break
    #         # else:
    #         #     old_dist_sum = new_dist_sum

    # for c in centers:
    #     print(c.attributes)
    #
    # figure = plt.figure()
    # figure.canvas.set_window_title("Kmeans")
    # axes = figure.add_subplot(1, 1, 1)
    # color_range = list(range(0x000000, 0xEFFFFF)) + list(range(0xFEFFFF, 0xEFFFFF))
    # for g in groups:
    #     random_color = "#{:06x}".format(random.choice(color_range))
    #     for point in g:
    #         axes.scatter(point.attributes[0], point.attributes[1], color=random_color)
    #
    # for c in centers:
    #     axes.scatter(c.attributes[0], c.attributes[1], color="#ff0000")
    #
    # plt.show()


if __name__ == '__main__':
    main()
