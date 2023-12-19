import re
import math
from collections import defaultdict
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
# print(f[0].split(": ")[1])
# print(seeds)
q = math.inf
maps = buildMaps(f)
for seed in seeds:
    for m in maps:
        seed = traverse(seed, m)
    q = min(q, seed)
print(q)



print(buildMaps(f))