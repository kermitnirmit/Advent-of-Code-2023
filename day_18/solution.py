import numpy as np
from copy import deepcopy
from collections import defaultdict, deque
from heapq import heapify, heappop, heappush

# from matplotlib.path import Path
import matplotlib.path as mpath

from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plt



f = [x for x in open("input.txt").read().strip().split("\n")]
#
# # dirs_2d_4 = {(0, 1), (1, 0), (0, -1), (-1, 0)}
#
# dmap = {
#     'U' : (1, 0),
#     'R' : (0, 1),
#     'D' : (-1, 0),
#     'L' : (0, -1)
# }
#
# curr = (0,0)
# points = [curr]
# mini = 0
# maxi = 0
# minj = 0
# maxj = 0
#
# for line in f:
#     d, count, _ = line.split(" ")
#     count = int(count)
#     dir = dmap[d]
#     for i in range(count):
#         i, j = curr
#         curr = (i + dir[0], j + dir[1])
#         mini = min(mini, curr[0])
#         maxi = max(maxi, curr[0])
#         minj = min(minj, curr[1])
#         maxj = max(maxj, curr[1])
#         points.append(curr)
#
# y_values, x_values = zip(*points)
#
# plt.scatter(x_values, y_values, label='Points', color='blue', marker='o')
# # plt.show()
#
# dirs_2d_4 = {(0, 1), (1, 0), (0, -1), (-1, 0)}
#
# s = [(50, 50)]
# #
# p_set = {*points}
#
# while s:
#     curr = s.pop()
#     if curr in p_set:
#         continue
#     else:
#         p_set.add(curr)
#         for di, dj in dirs_2d_4:
#             ni, nj = curr[0] + di, curr[1] + dj
#             s.append((ni,nj))
#
# print(len(p_set))

# p2
dirs_2d_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
points = [(0,0)]
curr = (0,0)
perimeter = 0
for line in f:
    _, _, hexadecimal = line.split(" ")
    hexadecimal = hexadecimal[2:-1]
    dist, d = hexadecimal[:-1], hexadecimal[-1]
    # print(dist, d)
    dist = int(dist, 16)
    # print(dist, d)
    di, dj = dirs_2d_4[int(d)]
    curr = (curr[0] + (di * dist), curr[1] + (dj * dist))
    points.append(curr)
    perimeter += dist
    # print(perimeter)

# print(points)


def interior_area(points):
    path = [*points]
    return sum(
        r1 * c2 - r2 * c1
        for (r1, c1), (r2, c2) in zip(path, path[1:])
    ) / 2

area = interior_area(points)

# pick's theorem - find the number of points in a shape given its area
num_interior_points = int(abs(area) - 0.5 * len(points))
print(int(abs(area) + perimeter // 2 + 1))