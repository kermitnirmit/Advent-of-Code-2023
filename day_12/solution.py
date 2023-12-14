import re

import numpy as np
f = [x for x in open("input1.txt").read().strip().split("\n")]

for line in f:
    print(line)
    a = re.findall("\?+", line)
    print(a)