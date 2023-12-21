from collections import defaultdict
from copy import deepcopy

f = [x for x in open("input.txt").read().split("\n")]

n = len(f)
blocks = set()
s = None
for i, line in enumerate(f):
    for j, char in enumerate(line):
        if char == "#":
            blocks.add((i,j))
        if char == "S":
            s = ((i,j))
#
dirs_2d_4 = {(0, 1), (1, 0), (0, -1), (-1, 0)}

def explore(spots):
    newSpots = set()
    for spot in spots:
        i, j = spot
        for di, dj in dirs_2d_4:
            ni, nj = i + di, j + dj
            sni, snj = ni % len(f), nj % len(f[0])
            if (sni, snj) not in blocks:
                newSpots.add((ni,nj))
    return newSpots


spots = {s}
vals = []
for i in range(1, 10000):
    spots = explore(spots)
    if i == 64:
        print(len(spots))
    if i % len(f) == 26501365 % len(f):
        after = len(spots)
        vals.append(after)
        if len(vals) == 4:
            break
vals = vals[1:]
def get_polynomial(n, firstThree):
    a0, a1, a2 = firstThree
    b0 = a0
    b1 = a1-a0
    b2 = a2-a1
    return b0 + b1*n + (n*(n-1)//2)*(b2-b1)

goal = 26501365

print(get_polynomial((goal // n - 1), vals))