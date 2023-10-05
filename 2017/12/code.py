# Advent of code Year 2017 Day 12 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip().split(" <-> ") for d in input_file.readlines()]

G = {int(n): {int(k) for k in l.split(",")}  for n,l in input}

def get_cc(G, s):
    start = s
    visited = {start}
    Q = [start]

    while Q: 
        v = Q.pop()
        visited.add(v)
        for u in G[v]:
            if u not in visited: Q.append(u)


    return visited

p1 = get_cc(G,0)

print("Part One : "+ str(len(p1)))

p2 = 1 
visited = p1
for v in range(len(G)):
    if v not in visited:
        p2 += 1
        visited.update( get_cc(G,v) )


print("Part Two : "+ str(p2))