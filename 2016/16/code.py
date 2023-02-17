# Advent of code Year 2016 Day 16 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def dragon_curve(s,stop=272):
    a = s
    while len(a) < stop:
        b = a[::-1]
        b = "".join("0" if c == "1" else "1" for c in b)
        a += ("0" + b)
    return a[:stop]

def checksum(s):
    cs = "".join("1" if s[i] == s[i+1] else "0" for i in range(0,len(s),2))
    if len(cs) % 2 == 0: return checksum(cs)
    else: return cs

# input = "10000"

s = dragon_curve(input)
p1 = checksum(s)

print("Part One : "+ str(p1))

s = dragon_curve(input,35651584)
p2 = checksum(s)

print("Part Two : "+ str(p2))