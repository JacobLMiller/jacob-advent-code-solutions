# Advent of code Year 2016 Day 21 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]

import re
def exec_instr(s,instr):
    new_s = list(s)
    n = len(s)
    if "move position" in instr:
        instr = instr.replace("move position ","").replace(" to position ",",").split(",")
        i,j = instr 
        i,j = int(i), int(j)
        c = s[i]
        new_s.pop(i)
        new_s.insert(j,c)
        return "".join(new_s)
    elif "swap position" in instr:
        instr = [int(i) for i in instr.replace("swap position ", "").replace(" with position ", ",").split(",")]
        i,j = instr 
        tmp = s[i]
        new_s[i] = s[j]
        new_s[j] = tmp 
        return "".join(new_s)
    elif "reverse position" in instr:
        instr = [int(i) for i in instr.replace("reverse positions ","").replace(" through ",",").split(",")]
        i,j = instr
        sub = s[i:j+1][::-1]
        new_s = [sub[x-i] if i <= x <= j else new_s[x] for x in range(n)]
        return "".join(new_s)
    elif "swap letter" in instr:
        instr = instr.replace("swap letter ","").replace(" with letter ",",").split(",")
        a,b = instr
        new_s = [a if c == b else b if c == a else c for c in s]
        return "".join(new_s)
    elif "rotate based on" in instr:
        instr = instr.replace("rotate based on position of letter ","")
        a = instr[0]
        i = s.find(a)
        i = i + 2 if i >= 4 else i + 1
        new_s = [new_s[(x-i) % n] for x in range(n)]
        return "".join(new_s)
    elif "rotate right" in instr:
        instr = instr.replace("rotate right ","")
        i = int(instr[0])
        new_s = [new_s[(x-i) % n] for x in range(n)]
        return "".join(new_s)
    elif "rotate left" in instr:
        instr = instr.replace("rotate left ","")
        i = int(instr[0])
        new_s = [new_s[(x+i) % n] for x in range(n)]
        return "".join(new_s)

    print("yuh oh")
    
s = "abcdefgh"

for instr in input:
    s = exec_instr(s,instr)

print("Part One : "+ str(s))


from itertools import permutations 

for s_og in permutations("abcdefgh"):
    s = "".join(s_og)
    for instr in input:
        s = exec_instr(s,instr)
    if s == "fbgdceah":
        p2 = s_og
        break





print("Part Two : "+ str("".join(p2)))