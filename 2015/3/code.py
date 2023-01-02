# Advent of code Year 2015 Day 3 solution
# Author = ?
# Date = December 2022 

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

d_map = {
    ">": 1,
    "<": -1,
    "^": 1j,
    "v": -1j
}

instr = [d_map[d] for d in input]

visited = {0}
loc = 0
for ins in instr:
    loc += ins 
    visited.add(loc)

print("Part One : "+ str(len(visited)))

human = [d for i,d in enumerate(instr) if i % 2 == 0]
robo = [d for i,d in enumerate(instr) if i % 2 == 1]

visited = {0}
loc = 0
for ins in human:
    loc += ins 
    visited.add(loc)
loc = 0
for ins in robo:
    loc += ins 
    visited.add(loc)



print("Part Two : "+ str(len(visited)))