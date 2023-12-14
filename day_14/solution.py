import numpy as np
from copy import deepcopy
from collections import defaultdict
f = [x for x in open("input.txt").read().strip().split("\n")]

grid = []
for line in f:
    grid.append(np.array(list(line)))
grid = np.array(grid)

og_grid = deepcopy(grid)

# print(grid)

def tilt(grid):
    for c in range(len(grid[0])):
        for r in range(len(grid)):
            if grid[r][c] == "O":
                grid[r][c] = "."
                curr_r = r
                while True:
                    curr_r -= 1
                    # stop if it's something
                    if curr_r == -1 or (curr_r >= 0 and grid[curr_r][c] != "."):
                        grid[curr_r+1][c] = "O"
                        break


seen_before = defaultdict(list)
def calculateLoad(grid):
    l = 0
    for index, row in enumerate(grid):
        l += ((len(grid) - index) * sum(1 if x == "O" else 0 for x in row))
    return l
tilt(grid)
print(calculateLoad(grid))
grid = og_grid
def cycle(grid):
    for i in range(4):
        tilt(grid)
        grid = np.rot90(grid, 3)
    load = calculateLoad(grid)
    return load



for i in range(500):
    newLoad = cycle(grid)
    seen_before[newLoad].append(i+1)

# print(len(seen_before))
seen_before_2 = defaultdict(list)


# find cycle length

cycle_length = 1
for k,v in seen_before.items():
    for v1, v2 in zip(v[-5:], v[-4:]):
        cycle_length = max(cycle_length, v2 - v1)


for k,v in seen_before.items():
    for x in set(v[-5:]):
        seen_before_2[x % cycle_length].append(k)

print(seen_before_2[1000000000 % cycle_length][-1])
