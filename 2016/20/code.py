# Advent of code Year 2016 Day 20 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [[int(n) for n in d.strip().split("-")] for d in input_file.readlines()]


data = sorted(input,key=lambda x: x[0])

def test(n):
    for lb,ub in data:
        if lb <= n <= ub:
            return False 
    return n < 2**32

filter = [ub+1 for _,ub in data]

valids = [n for n in filter if test(n)]
p1 = valids[0]

print("Part One : "+ str(p1))

p2 = len(valids)

print("Part Two : "+ str(p2))