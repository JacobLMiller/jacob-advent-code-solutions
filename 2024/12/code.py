# Advent of code Year 2024 Day 12 solution
# Author = Jacob Miller
# Date = December 2024

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [[c for c in row.strip()] for row in input_file.readlines()]

class Region():
    def __init__(self,locs,type):
        self.locs = {l for l in locs}
        self.type = type

from collections import defaultdict
regiondict = defaultdict(lambda: -1)
for y,row in enumerate(input):
    for x, plant in enumerate(row):
        regiondict[complex(x,y)] = plant

visited = set()
components = list()

h,w = len(input), len(input[0])

for y in range(h):
    for x in range(w):
        v = complex(x,y)
        if v in visited: continue
        components.append({v})
        stack = [v]
        visited.add(v)
        
        while stack:
            v = stack.pop()
            components[-1].add(v)
            for dir in {1,-1,1j,-1j}:
                u = v + dir 
                if u in regiondict and u not in visited and regiondict[u] == regiondict[v]:
                    stack.append(u)
                    visited.add(u)

p1 = 0
for component in components:
    for u in component: break 
    plant = regiondict[u]

    p = sum(
        sum(regiondict[v+dir] != plant 
        for dir in {-1,1,-1j,1j}) 
        for v in component
    )
    p1 += (p * len(component))

print("Part One : "+ str(p1))

for component in sorted(components,key=len):
    for u in component: break 
    plant = regiondict[u]

    sides = 0
    build = set()
    for u in component:
        sides += 4 
        build.add(u)
        for d in {1,-1,1j,-1j}:
            if u + d in build: sides -= 4
    print(plant, sides)

print("Part Two : "+ str(None))