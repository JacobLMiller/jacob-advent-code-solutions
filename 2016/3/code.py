# Advent of code Year 2016 Day 3 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]
    tris = [[int(d) for d in ",".join(line.split()).split(",")] for line in input]


def is_valid(a,b,c):
    if a+b > c and a+c > b and b+c > a:
        return True 
    return False 

p1 = sum(is_valid(*t) for t in tris)

print("Part One : "+ str(p1))

import numpy as np 

tris = np.array(tris)

p2 = 0
for col in range(3):
    t1 = tris[:,col]
    for i in range(0,t1.shape[0],3):
        p2 += is_valid(t1[i],t1[i+1],t1[i+2])


print("Part Two : "+ str(p2))