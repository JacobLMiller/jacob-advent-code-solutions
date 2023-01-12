# Advent of code Year 2015 Day 25 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()


start = 20151125
row, col = 2978, 3083

next = lambda old: (old * 252533) % 33554393

part = sum(range(row + col -1)) + col

tgt = (row,col)

code = start 
for i in range(part-1):
    code = next(code)

print("Part One : "+ str(code))



print("Part Two : "+ str(None))