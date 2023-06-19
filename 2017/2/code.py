# Advent of code Year 2017 Day 2 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]

import re 

data = [[int(d) for d in re.findall(r'\d+',s)] for s in input]

checksum = 0 
for line in data:
    s = min(line)
    m = max(line)
    checksum += (m-s)


print("Part One : "+ str(checksum))

checksum = 0
for line in data:
    for u in line:
        for v in line:
            if u == v: continue 
            if u % v == 0:
                checksum += (u/v)

print("Part Two : "+ str(checksum))