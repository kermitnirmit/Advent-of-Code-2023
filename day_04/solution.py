import re
from collections import defaultdict
f = [x for x in open("input.txt").read().strip().split("\n")]

lines = [] # (winnings , others)
win_counts = []
card_counts = [1 for line in f]
print(card_counts)
for index, line in enumerate(f):
    # print(line.split(":"))
    num_cards = card_counts[index]
    both = line.split(": ")[1]
    l,r = both.split(" | ")
    # print(l,"right", r)
    lnums = set([int(x) for x in re.findall(r"\d+", l)])
    rnums = set([int(x) for x in re.findall(r"\d+", r)])
    # print(lnums, "numbers", rnums)
    v = 2 ** (len(lnums.intersection(rnums)) - 1)
    if v == 0.5:
        v = 0
    lines.append(v)
    match_count = len(lnums.intersection(rnums))
    for i in range(match_count):
        card_counts[index + i + 1] += num_cards

    # win_counts.append()
# print(lines)
# print(sum(lines))
# print(win_counts)
print(sum(card_counts))