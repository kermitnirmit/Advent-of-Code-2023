import re
from functools import lru_cache

import numpy as np
f = [x for x in open("input.txt").read().strip().split("\n")]

# @lru_cache()

DP = {}
def recurse(s, b, s_index, b_index, curr_len):
    key = (s_index, b_index, curr_len)
    if key in DP:
        return DP[key]
    if s_index == len(s): #done with the string
        if b_index == len(b) and curr_len == 0: #we finished all the groups and have no extra hashes
            return 1
        elif b_index == len(b) - 1 and curr_len == b[b_index]:
            return 1
        else:
            return 0
    ret = 0
    for c in ".#":
        if s[s_index] == c or s[s_index] == "?":
            if c == "." and curr_len == 0:
                ret += recurse(s, b, s_index + 1, b_index, curr_len) # move to the next character... not important
            elif c == "." and curr_len > 0 and b_index < len(b) and curr_len == b[b_index]:
                ret += recurse(s, b, s_index + 1, b_index + 1, 0) #we completed one, so move to the next character and restart
            elif c == "#":
                ret += recurse(s, b, s_index + 1, b_index, curr_len + 1)
    DP[key] = ret
    return ret


q = 0
for line in f:
    stuff, groups = line.split(" ")
    groups = [int(a) for a in groups.split(",")]

    stuff = "?".join([stuff, stuff, stuff, stuff, stuff])
    groups = groups * 5
    DP.clear()
    curr = recurse(stuff, groups, 0, 0, 0)
    q += curr
print(q)