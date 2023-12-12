import re
from math import lcm
f = [x for x in open("input.txt").read().strip().split("\n")]
insts = f[0]
m = {}
for line in f[2:]:
    words = re.findall(r'\b\w+\b', line)
    m[words[0]] = [words[1], words[2]]
curr = "AAA"
steps = 0
# part 1
while True:
    options = m[curr]
    which = insts[steps % len(insts)]
    steps += 1
    if which == "L":
        curr = options[0]
    else:
        curr = options[1]
    if curr == "ZZZ":
        print(steps)
        break

starts = []
for k,v in m.items():
    if k[-1] == "A":
        starts.append(k)
steps = 0
ends = []
for k,v in m.items():
    if k[-1] == "Z":
        ends.append(k)
lengths = []
for curr in starts:
    steps = 0
    while True:
        options = m[curr]
        which = insts[steps % len(insts)]
        steps += 1
        if which == "L":
            curr = options[0]
        else:
            curr = options[1]
        if curr[-1] == "Z":
            lengths.append(steps)
            break
print(lcm(*lengths))

