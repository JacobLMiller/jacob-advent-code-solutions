# Advent of code Year 2015 Day 6 solution
# Author = ?
# Date = December 2022


with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    input = [d.strip().replace(" through ", ",") for d in input]

    input = [d.replace("turn off ", "0,")
              .replace("turn on ", "1,")
              .replace("toggle ", "2,") for d in input]


instr = [[int(s) for s in d.split(",")] for d in input]

grid = {(x,y): False for x in range(1000) for y in range(1000)}
grid2 = {(x,y): 0 for x in range(1000) for y in range(1000)}

def flip(ins, val):
    if ins == 0:
        return False 
    elif ins == 1:
        return True
    elif ins == 2:
        return not val
    
def flip2(ins,val):
    if ins == 0:
        return max(0,val-1)
    elif ins == 1:
        return val+1
    elif ins == 2:
        return val+2

for ins, x1,y1, x2,y2 in instr:
    for x in range(x1,x2+1):
        for y in range(y1, y2+1):
            grid[(x,y)] = flip(ins, grid[(x,y)])
            grid2[(x,y)] = flip2(ins,grid2[(x,y)])

on = sum(grid.values())
on2 = sum(grid2.values())

print("Part One : "+ str(on))



print("Part Two : "+ str(on2))