import re
from collections import deque
f = [x for x in open("input.txt").read().strip().split("\n")]

s = 0
p2 = 0
for line in f:
    nums = re.findall(r"[-+]?\d+", line)
    nums = [int(n) for n in nums]
    layers = [nums]
    for i in range(len(nums)):
        nextLayer = []
        for q, w in zip(layers[i], layers[i][1:]):
            nextLayer.append(w - q)
        layers.append(nextLayer)
        if sum(nextLayer) == 0:
            break
        if len(nextLayer) == 1:
            layers.append([0])
            break
    for i in range(len(layers) - 2, -1, -1):
        layers[i].append(layers[i][-1] + layers[i+1][-1])
    for i in range(len(layers) - 2, -1, -1):
        layers[i].insert(0, (layers[i][0] - layers[i+1][0]))
    s += layers[0][-1]
    p2 += layers[0][0]
print(s)
print(p2)

