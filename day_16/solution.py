import numpy as np
from copy import deepcopy
from collections import defaultdict, deque

f = [x for x in open("input.txt").read().strip().split("\n")]


s = [((0,0), (0,1))]




def bfs(s):
    s = deque(s)
    visitedCells = set()

    visited = set()



    while s:
        # print(s)
        currPos, currDir = s.popleft()

        if (currPos, currDir) in visited:
            continue
        else:
            # visited.add((currPos, currDir))
            # visitedCells.add(currPos)
            i, j = currPos
            di, dj = currDir
            # print(currPos, currDir)
            # input("continue")
            if 0 <= i < len(f) and 0 <= j < len(f[0]):
                visited.add((currPos, currDir))
                visitedCells.add(currPos)
                if f[i][j] == ".": # continue moving
                    s.append(((i + di, j + dj), (di, dj)))
                elif f[i][j] == "|" and di == 0:
                    # up and down
                    s.append(((i + 1, j), (1, 0)))
                    s.append(((i - 1, j), (-1, 0)))
                elif f[i][j] == "-" and dj == 0:
                    # left and right
                    s.append(((i, j-1), (0, -1)))
                    s.append(((i, j+1), (0, 1)))
                elif f[i][j] in "/\\":
                    if f[i][j] == "/":
                        s.append(((i - dj, j - di), (-dj, -di)))
                    if f[i][j] == "\\":
                        s.append(((i + dj, j + di), (dj, di)))
                else:
                    s.append(((i + di, j + dj), (di, dj)))
    return len(visitedCells)

def find_all_edges():
    q = []
    for i in range(len(f)):
        q.append(((i, 0), (0,1))) # left edge, going right
        q.append(((i, len(f[0]) - 1), (0, -1))) # right edge going left
    for i in range(len(f[0])):
        q.append(((0, i), (1,0))) # top edge going down
        q.append(((len(f)-1, i), (-1, 0))) # bottom edge going up
    return q


w = 0
for startPos, startDir in find_all_edges():
    w = max(w, bfs([(startPos, startDir)]))
print(w)


# print(len(visitedCells))
