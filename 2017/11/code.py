# Advent of code Year 2017 Day 11 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().split(",")


def manhattan_hex(x1,x2):
    dy = x1.real - x2.real
    dx = x1.imag - x2.imag 

    if dy != 0 and dx != 0 and dy / abs(dy) == dx / abs(dx):
        return abs(dx+dy)
    else:
        return max(abs(dx), abs(dy))

def move(dir):
    if dir == "n":
        return 1+0j
    elif dir == "ne":
        return 1-1j 
    elif dir == "se": 
        return 0-1j 
    elif dir == "s":
        return -1+0j
    elif dir == "sw":
        return -1+1j 
    elif dir == "nw":
        return 0+1j
    

start = 0 + 0j
visited = {start}

cur = start 
p2 = 0
for dir in input:
    # print(f"move {dir} -> {cur + move(dir)}")
    cur += move(dir)
    visited.add(cur)
    p2 = max(p2, manhattan_hex(start,cur))

p1 = int(manhattan_hex(start,cur))

print("Part One : "+ str(p1))



print("Part Two : "+ str(p2))