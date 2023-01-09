# Advent of code Year 2015 Day 8 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [d.strip() for d in input_file.readlines()]

# input = ["\"aaa\\\\aaa\""]

def mem(s):
    n = len(s)
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\' and s[i+1] in  ['\\', '\"']:
            n -= 1
            i += 1
        elif c == '\\' and s[i+1] == 'x':
            n -= 3
            i += 3
        i += 1
    
    print(s)
    print(len(s), n-2)
    return n - 2

def expand(s):
    n = len(s)
    i = 0 
    while i < len(s):
        c = s[i]
        if c == '\\' and s[i+1] in  ['\\', '\"']:
            n += 2
            i += 1
        elif c == '\\' and s[i+1] == 'x':
            n += 1
            i += 3
        i += 1
    print(s)
    print(n + 4, len(s))
    return n + 4

p1 = sum([len(s) for s in input]) - sum([mem(s) for s in input])

print("Part One : "+ str(p1))

p2 = sum([expand(s) for s in input]) - sum([len(s) for s in input])

print("Part Two : "+ str(p2))