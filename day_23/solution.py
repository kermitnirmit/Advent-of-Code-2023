import time
from collections import deque, defaultdict

f = [x for x in open("input.txt").read().split("\n")]
dirs_2d_4 = {(0, 1), (1, 0), (0, -1), (-1, 0)}

paths = -1


start = (0,0)

for i in range(len(f[0])):
    if f[0][i] == ".":
        start = (0, i)
        break

target = (len(f) - 1, len(f[0]) -1)
for i in range(len(f[-1])):
    if f[-1][i] == ".":
        target = (len(f) - 1, i)
        break


dmap = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
}


valid_paths = []
start_time = time.time()
def bfs(start):
    q = deque([(start, 0, set())])

    while q:
        curr, l, visited = q.popleft()
        if curr == target:
            valid_paths.append(l)
        if curr in visited:
            continue
        i, j = curr
        # visited.add(curr)
        if 0 <= i < len(f) and 0 <= j < len(f[0]):
            if f[i][j] == ".":
                for di, dj in dirs_2d_4:
                    nvisited = visited.copy()
                    nvisited.add(curr)
                    q.append(((i + di, j + dj), l + 1, nvisited))
            if f[i][j] in "><v^":
                di, dj = dmap[f[i][j]]
                nvisited = visited.copy()
                nvisited.add(curr)
                q.append(((i + di, j + dj), l + 1, nvisited))

bfs(start)
print(max(valid_paths))
end_time = time.time()

print("p1 runtime", end_time - start_time)
#
decision_points = set()


start_time = time.time()
def lookup(i,j):
    if 0 <= i < len(f) and 0 <= j < len(f[0]):
        return f[i][j]
    else:
        return "#"

for i in range(len(f)):
    for j in range(len(f[0])):
        neighbors = 0
        if lookup(i,j) in ".<>^v":
            for di, dj in dirs_2d_4:
                if lookup(i + di, j + dj) != "#":
                    neighbors += 1
            if neighbors > 2:
                decision_points.add((i,j))
decision_points.add(start)
decision_points.add(target)
adj_list = defaultdict(dict)


left_to_match = decision_points.copy()

while left_to_match:
    curr = left_to_match.pop()
    q = deque([(curr, 0)])
    v = set()
    while q:
        c, l = q.popleft()
        if c in v:
            continue
        if c != curr and c in decision_points:
            adj_list[c][curr] = l
            adj_list[curr][c] = l
            # adj_list[c].add((curr, l))
            # adj_list[curr].add((c, l))
            v.add(c)
            continue
        v.add(c)
        for di, dj in dirs_2d_4:
            ni, nj = c[0] + di, c[1] + dj
            if lookup(ni, nj) != "#":
                q.append(((ni, nj), l + 1))



def dfs(visited, curr, paths):
    if curr == target:
        return paths

    if curr in visited:
        return 0

    max_path_length = 0
    visited.add(curr)
    if target in adj_list[curr].keys():
        max_path_length = max(max_path_length, paths + adj_list[curr][target])
    else:
        for neighbor, dist in adj_list[curr].items():
            if neighbor == target:  # Directly go to target if it's a neighbor
                max_path_length = max(max_path_length, paths + dist)
            if neighbor not in visited:
                path_length = dfs(visited, neighbor, paths + dist)
                max_path_length = max(path_length, max_path_length)

    visited.remove(curr)
    return max_path_length

print(dfs(set(), start, 0))
end_time = time.time()

print("p2 runtime", end_time-start_time)