import re
import math
from collections import defaultdict
from tqdm import tqdm, trange

f = [x for x in open("input.txt").read().strip().split("\n\n")]


def buildMaps(f):
    maps = []
    for stuff in f[1:]:
        lines = stuff.splitlines()[1:]
        q = []
        for line in lines:
            q.append([int(x) for x in line.split()])
        maps.append(q)
    return maps


def traverse(x, m):
    for dr, sr, c in m:
        if sr <= x < sr + c:
            x = dr + (x - sr)
            break
    return x

seeds = [int(x) for x in (f[0].split(": ")[1]).split()]
q = math.inf
maps = buildMaps(f)

for seed in seeds:
    for m in maps:
        seed = traverse(seed, m)
    q = min(q, seed)
print(q)

seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i + 1]))

def superTraverse(x):
    for m in maps:
        x = traverse(x, m)
    return x


def recurse(low, dist):
    if dist == 1:
        return min(superTraverse(low), superTraverse(low + 1))
    step = dist // 2
    middle = low + step

    start = superTraverse(low)
    mid = superTraverse(middle)
    high = superTraverse(low + dist)

    found = math.inf
    if start + step != mid:
        found = recurse(low, step)
    if mid + dist - step != high:
        found = min(found, recurse(middle, dist - step))
    return found


superMin = math.inf
for i, seed_range in enumerate(seed_ranges):
    superMin = min(superMin, recurse(seed_range[0], seed_range[1]))
print(superMin)