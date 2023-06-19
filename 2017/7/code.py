# Advent of code Year 2017 Day 7 solution
# Author = ?
# Date = December 2018
import re

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]

sizes = dict()
T = dict()
T_sum = dict()
T_child = dict()

for row in input:
    parent = row.split(" ")[0]
    size = int(re.findall(r'\d+', row)[0])
    sizes[parent] = size 
    if "->" in row:
        children = row.split("->")[1].replace(" ","")
        T_child[parent] = children.split(",")
        for child in children.split(","):
            T[child] = parent
    else: T_child[parent] = list()
        
for key in sizes.keys():
    if key not in T:
        p1 = key

print("Part One : "+ str(p1))

import networkx as nx 
from collections import Counter
G = nx.DiGraph()
for row in input:
    name = row.split(" ")[0]
    G.add_node(name, weight = int(re.findall(r'\d+', row)[0]))

    if "->" in row:
        children = row.split("->")[1].replace(" ","").split(",")
        for child in children:
            G.add_edge(name,child)

ordered = list(nx.topological_sort(G))

weights = dict()
for node in reversed(ordered):
    total = G.nodes[node]['weight']

    counts = Counter(weights[child] for child in G[node])
    unbalanced = None

    for child in G[node]:
        # If this child's weight is different than others, we've found it
        if len(counts) > 1 and counts[weights[child]] == 1:
            unbalanced = child
            break

        # Otherwise add to the total weight
        val = weights[child]
        total += weights[child]

    if unbalanced:
        # Find the weight adjustment and the new weight of this node
        diff = weights[unbalanced] - val
        print('PART 2:', G.nodes[unbalanced]['weight'] - diff)
        break

    weights[node] = total


print("Part Two : "+ str(None))