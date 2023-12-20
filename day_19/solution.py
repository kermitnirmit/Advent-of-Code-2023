from copy import copy, deepcopy

from utils import ints, words
import numpy as np
from collections import defaultdict, deque
from heapq import heapify, heappop, heappush

class Rating:
    def __init__(self, vals):
        mapping = dict()
        keys = "xmas"
        for i, k in enumerate(keys):
            mapping[k] = vals[i]
        self.mapping = mapping



    def __repr__(self):
        return str(self.mapping)

    def getTotal(self):
        return sum(self.mapping.values())
workflows, ratings = [x for x in open("input.txt").read().split("\n\n")]


q = defaultdict(list)

for workflow in workflows.splitlines():
    name, rest = workflow.split("{")
    rest = rest[:-1].split(",")
    # print(workflow)
    q[name] = rest
workflows = q

# print(workflows)

w = []
for rating in ratings.splitlines():
    q = ints(rating)
    w.append(Rating(q))
ratings = w


approved = []
rejected = []
for rating in ratings:
    curr = workflows["in"]
    keepGoing = True
    while keepGoing and len(curr) > 0:
        # print(curr)
        for step in curr:
            if ":" in step:
                ineq, dest = step.split(":")
                # print(ineq, "destination:", dest)
                key = ineq[0]
                opr = ineq[1]
                v = int(ineq[2:])
                # print(rating.mapping[key], opr, v)
                s = f"{rating.mapping[key]}{opr}{v}"
                evaluation = eval(s)
                # print(evaluation)
                # input("continue")
                if evaluation:
                    if dest in "AR":
                        if dest == "A":
                            # print("approving")
                            keepGoing = False
                            approved.append(rating)
                            break

                        else:
                            # print("rejecting")
                            keepGoing = False
                            rejected.append(rating)
                            break
                    else:
                        # print("going to the next one", dest)
                        curr = workflows[dest]
                        break
                # print("eval was false, going to the next step")
            else:
                if step in "AR":
                    if step == "A":
                        # print("approving")
                        keepGoing = False
                        approved.append(rating)
                        break

                    else:
                        # print("rejecting")
                        keepGoing = False
                        rejected.append(rating)
                        break
                else:
                    # print("going to the next one", step)
                    curr = workflows[step]
                    break


# print("approved:", approved)
#
print(sum(x.getTotal() for x in approved))
# print("rejected: ", rejected)




def keep_it_going(valids, curr):
    if curr == "A":
        p = 1
        for k,v in valids.items():
            p *= (v.stop - v.start)
        return p
    valids = deepcopy(valids)
    if curr == "R":
        return 0
    tot = 0
    for step in workflows[curr][:-1]:
        ineq, dest = step.split(":")
        k, opr, v = ineq[0], ineq[1], int(ineq[2:])
        if opr == ">":
            dest_range = range(v + 1, valids[k].stop)
            after_range = range(valids[k].start, v + 1)
        else:
            dest_range = range(valids[k].start, v)
            after_range = range(v, valids[k].stop)

        valids[k] = dest_range
        tot += keep_it_going(valids, dest)
        valids[k] = after_range
    tot += keep_it_going(valids, workflows[curr][-1])
    return tot

starts = {
    "x": range(1, 4001),
    "m": range(1, 4001),
    "a": range(1, 4001),
    "s": range(1, 4001)
}

print(keep_it_going(starts, "in"))




# paths_to_approval = []
#
#
# q = ["in"]
#
# keys = "xmas"
# valids = {}
#
# for k in keys:
#     valids[k] = np.array([1] * 4001)
#     valids[k][0] = 0
#
#
# q = [("in", [])]
# q = deque(q)
# while q:
#     curr, path = q.popleft()
#     if curr == "A":
#         paths_to_approval.append(path)
#     if curr == "R":
#         continue
#     nexts = workflows[curr]
#
#     for step in nexts:
#         if ":" in step:
#             ineq, dest = step.split(":")
#             q.append((dest, path + [curr]))
#         else:
#             q.append((step, path + [curr]))
# print(paths_to_approval)
#
# for path in paths_to_approval[:1]:
#     for a,b in zip(path, path[1:]):
#         nexts = workflows[a]
#         for step in nexts:
#             if ":" in step:
#                 ineq, dest = step.split(":")
#                 key = ineq[0]
#                 opr = ineq[1]
#                 val = int(ineq[2:])
#                 if b == dest:
#                     # must get true
#                     if opr == "<": # must be less than, so anything greater or equal to is false
#                         valids[key][val:] = 0
#                     else: # must be greater than, so anything <= is false
#                         valids[key][1:val] = 0
#                 else:
#                     # must get false
#                     if opr == "<":
#                         valids[key][1:val] = 0
#                     else:
#                         valids[key][val+1:] = 0
#     nexts = workflows[path[-1]]
#     print("the final step, getting to A", nexts)
#     for step in nexts:
#         if ":" in step:
#             ineq, dest = step.split(":")
#             key = ineq[0]
#             opr = ineq[1]
#             val = int(ineq[2:])
#             if dest == "A":
#
# for k,v in valids.items():
#     print(k, sum(v))
