import re
from collections import defaultdict
f = [x for x in open("input.txt").read().strip().split("\n")]

ts = re.findall("\d+", f[0])
ds = re.findall("\d+", f[1])
pairs = [(int(x[0]), int(x[1])) for x in zip(ts, ds)]
# print(pairs)
ans = []
# for t, d in pairs:
#     c = 0
#     for hold in range(t+1):
#         dist = hold * (t-hold)
#         # print(hold, dist)
#         if dist > d:
#             c += 1
#     ans.append(c)
# p = 1
# for a in ans:
#     p *= a



t = int("".join([char for char in f[0] if char.isdigit()]))
d = int("".join([char for char in f[1] if char.isdigit()]))

# print(t)
# print(d)

low = 0
hi = t


while hi > low:
    mid = (hi + low ) // 2

    dist = mid * (t-mid)
    if dist > d:
        # too long, let's try a shorter hold
        hi = mid - 1
    else:
        low = mid + 1

rlow = low


low = 0
hi = t


while hi > low:
    mid = (hi + low ) // 2

    dist = mid * (t-mid)
    if dist > d:
        # made it, let's try a longer number
        low = mid + 1
    else:
        hi = mid - 1

rhigh = hi


print(5733493 * (t- 5733493) - d)


print(rlow, rhigh)
print("part2 answer: ", rhigh - 5733493 + 1)



# 13
3


# print(p)
# print(ans)