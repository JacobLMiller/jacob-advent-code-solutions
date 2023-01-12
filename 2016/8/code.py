# Advent of code Year 2016 Day 8 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]

class Grid():
    def __init__(self,l,w):
        self.G = dict()
        for i in range(w):
            for j in range(l):
                self.G[(i,j)] = False 
        self.w = w 
        self.l = l
    
    def rect(self,a,b):
        for i in range(a):
            for j in range(b):
                self.G[(i,j)] = True 
    
    def rotate_row(self,a,b):
        row = [self.G[(i,a)] for i in range(self.w)]
        for i, val in enumerate(row):
            self.G[((i+b) % self.w, a)] = val
    
    def rotate_column(self,a,b):
        col = [self.G[(a,i)] for i in range(self.l)]
        for i, val in enumerate(col):
            self.G[(a, (i+b) % self.l)] = val

G = Grid(6,50)

import re
for instr in input:
    a,b = re.findall(r'\d+', instr)
    a,b = int(a), int(b)
    if "rect" in instr:
        G.rect(a,b)
    elif "row" in instr:
        G.rotate_row(a,b)
    elif "column" in instr:
        G.rotate_column(a,b)

p1 = sum(val for val in G.G.values())

print("Part One : "+ str(p1))

for row in range(G.l):
    print("".join(["#" if G.G[(j,row)] else "." for j in range(G.w)]))

print("Part Two : "+ str(None))