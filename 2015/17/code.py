# Advent of code Year 2015 Day 17 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [int(d) for d in input_file.read().replace("\n",",").split(",")]


print(input)
import itertools 

p1 = 0
min_num = 0
for k in range(len(input)):
    p1 += sum([sum(c) == 150 for c in itertools.combinations(input,k)])
    if min_num == 0 and p1 > 0:
        p2 = p1
        min_num = 1

print("Part One : "+ str(p1))



print("Part Two : "+ str(p2))