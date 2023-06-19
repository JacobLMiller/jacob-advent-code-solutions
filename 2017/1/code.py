# Advent of code Year 2017 Day 1 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [int(d) for d in input_file.read().strip()]

p1 = 0
for i in range(len(input)):
    if input[i] == input[(i+1) % len(input)]: p1 += input[i]

print("Part One : "+ str(p1))

p2 = 0 
n = len(input)
for i in range(n):
    if input[i] == input[(i+(n//2)) % n]: p2+= input[i]

print("Part Two : "+ str(p2))