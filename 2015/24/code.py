# Advent of code Year 2015 Day 24 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [int(d) for d in input_file.read().replace("\n", " ").split(" ")]


import math
from itertools import combinations

def find_qe(n=3):
    tgt = sum(input) // n 
    for i in range(len(input)):
        qe = [math.prod(c) for c in combinations(input,i) if sum(c) == tgt]

        if qe:
            return min(qe)

p1 = find_qe(3)

print("Part One : "+ str(p1))

p2 = find_qe(4)

print("Part Two : "+ str(p2))