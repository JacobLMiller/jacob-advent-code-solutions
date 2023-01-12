# Advent of code Year 2016 Day 1 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().strip().split(", ")

start = 0j

dirs = [1j, 1,-1j,-1]

i = 0

cur = start

p2 = None 
visited = {start}
for instr in input:
    d = instr[0]
    steps = int(instr[1:])

    if d == "L": i = (i-1) % 4
    else: i = (i+1) % 4

    dir = dirs[i]
    for step in range(steps):
        cur += dir 

        if cur not in visited:
            visited.add(cur)
        elif cur in visited and p2 == None:
            p2 = cur

p1 = abs(start.real - cur.real) + abs(start.imag - cur.imag)

p2 = abs(start.real - p2.real) + abs(start.imag - p2.imag)

print("Part One : "+ str(int(p1)))



print("Part Two : "+ str(int(p2)))