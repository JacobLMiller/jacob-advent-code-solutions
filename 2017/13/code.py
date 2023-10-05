# Advent of code Year 2017 Day 13 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip().split(":") for d in input_file.readlines()]

orbits = {int(key): int(val) + int(val) - 2 for key, val in input}

p1 = list(filter(lambda tup: (tup[0] ) % tup[1] == 0, orbits.items()))
p1 = sum( depth * ((r + 2) // 2) for depth, r in p1)

print("Part One : "+ str(p1))

correct = lambda x: all( (x+i) % val > 0 for i,val in orbits.items())

p2 = 1
while not correct(p2):
    p2 += 1

print("Part Two : "+ str(p2))