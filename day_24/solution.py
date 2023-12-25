import itertools

from z3 import *

from day_24.utils import ints, sign

f = [x for x in open("input.txt").read().split("\n")]

hailstone_map = {}
for line in f:
    numbers = ints(line)
    hailstone_map[tuple(numbers[:3])] = tuple(numbers[3:])


def is_after(point, intersection, dx, dy):
    # just make sure they have the same sign
    x_after = sign(intersection[0] - point[0]) == sign(dx)
    y_after = sign(intersection[1] - point[1]) == sign(dy)

    return x_after and y_after


# min_x = 7
min_x = 200000000000000
# max_y = 28
max_y = 400000000000000
c = 0

hailstones = list(hailstone_map.keys())

# this was neat, made sure you never saw (a,b) and then (b,a)
for a, b in itertools.combinations(hailstone_map.keys(), 2):
    # thanks middle school math
    adx = hailstone_map[a][0]
    ady = hailstone_map[a][1]
    bdx = hailstone_map[b][0]
    bdy = hailstone_map[b][1]

    # find the slope on a 2d plane by dy/dx
    m1 = ady / adx
    m2 = bdy / bdx

    # find the intercept y = mx + b -> y - mx = b
    b1 = a[1] - m1 * a[0]
    b2 = b[1] - m2 * b[0]

    # parallel lines don't intersect
    if m1 == m2:
        intersection = None
    else:
        # y1 = m1x1+b1 and y2 = m2x2 + b2
        # set ys equal and you get m1x1 + b1 = m2x2 + b2
        # rearrange and you get b2-b1 / (m1 - m2) = x
        x_intersect = (b2 - b1) / (m1 - m2)
        # plug that x in to either equation and you get the y value
        y_intersect = m1 * x_intersect + b1
        intersection = (x_intersect, y_intersect)
        if max_y >= intersection[0] >= min_x and min_x <= intersection[1] <= max_y:
            is_after_line1 = is_after(a, intersection, hailstone_map[a][0], hailstone_map[a][1])
            is_after_line2 = is_after(b, intersection, hailstone_map[b][0], hailstone_map[b][1])
            if is_after_line1 and is_after_line2:
                c += 1
print(c)

# https://github.com/Z3Prover/z3 made this so easy
s = Solver()
I = lambda name: z3.BitVec(name, 64)
x, y, z = I("x"), I("y"), I("z")
dx, dy, dz = I("dx"), I("dy"), I("dz")

for i, (k, v) in enumerate(hailstone_map.items()):
    cx, cy, cz = k
    vx, vy, vz = v
    t = I(f't_{i}')

    s.add(t > 0)
    s.add(x + dx * t == cx + vx * t)
    s.add(y + dy * t == cy + vy * t)
    s.add(z + dz * t == cz + vz * t)

assert s.check() == sat
m = s.model()

x, y, z = m.eval(x), m.eval(y), m.eval(z)
x, y, z = x.as_long(), y.as_long(), z.as_long()
print(x + y + z)

