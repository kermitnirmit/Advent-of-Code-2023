import re
from collections import defaultdict
f = [x for x in open("input.txt").read().strip().split("\n")]

numbers = [] # (number, row, col of start)


for index, line in enumerate(f):
    matches = re.finditer(r'\d+', line)
    numbers.extend([(match.group(), index, match.start()) for match in matches])


numbers_with_part = []
gear_ratios = defaultdict(list)

for num, row, col in numbers:
    l = len(str(num))
    # go from row - 1 to row + 1 and col - 1 to col + 1 excluding row from col -> col + len
    hasPart = False
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + l + 1):
            if 0 <= r < len(f) and 0 <= c < len(f[0]):
                if f[r][c] not in ".0123456789":
                    if f[r][c] == "*":
                        gear_ratios[f"{r},{c}"].append(int(num))
                    hasPart = True
                    break
    if hasPart:
        numbers_with_part.append(int(num))
s = 0
for _, v in gear_ratios.items():
    if len(v) == 2:
        s += (v[0] * v[1])


print(sum(numbers_with_part))
print(s)
