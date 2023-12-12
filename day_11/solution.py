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

print("Before")
print(arr)

# for i in range(len(arr) - 1, -1, -1):
#     if i in rows_to_dupe:
#         arr = np.insert(arr, i, arr[i], 0)
# for i in range(len(arr[0]) - 1, -1, -1):
#     if i in cols_to_dupe:
#         arr = np.insert(arr, i, arr.T[i], 1)

galaxies = []

for i, r in enumerate(arr):
    for j, c in enumerate(r):
        if c == "#":
            galaxies.append((i,j))
paths = 0
emptyDuplicator = 999999
for q in galaxies:
    for w in galaxies:
        minx = min(q[0], w[0])
        maxx = max(q[0], w[0])

        miny = min(q[1], w[1])
        maxy = max(q[1], w[1])

        emptyRows = 0
        emptyCols = 0
        for i in range(minx, maxx):
            if i in rows_to_dupe:
                emptyRows += 1
        for i in range(miny, maxy):
            if i in cols_to_dupe:
                emptyCols += 1

        paths += (abs(q[0] - w[0]) + (emptyRows * emptyDuplicator) + abs(q[1] - w[1])) + (emptyCols * emptyDuplicator)
paths /= 2

print(int(paths))

# print(rows_to_dupe)
# print(cols_to_dupe)