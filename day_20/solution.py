import math
from copy import copy, deepcopy

from utils import ints, words
import numpy as np
from collections import defaultdict, deque
from heapq import heapify, heappop, heappush


f = [x for x in open("input.txt").read().split("\n")]
class Node:
    def __init__(self, name, type, dests):
        self.name = name
        self.type = type
        self.memory = {}
        self.dests = dests
        self.state = False

    def __repr__(self):
        if len(self.memory) > 0:
            return f"({self.name=}, {self.state=}, {self.memory=})"
        return f"({self.name=}, {self.state=})"
    def handle_flow(self, pulse, src):
        if pulse == 0 and self.type == "%":
            before = self.state
            self.state = not self.state
            return not before
        if self.type == "&":
            self.memory[src] = pulse
            if all(self.memory.values()):
                return False
            else:
                return True
        if self.type == "b":
            # broadcaster, just publish the same pulse to each one
            return pulse


nodes = {}
for line in f:
    # print(line)
    src, destination = line.split(" -> ")
    destinations = destination.split(", ")
    if src[0] == "%":
        # flip flop
        nodes[src[1:]] = Node(src[1:], "%", destinations)
    elif src[0] == "&":
        # conjunction
        nodes[src[1:]] = Node(src[1:], "&", destinations)
    else:
        # broadcaster
        nodes[src] = Node(src, "b", destinations)
# nodes["output"] = Node("output", "n", [])
# nodes["rx"] = Node("rx", "n", [])

for i in nodes.keys():
    if nodes[i].type == "&":
        for j in nodes.keys():
            if i != j:
                if nodes[i].name in nodes[j].dests:
                    nodes[i].memory[nodes[j].name] = False
blank_nodes_to_add = []
for i in nodes.keys():
    for dest in nodes[i].dests:
        if dest not in nodes:
            blank_nodes_to_add.append(dest)

for n in blank_nodes_to_add:
    nodes[n] = Node(n, "n", [])

cycle_lengths = []

rx_parent = None
for i in nodes.keys():
    for dest in nodes[i].dests:
        if dest == "rx":
            rx_parent = nodes[i].name
cycle_markers = []
for i in nodes.keys():
    if rx_parent in nodes[i].dests:
        cycle_markers.append(nodes[i].name)
def press_button(i):
    pulses = deque([(False, "broadcaster", "button")])
    lows = highs = 0
    while pulses:
        pulse, currName, src = pulses.popleft()
        # pulseName = "high" if pulse else "low"
        if pulse:
            highs += 1
        else:
            lows += 1
        # print(f"{src} -{pulseName}-> {currName}")
        currNode = nodes[currName]
        outBound = currNode.handle_flow(pulse, src)
        if outBound is not None:
            # qh, pv, xm, hz all go into kh. a high pulse from them is
            # needed to activate kh which would send a low pulse to rx
            if outBound and currName in cycle_markers:
                cycle_lengths.append(i)
            for dest in currNode.dests:
                pulses.append((outBound, dest, currName))
    return (lows, highs)

lcounter, hcounter = 0, 0



for i in range(1, 5000):
    nlow, nhigh = press_button(i)
    lcounter += nlow
    hcounter += nhigh
    if i == 1000:
        print(lcounter * hcounter)
print(math.lcm(*cycle_lengths))