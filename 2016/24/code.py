# Advent of code Year 2016 Day 24 solution
# Author = ?
# Date = December 2022
import numpy as np

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]


def bfs(start,end,grid):
    Q = [start]
    visited = {start}
    dist = {start: 0}


    directions = (-1,1,-1j,1j)
    while len(Q) > 0:
        v = Q.pop(0)
        if v == end: return dist[v]
        
        for dir in directions:
            u = v + dir 
            if grid[u] != "#" and u not in visited:
                Q.append(u)
                visited.add(u)
                dist[u] = dist[v] + 1



#Find locations, store in dict
#apsp via bfs for each pair
#brute force tsp on this matrix
interests = dict()
grid = dict()

for i,row in enumerate(input):
    for j,c in enumerate(row):
        grid[complex(j,i)] = c
        if c.isnumeric(): 
            interests[int(c)] = complex(j,i)


n = len(interests.keys())
d = np.zeros((n,n))
for i in range(n):
    for j in range(i):
        if i == j: continue 
        dist = bfs(interests[i],interests[j],grid)
        d[j,i] = dist
        d[i,j] = dist

order = [i for i in range(1,8)]
from itertools import permutations
min_dist = 100000000


for pot in permutations(order):
    pot = [0] + list(pot)
    length = sum(d[a,b] for a,b in zip(pot,pot[1:]))
    min_dist = min(min_dist,int(length))

print("Part One : "+ str(min_dist))

p2 = 1000000000
for pot in permutations(order):
    pot = [0] + list(pot) + [0]
    length = sum(d[a,b] for a,b in zip(pot,pot[1:]))
    p2 = min(p2,int(length))

print("Part Two : "+ str(p2))