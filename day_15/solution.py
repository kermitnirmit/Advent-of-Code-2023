import numpy as np
from copy import deepcopy
from collections import defaultdict

f = [x for x in open("input.txt").read().strip().split(",")]
q = 0


def calculateValue(step):
    c = 0
    for char in step:
        c += ord(char)
        c *= 17
        c %= 256
    return c


for step in f:
    q += calculateValue(step)
print(q)

boxes = defaultdict(list)

for step in f:
    if "=" in step:
        l, r = step.split("=")
        r = int(r)
        hash_v = calculateValue(l)
        thereAlready = False
        for index, item in enumerate(boxes[hash_v]):
            if item[0] == l:
                boxes[hash_v][index] = (l, r)
                thereAlready = True
                break
        if not thereAlready:
            boxes[hash_v].append((l, r))
    elif "-" in step:
        s = step[:-1]
        hash_v = calculateValue(s)
        for index, item in enumerate(boxes[hash_v]):
            if item[0] == s:
                del boxes[hash_v][index]
                break

total = 0
for k, v in boxes.items():
    for index, lens in enumerate(v):
        total += ((1 + k) * (index + 1) * lens[1])

print(total)
