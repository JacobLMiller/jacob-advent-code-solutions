# Advent of code Year 2016 Day 13 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()


fav = 1364

def is_valid(c):
    x,y = c.real, c.imag
    n = int( x * x + 3*x + 2*x*y + y + y*y + fav )
    b = bin(n)[2:]
    if sum(True for bit in b if bit == "1") % 2 == 0:
        return True 
    return False
    
def bfs(s,t,limit=1000):
    Q = [s]
    visited = {s}
    dst = {s: 0}

    directions = [1,-1,1j,-1j]
    while Q:
        v = Q.pop()
        if v == t or dst[v] > limit:
            return dst[v], visited

        for u in [v+d for d in directions]:
            if u.real < 0 or u.imag < 0:
                continue 
            if u not in visited and is_valid(u):
                Q.insert(0,u)
                visited.add(u)
                dst[u] =  dst[v] + 1
                
    print("not found")
    return None
        


s = 1+1j
t = 31+39j

p1, _ = bfs(s,t)

_,p2 = bfs(s,1000+1000j,49)



print("Part One : "+ str(p1))



print("Part Two : "+ str(len(p2)))