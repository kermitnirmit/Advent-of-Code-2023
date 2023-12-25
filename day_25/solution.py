import networkx as nx

from collections import defaultdict

f = [x for x in open("input.txt").read().splitlines()]


adj_list = defaultdict(list)

for line in f:
    left, right = line.split(": ")
    right = right.split()
    for q in right:
        adj_list[left].append(q)
        adj_list[q].append(left)

graph = nx.from_dict_of_lists(adj_list)

# total luck here, i just grabbed random points from my adjacency list until i got a size of non 1.
# picking fqt and bzs for example (they're connected) creates a component of size 1 and one of size n-1.
# (not what we're looking for)
remove_these = nx.minimum_edge_cut(graph, 'fqt', 'jkk')

graph.remove_edges_from(remove_these)

sizes = [len(component) for component in nx.connected_components(graph)]

print(sizes)
print(sizes[0] * sizes[1])