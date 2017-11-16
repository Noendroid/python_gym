import random

import matplotlib.pyplot as plt

from Point_array import Point


def get_data_from_file(file_name):
    details = []
    with open(file_name, "r") as customers_file:
        for line in customers_file:
            details.append(line.split("\t"))
    items = []
    for d in details:
        c = Point(d)
        items.append(c)
    return items


def get_groups(points, centers):
    groups = []
    for c in range(len(centers)):
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
        c.sum = [0] * 2
        if len(groups[i]) > 0:
            for point in groups[i]:
                c.sum[0] += point.x
                c.sum[1] += point.y
            for x, a in enumerate(c.attributes):
                a = c.sum[x] / len(groups[i])
    return centers


def same_centers(old, new):
    if len(old) != len(new):
        return False
    for i in range(len(old)):
        if old[i].attributes is not new[i].attributes:
            return False
    return True


def get_distance(center, points):
    distance_sum = 0
    for p in points:
        distance_sum += center.dist(p)
    return distance_sum


def main():
    print("start")
    k = 2
    new_centers = [None] * k
    points = get_data_from_file("data.TXT")
    # while True:
    #     for i in range(k):
    #         new_centers[i] = points[random.randint(0, len(points) - 1)]
    #         for a in new_centers[i].attributes:
    #             a += random.randint(-100, 100)
    #     if len(new_centers) == len(set(new_centers)):
    #         break

    for i in range(k):
        new_centers[i] = points[random.randint(0, len(points) - 1)]
        for a in new_centers[i].attributes:
            a += random.randint(-50, 50)
    while True:
        groups = get_groups(points, new_centers)
        old_sums = [0] * len(new_centers)
        for i, c in enumerate(new_centers):
            for g in groups[i]:
                old_sums[i] = get_distance(c, g)
        new_centers = get_new_centers(new_centers, points)
        new_sums = [0] * len(new_centers)
        for i, c in enumerate(new_centers):
            for g in groups[i]:
                new_sums[i] = get_distance(c, g)

        print(new_sums)
        print(old_sums)
        break

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

    for c in new_centers:
        print(c.attributes)

    figure = plt.figure()
    figure.canvas.set_window_title("Kmeans")
    axes = figure.add_subplot(1, 1, 1)
    color_range = list(range(0x000000, 0xEFFFFF)) + list(range(0xFEFFFF, 0xEFFFFF))
    for g in groups:
        random_color = "#{:06x}".format(random.choice(color_range))
        for point in g:
            axes.scatter(point.attributes[0], point.attributes[1], color=random_color)

    for c in new_centers:
        axes.scatter(c.attributes[0], c.attributes[1], color="#ff0000")

    plt.show()


if __name__ == '__main__':
    main()
