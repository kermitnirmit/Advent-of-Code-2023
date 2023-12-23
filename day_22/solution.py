from collections import deque

f = [x for x in open("input.txt").read().split("\n")]

blocks = {}
for i, line in enumerate(f):
    s, e = line.split("~")
    s = tuple(int(x) for x in s.split(","))
    e = tuple(int(x) for x in e.split(","))
    blocks[i] = ((s,e))

gminx = min(min(x0, x1) for ((x0, _, _), (x1, _, _)) in blocks.values())
gminy = min(min(y0, y1) for ((_, y0, _), (_, y1, _)) in blocks.values())
gmaxx = max(max(x0, x1) for ((x0, _, _), (x1, _, _)) in blocks.values())
gmaxy = max(max(y0, y1) for ((_, y0, _), (_, y1, _)) in blocks.values())

grid = dict(((x,y,0), -1) for x in range(gminx, gmaxx+1) for y in range(gminy, gmaxy+1))


falling = list(range(len(blocks)))

falling.sort(key=lambda x: min(blocks[x][0][2], blocks[x][1][2]))
falling = deque(falling)

resting_on = {}
while falling:
    curr = falling.popleft()
    block = blocks[curr]

    rest = set()
    resting_z = -1

    minx, maxx = min(block[0][0], block[1][0]), max(block[0][0], block[1][0])
    miny, maxy = min(block[0][1], block[1][1]), max(block[0][1], block[1][1])
    minz, maxz = min(block[0][2], block[1][2]), max(block[0][2], block[1][2])

    for (gx, gy, gz), r in grid.items():
        if minx <= gx <= maxx and miny <= gy <= maxy:
            if gz > resting_z:
                resting_z = gz
                rest = set([r])
            elif gz == resting_z:
                rest.add(r)
    resting_on[curr] = rest
    distance = (resting_z + 1) - minz
    minz, maxz = minz + distance, maxz + distance

    for z in range(minz, maxz + 1):
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                assert ((x,y,z) not in grid)
                grid[(x,y,z)] = curr

can_kill = set(range(len(blocks)))
for v in resting_on.values():
    if len(v) == 1:
        r1, = v
        can_kill.discard(r1)

print(len(can_kill))


tot = 0
for k in range(len(blocks)):
    # if it's safe to disintegrate, then it won't cause a chain reaction. skip these
    if k in can_kill:
        continue
    fall = set()
    nfall = {k}
    # if nfall is bigger than fall then the chain reaction is still going
    while len(nfall) > len(fall):
        fall.update(nfall)
        for i in range(len(blocks)):
            # if all the blocks that i is resting on are blowing up, then it will also fall
            if all(nblock in nfall for nblock in resting_on[i]):
                nfall.add(i)
    # -1 so we don't count itself
    tot += len(fall) - 1
print(tot)
