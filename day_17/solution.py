import numpy as np
from copy import deepcopy
from collections import defaultdict, deque
from heapq import heapify, heappop, heappush

f = [x for x in open("input.txt").read().strip().split("\n")]

dirs_2d_4 = {(0, 1), (1, 0), (0, -1), (-1, 0)}


def findOpposite(currDir):
    di, dj = currDir
    if di != 0:
        return (-di, dj)
    else:
        return (di, -dj)

def bfs(s):
    heapify(s)
    visited = set()
    while s:
        curr = heappop(s)
        # print(curr)
        # input("continue")
        heatLoss, streak, currPos, currDir = curr
        if (currPos, currDir, streak) in visited:
            continue
        else:
            i, j = currPos
            if 0 <= i < len(f) and 0 <= j < len(f[0]):
                if i == len(f) - 1 and j == len(f[0]) - 1:
                    return heatLoss
                visited.add((currPos, currDir, streak))

                reverseDir = findOpposite(currDir)

                actualDirs = dirs_2d_4.difference({reverseDir})
                # print(actualDirs, currDir)
                if streak == 3:
                    actualDirs = actualDirs.difference({currDir})
                for di, dj in actualDirs:
                    if 0 <= i + di < len(f) and 0 <= j + dj < len(f[0]):
                        newStreak = streak + 1 if (di, dj) == currDir else 1
                        heappush(s, (heatLoss + int(f[i+di][j+dj]), newStreak, (i + di, j + dj), (di, dj)))


def bfs_2(s):
    heapify(s)
    visited = set()
    while s:
        curr = heappop(s)
        heatLoss, streak, currPos, currDir = curr
        if (currPos, currDir, streak) in visited:
            continue
        else:
            i, j = currPos
            if 0 <= i < len(f) and 0 <= j < len(f[0]):
                if i == len(f) - 1 and j == len(f[0]) - 1 and streak >= 4:
                    return heatLoss
                visited.add((currPos, currDir, streak))

                reverseDir = findOpposite(currDir)

                actualDirs = dirs_2d_4.difference({reverseDir})
                # print(actualDirs, currDir)
                if streak == 10:
                    actualDirs = actualDirs.difference({currDir})
                if streak < 4 and streak != 0:
                    actualDirs = {currDir}
                # print(curr)
                # print(actualDirs)
                # input("continue")
                for di, dj in actualDirs:
                    if 0 <= i + di < len(f) and 0 <= j + dj < len(f[0]):
                        newStreak = streak + 1 if (di, dj) == currDir else 1
                        heappush(s, (heatLoss + int(f[i+di][j+dj]), newStreak, (i + di, j + dj), (di, dj)))

# print(bfs([(0, 0, (0,0), (0,0))]))
print(bfs_2([(0, 0, (0,0), (0,0))]))

