import re
f = [x for x in open("input.txt").read().strip().split("\n")]
# 12 red cubes, 13 green cubes, and 14 blue cubes
lines = [x.split(": ")[1] for x in f]
ret = 0
for index, line in enumerate(lines):
    turns = line.split("; ")
    bag = { "red": 12, "green": 13, "blue": 14}
    currs = { "red": 0, "green": 0, "blue": 0}
    possible = True
    for turn in turns:
        matches = re.findall(r'(\d+)\s(\w+)', turn)
        # print(matches)
        for num, color in matches:
            if int(num) > currs[color]:
                currs[color] = int(num)
    # print(currs)
    p = 1
    for v in currs.values():
        p *= v
    # print(p)
    ret += p
    #         if int(num) > bag[color]:
    #             possible = False
    #             break
    #
    # if possible:
    #     print(possible, index + 1)
    #     ret += (index + 1)

print(ret)
# print(lines)