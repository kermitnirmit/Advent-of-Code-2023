import re
from functools import lru_cache

import numpy as np
f = [x for x in open("input.txt").read().strip().split("\n")]

@lru_cache()
def recurse(s, groupsToFind):
    # print("starting string is", s, "looking for these groups", groupsToFind)
    # input("continue")
    if len(groupsToFind) == 0 and ("#" not in s):
        return 1
    if (len(groupsToFind) == 0) != (len(s) == 0):
        return 0
    if s[0] == ".":
        # print("found a dot, going to the next one", s, groupsToFind)
        return recurse(s[1:], groupsToFind)
    if s[0] == "?":
        newS = "#" + s[1:]
        newerS = "." + s[1:]
        # print("found a ?, trying both possibilities")
        return recurse(newS, groupsToFind) + recurse(newerS, groupsToFind)
    if s[0] == "#":
        lenICare = int(groupsToFind[0])
        # print("found a #", "this is what i'm looking for: ", s, lenICare, s[:lenICare])
        if len(s) >= lenICare and (lenICare == len(s) or s[lenICare] != "#") and "." not in set(s[:lenICare]):
            # print("that was valid")
            return recurse(s[lenICare + 1:], groupsToFind[1:])
        # else:
        #     print("that was not valid")

    return 0


q = 0
for line in f:
    stuff, groups = line.split(" ")
    groups = [int(a) for a in groups.split(",")]
    q += recurse(stuff, groups)
print(q)
#
# q = 0
# for line in f:
#     stuff, groups = line.split(" ")
#     groups = [int(a) for a in groups.split(",")]
#     print(stuff * 5)
#     print(groups * 5)
#     # q += recurse(stuff * 5, groups * 5)
# print(q)