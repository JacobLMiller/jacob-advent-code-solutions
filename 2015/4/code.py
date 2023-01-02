# Advent of code Year 2015 Day 4 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

import hashlib

for i in range(1000000):
    s = bytes(input+str(i),encoding='utf-8')
    s = hashlib.md5(s).hexdigest()
    if s[:5] == "00000":
        p1 = i 
        break

p2 = 0
for i in range(100000000):
    s = bytes(input+str(i),encoding='utf-8')
    s = hashlib.md5(s).hexdigest()
    if s[:6] == "000000":
        p2 = i 
        break
    
    

print("Part One : "+ str(p1))



print("Part Two : "+ str(p2))