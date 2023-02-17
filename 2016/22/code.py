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
        if per == 0:
            print("I am empty")

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



print("Part Two : "+ str(None))