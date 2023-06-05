# Advent of code Year 2017 Day 3 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = int(input_file.read())

def manhattan(x1,y1,x2,y2):
    return abs(x2-x1) + abs(y2-y1) 

import math
def spiral(n):
        k = math.ceil((math.sqrt(n)-1)/2)
        t=2*k+1
        m=t**2 
        t=t-1
        if n >= m-t:  return k-(m-n),-k        
        else: m=m-t
        if n >= m-t:  return -k,-k+(m-n) 
        else: m=m-t
        if n >= m-t: return -k+(m-n),k 
        else: return k,k-(m-n-t)

p = spiral(input)

p1 = manhattan(0,0,*p)

print("Part One : "+ str(p1))

def calc(cur,grid):
    dirs = [1,1+1j,1j,-1+1j,-1,-1-1j,-1j,1-1j]
    val = 0
    for d in dirs:
        if cur+d in grid:
            val += grid[cur+d]
    return val


def spiral2(n):
    grid = {0+0j: 1}
    dirs = [1,1j,-1,-1j]
    i,d = 1,0 
    num = 1
    cur = 0+0j
    while i < n:
        for _ in range(2):
            for j in range(num):
                cur = cur + dirs[d]
                grid[cur] = calc(cur,grid)
                i += 1
                if grid[cur] > n: return grid[cur]
            d = (d+1)%4
        num += 1

p2 = spiral2(input)



print("Part Two : "+ str(p2))