# Advent of code Year 2015 Day 20 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
    input = int(input)

from functools import reduce

def factors(n):
    return set(reduce(list.__add__, 
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
i = 785000
while True:
    if i % 1000 == 0: print(i)
    val = sum(v*10 for v in factors(i))
    if val > input:
        p1 = i 
        break
    i += 1

print("Part One : "+ str(p1))

i = 500000
while True: 
    if i % 1000 == 0: print(i)
    val = sum(v*11 for v in factors(i) if i <v*50 )
    if val > input:
        p2 = i
        break 
    i += 1



print("Part Two : "+ str(p2))