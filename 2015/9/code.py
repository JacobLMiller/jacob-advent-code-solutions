# Advent of code Year 2015 Day 9 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]
    input = [d.replace(" = ", ",").replace(" to ",",") for d in input]


locs = set()
for d in input:
    loc,l2,_ = d.split(",")
    locs.add(loc)
    locs.add(l2)

loc_map = {l: i for i,l in enumerate(locs)}

n = len(locs)
d = [[0 for _ in range(n)] for _ in range(n)]
for line in input:
    src,dst,w = line.split(",")
    src,dst = loc_map[src], loc_map[dst]
    d[src][dst] = int(w)
    d[dst][src] = int(w)

import itertools
min_w = 1000000
max_w = 0
for path in itertools.permutations(range(n)):
    p_w = sum([d[src][dst] for src,dst in itertools.pairwise(path)])
    min_w = min(min_w,p_w)
    max_w = max(max_w,p_w)
    
    

print("Part One : "+ str(min_w))



print("Part Two : "+ str(max_w))