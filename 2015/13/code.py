# Advent of code Year 2015 Day 13 solution
# Author = ?
# Date = December 2022

import itertools


with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]
    input = [d.replace(" would lose ", ",-").replace(" would gain ", ",")
                .replace(" happiness units by sitting next to ", ",")
                .replace('.',"")
                for d in input]

def calc_happiness(path,d):
    val = sum([d[e1][e2] + d[e2][e1] for e1,e2 in itertools.pairwise(path)])
    return val + d[path[-1]][path[0]] + d[path[0]][path[-1]]


people = set()
for edge in input:
    name, _, _ = edge.split(',')
    people.add(name)

p_map = {n: i for i,n in enumerate(people)}

n = len(people)
d = [[0 for _ in range(n+1)] for _ in range(n+1)]

for edge in input:
    src, w, dst = edge.split(",")
    src,dst = int(p_map[src]), int(p_map[dst])
    d[src][dst] = int(w) 


ans = max({calc_happiness(path,d) for path in itertools.permutations(range(n))})

print("Part One : "+ str(ans))


ans2 = max(
    {calc_happiness(path,d) for path in itertools.permutations(range(n+1))}
)

print("Part Two : "+ str(ans2))