# Advent of code Year 2015 Day 1 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()


d_map = {
    "(": 1,
    ")": -1
}
instr = [d_map[d] for d in input]

p1 = sum(instr)

print("Part One : "+ str(p1))


p2 = 0 
for i,d in enumerate(instr):
    p2 += d 
    if p2 < 0:
        p2 = i +1
        break


print("Part Two : "+ str(p2))