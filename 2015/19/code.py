# Advent of code Year 2015 Day 19 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip().split(" => ") for d in input_file.readlines()]


inpstr = input[-1][0]
input.pop()
input.pop()


from collections import defaultdict

D = defaultdict(lambda: 0)

for src, tgt in input:
    D[src] += 1

import re 
p1 = set()
for src,tgt in input:
    for match in re.finditer(src, inpstr):
            s,e = match.start(), match.end()
            p1.add( inpstr[:s] + tgt + inpstr[e:] )


print("Part One : "+ str(len(p1)))

def rep_string(s):
    res = list()
    for src,tgt in input:
        for match in re.finditer(tgt,s):
            b,e = match.start(), match.end()
            res.append(s[:b] + src + s[e:])
    return res
            

def heuristic(Q,size=1000):
    return sorted(Q, key= lambda x: len(x[0]))[:size]

def BFS(start='e',end=inpstr):

    beg = (start, 0)
    Q = [beg]
    visited = {beg}

    depth = set()
    while len(Q) > 0:
        s,t = Q.pop()
        if s == end:
            return t
        
        if t not in depth:
            Q = heuristic(Q,1000)
            print(f"Depth: {t}, Len: {len(s)}")
            depth.add(t)

        children = rep_string(s)
        for c in children:
            if (c,t+1) not in visited: 
                visited.add((c,t+1))
                Q.insert(0,(c,t+1))

p2 = BFS(start=inpstr,end='e')

print("Part Two : "+ str(p2))