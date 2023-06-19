# Advent of code Year 2017 Day 5 solution
# Author = ?
# Date = December 2018

def get_input():
    with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
        input = [int(d.strip()) for d in input_file.readlines()]
    return input

instr = get_input()

i = 0 
p1 = 0
while 0 <= i < len(instr):
    tmp = instr[i]
    instr[i] += 1
    i += tmp 
    p1 += 1



print("Part One : "+ str(p1))



instr = get_input()

i = 0 
p2 = 0
while 0 <= i < len(instr):
    tmp = instr[i]
    if tmp >= 3:
        instr[i] -= 1
    else: instr[i] += 1
    i += tmp 
    p2 += 1

print("Part Two : "+ str(p2))