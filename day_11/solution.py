import numpy as np
f = [x for x in open("input.txt").read().strip().split("\n")]


# print(f)
rows_to_dupe = []
cols_to_dupe = []
arr = []

for line in f:
    c = list(line)
    arr.append(c)

arr = np.array(arr)


for index, line in enumerate(arr):
    if sum(1 if x == "#" else 0 for x in line) == 0:
        rows_to_dupe.append(index)

for index, line in enumerate(arr.T):
    if sum(1 if x == "#" else 0 for x in line) == 0:
        cols_to_dupe.append(index)


galaxies = []

for i, r in enumerate(arr):
    for j, c in enumerate(r):
        if c == "#":
            galaxies.append((i,j))
paths = 0
emptyDuplicator = [1, 999999]
for mult in emptyDuplicator:
    for q in galaxies:
        for w in galaxies:
            minx = min(q[0], w[0])
            maxx = max(q[0], w[0])

            miny = min(q[1], w[1])
            maxy = max(q[1], w[1])

            emptyRows = 0
            emptyCols = 0

            for i in rows_to_dupe:
                if i in range(minx, maxx):
                    emptyRows += 1

            for i in cols_to_dupe:
                if i in range(miny, maxy):
                    emptyCols += 1

            paths += (abs(q[0] - w[0]) + (emptyRows * mult) + abs(q[1] - w[1])) + (emptyCols * mult)
    paths /= 2

    print(int(paths))
