# Advent of code Year 2016 Day 11 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

pol, thul, prom, ruth, cob = 1,2,3,4,5

start = (
    tuple(sorted((pol,thul,-thul,prom, ruth,-ruth, cob, -cob))),
    tuple(sorted((-pol,-prom))),
    (),
    ()
)

start = (0,start)

def is_valid(floor):
    if not floor or floor[-1] < 0:
        return True
    return all(-chip in floor for chip in floor if chip < 0)


import heapq
from itertools import combinations
def astar(s):

    # def h(x):
    #     return abs(x[0]-t[0]) + abs(x[1]-t[1])    

    g_dst = {s: 0}
    f_dst = [(0, s)]
    heapq.heapify(f_dst)

    while f_dst[0]:
        _,v = heapq.heappop(f_dst) 
        E, floors = v 
        if E == 3 and all(len(f) == 0 for f in floors[:-1]):
            return g_dst[v]

        directions = [dir for dir in (-1,1) if 0 <= E + dir < 4]
        moves = list(combinations(floors[E],2))+ list(combinations(floors[E],1))
        for move in moves:
            for dir in directions:
                new_floors = list(floors)
                new_floors[E] = tuple(x for x in floors[E] if x not in move)
                new_floors[E + dir] = tuple(sorted((x for x in floors[E + dir] + move)))

                if not is_valid(new_floors[E]) or not is_valid(new_floors[E+dir]):
                    continue 

                u = (E + dir, tuple(new_floors))
                dist = g_dst[v] + 1

                if u not in g_dst or dist < g_dst[u]:
                    g_dst[u] = dist
                    heapq.heappush( f_dst, (dist - len(new_floors[3]) * 10, u) )

    print("Never completed")
    return None

p1 = astar(start)

print("Part One : "+ str(p1))

ele, dil = 6,7

start = (
    tuple(sorted((pol,thul,-thul,prom, ruth,-ruth, cob, -cob, ele,-ele,dil,-dil))),
    tuple(sorted((-pol,-prom))),
    (),
    ()
)

start = (0,start)

p2 = astar(start)


print("Part Two : "+ str(p2))