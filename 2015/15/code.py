# Advent of code Year 2015 Day 15 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]
    input = [d.replace(": capacity ", ",")
                .replace(" durability ", "")
                .replace(" flavor ", "")
                .replace(" texture ", "")
                .replace(" calories ", "")
                for d in input]

cal = [int(d.split(',')[-1]) for d in input]

def sum_to_100(n):
    for i in range(100):
        for j in range(100):
            for k in range(100):
                for l in range(100):
                    if i+j+k+l == 100:
                        yield [i,j,k,l]

def sum_to_1002(n):
    for i in range(100):
        for j in range(100):
            for k in range(100):
                for l in range(100):
                    if i+j+k+l == 100 and (i*cal[0]) + (j*cal[1]) + (k*cal[2]) + (l*cal[3]) == 500:
                        yield [i,j,k,l]

ings = [[int(i) for i in d.split(",")[1:5]] for d in input]

for row in ings:
    print(row)

import math
def val(amt):
    sums = [
        max(0,sum([
            a*ings[i][j] for a,i in zip(amt, range(len(ings)))
        ]))
        for j in range(len(ings[0]))
    ]
    
    return math.prod(sums)


p1 = 0
for amt in sum_to_100(2):
    p1 = max(p1,val(amt))

print("Part One : "+ str(p1))

p2 = 0
for amt in sum_to_1002(2):
    p2 = max(p2,val(amt))

print("Part Two : "+ str(p2))