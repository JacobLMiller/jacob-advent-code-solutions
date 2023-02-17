# Advent of code Year 2016 Day 7 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]


print(input[0])

import re 

def is_valid(s):
    print(s)
    for i in range(len(s)-3):
        a,b,c,d = s[i:i+4]
        if a+b == d+c and a != b:
            return True 
    return False

p1 = 0

for st in input:
    st = st.replace("[",",").replace(']',",")
    split = st.split(",")
    within = [s for i,s in enumerate(split) if i % 2 == 1]
    without = [s for i,s in enumerate(split) if i % 2 == 0]
    if any([is_valid(s) for s in within]): continue 
    if any([is_valid(s) for s in without]): p1 += 1

print("Part One : "+ str(p1))

def get_outs(instr):
    out = set()
    for s in instr:
        for i in range(len(s)-2):
            if s[i] == s[i+2] and s[i] != s[i+1]:
                out.add(s[i:i+3])
    return out

p2 = 0
for st in input:
    st = st.replace("[",",").replace("]",",")
    split = st.split(",")
    within = [s for i,s in enumerate(split) if i % 2 == 1]
    without = [s for i,s in enumerate(split) if i % 2 == 0]

    outs = get_outs(without)
    rev = {s[1]+s[0]+s[1] for s in outs}
    if any([any(r in s for r in rev) for s in within]): p2 += 1



print("Part Two : "+ str(p2))