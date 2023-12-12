import numpy as np
from collections import deque
f = [x for x in open("input.txt").read().strip().split("\n")]
# pipe to direction mapping

m = {
    "F": {"U": "R", "L": "D"},
    "|": {"U": "U", "D": "D"},
    "-": {"L": "L", "R": "R"},
    "L": {"D": "R", "L": "U"},
    "7": {"U": "L", "R": "D"},
    "J": {"R": "U", "D": "L"}
}
# direction to di,dj mapping
d = {
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
}
# find the s
S = (0,0)
for i, l in enumerate(f):
    for j, c in enumerate(l):
        if c == "S":
            S = (i,j)
toVisit = deque()

for dir, diff in d.items():
    i, j = S
    di, dj = diff
    ni, nj = i + di, j + dj
    toVisit.append(((ni, nj), dir, [S]))


visited = set(S)

thePath = []
while toVisit:
    p, currDir, path = toVisit.popleft()
    if p == S and len(path) != 0:
        thePath = path
        print(len(path) // 2)
        break
    charAtPoint = f[p[0]][p[1]]
    if charAtPoint != "." and currDir in m[charAtPoint]:
        nextDir = m[charAtPoint][currDir]
        i, j = p
        di, dj = d[nextDir]
        np = (i + di, j + dj)
        toVisit.append((np, nextDir, path + [p]))

# pick's theorem
def interior_area(points):
    path = [*points, points[0]]
    return sum(
        r1 * c2 - r2 * c1
        for (r1, c1), (r2, c2) in zip(path, path[1:])
    ) / 2



area = interior_area(path)

# pick's theorem - find the number of points in a shape given its area
num_interior_points = int(abs(area) - 0.5 * len(path) + 1)
print(num_interior_points)
