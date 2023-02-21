# Advent of code Year 2016 Day 22 solution
# Author = ?
# Date = December 2022

import re
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [[int(n) for n in re.findall(r'\d+', d.strip())] for d in input_file.readlines()][2:]

class Node():
    def __init__(self,x,y,size,used,avail,per):
        self.x = x
        self.y = y 
        self.size = size 
        self.used = used 
        self.avail = avail 
        self.per = per

nodes = [Node(*d) for d in input]
n = len(nodes)

p1 = 0
for i in range(n):
    for j in range(n):
        if i == j: continue
        A,B = nodes[i], nodes[j]
        if A.used > 0 and A.used <= B.avail: 
            p1 += 1


print("Part One : "+ str(p1))

def bfs(start,end,grid,bx,by):
    Q = [start]
    visited = {start}
    steps = {start: 0}

    directions = [1,-1,1j,-1j]
    while Q:
        v = Q.pop(0)
        if v == end:
            return steps[v]

        for dir in directions:
            cand = v + dir
            if cand not in visited and 0 <= cand.real <= bx and 0 <= cand.imag <= by:
                A = grid[v]
                B = grid[cand]
                if B.used <= A.size:
                    Q.append(cand)
                    visited.add(cand)
                    steps[cand] = steps[v] + 1
    print("yuh oh")


grid = dict()
empty = None
max_x = 0
max_y = 0
for node in nodes:
    grid[complex(node.x, node.y)] = node 
    if node.per == 0:
        empty = complex(node.x,node.y)
    max_x = max(max_x,node.x)
    max_y = max(max_y, node.y)

i = 0
for y in range(max_y+1):
    for x in range(max_x+1):
        A = grid[complex(x,y)]
        if A.x == 0 and A.y == 0:
            print("!",end="")
        elif A.x == max_x and A.y == 0:
            print("G",end="")
        elif A.per == 0:
            print("_",end="")
        elif A.used > grid[empty].avail:
            print("#",end="")
        else: print(".",end="")
        i += 1
    print()

p2 = bfs(empty,complex(max_x-1,0),grid,max_x,max_y)

p2 += (5*(max_x-1)) + 1
print("Part Two : "+ str(p2))

